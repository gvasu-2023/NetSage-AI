from rules.interface_rules import (
    diagnose_interface_administratively_down
)


def test_interface_rule_ignores_healthy_interface():
    case_data = {
        "category": "Interface",
        "topology": {
            "faulty_device": "SW1",
            "faulty_interface": "Fa0/1",
            "connected_device": "PC1"
        },
        "interface": {
            "name": "Fa0/1",
            "admin_status": "up",
            "oper_status": "up",
            "status_reason": "connected"
        },
        "expected_state": {
            "admin_status": "up",
            "oper_status": "up"
        }
    }

    diagnosis = diagnose_interface_administratively_down(case_data)

    assert diagnosis["fault_detected"] is False