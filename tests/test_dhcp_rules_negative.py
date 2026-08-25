from rules.dhcp_rules import diagnose_dhcp_service_failure


def test_dhcp_rule_does_not_trigger_when_service_is_enabled():
    case_data = {
        "category": "DHCP",
        "symptoms": {
            "dhcp_client_ip_address": "192.168.30.100",
            "dhcp_client_default_gateway": "192.168.30.1"
        },
        "dhcp": {
            "server": "Server0",
            "service_enabled": True
        }
    }

    diagnosis = diagnose_dhcp_service_failure(case_data)

    assert diagnosis["fault_detected"] is False


def test_dhcp_rule_does_not_trigger_for_non_dhcp_case():
    case_data = {
        "category": "Gateway",
        "symptoms": {},
        "dhcp": {}
    }

    diagnosis = diagnose_dhcp_service_failure(case_data)

    assert diagnosis["fault_detected"] is False