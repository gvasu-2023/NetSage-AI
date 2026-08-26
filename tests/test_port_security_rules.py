from rules.port_security_rules import (
    diagnose_port_security_violation
)


def test_port_security_violation_detected():

    case_data = {
        "case_id": "CASE010",
        "title": "Port Security Violation",
        "category": "Port Security",

        "topology": {
            "faulty_device": "SW1",
            "faulty_interface": "Fa0/1",
            "affected_host": "PC1"
        },

        "port_security": {
            "enabled": True,
            "port_status": "Secure-shutdown",
            "violation_mode": "Shutdown",
            "maximum_mac_addresses": 1,
            "total_mac_addresses": 1,
            "sticky_mac_addresses": 1,
            "security_violation_count": 1,
            "interface_status": "err-disabled"
        }
    }

    result = diagnose_port_security_violation(case_data)

    assert result["fault_detected"] is True
    assert result["category"] == "Port Security"
    assert result["diagnosis"] == "Port Security Violation"
    assert result["faulty_device"] == "SW1"
    assert result["faulty_interface"] == "Fa0/1"
    assert result["osi_layer"] == "Layer 2"
    assert result["confidence"] == "High"
    assert result["port_status"] == "Secure-shutdown"
    assert result["violation_mode"] == "Shutdown"
    assert result["security_violation_count"] == 1
    assert result["interface_status"] == "err-disabled"