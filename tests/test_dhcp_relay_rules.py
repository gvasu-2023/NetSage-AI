from rules.dhcp_relay_rules import (
    diagnose_dhcp_relay_missing
)


def test_dhcp_relay_missing_detected():

    case_data = {
        "case_id": "CASE011",
        "title": "DHCP Relay Missing",
        "category": "DHCP Relay",

        "topology": {
            "faulty_device": "R1",
            "faulty_interface": "GigabitEthernet0/0.20",
            "client_device": "PC2",
            "client_network": "192.168.20.0/24",
            "dhcp_server": "Server0",
            "dhcp_server_ip": "192.168.30.10"
        },

        "dhcp_relay": {
            "helper_address_configured": False,
            "expected_helper_address": "192.168.30.10"
        },

        "symptoms": {
            "dhcp_request": "failed",
            "client_ip_address": "169.254.9.220",
            "default_gateway": "0.0.0.0",
            "dns_server": "0.0.0.0",
            "apipa_assigned": True
        }
    }

    result = diagnose_dhcp_relay_missing(case_data)

    assert result["fault_detected"] is True
    assert result["category"] == "DHCP Relay"
    assert result["diagnosis"] == "DHCP Relay Missing"
    assert result["faulty_device"] == "R1"
    assert result["faulty_interface"] == "GigabitEthernet0/0.20"
    assert result["osi_layer"] == "Layer 3"
    assert result["confidence"] == "High"
    assert result["client_device"] == "PC2"
    assert result["dhcp_server"] == "Server0"
    assert result["expected_helper_address"] == "192.168.30.10"
    assert result["apipa_assigned"] is True