"""
Verifier for the log-report task.

Ground truth is derived from the access.log shipped with the task:
  total_requests = 6
  unique_ips     = 3
  top_path       = "/index.html"

A no-op agent (produces no file) must score 0.
A trivially non-empty file that is not valid JSON must score 0.
A file with wrong values must score 0.
Only the correct report scores 1.
"""

import json
from pathlib import Path

REPORT = Path("/app/report.json")

EXPECTED_TOTAL    = 6
EXPECTED_UNIQUE   = 3
EXPECTED_TOP_PATH = "/index.html"


def _load():
    """Load and parse report.json, failing clearly if absent or malformed."""
    assert REPORT.exists(), (
        f"{REPORT} not found — agent did not produce the report"
    )
    text = REPORT.read_text().strip()
    assert text, f"{REPORT} is empty"
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise AssertionError(f"{REPORT} is not valid JSON: {exc}") from exc


def test_total_requests():
    """total_requests must equal the number of lines in the log (6)."""
    data = _load()
    assert "total_requests" in data, "key 'total_requests' missing from report"
    assert data["total_requests"] == EXPECTED_TOTAL, (
        f"total_requests: expected {EXPECTED_TOTAL}, got {data['total_requests']}"
    )


def test_unique_ips():
    """unique_ips must equal the number of distinct IPs in the log (3)."""
    data = _load()
    assert "unique_ips" in data, "key 'unique_ips' missing from report"
    assert data["unique_ips"] == EXPECTED_UNIQUE, (
        f"unique_ips: expected {EXPECTED_UNIQUE}, got {data['unique_ips']}"
    )


def test_top_path():
    """top_path must be the most-requested URL path ('/index.html')."""
    data = _load()
    assert "top_path" in data, "key 'top_path' missing from report"
    assert data["top_path"] == EXPECTED_TOP_PATH, (
        f"top_path: expected '{EXPECTED_TOP_PATH}', got '{data['top_path']}'"
    )
