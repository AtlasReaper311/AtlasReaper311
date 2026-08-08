#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "update_readme.py"
SPEC = importlib.util.spec_from_file_location("update_readme", MODULE_PATH)
assert SPEC and SPEC.loader
update_readme = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(update_readme)


class UpdateReadmeTests(unittest.TestCase):
    def test_estate_count_requires_atlas_infra_projection_contract(self):
        line, badge = update_readme.estate_line_and_badge(update_readme.SAMPLE_PROJECTION)
        self.assertEqual(line, "[estate]   33 governed public repos")
        self.assertIn("estate-33_repos", badge)

        drifted = dict(update_readme.SAMPLE_PROJECTION)
        drifted["repository_count"] = 34
        line, badge = update_readme.estate_line_and_badge(drifted)
        self.assertIn("couldn't confirm", line)
        self.assertIn("unconfirmed", badge)

    def test_latest_writing_ignores_coming_soon_and_selects_highest_published_w_number(self):
        latest = update_readme.latest_published_writing(update_readme.SAMPLE_WRITING_INDEX)
        self.assertIsNotNone(latest)
        assert latest is not None
        self.assertEqual(latest["w_label"], "W-07")
        self.assertEqual(latest["title"], "Atlas Lab")
        self.assertEqual(latest["href"], "/writing/atlas-lab-observability/")

    def test_rendered_block_does_not_present_account_commit_volume(self):
        block = update_readme.render_block(
            update_readme.SAMPLE_PROJECTION,
            update_readme.SAMPLE_DEPLOY,
            update_readme.SAMPLE_WRITING_INDEX,
        )
        self.assertIn("[estate]   33 governed public repos", block)
        self.assertIn("[writing]  W-07 · Atlas Lab", block)
        self.assertNotIn("[activity]", block)
        self.assertNotIn("commits in the last 90 days", block)
        self.assertNotIn("writing/manifest.json", block)

    def test_static_accuracy_corrections_are_idempotent(self):
        old_heading = "## Public repositories"
        old_paragraph = (
            "The public estate map lives in [`atlas-api-public/data/estate.manifest.json`]"
            "(https://github.com/AtlasReaper311/atlas-api-public/blob/main/data/estate.manifest.json). "
            "The public registry shows approved live Workers; the manifest describes the intentionally "
            "published architecture. Repository visibility is not inferred from account membership."
        )
        source = old_heading + "\n\n" + old_paragraph + "\n"
        corrected = update_readme.apply_static_accuracy_corrections(source)
        self.assertIn("## Selected public repositories", corrected)
        self.assertIn("atlas-infra/policy/public-repository-classifications.json", corrected)
        self.assertNotIn("The public estate map lives", corrected)
        self.assertEqual(
            update_readme.apply_static_accuracy_corrections(corrected),
            corrected,
        )

    def test_splice_changes_only_live_region(self):
        original = "before\n<!-- ATLAS:LIVE:START -->\nold\n<!-- ATLAS:LIVE:END -->\nafter\n"
        block = "<!-- ATLAS:LIVE:START -->\nnew\n<!-- ATLAS:LIVE:END -->"
        updated = update_readme.splice(original, block)
        self.assertEqual(
            updated,
            "before\n<!-- ATLAS:LIVE:START -->\nnew\n<!-- ATLAS:LIVE:END -->\nafter\n",
        )


if __name__ == "__main__":
    unittest.main()
