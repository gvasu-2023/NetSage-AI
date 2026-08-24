from pathlib import Path

from rules.case_loader import load_case
from rules.vlan_rules import diagnose_vlan_assignment


def test_wrong_vlan_assignment_detection():
    """
    CASE002 should be detected as a wrong VLAN assignment.
    """

    project_root = Path(__file__).resolve().parent.parent

    case_path = (
        project_root
        / "data"
        / "cases"
        / "CASE002_Wrong_VLAN_Assignment"
        / "case.json"
    )

    case_data = load_case(case_path)

    diagnosis = diagnose_vlan_assignment(case_data)

    assert diagnosis["fault_detected"] is True
    assert diagnosis["category"] == "VLAN"
    assert diagnosis["diagnosis"] == "Wrong VLAN Assignment"
    assert diagnosis["faulty_device"] == "SW1"
    assert diagnosis["faulty_interface"] == "Fa0/2"
    assert diagnosis["actual_vlan"] == 10
    assert diagnosis["expected_vlan"] == 20
    assert diagnosis["osi_layer"] == "Layer 2"
    assert diagnosis["confidence"] == "High"