import os
import json
import time
from .project_discovery_engine import ProjectDiscoveryEngine
from .global_certifiers import (
    GlobalArchitectureCertifier, GlobalFunctionalCertifier,
    GlobalScientificCertifier, GlobalSecurityCertifier
)
from .global_certifiers_ext import (
    GlobalPerformanceCertifier, GlobalAPICertifier, GlobalQualityCertifier,
    GlobalTestingCertifier, GlobalDocumentationCertifier, GlobalGovernanceCertifier
)
from .global_certification_calculator import GlobalGlobalCertificationIndex
from .evidence_consolidation_engine import EvidenceConsolidationEngine, LegacyCertificationMigrator

class GlobalCertificationEngine:
    """
    Orchestrator for Phase 129 - Global Autocertification.
    """
    def __init__(self):
        self.discovery = ProjectDiscoveryEngine()
        self.arch_cert = GlobalArchitectureCertifier()
        self.func_cert = GlobalFunctionalCertifier()
        self.sci_cert = GlobalScientificCertifier()
        self.sec_cert = GlobalSecurityCertifier()
        self.perf_cert = GlobalPerformanceCertifier()
        self.api_cert = GlobalAPICertifier()
        self.qual_cert = GlobalQualityCertifier()
        self.test_cert = GlobalTestingCertifier()
        self.doc_cert = GlobalDocumentationCertifier()
        self.gov_cert = GlobalGovernanceCertifier()

        self.ggci_engine = GlobalGlobalCertificationIndex()
        self.consolidation = EvidenceConsolidationEngine()
        self.migrator = LegacyCertificationMigrator()

        self.results = {}

    def run_full_certification(self):
        print("Starting Global Autocertification Process...")

        # 1. Discovery
        inventory = self.discovery.scan_repository()
        self.discovery.export_inventories()

        # 2. Specialized Certifications
        self.results["Architecture"] = self.arch_cert.certify(inventory)
        self.results["Functional"] = self.func_cert.certify(inventory)
        self.results["Scientific"] = self.sci_cert.certify(inventory)
        self.results["Security"] = self.sec_cert.certify(inventory)
        self.results["Performance"] = self.perf_cert.certify(inventory)
        self.results["APIs"] = self.api_cert.certify(inventory)
        self.results["Quality"] = self.qual_cert.certify(inventory)
        self.results["Testing"] = self.test_cert.certify(inventory)
        self.results["Documentation"] = self.doc_cert.certify(inventory)
        self.results["Governance"] = self.gov_cert.certify(inventory)

        # 3. GGCI Calculation
        ggci = self.ggci_engine.update_index(self.results)

        # 4. Evidence Consolidation
        self.consolidation.consolidate(inventory)

        # 5. Legacy Migration
        self.migrator.migrate_to_history()

        # 6. Final Report Export
        self._export_global_results(ggci)

        return ggci

    def _export_global_results(self, ggci):
        with open("global_certification_results.json", "w") as f:
            json.dump({
                "ggci": ggci,
                "timestamp": time.time(),
                "dimensions": self.results
            }, f, indent=2)

        with open("ggci_metrics.json", "w") as f:
            json.dump({"ggci": ggci}, f)
