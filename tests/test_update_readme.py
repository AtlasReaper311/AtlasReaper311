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

    def test_static_prose_is_not_rewritten_by_updater(self):
        original = (
            "before\n## Public repositories\n"
            "<!-- ATLAS:LIVE:START -->\nold\n<!-- ATLAS:LIVE:END -->\n"
            "after\n"
        )
        block = "<!-- ATLAS:LIVE:START -->\nnew\n<!-- ATLAS:LIVE:END -->"
        updated = update_readme.splice(original, block)
        self.assertEqual(
            updated,
            "before\n## Public repositories\n"
            "<!-- ATLAS:LIVE:START -->\nnew\n<!-- ATLAS:LIVE:END -->\n"
            "after\n",
        )

    def test_splice_preserves_bytes_outside_live_region(self):
        prefix = "prefix\n\N{SNOWMAN}\n"
        suffix = "\n## Static profile prose\nunchanged\n"
        original = prefix + "<!-- ATLAS:LIVE:START -->\nold\n<!-- ATLAS:LIVE:END -->" + suffix
        block = "<!-- ATLAS:LIVE:START -->\nnew\n<!-- ATLAS:LIVE:END -->"
        updated = update_readme.splice(original, block)
        self.assertTrue(updated.startswith(prefix))
        self.assertTrue(updated.endswith(suffix))

    def test_render_block_is_deterministic(self):
        first = update_readme.render_block(
            update_readme.SAMPLE_PROJECTION,
            update_readme.SAMPLE_DEPLOY,
            update_readme.SAMPLE_WRITING_INDEX,
        )
        second = update_readme.render_block(
            update_readme.SAMPLE_PROJECTION,
            update_readme.SAMPLE_DEPLOY,
            update_readme.SAMPLE_WRITING_INDEX,
        )
        self.assertEqual(first, second)

    def test_migration_static_replacements_are_removed(self):
        self.assertFalse(hasattr(update_readme, "STATIC_REPLACEMENTS"))


if __name__ == "__main__":
    unittest.main()
