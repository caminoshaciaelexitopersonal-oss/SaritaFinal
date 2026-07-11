import collections

class ServiceDependencyManager:
    """
    Manages dependency declarations between services and prevents cyclic loads.
    """
    def __init__(self):
        self.dependencies = collections.defaultdict(list)

    def declare_dependency(self, service_id: str, depends_on: str):
        self.dependencies[service_id].append(depends_on)

    def check_cycles(self) -> bool:
        visited = set()
        stack = set()

        def dfs(node):
            visited.add(node)
            stack.add(node)
            for neighbor in self.dependencies[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in stack:
                    return True
            stack.remove(node)
            return False

        for service in list(self.dependencies.keys()):
            if service not in visited:
                if dfs(service):
                    return True # Cycle detected!
        return False
