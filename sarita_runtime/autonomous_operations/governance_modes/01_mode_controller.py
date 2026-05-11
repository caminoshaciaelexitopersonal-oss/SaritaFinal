class ModeController:
    def __init__(self):
        self.current_mode = "NORMAL"

    def switch_mode(self, new_mode):
        print(f"CRITICAL: Switching System Governance to {new_mode} mode.")
        self.current_mode = new_mode
        self.apply_mode_rules(new_mode)

    def apply_mode_rules(self, mode):
        if mode == "WAR_MODE":
            print("- Rule: AI tools restricted to defensive only.")
            print("- Rule: Financial transactions > $1000 require manual override.")
            print("- Rule: Telemetry sampling increased to 100%.")
        elif mode == "LOCKDOWN":
            print("- Rule: All external ingress blocked.")
            print("- Rule: Core database in read-only mode.")

if __name__ == "__main__":
    ctrl = ModeController()
    ctrl.switch_mode("WAR_MODE")
