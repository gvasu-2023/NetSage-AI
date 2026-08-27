# CASE015 — DNS Service Failure

## Fault Description

PC1 is configured with the correct DNS server at `192.168.30.10`, and the DNS record for `external-pc.netsage.local` exists on Server0.

However, the DNS service on Server0 is disabled.

Because the DNS service is not running, PC1 cannot resolve `external-pc.netsage.local` to its expected IP address, even though direct IP connectivity to the destination is working.

## Topology

- DNS Client: PC1
- Client Network: `192.168.10.0/24`
- DNS Server: Server0
- DNS Server IP: `192.168.30.10`
- Hostname: `external-pc.netsage.local`
- Expected IP Address: `172.16.10.10`
- Faulty Device: Server0

## Symptoms

- Direct IP connectivity works
- DNS server is configured correctly on PC1
- DNS record exists on Server0
- Hostname resolution fails
- `ping 172.16.10.10` succeeds
- `ping external-pc.netsage.local` fails

## Root Cause

The DNS service on Server0 is disabled.

The DNS record exists, but Server0 cannot answer DNS queries while the DNS service is OFF.

## Evidence

### 01 — Healthy DNS Record

Shows that the DNS service is enabled in the healthy baseline and that the record exists:

```text
external-pc.netsage.local → 172.16.10.10