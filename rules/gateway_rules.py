def diagnose_default_gateway(case_data):
    """
    Detects an incorrect default gateway configuration.
    """

    device_configs = case_data.get("device_configs", {})
    pc1 = device_configs.get("PC1", {})

    configured_gateway = pc1.get("configured_default_gateway")
    correct_gateway = pc1.get("correct_default_gateway")

    if configured_gateway != correct_gateway:
        return {
            "fault_detected": True,
            "category": "Gateway",
            "diagnosis": "Wrong Default Gateway",
            "faulty_device": "PC1",
            "configured_gateway": configured_gateway,
            "expected_gateway": correct_gateway,
            "osi_layer": "Layer 3",
            "confidence": "High",
            "explanation": (
                f"PC1 is configured with default gateway "
                f"{configured_gateway}, but the expected gateway is "
                f"{correct_gateway}."
            ),
            "recommended_fix": (
                f"Change PC1 default gateway from "
                f"{configured_gateway} to {correct_gateway}."
            )
        }

    return {
        "fault_detected": False
    }