# CASE010 - Port Security Violation

## Fault

A port security violation occurs on switch SW1 interface Fa0/1.

The interface is configured to allow only one MAC address with the violation mode set to shutdown. When a different device is connected to the secured port, the maximum allowed MAC address limit is violated.

## Faulty Device

- Device: SW1
- Interface: Fa0/1
- Affected Host: PC1

## Symptoms

- Port security status becomes Secure-shutdown.
- Security violation count increases to 1.
- Interface Fa0/1 enters the err-disabled state.
- The affected host loses network connectivity.

## Evidence

The Packet Tracer evidence confirms:

- Port Security: Enabled
- Port Status: Secure-shutdown
- Violation Mode: Shutdown
- Maximum MAC Addresses: 1
- Security Violation Count: 1
- Interface Status: err-disabled

## Expected Diagnosis

NetSage AI should identify the fault as:

Port Security Violation

The fault should be classified as a Layer 2 network fault.

## Recommended Fix

Investigate the unauthorized or unexpected MAC address connected to the secured port.

If the new device is authorized, clear or update the configured secure MAC address and restore the interface by shutting it down and enabling it again.

Example commands:

```text
enable
configure terminal
interface fa0/1
shutdown
no shutdown