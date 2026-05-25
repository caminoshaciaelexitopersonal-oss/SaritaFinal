import logging

class PrivilegeSurfaceMinimizer:
    """
    Minimizes the privilege surface area across the execution chain.
    """
    def __init__(self, controller):
        self.controller = controller

    async def minimize_chain_privileges(self):
        logging.info("Surface Minimizer: Starting physical privilege reduction.")
        await self.controller.drop_all_capabilities_except(["CAP_SYS_RAWIO", "CAP_NET_ADMIN"])
        await self.controller.enforce_minimal_surface()
        return True
