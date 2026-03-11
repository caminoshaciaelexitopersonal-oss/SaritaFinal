import os
import shutil

def cleanup():
    # Remove all Jules-generated temporary scripts from root
    root_files = os.listdir('.')
    for f in root_files:
        if f.endswith('.py') and f not in ['manage.py']:
            if f.startswith(('fix_', 'cleanup_', 'detailed_', 'tech_debt_', 'agent_readiness', 'generate_stub', 'run_5000', 'audit_results', 'test_implemented', 'final_stub', 'chaos_simulation', 'mass_load_simulation', 'bottleneck_analysis', 'enterprise_security_simulation', 'security_hardening_test', 'ecosystem_integration_test', 'audit_results', 'detailed_audit', 'detailed_db_audit', 'db_map')):
                os.remove(f)
                print(f"Removed legacy script: {f}")

cleanup()
