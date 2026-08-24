from pathlib import Path

from rules.case_loader import load_case
from rules.gateway_rules import diagnose_default_gateway


def test_wrong_default_gateway_detection():
    """
    CASE001 should be detected as a wrong default gateway.
    """

    project_root = Path(__file__).resolve().parent.parent

    case_path = (
        project_root
        / "data"
        / "cases"
        / "CASE001_Wrong_Default_Gateway"
        / "case.json"
    )

    case_data = load_case(case_path)

    diagnosis = diagnose_default_gateway(case_data)

    assert diagnosis["fault_detected"] is True
    assert diagnosis["diagnosis"] == "Wrong Default Gateway"
    assert diagnosis["faulty_device"] == "PC1"
    assert diagnosis["configured_gateway"] == "192.168.10.254"
    assert diagnosis["expected_gateway"] == "192.168.10.1"
    assert diagnosis["osi_layer"] == "Layer 3"
    assert diagnosis["confidence"] == "High"