#!/usr/bin/env python3
"""Regenerate the live block in the profile README.

Fetches three read-only public sources and rewrites ONLY the content
between the ATLAS:LIVE markers, so hand-written bio text survives every
run untouched:

  /pulse                 aggregate GitHub stats (KV-cached hourly upstream)
  /deploy-watch/latest   latest Cloudflare Pages deploy snapshot
  writing/manifest.json  published case studies (flat array, may not exist)

Response shapes were confirmed against the live endpoints on 2026-07-13;
the SAMPLE_* constants at the bottom document them and drive --sample.

Failure policy, per source:
  data source unreachable  -> honest "couldn't confirm" line, run continues
  README markers missing   -> hard failure; that's a config error a human
                              must fix, and failing loudly is the fix

Nothing here embeds a fetch timestamp. Identical upstream data renders to
identical bytes, so the workflow's diff-before-commit step can skip runs
where nothing genuinely changed. Stdlib only: no pip step in the workflow,
one fewer thing to break.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

PULSE_URL = "https://api.atlas-systems.uk/pulse"
DEPLOY_URL = "https://api.atlas-systems.uk/deploy-watch/latest"
MANIFEST_URL = "https://atlas-systems.uk/writing/manifest.json"
WRITING_URL = "https://atlas-systems.uk/writing/"

README_PATH = Path(__file__).resolve().parent.parent / "README.md"
START_MARKER = "<!-- ATLAS:LIVE:START -->"
END_MARKER = "<!-- ATLAS:LIVE:END -->"

TIMEOUT_SECONDS = 10
USER_AGENT = "atlas-readme-refresh (github.com/AtlasReaper311/AtlasReaper311)"

# Terminal status glyphs stay monochrome text inside the code block; the
# colour signal lives in the shields badge below it. Emoji dots in a README
# would fight the estate's restraint.
STATUS_WORDS = {
    "success": ("operational", "4ade80"),
    "failure": ("failing", "e24b4a"),
    "canceled": ("canceled", "aaa9a0"),
    "unknown": ("unknown", "555560"),
}
BUILDING = ("building", "f5a623")  # any other status means in progress


def fetch_json(url: str):
    """One source, one honest outcome: parsed JSON or None."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            if response.status != 200:
                print(f"warning: {url} returned {response.status}", file=sys.stderr)
                return None
            return json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        print(f"warning: couldn't fetch {url}: {exc}", file=sys.stderr)
        return None


def iso_to_display(raw) -> str | None:
    """ISO timestamp -> 'YYYY-MM-DD HH:MM UTC', or None if unparseable."""
    if not isinstance(raw, str):
        return None
    try:
        parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def shield(label: str, message: str, color: str) -> str:
    def esc(text: str) -> str:
        return (
            text.replace("-", "--").replace("_", "__").replace(" ", "_").replace("/", "%2F")
        )

    return (
        f"https://img.shields.io/badge/{esc(label)}-{esc(message)}-{color}"
        "?style=flat-square&labelColor=0a0a0f"
    )


# ------------------------------------------------------------- renderers


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


def pulse_lines_and_badge(pulse) -> tuple[list[str], str]:
    totals = pulse.get("totals") if isinstance(pulse, dict) else None
    if not isinstance(totals, dict):
        lines = ["[estate]   ? couldn't confirm estate stats at last refresh"]
        return lines, f"![estate]({shield('estate', 'unconfirmed', '555560')})"

    repos = totals.get("publicRepos")
    stars = totals.get("stars")
    commits = totals.get("commitsLast90Days")

    repo_text = f"{repos} public repos" if isinstance(repos, int) else "repos unconfirmed"
    star_text = f" · {stars} stars" if isinstance(stars, int) else ""
    lines = [f"[estate]   {repo_text}{star_text}"]
    if isinstance(commits, int):
        lines.append(f"[activity] {commits} commits in the last 90 days")

    message = f"{repos} repos" if isinstance(repos, int) else "unconfirmed"
    return lines, f"![estate: {message}]({shield('estate', message, 'f5a623')})"


