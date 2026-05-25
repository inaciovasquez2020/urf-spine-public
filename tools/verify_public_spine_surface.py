#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]

required_files = [
    "README.md",
    "examples/minimal_certificate/minimal_spine_certificate.json",
]

for rel in required_files:
    if not (root / rel).exists():
        raise SystemExit(f"missing required file: {rel}")

readme = (root / "README.md").read_text()

required_readme_tokens = [
    "Public audit surface",
    "sanitized public mirror",
    "not theorem-prover-complete",
    "not a primary mathematics-closure repository",
    "do not constitute theorem-level closure",
]

for token in required_readme_tokens:
    if token not in readme:
        raise SystemExit(f"missing README token: {token}")

cert = json.loads((root / "examples/minimal_certificate/minimal_spine_certificate.json").read_text())

if cert.get("status") != "PUBLIC_AUDIT_SURFACE_ONLY":
    raise SystemExit("invalid certificate status")

required_boundaries = [
    "not theorem-prover-complete",
    "not a primary mathematics-closure repository",
    "does not prove unrestricted Chronos-RR",
    "does not prove unrestricted H4.1/FGL",
    "does not prove P vs NP",
    "does not prove any Clay problem",
]

for token in required_boundaries:
    if token not in cert.get("boundaries", []):
        raise SystemExit(f"missing boundary: {token}")

print("PUBLIC_SPINE_SURFACE_OK")
