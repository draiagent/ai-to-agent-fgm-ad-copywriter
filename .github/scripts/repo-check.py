from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
required = [
    "README.md", "AGENTS.md", "VERSION", "CHANGELOG.md", "CONTRIBUTING.md",
    "LICENSE", "repo-metadata.json", "skill/fgm-ad-copywriter/SKILL.md",
    "skill/fgm-ad-copywriter/output-schema.json", "docs/methodology.md",
    "docs/usage.md", "docs/fact-verification.md", "docs/compliance-guardrails.md",
    "docs/validation.md", "docs/publishing.md", "docs/release-notes.md",
    "examples/product-input.json", "examples/output-example.md", "tests/test-cases.md"
]
errors = []
for rel in required:
    p = ROOT / rel
    if not p.exists() or p.stat().st_size == 0:
        errors.append(f"missing or empty: {rel}")

version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
metadata = json.loads((ROOT / "repo-metadata.json").read_text(encoding="utf-8"))
if metadata.get("version") != version:
    errors.append("VERSION and repo-metadata.json mismatch")

schema = json.loads((ROOT / "skill/fgm-ad-copywriter/output-schema.json").read_text(encoding="utf-8"))
if schema.get("title") != "FGM Ad Copywriter Output":
    errors.append("unexpected output schema title")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
for needle in ["Fact", "Gap", "Meaning", "Evidence", "Verify", "fgm-ad-copywriter"]:
    if needle not in readme:
        errors.append(f"README missing keyword: {needle}")

if errors:
    print("FAIL")
    for e in errors:
        print("-", e)
    sys.exit(1)
print("PASS: repository structure and core metadata validated")

# Release package checks (stdlib only)
import re
import hashlib
skill = (ROOT / 'skill/fgm-ad-copywriter/SKILL.md').read_text(encoding='utf-8')
assert skill.startswith('---\n'), 'missing Skill frontmatter'
frontmatter = skill.split('---', 2)[1]
assert 'name: fgm-ad-copywriter' in frontmatter and 'description:' in frontmatter
assert f'v{version}' in readme and f'[{version}]' in (ROOT/'CHANGELOG.md').read_text(encoding='utf-8')
assert f'v{version}' in (ROOT/'docs/release-notes.md').read_text(encoding='utf-8')
for md in ROOT.rglob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)', md.read_text(encoding='utf-8')):
        if '://' in target or target.startswith('#'):
            continue
        assert (md.parent / target.split('#')[0]).exists(), f'broken local link: {md.relative_to(ROOT)} -> {target}'
cards = sorted((ROOT/'assets/cards').glob('*.png'))
assert len(cards) == 6, 'expected exactly six final cards'
for i, card in enumerate(cards, 1):
    assert card.name.startswith(f'{i:02d}-')
    assert card.read_bytes().startswith(b'\x89PNG\r\n\x1a\n')
assert metadata['card_version'] == '0.1.0'
manifest = ROOT/'SHA256SUMS.txt'
listed = set()
for line in manifest.read_text(encoding='utf-8').splitlines():
    expected, rel = line.split('  ', 1)
    listed.add(rel)
    assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest() == expected, f'hash mismatch: {rel}'
actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and p.name != 'SHA256SUMS.txt'}
assert listed == actual, 'hash manifest file coverage mismatch'
print(f'PASS: Skill metadata, local links, {len(cards)} cards, version policy and {len(listed)} SHA-256 entries')
