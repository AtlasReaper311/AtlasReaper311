#!/usr/bin/env python3
"""Regenerate the governed live block in the profile README.

The generated block deliberately separates three evidence classes:

  Atlas Infra projection   governed public repository count
  deploy-watch             latest public site deployment snapshot
  Writing index            latest published case study

The updater rewrites only the content between the ATLAS:LIVE markers. It does
not use GitHub account membership as estate governance, does not present
automation-heavy repository commit volume as personal activity, and does not
depend on the legacy writing/manifest.json file.

Failure policy, per source:
  source unreachable or malformed -> honest "couldn't confirm" line
  README markers missing           -> hard failure

Nothing embeds a fetch timestamp. Identical evidence renders to identical
bytes, so the scheduled workflow can skip runs with no genuine change.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

PROJECTION_URL = (
    "https://raw.githubusercontent.com/AtlasReaper311/atlas-infra/main/"
    "policy/public-repository-classifications.json"
)
DEPLOY_URL = "https://api.atlas-systems.uk/deploy-watch/latest"
WRITING_INDEX_URL = "https://atlas-systems.uk/writing/"
WRITING_URL = "https://atlas-systems.uk/writing/"

README_PATH = Path(__file__).resolve().parent.parent / "README.md"
START_MARKER = "<!-- ATLAS:LIVE:START -->"
END_MARKER = "<!-- ATLAS:LIVE:END -->"

TIMEOUT_SECONDS = 10
USER_AGENT = "atlas-profile-refresh (github.com/AtlasReaper311/AtlasReaper311)"

PROJECTION_SCHEMA = "atlas-public-repository-classifications/projection/v1"
PROJECTION_AUTHORITY = "AtlasReaper311/atlas-infra"


STATIC_REPLACEMENTS = (
    (
        "## Public repositories",
        "## Selected public repositories",
    ),
    (
        "The public estate map lives in [`atlas-api-public/data/estate.manifest.json`](https://github.com/AtlasReaper311/atlas-api-public/blob/main/data/estate.manifest.json). The public registry shows approved live Workers; the manifest describes the intentionally published architecture. Repository visibility is not inferred from account membership.",
        "The authoritative public repository classification lives in [`atlas-infra/policy/public-repository-classifications.json`](https://github.com/AtlasReaper311/atlas-infra/blob/main/policy/public-repository-classifications.json). Runtime topology and presentation live in [`atlas-api-public/data/estate.manifest.json`](https://github.com/AtlasReaper311/atlas-api-public/blob/main/data/estate.manifest.json). They are separate contracts: repository governance is not inferred from topology, repository visibility, or account membership.",
    ),
)

STATUS_WORDS = {
    "success": ("operational", "4ade80"),
    "failure": ("failing", "e24b4a"),
    "canceled": ("canceled", "aaa9a0"),
    "unknown": ("unknown", "555560"),
}
BUILDING = ("building", "f5a623")


def fetch_text(url: str) -> str | None:
    """Fetch one public text source, returning None on an untrusted result."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            if response.status != 200:
                print(f"warning: {url} returned {response.status}", file=sys.stderr)
                return None
            return response.read().decode("utf-8")
    except (urllib.error.URLError, TimeoutError, UnicodeDecodeError, OSError) as exc:
        print(f"warning: couldn't fetch {url}: {exc}", file=sys.stderr)
        return None


def fetch_json(url: str):
    """Fetch and parse one public JSON source."""
    text = fetch_text(url)
    if text is None:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        print(f"warning: couldn't parse JSON from {url}: {exc}", file=sys.stderr)
        return None


def iso_to_display(raw) -> str | None:
    """ISO timestamp -> 'YYYY-MM-DD HH:MM UTC', or None if unparseable."""
    if not isinstance(raw, str):
        return None
    from datetime import datetime, timezone

    try:
        parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def shield(label: str, message: str, color: str) -> str:
    def esc(text: str) -> str:
        return (
            text.replace("-", "--")
            .replace("_", "__")
            .replace(" ", "_")
            .replace("/", "%2F")
        )

    return (
        f"https://img.shields.io/badge/{esc(label)}-{esc(message)}-{color}"
        "?style=flat-square&labelColor=0a0a0f"
    )


