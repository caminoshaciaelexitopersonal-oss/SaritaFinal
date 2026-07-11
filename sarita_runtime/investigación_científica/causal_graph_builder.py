class CausalGraphBuilder:
    """
    Constructs and traverses directed acyclic graphs (DAGs) representing causal structural equations.
    """
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, node: str):
        self.nodes.add(node)

    def add_edge(self, parent: str, child: str):
        self.nodes.add(parent)
        self.nodes.add(child)
        if parent not in self.edges:
            self.edges[parent] = []
        if child not in self.edges[parent]:
            self.edges[parent].append(child)

    def get_paths(self, start: str, end: str, path=None) -> list:
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.edges:
            return []
        paths = []
        for node in self.edges[start]:
            if node not in path:
                newpaths = self.get_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def detect_confounders(self, x: str, y: str) -> list:
        confounders = []
        for node in self.nodes:
            if node != x and node != y:
                paths_to_x = self.get_paths(node, x)
                paths_to_y = self.get_paths(node, y)
                if paths_to_x and paths_to_y:
                    confounders.append(node)
        return confounders
