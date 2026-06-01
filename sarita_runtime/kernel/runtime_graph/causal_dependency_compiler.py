import logging

class CausalDependencyCompiler:
    """
    Compiles physical resource lineage into vertex dependencies.
    Eliminates fragmented dependency governors.
    """
    def __init__(self, nervous_system):
        self.nervous_system = nervous_system

    def compile_physical_dependencies(self, task_id: str, physical_resources: list):
        logging.info(f"Dependency Compiler: Compiling lineage for {task_id}")
        vertex = self.nervous_system.get_vertex(task_id)
        if vertex:
            for res in physical_resources:
                # Add existing owner of resource as dependency
                owner = self.nervous_system.physical_ownership.get(res)
                if owner and owner != task_id:
                    vertex.add_dependency(owner)
        return True
