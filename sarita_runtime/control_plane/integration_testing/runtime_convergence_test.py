import asyncio
from sarita_runtime.control_plane.bootstrap.bootstrap_engine import BootstrapEngine
from sarita_runtime.control_plane.service_discovery.service_registry import ServiceRegistry

async def test_full_convergence():
    print("Integration Test: Startup and Discovery Convergence...")
    # 1. Start Bootstrap
    be = BootstrapEngine()
    await be.initialize_ecosystem()

    # 2. Register Service
    reg = ServiceRegistry()
    reg.register_service("TestWorker", "node-int-01")

    # 3. Validate
    if be.current_phase == "READY" and reg.get_service("TestWorker")["status"] == "ALIVE":
        print("Integration Test: PASS")
    else:
        print("Integration Test: FAIL")

if __name__ == "__main__":
    asyncio.run(test_full_convergence())
