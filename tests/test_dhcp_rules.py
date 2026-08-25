from rules.dhcp_rules import diagnose_dhcp_service_failure


def test_diagnose_dhcp_service_failure():
    case_data = {
        "category": "DHCP",
        "faulty_device": "Server0",
        "osi_layer": "Layer 7",
        "symptoms": {
            "dhcp_client_ip_address": "169.254.156.102",
            "dhcp_client_default_gateway": "0.0.0.0",
            "expected_network": "192.168.30.0/24"
        },
        "dhcp": {
            "server": "Server0",
            "service_enabled": False
        }
    }

    diagnosis = diagnose_dhcp_service_failure(case_data)

    assert diagnosis["fault_detected"] is True
    assert diagnosis["category"] == "DHCP"
    assert diagnosis["diagnosis"] == "DHCP Service Failure"
    assert diagnosis["faulty_device"] == "Server0"
    assert diagnosis["confidence"] == "High"