# CASE014 — Wrong Static Route Next Hop

## Fault Description

R1 requires a static route to reach the external network `172.16.10.0/24`, which is connected through R2.

The correct next hop from R1 is `10.0.0.2`. However, the static route is configured with the incorrect next hop `10.0.0.6`.

Because the configured next hop is unreachable, the static route is not installed in R1's routing table. As a result, traffic from the internal networks cannot reach the external network.

## Healthy Configuration

The correct static route is:

```text
ip route 172.16.10.0 255.255.255.0 10.0.0.2