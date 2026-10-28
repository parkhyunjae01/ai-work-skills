"""Check the checked-in catalog and public-source file hashes, without network."""
import hashlib
import json
import sys
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]


def local_path(value):
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Unsafe manifest path: {value}")
    resolved = ROOT.joinpath(*path.parts)
    if not resolved.resolve().is_relative_to(ROOT):
        raise ValueError(f"Path escapes repository: {value}")
    return resolved


def verify():
    catalog = json.loads((ROOT / "catalog.json").read_text())
    lock = json.loads((ROOT / "sources.lock.json").read_text())
    errors = []
    expected = set()
    for source in lock["sources"]:
        folders = sorted(str(PurePosixPath(p).parent) for p in source["files_sha256"] if p.endswith("/SKILL.md"))
        if folders != source["included_skill_folders"]:
            errors.append(f"Skill folder inventory mismatch: {source['repository']}")
        for path, digest in source["files_sha256"].items():
            relative = f"vendor/{source['repository']}/{path}"
            expected.add(relative)
            file = local_path(relative)
            if not file.is_file():
                errors.append(f"Missing file: {relative}")
            elif hashlib.sha256(file.read_bytes()).hexdigest() != digest:
                errors.append(f"Hash mismatch: {relative}")
    actual = {str(p.relative_to(ROOT)) for p in (ROOT / "vendor").rglob("*") if p.is_file()}
    errors.extend(f"Unrecorded vendor file: {p}" for p in sorted(actual - expected))
    names = set()
    bundled = 0
    for entry in catalog["skills"]:
        if entry["name"] in names:
            errors.append(f"Duplicate catalog name: {entry['name']}")
        names.add(entry["name"])
        if entry["status"] == "bundled":
            bundled += 1
            path = local_path(entry["local_path"])
            if not path.is_file() or entry["local_path"] not in expected:
                errors.append(f"Missing bundled entry: {entry['name']}")
            elif "../../CONNECTORS.md" in path.read_text():
                if not (path.parent / "../../CONNECTORS.md").is_file():
                    errors.append(f"Missing parent connector guide: {entry['name']}")
        elif entry["status"] == "link-only":
            if "local_path" in entry or not entry.get("reason"):
                errors.append(f"Invalid link-only entry: {entry['name']}")
        else:
            errors.append(f"Invalid status: {entry['name']}")
    for path in ("README.md", "LICENSE", "SOURCES.md", "docs/CATALOG.md", "docs/MODELS.md", "docs/PLUGINS.md"):
        if not local_path(path).is_file():
            errors.append(f"Missing documentation: {path}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"OK: {len(names)} catalog entries; {bundled} bundled; {len(names)-bundled} link-only; {len(expected)} source files verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(verify())
