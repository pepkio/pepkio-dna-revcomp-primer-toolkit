"""Test configuration and fixtures."""

from __future__ import annotations

from pathlib import Path

import pytest
from dotenv import load_dotenv

# Load .env from workspace root or parent dirs if available
root_env = Path(__file__).resolve().parents[3] / ".env"
if root_env.exists():
    load_dotenv(root_env)
else:
    load_dotenv()


@pytest.fixture
def mock_manifest():
    return {
        "schema_version": "1.0",
        "tool_id": "dna-revcomp-primer-toolkit",
        "title": "DNA RevComp & Primer Toolkit",
        "description": "Reverse, complement, and reverse-complement DNA",
        "tags": ["dna", "primer", "revcomp"],
        "category": "sequence-oligo",
        "execution_mode": "sync",
        "input": {
            "type": "object",
            "required": ["mode"],
            "properties": {
                "mode": {"type": "string"},
                "sequence": {"type": "string"},
            },
        },
        "examples": [
            {
                "name": "single_gapdh_primer",
                "input": {
                    "mode": "single",
                    "sequence": "GAAGGTGAAGGTCGGAGTC",
                    "uppercase": True,
                    "line_wrap": "none",
                    "output_nucleotide": "dna",
                },
                "output": {
                    "single": {
                        "rev_complement": "GACTCCGACCTTCACCTTC",
                    }
                },
            },
            {
                "name": "batch_two_primers",
                "input": {
                    "mode": "batch",
                    "batch_text": "GAPDH_F,GAAGGTGAAGGTCGGAGTC\nACTB_F,GGCTGGGGTGTTGAAGGT\n",
                },
                "output": {"batch": [{"name": "GAPDH_F"}]},
            },
        ],
    }


@pytest.fixture
def mock_run_response():
    return {
        "run_id": "run_test123",
        "status": "completed",
        "result": {
            "mode": "single",
            "single": {
                "input": "GAAGGTGAAGGTCGGAGTC",
                "rev_complement": "GACTCCGACCTTCACCTTC",
                "qc": {"gc_percent": 57.9, "tm_wallace_c": 60, "length_nt": 19},
            },
            "warnings": [],
        },
        "error": None,
        "result_url": "https://tools.example.com/api/tools/v1/runs/run_test123",
        "permalink": "https://tools.example.com/r/run_test123",
    }
