import unittest
from sarita_runtime.kernel.sovereign_constitution.constitutional_runtime_guard import ConstitutionalRuntimeGuard, ConstitutionalViolationException
from sarita_runtime.kernel.sovereign_constitution.autonomous_defense_engine import AutonomousDefenseEngine
from sarita_runtime.kernel.constitutional_court.constitutional_court import ConstitutionalCourt
from sarita_runtime.kernel.component_identity.sovereign_identity_engine import SovereignIdentityEngine

class ConstitutionalAttackValidation(unittest.TestCase):
    def setUp(self):
        self.engine = SovereignIdentityEngine()
        self.court = ConstitutionalCourt(self.engine)
        self.guard = ConstitutionalRuntimeGuard(self.court)

    def test_parallel_writer_attack(self):
        # Attempt to mutate state without certification
        with self.assertRaises(ConstitutionalViolationException):
            self.guard.enforce_certified_mutation("RogueWriter", __file__)

    def test_rogue_authority_attack(self):
        # Attempt to register a non-constitutional authority
        with self.assertRaises(ConstitutionalViolationException):
            ConstitutionalRuntimeGuard.enforce_unified_authority("RogueAuthority")

    def test_causal_bypass_attack(self):
        # Attempt to bypass the Graph and go Telemetry -> Scheduler
        with self.assertRaises(ConstitutionalViolationException):
            AutonomousDefenseEngine.validate_causal_path("Telemetry", "SovereignScheduler")

    def test_unauthorized_subsystem_attack(self):
        # Attempt to act as a rogue subsystem
        with self.assertRaises(ConstitutionalViolationException):
            AutonomousDefenseEngine.block_unauthorized_access("MaliciousSubsystem")

if __name__ == "__main__":
    unittest.main()
