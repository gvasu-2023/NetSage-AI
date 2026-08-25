from rules.routing_rules import diagnose_missing_static_route


def test_detect_missing_static_route():
    case_data = {
        "category": "Routing",

        "topology": {
            "faulty_device": "R1"
        },

        "routing": {
            "destination_network": "172.16.10.0",
            "subnet_mask": "255.255.255.0",
            "next_hop": "10.0.0.2",
            "route_present": False
        },

        "expected_state": {
            "route_present": True
        }
    }

    diagnosis = diagnose_missing_static_route(case_data)

    assert diagnosis["fault_detected"] is True
    assert diagnosis["category"] == "Routing"
    assert diagnosis["diagnosis"] == "Missing Static Route"
    assert diagnosis["faulty_device"] == "R1"
    assert diagnosis["osi_layer"] == "Layer 3"
    assert diagnosis["confidence"] == "High"
    assert diagnosis["destination_network"] == "172.16.10.0"
    assert diagnosis["subnet_mask"] == "255.255.255.0"
    assert diagnosis["next_hop"] == "10.0.0.2"