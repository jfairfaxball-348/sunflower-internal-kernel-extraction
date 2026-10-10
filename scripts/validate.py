#!/usr/bin/env python3
"""Validate project records; no network or proof claims."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OPEN = {"CONFIRMED_OPEN_FROM_CURRENT_AUTHORITATIVE_EVIDENCE", "STRONG_EVIDENCE_OPEN",
        "STATUS_UNCERTAIN", "ALREADY_SOLVED", "MATERIALLY_SUPERSEDED"}
REQUIRED = ["README.md", "AGENTS.md", "authoritative/START_HERE.md",
            "authoritative/STATE.json", "authoritative/PARENT_RECONCILIATION.md",
            "authoritative/STANDARDS.md", "authoritative/SESSION_PROTOCOL.md",
            "project_manifest.json", "research/TARGET.md", "research/TARGET.json",
            "research/SOURCES.json", "research/FRONTIER_AUDIT.md",
            "research/SEARCH_LOG.md", "research/NOVELTY_LEDGER.md",
            "research/CLAIMS.json", "research/DECISIONS_AND_RISKS.md",
            "formalisation/AUDIT.md", "formalisation/STATUS.json",
            "proofs/README.md", "publication/STATUS.json", "experiments/README.md",
            "experiments/SEMANTIC_FIXTURES.json", "sessions/HISTORY.md",
            "sessions/AI_USE.md", "sessions/PROGRESS_AUDITS.md",
            "sessions/P001-S000/INPUT.md", "sessions/P001-S000/INPUT_MANIFEST.json",
            "sessions/P001-S000/CLOSEOUT.md", "sessions/NEXT_SESSION.md",
            "validation/GITHUB_EVIDENCE.json", ".github/workflows/research-integrity.yml"]


def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def check_target(target):
    assert target["id"] == "TIK"
    assert target["quantifiers"] == ["forall k>=1", "exists c_k>0", "forall m>=2",
                                     "forall n>=k", "forall F subset binom([n],k)",
                                     "exists H subset F"]
    assert target["constant_depends_only_on"] == ["k"]
    assert target["retained_fraction"] == "c_k*m^(-k)"
    assert target["witness_family"] == "H"
    assert target["distinct_petals"] and target["exact_kernel"]
    assert target["empty_kernel_allowed"]
    assert not target["witness_must_include_selected_pair"]
    assert not target["common_projected_pattern_required"]


def main():
    for path in REQUIRED:
        assert (ROOT / path).is_file(), path
    for path in ROOT.rglob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))
    state, manifest = read("authoritative/STATE.json"), read("project_manifest.json")
    target = read("research/TARGET.json")
    check_target(target)
    assert manifest["project_id"] == "P001"
    assert manifest["parent"]["repository_id"] == 1412469441
    assert manifest["child"]["repository_id"] == 1412820282
    assert manifest["parent"]["repository"] == "jfairfaxball-348/sunflower-structures-programme"
    assert manifest["child"]["repository"] == "jfairfaxball-348/sunflower-internal-kernel-extraction"
    assert state["open_status"] in OPEN
    assert state["open_status"] == manifest["open_status"]
    assert state["novelty_status"] == manifest["novelty_status"]
    assert state["session_completed"] == manifest["session_completed"]
    assert state["next_session"] == manifest["next_obligation"]["session"]
    assert len(manifest["next_obligation"]["objectives"]) == 1
    assert manifest["next_obligation"]["executed"] is False
    formal, publication = read("formalisation/STATUS.json"), read("publication/STATUS.json")
    assert formal["status"] == manifest["formal_verification"]["status"]
    assert publication["status"] == manifest["publication_status"]
    if formal["status"] == "NOT_STARTED":
        assert formal["lean_version"] is None and formal["mathlib_commit"] is None
        assert formal["compiled_declarations"] == []
        assert not list((ROOT / "formalisation").rglob("*.lean"))
    if state["new_theorems"] == 0:
        assert manifest["proof_references"] == []
        assert formal["status"] == "NOT_STARTED"
    sources = read("research/SOURCES.json")
    ids = {source["id"] for source in sources}
    assert len(ids) == len(sources)
    assert {"JJSW26", "RAO26", "KUP25", "VC25", "VC26", "SHANG26", "SMALL26", "AFP21", "PAL26", "MATHLIB"} <= ids
    for source in sources:
        assert source["url"].startswith("https://") and source["locator"] and source["access_level"]
    for claim in read("research/CLAIMS.json"):
        assert set(claim["sources"]) <= ids
        assert claim["formal_status"] == "NONE"
    for receipt in sorted((ROOT / "sessions").glob("P001-S*/INPUT_MANIFEST.json")):
        prompt = json.loads(receipt.read_text(encoding="utf-8"))
        actual = hashlib.sha256((ROOT / prompt["path"]).read_bytes()).hexdigest()
        assert actual == prompt["sha256"], ("Incoming prompt changed", receipt)
    if state["session_completed"] == "P001-S001":
        for path in ["sessions/P001-S001/INPUT.md", "sessions/P001-S001/INPUT_MANIFEST.json",
                     "sessions/P001-S001/CLOSEOUT.md", "sessions/P001-S001/ENTRY_EVIDENCE.json",
                     "sessions/P001-S001/SOURCE_RECEIPT.json", "research/S001_N1.md",
                     "research/R3_FEASIBILITY.md"]:
            assert (ROOT / path).is_file(), path
        assert state["new_theorems"] == 0
        assert state["restricted_rank3_open_status"] == "STATUS_UNCERTAIN"
        assert state["last_outcome"] == "MECHANISM_OBSTRUCTION_AND_REMAINING_LEMMA"
        assert manifest["next_obligation"]["objectives"] == ["L_AVG"]
        assert state["next_session"] == "P001-S002"
        assert not (ROOT / "sessions/P001-S002").exists(), "Successor must not execute in S001"
    if state["session_completed"] == "P001-S002":
        for path in ["sessions/P001-S002/INPUT.md", "sessions/P001-S002/INPUT_MANIFEST.json",
                     "sessions/P001-S002/CLOSEOUT.md", "research/S002_N1.md",
                     "research/L_AVG_FEASIBILITY.md", "sessions/P001-S002/ENTRY_EVIDENCE.json"]:
            assert (ROOT / path).is_file(), path
        assert state["new_theorems"] == 0
        assert state["restricted_rank3_open_status"] == "STATUS_UNCERTAIN"
        assert state["last_outcome"] == "RESTRICTED_SUNFLOWER_FREE_BOUND_GENERAL_L_AVG_UNRESOLVED"
        assert manifest["next_obligation"]["objectives"] == ["L_AVG_HEAVY_LINK_CHARGING"]
        assert state["next_session"] == "P001-S003"
        assert not (ROOT / "sessions/P001-S003").exists(), "Successor must not execute in S002"
    handoff = (ROOT / "sessions/NEXT_SESSION.md").read_text()
    assert state["next_session"] in handoff and "STOP" in handoff and "R3" in handoff
    if state["session_completed"] == "P001-S000":
        assert not (ROOT / "sessions/P001-S001").exists(), "Successor must not execute in bootstrap"
    fixture = read("experiments/SEMANTIC_FIXTURES.json")
    assert fixture["kind"] == "FIXED_SEMANTIC_CONTROLS_NOT_RESEARCH_ENUMERATION"
    assert fixture["resource_limits"]["seconds"] <= 10
    assert len(fixture["cases"]) == 10
    for case in fixture["cases"]:
        assert len(case["ambient"]) <= 6 and case["m"] <= 3
    evidence = read("validation/GITHUB_EVIDENCE.json")
    sha = manifest["latest_validated_commit"]
    if sha is not None:
        assert re.fullmatch(r"[0-9a-f]{40}", sha)
        assert any(r["head_sha"] == sha and r["conclusion"] == "success"
                   and r["jobs"] and all(j["conclusion"] == "success" for j in r["jobs"])
                   for r in evidence["child_runs"])
    # Approval staging is not a substantive child session. Verify exact approved-draft and outgoing handoff bytes.
    approval_path = ROOT / "sessions/P001-S006/APPROVAL_MANIFEST.json"
    if approval_path.exists() and state["session_completed"] == "P001-S005":
        approval = json.loads(approval_path.read_text(encoding="utf-8"))
        assert approval["stage"] == "HANDOFF_APPROVED_NOT_EXECUTED"
        assert approval["session"] == "P001-S006" and approval["session_executed"] is False
        assert state["session_completed"] == "P001-S005"
        assert state["next_session"] == "P001-S006" and state["next_executed"] is False
        assert state["next_objective"] == "BLOCK_COMPATIBILITY_FEASIBILITY_GATE"
        assert manifest["next_obligation"]["objectives"] == ["BLOCK_COMPATIBILITY_FEASIBILITY_GATE"]
        assert hashlib.sha256((ROOT / approval["approved_draft_path"]).read_bytes()).hexdigest() == approval["approved_draft_sha256"]
        assert hashlib.sha256((ROOT / approval["executable_path"]).read_bytes()).hexdigest() == approval["executable_sha256"]
        assert not (ROOT / "sessions/P001-S006/INPUT.md").exists(), "S006 must not be executed during approval staging"
        assert not (ROOT / "sessions/P001-S006/CLOSEOUT.md").exists(), "S006 must not be closed during approval staging"
    if state["session_completed"] == "P001-S006":
        for path in ["sessions/P001-S006/INPUT.md", "sessions/P001-S006/INPUT_MANIFEST.json",
                     "sessions/P001-S006/CLOSEOUT.md", "sessions/P001-S006/ENTRY_EVIDENCE.json",
                     "research/S006_N1_BLOCK_COMPATIBILITY.md",
                     "research/S006_BLOCK_COMPATIBILITY_SPEC.md",
                     "research/S006_BLOCK_COMPATIBILITY_ANALYSIS.md"]:
            assert (ROOT / path).is_file(), path
        assert state["next_session"] == "P001-S007"
        assert state["last_outcome"] == "RESTRICTED_BSEL_ONLY"
        assert manifest["next_obligation"]["objectives"] == ["HUMAN_BLOCK_COMPATIBILITY_DECISION_GATE"]
        assert state["new_theorems"] == 0 and state["restricted_rank3_open_status"] == "STATUS_UNCERTAIN"
    # Check relative documentation links resolve, excluding remote and fragment-only links.
    for path in ROOT.rglob("*.md"):
        for ref in re.findall(r"\]\(([^\s)]+)\)", path.read_text(encoding="utf-8")):
            if "://" not in ref and not ref.startswith("#"):
                assert (path.parent / ref.split("#")[0]).exists(), (path, ref)
    print("PASS: structure, JSON, quantifiers, witness semantics, statuses, source links, prompt hash, one successor and observed CI receipts")


if __name__ == "__main__":
    main()
