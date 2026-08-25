def diagnose_missing_static_route(case_data):
    """
    Diagnose a missing static route.
    """

    if case_data.get("category") != "Routing":
        return {
            "fault_detected": False
        }

    routing = case_data.get("routing", {})
    expected_state = case_data.get("expected_state", {})
    topology = case_data.get("topology", {})

    route_present = routing.get("route_present")
    expected_route_present = expected_state.get("route_present")

    if (
        route_present is False
        and expected_route_present is True
    ):
        destination_network = routing.get(
            "destination_network"
        )

        subnet_mask = routing.get(
            "subnet_mask"
        )

        next_hop = routing.get(
            "next_hop"
        )

        faulty_device = topology.get(
            "faulty_device"
        )

        return {
            "fault_detected": True,
            "category": "Routing",
            "diagnosis": "Missing Static Route",
            "faulty_device": faulty_device,
            "osi_layer": "Layer 3",
            "confidence": "High",
            "destination_network": destination_network,
            "subnet_mask": subnet_mask,
            "next_hop": next_hop,
            "explanation": (
                f"{faulty_device} is missing the static route "
                f"to {destination_network}/{subnet_mask}. "
                f"The expected next hop is {next_hop}."
            ),
            "recommended_fix": (
                f"Configure the missing static route on "
                f"{faulty_device}: ip route "
                f"{destination_network} "
                f"{subnet_mask} "
                f"{next_hop}"
            )
        }

    return {
        "fault_detected": False
    }