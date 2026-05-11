import os
import json

class CentralizedConfig:
    def __init__(self, env="staging"):
        self.env = env
        self.config_store = {
            "global": {"trace_enabled": True, "log_level": "INFO"},
            "kafka": {"brokers": ["localhost:9092"], "retry_limit": 5},
            "ai": {"default_model": "gpt-4", "auth_level": 5}
        }

    def get_config(self, module):
        return self.config_store.get(module, {})

    def override_config(self, module, overrides):
        if module in self.config_store:
            self.config_store[module].update(overrides)
            print(f"Config for {module} updated at runtime.")

if __name__ == "__main__":
    cfg = CentralizedConfig()
    print(cfg.get_config("kafka"))
    cfg.override_config("kafka", {"retry_limit": 10})
