@'
# CASE012 — Native VLAN Mismatch

## Fault Description

A native VLAN mismatch exists on the trunk connection between SW1 and R1.

SW1 interface `GigabitEthernet0/1` is configured with native VLAN 10, while R1 interface `GigabitEthernet0/0` uses the default native VLAN 1.

Because untagged traffic is interpreted differently on each side of the trunk, VLAN 10 connectivity is affected.

## Topology

- Switch: SW1
- Switch Interface: `GigabitEthernet0/1`
- Router: R1
- Router Interface: `GigabitEthernet0/0`
- SW1 Native VLAN: `10`
- R1 Native VLAN: `1`

## Symptoms

- VLAN 10 connectivity is affected
- PC1 cannot communicate correctly through the router
- VLAN 20 connectivity remains functional
- VLAN 30 connectivity remains functional

## Root Cause

The native VLAN configuration is inconsistent across the trunk link.

SW1 uses native VLAN 10:

```text
switchport trunk native vlan 10