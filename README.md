# NetSage AI

AI-Assisted Network Troubleshooting with Human Review.

## Project Overview

NetSage AI is an evidence-grounded AI troubleshooting assistant for Cisco Packet Tracer and networking lab problems.

The system analyzes:

- Network symptoms
- Topology information
- Cisco show-command outputs
- Deterministic rule-checker findings

It then provides:

- Likely root cause
- OSI layer
- Confidence score
- Evidence
- Recommended next command
- Suggested fix steps

All AI diagnoses require human review before a fix is accepted.

## Project Components

- Network troubleshooting case dataset
- Deterministic Python rule checker
- AI diagnosis engine
- Structured prompt library
- Human review system
- Responsible AI correction log
- Analytics dashboard

## Safety Principle

AI diagnoses are recommendations only. A human reviewer must accept, edit, or reject every diagnosis.