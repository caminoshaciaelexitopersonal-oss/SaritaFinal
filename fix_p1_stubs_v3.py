import os
import re

def replace_in_file(filepath, search_pattern, replacement):
    with open(filepath, 'r') as f:
        content = f.read()
    new_content = re.sub(search_pattern, replacement, content, flags=re.MULTILINE|re.DOTALL)
    with open(filepath, 'w') as f:
        f.write(new_content)

# 3. Implement verify_chain in audit_engine.py
audit_logic = """    @staticmethod
    def verify_chain(logs):
        \"\"\"
        Verifica la integridad de una cadena de registros de auditoría.
        \"\"\"
        if not logs:
            return True, "Chain empty"

        previous_hash = ""
        for i, log in enumerate(logs):
            # Asumimos que log tiene data_json y integrity_hash
            calculated_hash = AuditEngine.generate_hash(log.data_json, previous_hash)
            if calculated_hash != log.integrity_hash:
                return False, f"Integrity break at sequence {i} (ID: {log.id})"
            previous_hash = log.integrity_hash

        return True, "Integrity verified\""""

replace_in_file('backend/apps/core_erp/audit_engine.py',
                r'    @staticmethod\s+def verify_chain\(logs\):\s+.*?pass',
                audit_logic)

print("Priority 1 stubs implemented v3.")
