class ServiceLocator:
    """
    Service Locator pattern provider for decoupled dependency resolution.
    """
    _registry = None

    @classmethod
    def set_registry(cls, registry):
        cls._registry = registry

    @classmethod
    def locate(cls, service_id: str):
        if not cls._registry:
            return None
        return cls._registry.get_service(service_id)