def latest_case_study(manifest):
    """Newest published entry, or None. The consumer sorts by date itself
    rather than trusting the file's order; a manifest is data, not a
    promise about ordering."""
    if not isinstance(manifest, list):
        return None
    dated = [
        entry
        for entry in manifest
        if isinstance(entry, dict)
        and isinstance(entry.get("slug"), str)
        and isinstance(entry.get("date"), str)
    ]
    if not dated:
        return None
    return sorted(dated, key=lambda entry: entry["date"], reverse=True)[0]


def writing_line_and_badge(manifest) -> tuple[str, str]:
    entry = latest_case_study(manifest)
    if entry is None:
        # The manifest is a recommendation, not yet a guarantee; degrade to
        # a plain pointer instead of failing the whole refresh.
        line = "[writing]  latest case study: atlas-systems.uk/writing"
        badge = f"[![writing: case studies]({shield('writing', 'case studies', 'e8e8e0')})]({WRITING_URL})"
        return line, badge

    w_number = str(entry.get("w_number") or "W-??")
    title = str(entry.get("title") or entry["slug"])
    line = f"[writing]  {w_number} · {title} · {entry['date']}"
    url = f"{WRITING_URL}{entry['slug']}/"
    badge = f"[![writing: {w_number}]({shield('writing', w_number, 'e8e8e0')})]({url})"
    return line, badge


def render_block(pulse, deploy, manifest) -> str:
    deploy_line, deploy_badge = deploy_line_and_badge(deploy)
    pulse_lines, pulse_badge = pulse_lines_and_badge(pulse)
    writing_line, writing_badge = writing_line_and_badge(manifest)

    # `status` is a real command in the estate shell overlay on
    # atlas-systems.uk; the profile README speaks the same dialect.
    terminal = "\n".join(
        [
            "atlas@SPECULAR-CORE:~$ status",
            deploy_line,
            *pulse_lines,
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
            f"{pulse_badge} {deploy_badge} {writing_badge}",
            "",
            "<sub>live estate telemetry · regenerates every 6 hours · "
            "commits only on genuine change</sub>",
            END_MARKER,
        ]
    )


# ------------------------------------------------------------------ main


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
    return readme_text[:start] + block + readme_text[end + len(END_MARKER):]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run", action="store_true", help="print the rendered block, write nothing"
    )
    parser.add_argument(
        "--sample",
        action="store_true",
        help="render from the embedded confirmed-shape samples, no network",
    )
    args = parser.parse_args()

    if args.sample:
        pulse, deploy, manifest = SAMPLE_PULSE, SAMPLE_DEPLOY, SAMPLE_MANIFEST
    else:
        pulse = fetch_json(PULSE_URL)
        deploy = fetch_json(DEPLOY_URL)
        manifest = fetch_json(MANIFEST_URL)

    block = render_block(pulse, deploy, manifest)

    if args.dry_run or args.sample:
        print(block)
        return 0

    existing = README_PATH.read_text(encoding="utf-8")
    updated = splice(existing, block)

    if updated == existing:
        print("unchanged: rendered block matches README, nothing to commit")
        return 0

    README_PATH.write_text(updated, encoding="utf-8")
    print("changed: README live block rewritten")
    return 0


# Shapes confirmed against the live endpoints, 2026-07-13. Trimmed to the
# fields this script reads; the real payloads carry more.
SAMPLE_PULSE = {
    "generatedAt": "2026-07-13T14:31:31.415Z",
    "user": "AtlasReaper311",
    "totals": {"publicRepos": 24, "stars": 11, "commitsLast90Days": 478},
}

SAMPLE_DEPLOY = {
    "ok": True,
    "deployId": "15034c61-0297-4846-ac3c-d68c4fc55d41",
    "status": "success",  # success | failure | canceled | anything-else=building
    "branch": "main",
    "commitSha": "55f3e6b",
    "createdOn": "2026-07-08T17:14:16.261773Z",
    "endedOn": "2026-07-08T17:14:18.793486Z",
    "checkedAt": "2026-07-08T17:15:46.284Z",
}

SAMPLE_MANIFEST = [
    {
        "slug": "overclocking-specular-core",
        "title": "Overclocking SPECULAR-CORE",
        "date": "2026-06-22",
        "w_number": "W-04",
    }
]


if __name__ == "__main__":
    raise SystemExit(main())
