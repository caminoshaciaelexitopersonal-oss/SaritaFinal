from sarita_runtime.kernel.sovereign_constitution.constitutional_runtime_guard import ConstitutionalRuntimeGuard

class ConstitutionalMutationBlocker:
    """Explicit blocker for unauthorized mutations (Phase 81.2)."""
    @staticmethod
    def block_illegal_mutation():
        ConstitutionalRuntimeGuard.enforce_single_writer()
