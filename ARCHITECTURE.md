# Security Compliance Orchestrator Architecture

## Current Architecture

The Security Compliance Orchestrator is designed to separate evidence collection from evidence evaluation.

At this stage, the project has three main responsibilities:

1. Collect security evidence.
2. Evaluate that evidence against security expectations.
3. Coordinate the flow between components.

## Current Data Flow

AWS IAM
    ↓
AWSIAMCollector
    ↓
Normalized IAM Evidence
    ↓
Audit Agent
    ↓
Findings
    ↓
Orchestrator Output

## Key Design Principle

Collectors gather facts.

Audit agents interpret facts.

The orchestrator coordinates the flow.