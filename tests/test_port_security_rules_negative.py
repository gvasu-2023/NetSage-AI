from rules.port_security_rules import (
    diagnose_port_security_violation
)


def test_no_port_security_violation_detected():

    case_data = {
        "case_id": "TEST001",
        "title": "Healthy Port Security Configuration",
        "category": "Port Security",

        "topology": {
            "faulty_device": "SW1",
            "faulty_interface": "Fa0/1"
        },

        "port_security": {
            "enabled": True,
            "port_status": "Secure-up",
            "violation_mode": "Shutdown",
            "maximum_mac_addresses": 1,
            "total_mac_addresses": 1,
            "security_violation_count": 0,
            "interface_status": "connected"
        }
    }

    result = diagnose_port_security_violation(case_data)

    assert result["fault_detected"] is False