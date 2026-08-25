from rules.routing_rules import diagnose_missing_static_route


def test_no_fault_when_static_route_is_present():
    case_data = {
        "category": "Routing",

        "topology": {
            "faulty_device": "R1"
        },

        "routing": {
            "destination_network": "172.16.10.0",
            "subnet_mask": "255.255.255.0",
            "next_hop": "10.0.0.2",
            "route_present": True
        },

        "expected_state": {
            "route_present": True
        }
    }

    diagnosis = diagnose_missing_static_route(case_data)

    assert diagnosis["fault_detected"] is False