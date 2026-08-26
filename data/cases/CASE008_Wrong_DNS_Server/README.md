# CASE008 - Wrong DNS Server

## Overview

This case simulates a DNS name resolution failure caused by an incorrect DNS server configuration on PC1.

PC1 has valid IP connectivity to the network and can reach the External-PC directly using its IP address. However, PC1 is configured with an incorrect DNS server address, causing hostname resolution to fail.

## Root Cause

PC1 is configured with the wrong DNS server address.

Configured DNS server:

```text
192.168.10.254