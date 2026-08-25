# CASE004 - Interface Administratively Down

## Overview

This case simulates a network connectivity failure caused by an administratively disabled switch interface.

PC1 is connected to SW1 through interface Fa0/1. The interface is intentionally configured with the `shutdown` command.

## Root Cause

SW1 interface Fa0/1 is administratively down.

The interface was previously operational and connected to PC1.

## Faulty Device

- Device: SW1
- Interface: Fa0/1
- Connected Device: PC1

## Expected Symptoms

- PC1 cannot communicate with its default gateway.
- Ping from PC1 to 192.168.10.1 fails.
- SW1 Fa0/1 shows administratively down.
- The line protocol is down.

## Verification Evidence

### Healthy Baseline

Before the fault:

```text
FastEthernet0/1 is up, line protocol is up