def deploy_line_and_badge(deploy) -> tuple[str, str]:
    if not isinstance(deploy, dict) or not deploy.get("ok"):
        line = "[deploy]   ? couldn't confirm deploy state at last refresh"
        return line, f"![deploy]({shield('deploy', 'unconfirmed', '555560')})"

    status = str(deploy.get("status", "unknown"))
    word, color = STATUS_WORDS.get(status, BUILDING)
    sha = str(deploy.get("commitSha") or "-------")[:7]
    when = iso_to_display(deploy.get("endedOn")) or iso_to_display(deploy.get("createdOn"))
    when_text = f" · {when}" if when else ""
    glyph = "●" if status == "success" else "○"
    line = f"[deploy]   {glyph} {word} · {sha}{when_text}"
    return line, f"![deploy: {word}]({shield('deploy', word, color)})"


def estate_line_and_badge(projection) -> tuple[str, str]:
    repositories = projection.get("repositories") if isinstance(projection, dict) else None
    count = projection.get("repository_count") if isinstance(projection, dict) else None
    valid = (
        isinstance(projection, dict)
        and projection.get("schema_version") == PROJECTION_SCHEMA
        and projection.get("authority") == PROJECTION_AUTHORITY
        and isinstance(repositories, list)
        and isinstance(count, int)
        and count == len(repositories)
    )
    if not valid:
        line = "[estate]   ? couldn't confirm governed repository count at last refresh"
        return line, f"![estate]({shield('estate', 'unconfirmed', '555560')})"

    line = f"[estate]   {count} governed public repos"
    badge = f"![estate: {count} repos]({shield('estate', f'{count} repos', 'f5a623')})"
    return line, badge


