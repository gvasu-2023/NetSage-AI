# CASE006 - Wrong Subnet Mask

## Overview

This case simulates an incorrect subnet mask configuration on PC1.

The healthy VLAN 10 network uses the subnet:

192.168.10.0/24

PC1 is intentionally configured with an incorrect subnet mask while retaining the correct IP address and default gateway.

## Root Cause

PC1 is configured with the subnet mask:

255.255.255.248

The expected subnet mask is:

255.255.255.0

## Faulty Device

- Device: PC1
- IP Address: 192.168.10.10
- Configured Subnet Mask: 255.255.255.248
- Expected Subnet Mask: 255.255.255.0
- Default Gateway: 192.168.10.1

## Expected Network

- Network: 192.168.10.0/24
- Gateway: 192.168.10.1

## Verification Evidence

### PC1 Incorrect Subnet Mask

PC1 is configured with the correct IP address and gateway but an incorrect subnet mask.

Configured:

255.255.255.248

Expected:

255.255.255.0

### Remote Connectivity Result

The remote ping was successful in Cisco Packet Tracer despite the incorrect subnet mask configuration.

The case is therefore diagnosed using the explicit configuration mismatch rather than relying only on ping failure.

### Router VLAN 10 Configuration

R1 is configured with:

```text
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0