from rules.duplicate_ip_rules import (
    diagnose_duplicate_ip_address
)


def test_no_duplicate_ip_address_detected():

    case_data = {
        "case_id": "TEST013",
        "title": "Healthy IP Configuration",
        "category": "IP Configuration",

        "topology": {
            "faulty_device": "PC3",
            "conflicting_device": "PC1",
            "affected_network": "192.168.10.0/24",
            "default_gateway": "192.168.10.1"
        },

        "ip_configuration": {
            "duplicate_ip_detected": False,
            "pc1_ip_address": "192.168.10.10",
            "pc3_ip_address": "192.168.10.12",
            "duplicate_ip_address": None,
            "expected_pc3_ip": "192.168.10.12"
        },

        "symptoms": {
            "ip_conflict_detected": False,
            "gateway_ping": "successful",
            "remote_ping": "successful"
        }
    }

    result = diagnose_duplicate_ip_address(case_data)

    assert result["fault_detected"] is False