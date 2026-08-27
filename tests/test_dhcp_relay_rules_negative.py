from rules.dhcp_relay_rules import (
    diagnose_dhcp_relay_missing
)


def test_no_dhcp_relay_fault_when_helper_address_exists():

    case_data = {
        "case_id": "TEST011",
        "title": "Healthy DHCP Relay",
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
            "helper_address_configured": True,
            "expected_helper_address": "192.168.30.10"
        },

        "symptoms": {
            "dhcp_request": "successful",
            "client_ip_address": "192.168.20.100",
            "apipa_assigned": False
        }
    }

    result = diagnose_dhcp_relay_missing(case_data)

    assert result["fault_detected"] is False