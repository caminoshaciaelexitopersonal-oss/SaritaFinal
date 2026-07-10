from .service_locator import ServiceLocator

class KernelServiceLocator:
    """
    Unified Kernel adapter for locating service instances cleanly.
    """
    @staticmethod
    def get_service(service_id: str):
        return ServiceLocator.locate(service_id)
