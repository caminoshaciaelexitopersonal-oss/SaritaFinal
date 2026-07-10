from .dashboard_engine import DashboardEngine
from .system_monitor import SystemMonitor
from .architecture_dashboard import ArchitectureDashboard
from .governance_dashboard import GovernanceDashboard
from .consistency_dashboard import ConsistencyDashboard
from .certification_dashboard import CertificationDashboard
from .runtime_dashboard import RuntimeDashboard
from .alert_dashboard import AlertDashboard
from .decision_dashboard import DecisionDashboard
from .learning_dashboard import LearningDashboard
from .cosmogenesis_dashboard import CosmogenesisDashboard
from .global_index_dashboard import GlobalIndexDashboard

class ControlCenter:
    """
    Sovereign Operational Console (Phase 132).
    A single unified cockpit for real-time visualization of SARITA's entire state.
    """
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.dashboard_engine = DashboardEngine()
        self.system_monitor = SystemMonitor()

        # Sub-Dashboards
        self.architecture = ArchitectureDashboard()
        self.governance = GovernanceDashboard()
        self.consistency = ConsistencyDashboard()
        self.certification = CertificationDashboard()
        self.runtime = RuntimeDashboard()
        self.alert = AlertDashboard()
        self.decision = DecisionDashboard()
        self.learning = LearningDashboard()
        self.cosmogenesis = CosmogenesisDashboard()
        self.global_index = GlobalIndexDashboard()

    def generate_consolidated_report(self) -> dict:
        """
        Gathers real-time states and renders a complete, multi-dimensional console report.
        """
        state = self.state_manager
        return {
            "console_title": "SARITA SOVEREIGN CONTROL PANEL",
            "system_load": self.system_monitor.get_system_load(),
            "dashboards": {
                "architecture": self.architecture.render(state),
                "governance": self.governance.render(state),
                "consistency": self.consistency.render(state),
                "certification": self.certification.render(state),
                "runtime": self.runtime.render(state),
                "alert": self.alert.render(state),
                "decision": self.decision.render(state),
                "learning": self.learning.render(state),
                "cosmogenesis": self.cosmogenesis.render(state),
                "global_index": self.global_index.render(state)
            }
        }
