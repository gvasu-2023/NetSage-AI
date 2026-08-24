# NetSage AI - Network Troubleshooting Case Schema

## Purpose

Each network troubleshooting case represents a network fault that can be analyzed by:

1. The Python rule engine
2. The AI diagnosis engine
3. A human reviewer

---

## Case Fields

### 1. case_id

Unique identifier for each case.

Example:

CASE001

---

### 2. category

The primary network fault category.

Allowed categories:

- VLAN
- Gateway
- DHCP
- DNS
- Routing
- ACL
- NAT
- Wireless

---

### 3. title

A short descriptive title.

Example:

Host cannot communicate across VLANs

---

### 4. symptom

The observed network problem.

Example:

PC1 can communicate with devices in its own subnet but cannot reach the server in another VLAN.

---

### 5. topology

A text description of the relevant network topology.

Example:

PC1 → SW1 → R1 → Server

---

### 6. device_configs

Relevant device configuration information.

This may include:

- IP addresses
- subnet masks
- default gateways
- VLAN IDs
- interface information
- routing configuration

---

### 7. show_outputs

Cisco command outputs used as diagnostic evidence.

Example commands:

- show ip interface brief
- show ip route
- show vlan brief
- show interfaces trunk
- show access-lists
- show ip nat translations

---

### 8. expected_fault

The confirmed root cause.

Example:

VLAN 30 is missing from the switch configuration.

---

### 9. osi_layer

The primary OSI layer associated with the fault.

Example:

Layer 2

---

### 10. concept

The networking concept involved.

Example:

VLAN

---

### 11. severity

Business impact of the issue.

Allowed values:

- Low
- Medium
- High
- Critical

---

### 12. expected_next_command

The next diagnostic command that should be executed.

Example:

show vlan brief

---

### 13. expected_fix

The recommended configuration or correction.

Example:

Create VLAN 30 and assign the correct switch ports.

---

### 14. verification

The method used to confirm that the issue has been fixed.

Example:

Ping the destination host and confirm successful connectivity.

---

### 15. rule_checker_findings

Expected deterministic findings from the Python rule engine.

Example:

Missing VLAN 30 detected.

---

## AI Evaluation Fields

The following fields are generated after AI analysis.

- ai_root_cause
- ai_osi_layer
- ai_confidence
- ai_evidence
- ai_next_command
- ai_fix_steps

---

## Human Review Fields

The following fields are added during human review.

- review_status
- human_root_cause
- reviewer_notes
- final_diagnosis