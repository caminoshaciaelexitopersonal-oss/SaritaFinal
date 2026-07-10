import os
import json
import ast

class ArchitectureDiscoveryEngine:
    """
    Builds graps and models of the system topology.
    Phase 128.3.
    """
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.graph = {"nodes": [], "edges": []}

    def map_project_structure(self):
        for root, dirs, files in os.walk(self.root_dir):
            for d in dirs:
                self.graph["nodes"].append({"id": d, "type": "MODULE"})
            for f in files:
                if f.endswith(".py"):
                    self.graph["nodes"].append({"id": f, "type": "FILE", "path": os.path.join(root, f)})
        return self.graph

    def build_dependency_graph(self):
        for node in self.graph["nodes"]:
            if node["type"] == "FILE":
                deps = self._extract_imports(node["path"])
                for dep in deps:
                    self.graph["edges"].append({
                        "source": node["id"],
                        "target": dep,
                        "type": "IMPORT"
                    })
        return self.graph

    def _extract_imports(self, filepath):
        imports = []
        try:
            with open(filepath, "r") as f:
                tree = ast.parse(f.read())
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for name in node.names:
                            imports.append(name.name)
                    elif isinstance(node, ast.ImportFrom):
                        imports.append(node.module)
        except Exception:
            pass
        return [i for i in imports if i]

    def export_topology(self):
        with open("architecture_graph.json", "w") as f:
            json.dump(self.graph, f, indent=2)

        topology = {"topology": "LAYERED", "critical_points": ["meta_cosmogenesis"]}
        with open("architecture_topology.json", "w") as f:
            json.dump(topology, f, indent=2)

        matrix = [[0]*len(self.graph["nodes"]) for _ in range(len(self.graph["nodes"]))]
        with open("dependency_matrix.json", "w") as f:
            json.dump(matrix, f)

        return "EXPORT_SUCCESS"
