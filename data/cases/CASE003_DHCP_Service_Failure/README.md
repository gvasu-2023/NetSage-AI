# CASE003 - DHCP Service Failure

## Fault

The DHCP service on Server0 is disabled.

## Network Context

- DHCP Client: DHCP-PC
- DHCP Server: Server0
- DHCP Server IP: 192.168.30.10
- DHCP Client VLAN: VLAN 30
- Expected Network: 192.168.30.0/24
- Expected Default Gateway: 192.168.30.1

## Observed Symptoms

- DHCP-PC receives an APIPA address.
- DHCP-PC receives the address 169.254.156.102.
- The subnet mask is 255.255.0.0.
- The default gateway is 0.0.0.0.
- DHCP-PC cannot ping Server0 at 192.168.30.10.

## Root Cause

The DHCP service on Server0 is turned OFF.

## Expected Diagnosis

DHCP Service Failure

## Expected Fix

Enable the DHCP service on Server0.

## Evidence

1. DHCP service is OFF on Server0.
2. DHCP-PC receives an APIPA address.
3. DHCP-PC cannot reach Server0.
4. DHCP-PC is correctly assigned to VLAN 30.