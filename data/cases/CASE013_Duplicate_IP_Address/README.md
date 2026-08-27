# CASE013 — Duplicate IP Address

## Fault Description

PC1 and PC3 are configured with the same IPv4 address, `192.168.10.10`, on the `192.168.10.0/24` network.

A duplicate IP address creates an address conflict because two devices claim ownership of the same Layer 3 address. As a result, communication intended for `192.168.10.10` cannot be reliably delivered to the correct device.

PC1 remains configured with the valid address `192.168.10.10`, while PC3 should use its unique address `192.168.10.30`.

## Topology

- Faulty Device: PC3
- Conflicting Device: PC1
- Affected Network: `192.168.10.0/24`
- Duplicate IP Address: `192.168.10.10`
- Expected PC3 IP Address: `192.168.10.30`
- Default Gateway: `192.168.10.1`

## Healthy Baseline

Before introducing the fault:

- PC1 uses IP address `192.168.10.10`
- PC3 uses its unique expected IP address
- PC3 can successfully ping the default gateway
- PC3 can communicate with PC1

## Symptoms

After PC3 is configured with the duplicate address:

- PC1 and PC3 both use `192.168.10.10`
- PC3 experiences IP address conflict symptoms
- PC3 cannot reliably communicate on the network
- Ping to the default gateway fails
- Remote connectivity fails

## Root Cause

The IP address `192.168.10.10` is assigned to both PC1 and PC3.

This prevents the network from uniquely associating the IP address with a single device.

## Recommended Fix

Assign a unique IP address to PC3.

The required configuration is:

```text
PC1: 192.168.10.10
PC3: 192.168.10.30
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.10.1