from rules.interface_rules import (
    diagnose_interface_administratively_down
)


def test_interface_administratively_down():
    case_data = {
        "category": "Interface",
        "topology": {
            "faulty_device": "SW1",
            "faulty_interface": "Fa0/1",
            "connected_device": "PC1"
        },
        "interface": {
            "name": "Fa0/1",
            "admin_status": "down",
            "oper_status": "down",
            "status_reason": "administratively down"
        },
        "expected_state": {
            "admin_status": "up",
            "oper_status": "up"
        }
    }

    diagnosis = diagnose_interface_administratively_down(case_data)

    assert diagnosis["fault_detected"] is True
    assert diagnosis["category"] == "Interface"
    assert diagnosis["diagnosis"] == (
        "Interface Administratively Down"
    )
    assert diagnosis["faulty_device"] == "SW1"
    assert diagnosis["faulty_interface"] == "Fa0/1"
    assert diagnosis["confidence"] == "High"