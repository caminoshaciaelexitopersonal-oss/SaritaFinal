import sys
import os
import platform

class EnvironmentCapture:
    """
    Gathers physical environment configurations to guarantee reproducible replay contexts.
    """
    def __init__(self):
        pass

    def capture_environment_metadata(self) -> dict:
        return {
            "python_version": sys.version,
            "os_platform": platform.platform(),
            "cpu_architecture": platform.processor(),
            "working_directory": os.getcwd()
        }
