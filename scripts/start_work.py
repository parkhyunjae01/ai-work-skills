"""Copy optional work-note templates into a new folder; no network or AI calls."""

import argparse
import os
from pathlib import Path
import sys


TEMPLATE_ROOT = Path(__file__).resolve().parents[1] / "templates" / "work-session"
FILES = (
    "README.md", "TASK.md", "PLAN.md", "PROGRESS.md", "SOURCES.md",
    "DECISIONS.md", "VERIFICATION.md", "HANDOFF.md", "SUBMISSION.md",
    "AGENTS.example.md",
)


def new_destination(value):
    """Reject existing destinations, traversal, and symlinks at any path level."""
    supplied = Path(value).expanduser()
    if ".." in supplied.parts:
        raise ValueError("Use a path without '..'; supply the actual absolute path.")
    destination = Path(os.path.abspath(supplied))
    for component in (*reversed(destination.parents), destination):
        if component.is_symlink():
            raise ValueError(f"Symlink paths are not supported: {component}")
    if destination.exists():
        raise ValueError(f"Destination already exists; nothing will be overwritten: {destination}")
    if not destination.parent.is_dir():
        raise ValueError(f"Parent directory must already exist: {destination.parent}")
    return destination


def initialize(destination, dry_run=False):
    destination = new_destination(destination)
    contents = {}
    for name in FILES:
        source = TEMPLATE_ROOT / name
        if source.is_symlink() or not source.is_file():
            raise ValueError(f"Missing or unsafe template file: {source}")
        contents[name] = source.read_bytes()

    if dry_run:
        print(f"Dry run: would create {destination} with {len(contents)} template files.")
        return

    # mkdir is exclusive: if the destination appeared after validation, stop.
    destination.mkdir()
    for name, content in contents.items():
        # Exclusive mode also prevents overwriting a file created concurrently.
        with (destination / name).open("xb") as output:
            output.write(content)
    print(f"Created {len(contents)} work-note templates in {destination}")
    print("Start with TASK.md, PLAN.md and PROGRESS.md. AGENTS.example.md is not auto-applied.")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", required=True, help="New folder under an existing real directory")
    parser.add_argument("--dry-run", action="store_true", help="Validate and show the plan without writing")
    args = parser.parse_args(argv)
    try:
        initialize(args.destination, args.dry_run)
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
