# AI AGENT REGISTRY: SARITA PLATFORM v1.0
**Lead Auditor:** Jules (Senior AI Software Engineer)
**Date:** March 2026

The platform implements a Military-Style AI Hierarchy (N1-N7) for autonomous operations and strategic governance.

## 1. Hierarchy Structure
| Level | Rank | Responsibility |
| :---: | :--- | :--- |
| **N1** | **General** | Strategic orchestration and mission delegation (`SaritaOrchestrator`) |
| **N2** | **Coroneles** | Domain tactical leadership (Finance, Logistics, Governance) |
| **N3** | **Capitanes** | Plan generation and coordination of complex workflows |
| **N4** | **Tenientes** | Decomposition of plans into executable micro-tasks |
| **N5** | **Sargentos** | Verification of results and operational exception handling |
| **N6** | **Soldados** | Direct execution of tools and backend services |
| **N7** | **Cadetes** | Metric monitoring and data capture feedback loops |

## 2. Active Domain Agents (Coroneles)
| Agent Name | Function / Domain | Core Skill |
| :--- | :--- | :--- |
| `CoronelContable` | Financial Integrity | Double-entry validation and Ledger hashing |
| `CoronelOperativa`| Tourism Operations | Booking lifecycle and resource scheduling |
| `CoronelMarketing`| Growth & Acquisition| Lead qualification and funnel optimization |
| `CoronelNomina` | Human Capital | Payroll liquidation and legal compliance |
| `PeaceNetCoronel` | Risk Mitigation | Systemic stability and conflict resolution |
| `CoronelMonedero`| Fintech | Escrow management and payment security |

## 3. Tool Integration
Agents interact with the system via a standardized `Service Layer`, ensuring that AI decisions are translated into atomic, validated database transactions.

**Orchestration Engine:** LangGraph (Stateful Multi-Agent Graphs).
**Intelligence Pipeline:** Híbrido LLM (Local Ollama for privacy / Remote Groq-OpenAI for reasoning).
