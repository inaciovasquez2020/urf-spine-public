#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]

required_files = [
    "README.md",
    "examples/minimal_certificate/minimal_spine_certificate.json",
    "examples/reduction_hardening/public_reduction_hardening_target.json",
    "docs/status/PUBLIC_REDUCTION_HARDENING_TARGET_2026_06_23.md",
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


target = json.loads((root / "examples/reduction_hardening/public_reduction_hardening_target.json").read_text())
target_doc = (root / "docs/status/PUBLIC_REDUCTION_HARDENING_TARGET_2026_06_23.md").read_text()

if target.get("status") != "EXECUTABLE_REDUCTION_HARDENING_TARGET_ONLY":
    raise SystemExit("invalid reduction hardening target status")

if target.get("theorem_closure") is not False:
    raise SystemExit("reduction hardening target must not claim theorem closure")

if target.get("target_object", {}).get("name") != "PublicSpineExecutableReductionHardeningTarget":
    raise SystemExit("missing reduction hardening target object")

required_target_blockers = [
    "public reduction template manifest is present",
    "fixed-seed public reduction scripts are present",
    "hash-bound public gadget catalog is present",
    "verifier hook checks template-to-certificate binding",
]

for token in required_target_blockers:
    if token not in target.get("blocked_until", []):
        raise SystemExit(f"missing reduction hardening blocker: {token}")

required_target_boundaries = [
    "does not prove unrestricted Chronos-RR",
    "does not prove unrestricted H4.1/FGL",
    "does not prove P vs NP",
    "does not prove any Clay problem",
    "does not assert theorem-level reduction completeness",
    "does not assert external validation or peer-reviewed acceptance",
]

for token in required_target_boundaries:
    if token not in target.get("non_claims", []):
        raise SystemExit(f"missing reduction hardening boundary: {token}")

required_doc_tokens = [
    "Status: `EXECUTABLE_REDUCTION_HARDENING_TARGET_ONLY`",
    "PublicSpineExecutableReductionHardeningTarget",
    "versioned reduction template manifest",
    "fixed-seed reduction script inventory",
    "hash-bound gadget catalog",
    "verifier hook binding each public template to a finite certificate",
    "does not assert theorem-level reduction completeness",
]

for token in required_doc_tokens:
    if token not in target_doc:
        raise SystemExit(f"missing reduction hardening doc token: {token}")

print("PUBLIC_SPINE_SURFACE_OK")
