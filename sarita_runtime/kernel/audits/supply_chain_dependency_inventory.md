# Supply Chain Dependency Inventory - Phase 88.1

## Core System Dependencies
- **Runtime:** Python 3.x
- **Storage:** SQLite3 (WAL Mode)
- **IO:** io_uring (Linux Kernel 5.1+ / syscalls 425, 426, 427)
- **Security:** hashlib (SHA-256), hmac

## External Auditor Dependencies
- **Verification Logic:** Currently resides in `sarita_external_auditor/`
- **Data Exchange:** JSON over evidence export protocol.

## Critical Risks in Supply Chain
1. **Binary Substitution:** No proof that `sarita_runtime` running in production matches the source code in the repository.
2. **Implicit Trust:** Auditors are assumed to be "good" if they follow the protocol, without cryptographic identity backing from separate domains.
3. **Repository Lock-in:** The `kernel_constitutional_topology.json` is the sole source of architectural truth, but it is stored within the repo itself.

## Federated Mitigation Strategy
- Implement `reproducible_build_engine.py` to ensure binary-to-source mapping.
- Establish `auditor_trust_registry.py` to manage multi-domain cryptographic keys.
- Create `artifact_origin_registry.py` to track the provenance of every component.