class WritingIndexParser(HTMLParser):
    """Collect published Writing cards from the scheduler-owned index."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.entries: list[dict[str, str | int]] = []
        self._entry: dict[str, str | int] | None = None
        self._capture: str | None = None
        self._buffer: list[str] = []

    @staticmethod
    def _classes(attrs: dict[str, str | None]) -> set[str]:
        return set((attrs.get("class") or "").split())

    def handle_starttag(self, tag: str, attrs_list) -> None:
        attrs = dict(attrs_list)
        classes = self._classes(attrs)

        if tag == "a" and "article-entry" in classes:
            href = attrs.get("href") or ""
            if "coming-soon" in classes or not re.fullmatch(r"/writing/[a-z0-9-]+/", href):
                self._entry = None
                return
            self._entry = {"href": href}
            return

        if self._entry is None:
            return

        if tag == "span" and "article-number" in classes:
            self._capture = "number"
            self._buffer = []
        elif tag == "h2" and "article-title" in classes:
            self._capture = "title"
            self._buffer = []

    def handle_data(self, data: str) -> None:
        if self._entry is not None and self._capture is not None:
            self._buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self._entry is None:
            return

        if self._capture == "number" and tag == "span":
            raw = "".join(self._buffer).strip()
            match = re.fullmatch(r"W-(\d+)", raw)
            if match:
                self._entry["w_number"] = int(match.group(1))
                self._entry["w_label"] = raw
            self._capture = None
            self._buffer = []
            return

        if self._capture == "title" and tag == "h2":
            self._entry["title"] = " ".join("".join(self._buffer).split())
            self._capture = None
            self._buffer = []
            return

        if tag == "a":
            required = {"href", "w_number", "w_label", "title"}
            if required.issubset(self._entry):
                self.entries.append(dict(self._entry))
            self._entry = None
            self._capture = None
            self._buffer = []


def latest_published_writing(index_html: str | None) -> dict[str, str | int] | None:
    if not isinstance(index_html, str):
        return None
    parser = WritingIndexParser()
    try:
        parser.feed(index_html)
        parser.close()
    except Exception as exc:
        print(f"warning: couldn't parse Writing index: {exc}", file=sys.stderr)
        return None
    if not parser.entries:
        return None
    return max(parser.entries, key=lambda entry: int(entry["w_number"]))


def writing_line_and_badge(index_html: str | None) -> tuple[str, str]:
    entry = latest_published_writing(index_html)
    if entry is None:
        line = "[writing]  latest case study: atlas-systems.uk/writing"
        badge = (
            f"[![writing: case studies]({shield('writing', 'case studies', 'e8e8e0')})]"
            f"({WRITING_URL})"
        )
        return line, badge

    w_label = str(entry["w_label"])
    title = str(entry["title"])
    href = str(entry["href"])
    line = f"[writing]  {w_label} · {title}"
    badge = (
        f"[![writing: {w_label}]({shield('writing', w_label, 'e8e8e0')})]"
        f"(https://atlas-systems.uk{href})"
    )
    return line, badge


def render_block(projection, deploy, writing_index_html: str | None) -> str:
    deploy_line, deploy_badge = deploy_line_and_badge(deploy)
    estate_line, estate_badge = estate_line_and_badge(projection)
    writing_line, writing_badge = writing_line_and_badge(writing_index_html)

    terminal = "\n".join(
        [
            "atlas@SPECULAR-CORE:~$ status",
            deploy_line,
            estate_line,
            writing_line,
            "atlas@SPECULAR-CORE:~$ _",
        ]
    )

    return "\n".join(
        [
            START_MARKER,
            "```text",
            terminal,
            "```",
            "",
            f"{estate_badge} {deploy_badge} {writing_badge}",
            "",
            "<sub>governed estate + live publish state · refreshes every 6 hours · "
            "updates through a validated pull request</sub>",
            END_MARKER,
        ]
    )


def apply_static_accuracy_corrections(readme_text: str) -> str:
    """Apply the two profile prose corrections that must not drift silently."""
    updated = readme_text
    for old, new in STATIC_REPLACEMENTS:
        if old in updated:
            updated = updated.replace(old, new, 1)
            continue
        if new not in updated:
            raise SystemExit(
                "error: profile static accuracy anchor drifted; inspect README before refreshing"
            )
    return updated


def splice(readme_text: str, block: str) -> str:
    if START_MARKER not in readme_text or END_MARKER not in readme_text:
        raise SystemExit(
            f"error: README.md is missing {START_MARKER} / {END_MARKER}; "
            "add both markers once, then re-run"
        )
    start = readme_text.index(START_MARKER)
    end = readme_text.index(END_MARKER)
    if end < start:
        raise SystemExit("error: ATLAS:LIVE markers are reversed in README.md")
    return readme_text[:start] + block + readme_text[end + len(END_MARKER) :]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run", action="store_true", help="print the rendered block, write nothing"
    )
    parser.add_argument(
        "--sample",
        action="store_true",
        help="render from embedded confirmed-shape samples, no network",
    )
    args = parser.parse_args()

    if args.sample:
        projection = SAMPLE_PROJECTION
        deploy = SAMPLE_DEPLOY
        writing_index_html = SAMPLE_WRITING_INDEX
    else:
        projection = fetch_json(PROJECTION_URL)
        deploy = fetch_json(DEPLOY_URL)
        writing_index_html = fetch_text(WRITING_INDEX_URL)

    block = render_block(projection, deploy, writing_index_html)

    if args.dry_run or args.sample:
        print(block)
        return 0

    existing = README_PATH.read_text(encoding="utf-8")
    updated = apply_static_accuracy_corrections(splice(existing, block))

    if updated == existing:
        print("unchanged: rendered block matches README, nothing to commit")
        return 0

    README_PATH.write_text(updated, encoding="utf-8")
    print("changed: README live block rewritten")
    return 0


SAMPLE_PROJECTION = {
    "schema_version": PROJECTION_SCHEMA,
    "authority": PROJECTION_AUTHORITY,
    "repository_count": 33,
    "repositories": [{"repository": f"AtlasReaper311/example-{i}"} for i in range(33)],
}

SAMPLE_DEPLOY = {
    "ok": True,
    "status": "success",
    "commitSha": "aeaac264616dd9fcdc8510a3886382462f3a9077",
    "createdOn": "2026-08-07T11:55:00Z",
    "endedOn": "2026-08-07T11:57:00Z",
}

SAMPLE_WRITING_INDEX = """
<div class="articles">
  <a href="#" class="article-entry coming-soon" aria-disabled="true">
    <span class="article-number">W-08</span>
    <h2 class="article-title">SPECULAR-CORE: Architectural Recovery</h2>
  </a>
  <a href="/writing/atlas-lab-observability/" class="article-entry">
    <span class="article-number">W-07</span>
    <h2 class="article-title">Atlas Lab</h2>
  </a>
  <a href="/writing/overclocking-specular-core/" class="article-entry">
    <span class="article-number">W-04</span>
    <h2 class="article-title">Pushing the Limits: Overclocking SPECULAR-CORE</h2>
  </a>
</div>
"""


if __name__ == "__main__":
    raise SystemExit(main())
