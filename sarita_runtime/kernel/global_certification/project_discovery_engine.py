import os
import json
import re

class ProjectDiscoveryEngine:
    """
    Scans the repository to build a complete inventory of SARITA's components.
    Phase 129.3.
    """
    def __init__(self, root_dir="."):
        self.root_dir = root_dir
        self.inventory = {
            "phases": [],
            "modules": [],
            "engines": [],
            "apis": [],
            "tests": [],
            "audits": [],
            "indices": []
        }

    def scan_repository(self):
        print(f"Scanning repository at {self.root_dir}...")
        for root, dirs, files in os.walk(self.root_dir):
            if ".git" in root or "__pycache__" in root: continue

            for d in dirs:
                if d.startswith("phase_") or "phase" in d.lower():
                    self.inventory["phases"].append(d)

            for f in files:
                path = os.path.join(root, f)

                # Engines
                if f.endswith("_engine.py") or "engine" in f.lower():
                    self.inventory["engines"].append(path)

                # Modules (Simplified as python packages)
                if f == "__init__.py":
                    self.inventory["modules"].append(root)

                # Tests
                if f.startswith("test_") or f.endswith("_test.py") or "testing" in root:
                    self.inventory["tests"].append(path)

                # Audits
                if f.endswith(".md") and ("audit" in f.lower() or "report" in f.lower()):
                    self.inventory["audits"].append(path)

                # Indices
                if f.endswith("_index.py") or "index" in f.lower():
                    self.inventory["indices"].append(path)

                # APIs (Simplified)
                if "api" in f.lower() or "interface" in f.lower():
                    self.inventory["apis"].append(path)

        # Distinct phases from files like verify_phase_XXX.py
        for f in os.listdir(self.root_dir):
            match = re.search(r"phase_(\d+)", f)
            if match:
                self.inventory["phases"].append(match.group(1))

        self.inventory["phases"] = sorted(list(set(self.inventory["phases"])))
        return self.inventory

    def export_inventories(self):
        with open("project_inventory.json", "w") as f:
            json.dump(self.inventory, f, indent=2)

        with open("module_inventory.json", "w") as f:
            json.dump({"modules": list(set(self.inventory["modules"]))}, f, indent=2)

        with open("phase_inventory.json", "w") as f:
            json.dump({"phases": self.inventory["phases"]}, f, indent=2)

        return "INVENTORY_EXPORTED"
