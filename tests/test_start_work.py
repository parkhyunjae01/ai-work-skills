"""Meaningful filesystem checks for the optional template copier."""

import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "start_work.py"
SPEC = importlib.util.spec_from_file_location("start_work", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class WorkTemplateTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        # macOS may expose its temporary directory through /var -> /private/var.
        self.root = Path(self.temporary.name).resolve()
        self.destination = self.root / "work-notes"

    def tearDown(self):
        self.temporary.cleanup()

    def run_cli(self, *extra):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--destination", str(self.destination), *extra],
            capture_output=True, text=True,
        )

    def test_creates_exact_templates_without_activating_agents(self):
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual({p.name for p in self.destination.iterdir()}, set(MODULE.FILES))
        for name in MODULE.FILES:
            self.assertEqual((self.destination / name).read_bytes(), (MODULE.TEMPLATE_ROOT / name).read_bytes())
        self.assertFalse((self.destination / "AGENTS.md").exists())

    def test_existing_folder_and_existing_file_are_preserved(self):
        self.destination.mkdir()
        sentinel = self.destination / "TASK.md"
        sentinel.write_text("existing work", encoding="utf-8")
        result = self.run_cli()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(sentinel.read_text(), "existing work")
        self.assertEqual(list(self.destination.iterdir()), [sentinel])
        file_destination = self.root / "existing-file"
        file_destination.write_text("keep", encoding="utf-8")
        with self.assertRaises(ValueError):
            MODULE.initialize(str(file_destination))
        self.assertEqual(file_destination.read_text(), "keep")

    def test_dry_run_writes_nothing(self):
        result = self.run_cli("--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_symlink_parent_and_destination_are_rejected(self):
        real = self.root / "real"
        real.mkdir()
        link = self.root / "link"
        link.symlink_to(real, target_is_directory=True)
        with self.assertRaises(ValueError):
            MODULE.initialize(str(link / "notes"))
        self.assertEqual(list(real.iterdir()), [])
        dangling = self.root / "dangling"
        dangling.symlink_to(self.root / "missing", target_is_directory=True)
        with self.assertRaises(ValueError):
            MODULE.initialize(str(dangling))
        self.assertTrue(dangling.is_symlink())

    def test_missing_parent_and_traversal_are_rejected(self):
        with self.assertRaises(ValueError):
            MODULE.initialize(str(self.root / "missing" / "notes"))
        with self.assertRaises(ValueError):
            MODULE.initialize(str(self.root / "missing" / ".." / "notes"))
        self.assertEqual(list(self.root.iterdir()), [])

    def test_missing_source_does_not_leave_destination(self):
        original = MODULE.TEMPLATE_ROOT
        try:
            MODULE.TEMPLATE_ROOT = self.root / "no-templates"
            with self.assertRaises(ValueError):
                MODULE.initialize(str(self.destination))
        finally:
            MODULE.TEMPLATE_ROOT = original
        self.assertFalse(self.destination.exists())


if __name__ == "__main__":
    unittest.main()
