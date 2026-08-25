# CASE005 - Missing Static Route

## Overview

This case simulates an end-to-end network connectivity failure caused by a missing static route on R1.

The network 172.16.10.0/24 is connected to R2. R1 requires a static route through next hop 10.0.0.2 to reach that network.

The required route is intentionally removed from R1.

## Root Cause

R1 is missing the required static route to the 172.16.10.0/24 network.

The missing route is:

```text
ip route 172.16.10.0 255.255.255.0 10.0.0.2