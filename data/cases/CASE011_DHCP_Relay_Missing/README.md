# CASE011 - DHCP Relay Missing

## Fault Description

PC2 is configured to obtain its IP address automatically using DHCP. However, PC2 is located in VLAN 20 on the `192.168.20.0/24` network, while the DHCP server is located on Server0 in the `192.168.30.0/24` network.

The router interface `GigabitEthernet0/0.20` is not configured with a DHCP relay using `ip helper-address`.

Because DHCP requests are broadcasts, they cannot cross the router without a DHCP relay configuration.

As a result, PC2 fails to obtain a valid IP address and receives an APIPA address.

## Topology

- DHCP Client: PC2
- Client Network: `192.168.20.0/24`
- Default Gateway: `192.168.20.1`
- DHCP Server: Server0
- DHCP Server IP: `192.168.30.10`
- Faulty Device: R1
- Faulty Interface: `GigabitEthernet0/0.20`

## Symptoms

- DHCP request fails
- PC2 receives an APIPA address
- PC2 IP address: `169.254.9.220`
- Default gateway: `0.0.0.0`
- DNS server: `0.0.0.0`

## Root Cause

The DHCP relay is missing on R1 interface `GigabitEthernet0/0.20`.

The required configuration is:

```text
interface GigabitEthernet0/0.20
 ip helper-address 192.168.30.10