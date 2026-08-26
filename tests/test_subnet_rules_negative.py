from rules.subnet_rules import diagnose_wrong_subnet_mask


def test_does_not_detect_fault_when_subnet_mask_is_correct():

    case_data = {
        "category": "IP Configuration",
        "topology": {
            "faulty_device": "PC1"
        },
        "ip_configuration": {
            "ip_address": "192.168.10.10",
            "configured_subnet_mask": "255.255.255.0"
        },
        "expected_configuration": {
            "network": "192.168.10.0/24",
            "subnet_mask": "255.255.255.0"
        }
    }

    result = diagnose_wrong_subnet_mask(case_data)

    assert result["fault_detected"] is False