def diagnose_wrong_subnet_mask(case_data):
    """
    Diagnose a subnet mask mismatch.
    """

    if case_data.get("category") != "IP Configuration":
        return {
            "fault_detected": False
        }

    ip_configuration = case_data.get(
        "ip_configuration",
        {}
    )

    expected_configuration = case_data.get(
        "expected_configuration",
        {}
    )

    configured_subnet_mask = ip_configuration.get(
        "configured_subnet_mask"
    )

    expected_subnet_mask = expected_configuration.get(
        "subnet_mask"
    )

    if (
        configured_subnet_mask
        and expected_subnet_mask
        and configured_subnet_mask != expected_subnet_mask
    ):
        faulty_device = case_data.get(
            "topology",
            {}
        ).get(
            "faulty_device"
        )

        return {
            "fault_detected": True,
            "category": "IP Configuration",
            "diagnosis": "Wrong Subnet Mask",
            "faulty_device": faulty_device,
            "osi_layer": "Layer 3",
            "confidence": "High",
            "configured_subnet_mask": configured_subnet_mask,
            "expected_subnet_mask": expected_subnet_mask,
            "expected_network": expected_configuration.get(
                "network"
            ),
            "explanation": (
                f"{faulty_device} is configured with subnet mask "
                f"{configured_subnet_mask}, but the expected subnet "
                f"mask is {expected_subnet_mask} for network "
                f"{expected_configuration.get('network')}."
            ),
            "recommended_fix": (
                f"Change the subnet mask on {faulty_device} from "
                f"{configured_subnet_mask} to {expected_subnet_mask}."
            )
        }

    return {
        "fault_detected": False
    }