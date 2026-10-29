"""Verify the extension catalog and pinned source bytes; no network or execution."""

import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def within(root, value):
    path = PurePosixPath(value)
    if path.is_absolute() or '..' in path.parts or '\\' in value:
        raise ValueError(f'Unsafe relative path: {value}')
    target = root.joinpath(*path.parts)
    if not target.resolve().is_relative_to(root.resolve()):
        raise ValueError(f'Path escapes repository: {value}')
    return target


def verify(root=ROOT):
    errors = []
    catalog = json.loads((root / 'resources.json').read_text())
    lock = json.loads((root / 'resources.lock.json').read_text())
    expected = set()
    repos = set()
    for item in lock['files']:
        relative = item['local_path']
        if relative in expected:
            errors.append(f'Duplicate source: {relative}')
        expected.add(relative)
        repos.add(item['repository'])
        if relative != f"extras/{item['repository']}/{item['path']}":
            errors.append(f'Unexpected source layout: {relative}')
        if not re.fullmatch(r'[0-9a-f]{40}', item['ref']):
            errors.append(f'Unpinned source ref: {relative}')
        if item['url'] != f"https://raw.githubusercontent.com/{item['repository']}/{item['ref']}/{item['path']}":
            errors.append(f'Source URL/ref mismatch: {relative}')
        file = within(root, relative)
        if file.is_symlink() or not file.is_file():
            errors.append(f'Missing or unsafe source: {relative}')
            continue
        payload = file.read_bytes()
        if len(payload) != item['bytes'] or hashlib.sha256(payload).hexdigest() != item['sha256']:
            errors.append(f'Source bytes mismatch: {relative}')
    actual = {str(p.relative_to(root)) for p in (root / 'extras').rglob('*') if p.is_file()}
    errors += [f'Unrecorded extra: {p}' for p in sorted(actual - expected - {'extras/README.md'})]
    for repo in repos:
        if f'extras/{repo}/LICENSE' not in expected:
            errors.append(f'License missing from manifest: {repo}')

    ids = set()
    for item in catalog['resources']:
        if item['id'] in ids:
            errors.append(f'Duplicate resource id: {item["id"]}')
        ids.add(item['id'])
        if not item['url'].startswith('https://'):
            errors.append(f'Invalid source URL: {item["id"]}')
        mode = item['distribution']
        if mode not in ('selected-files', 'link-only', 'existing-skills'):
            errors.append(f'Invalid distribution: {item["id"]}')
        if mode == 'link-only' and item['local_paths']:
            errors.append(f'Unexpected bundled paths: {item["id"]}')
        if mode != 'link-only' and not item['local_paths']:
            errors.append(f'Missing local paths: {item["id"]}')
        for path in item['local_paths']:
            if not within(root, path).is_file():
                errors.append(f'Missing resource entry: {path}')
            if mode == 'selected-files' and path not in expected:
                errors.append(f'Unpinned resource entry: {path}')

    for path in ('docs/START_HERE.md', 'docs/HARNESSES.md', 'docs/TOOLKIT.md',
                 'extras/README.md', 'templates/work-session/README.md', 'scripts/start_work.py'):
        if not within(root, path).is_file():
            errors.append(f'Missing guide or utility: {path}')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'OK: {len(ids)} resources; {len(expected)} pinned extra files; {len(repos)} source licenses.')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(verify())
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f'Error: {error}', file=sys.stderr)
        raise SystemExit(1)
