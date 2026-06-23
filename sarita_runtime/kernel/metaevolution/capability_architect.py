import hashlib

class CapabilityArchitect:
    """
    Defines specifications for new capabilities.
    """
    def define_spec(self, index, diagnostic_report):
        # Generate a deterministic spec based on index and diagnostic report
        seed = f"cap_{index}_{diagnostic_report.get('timestamp')}"
        spec_id = hashlib.sha256(seed.encode()).hexdigest()[:8]

        return {
            "id": f"CAP-{spec_id}",
            "type": "evolved_module",
            "complexity_index": (index % 100) / 100.0,
            "domain": "kernel_optimization"
        }
