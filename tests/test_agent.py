from fastapi.testclient import TestClient
from docagent.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'draft the runbook outline', **{'payload': {'headings': ['Detect', 'Mitigate', 'Rollback']}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["outline"][0] == "Detect"
    refused = client.post("/agent/run", json={"goal": 'publish this to the wiki'}).json()
    assert refused["refused"] is True
