# CASE009 - ACL Blocks Traffic

## Overview

This case simulates a network connectivity failure caused by an Access Control List (ACL) blocking communication between PC1 and the remote network.

PC1 is unable to communicate with the remote device at 172.16.10.10 even though the physical connectivity and routing configuration are available.

## Root Cause

ACL 101 is configured on R1 to deny IP traffic from:

- Source: 192.168.10.10
- Destination: 172.16.10.10

The ACL is applied outbound on R1 GigabitEthernet0/1.

The remaining traffic is permitted by:

```text
permit ip any any