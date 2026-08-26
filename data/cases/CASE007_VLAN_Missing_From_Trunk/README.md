# CASE007 - VLAN Missing From Trunk

## Overview

This case simulates a network connectivity failure caused by VLAN 20 being excluded from the trunk link between SW1 and R1.

The network uses a router-on-a-stick architecture. VLANs 10, 20, and 30 must be carried across the trunk between the switch and router.

## Root Cause

VLAN 20 is missing from the allowed VLAN list on the SW1 trunk interface Gig0/1.

The trunk remains operational, but traffic belonging to VLAN 20 cannot reach the router subinterface configured for VLAN 20.

## Faulty Device

- Device: SW1
- Interface: Gig0/1
- Missing VLAN: 20
- Connected Device: R1

## Expected Symptoms

- The trunk interface remains operational.
- VLAN 10 and VLAN 30 remain active.
- VLAN 20 is missing from the active VLAN list on the trunk.
- The VLAN 20 client cannot reach its default gateway.
- A client in another VLAN can still reach its own default gateway.

## Verification Evidence

### Healthy Trunk

Before the fault, the trunk allowed:

```text
1,10,20,30