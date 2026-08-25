# NetSage-AI Project State

## Project Overview

**Project Name:** NetSage-AI  
**Project Type:** AI-Assisted Network Fault Diagnosis System  
**Development Approach:** Packet Tracer fault simulation + structured case data + rule-based diagnosis engine  
**Current Branch:** main

---

# 1. System Architecture

```text
Cisco Packet Tracer
        ↓
Network Fault Scenario
        ↓
Evidence Collection
        ↓
Structured case.json
        ↓
Case Loader
        ↓
Diagnosis Rules
        ↓
Diagnosis Engine
        ↓
Network Diagnosis Report


# 10. Next Immediate Action

## CASE004 - Interface Administratively Down

**Status:** In Progress

### Intended Fault

SW1 interface Fa0/1, which connects PC1 to the network, will be intentionally administratively shut down.

### Expected Symptoms

- PC1 cannot communicate with its default gateway.
- SW1 Fa0/1 shows administratively down.
- The physical cable remains connected.
- Other network devices remain operational.

### Expected Diagnosis

**Category:** Interface  
**Diagnosis:** Interface Administratively Down  
**Faulty Device:** SW1  
**Faulty Interface:** Fa0/1  
**OSI Layer:** Layer 1/2  
**Confidence:** High