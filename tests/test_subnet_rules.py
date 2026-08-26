from rules.subnet_rules import diagnose_wrong_subnet_mask


def test_detects_wrong_subnet_mask():

    case_data = {
        "category": "IP Configuration",
        "topology": {
            "faulty_device": "PC1"
        },
        "ip_configuration": {
            "ip_address": "192.168.10.10",
            "configured_subnet_mask": "255.255.255.248"
        },
        "expected_configuration": {
            "network": "192.168.10.0/24",
            "subnet_mask": "255.255.255.0"
        }
    }

    result = diagnose_wrong_subnet_mask(case_data)

    assert result["fault_detected"] is True
    assert result["category"] == "IP Configuration"
    assert result["diagnosis"] == "Wrong Subnet Mask"
    assert result["faulty_device"] == "PC1"
    assert result["configured_subnet_mask"] == "255.255.255.248"
    assert result["expected_subnet_mask"] == "255.255.255.0"
    assert result["osi_layer"] == "Layer 3"
    assert result["confidence"] == "High"