"""Integration tests against live Pepkio Tools API (local and production)."""

from __future__ import annotations

import os

import pytest

from pepkio_dna_revcomp_primer_toolkit.client import PepkioClient

ENVIRONMENTS = [
    ("local", "https://tools.localtest.me"),
    ("production", "https://tools.pepkio.com"),
]


def _api_key_for(base_url: str) -> str | None:
    if "localtest.me" in base_url:
        return os.getenv("LOCAL_PEPKIO_API_KEY")
    return os.getenv("PEPKIO_API_KEY")


@pytest.fixture(params=ENVIRONMENTS, ids=["local", "production"])
def live_client(request):
    env_name, default_base_url = request.param
    override_url = os.getenv("PEPKIO_API_BASE_URL")
    if override_url:
        if (env_name == "local" and "localtest" not in override_url) or (
            env_name == "production" and "localtest" in override_url
        ):
            pytest.skip(f"Skipping {env_name} because PEPKIO_API_BASE_URL={override_url}")
        base_url = override_url
    else:
        base_url = default_base_url

    api_key = _api_key_for(base_url)

    if not api_key:
        pytest.skip(f"No API key for {env_name} environment")

    with PepkioClient(api_key=api_key, base_url=base_url) as client:
        yield client


def test_get_manifest(live_client: PepkioClient):
    manifest = live_client.get_manifest(refresh=True)
    assert manifest["tool_id"] == "dna-revcomp-primer-toolkit"
    names = live_client.list_examples()
    assert "single_gapdh_primer" in names


def test_run_single_gapdh_primer_example(live_client: PepkioClient):
    inp = live_client.get_example_input("single_gapdh_primer")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.run_id
    assert result.permalink
    assert result.result is not None
    assert result.result.get("mode") == "single"
    assert result.result["single"]["rev_complement"] == "GACTCCGACCTTCACCTTC"
    assert result.result.get("error") is None

    # Test get_run with returned run_id
    fetched_run = live_client.get_run(result.run_id)
    assert fetched_run.run_id == result.run_id
    assert fetched_run.status == "completed"


def test_run_batch_two_primers_example(live_client: PepkioClient):
    inp = live_client.get_example_input("batch_two_primers")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.result is not None
    assert result.result.get("mode") == "batch"
    assert isinstance(result.result.get("batch"), list)
    assert len(result.result["batch"]) >= 1
