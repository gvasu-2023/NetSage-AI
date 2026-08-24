from rules.gateway_rules import diagnose_default_gateway


def test_correct_default_gateway_is_not_detected():
    """
    A correct gateway configuration must not be diagnosed as faulty.
    """

    case_data = {
        "device_configs": {
            "PC1": {
                "configured_default_gateway": "192.168.10.1",
                "correct_default_gateway": "192.168.10.1"
            }
        }
    }

    diagnosis = diagnose_default_gateway(case_data)

    assert diagnosis["fault_detected"] is False