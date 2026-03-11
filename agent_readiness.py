import os
import re

def check_agent_readiness():
    results = []
    agent_dir = 'backend/apps/sarita_agents'
    for root, dirs, files in os.walk(agent_dir):
        for file in files:
            if file.endswith('.py') and ('coronel' in file or 'capitan' in file or 'teniente' in file or 'soldado' in file):
                path = os.path.join(root, file)
                with open(path, 'r', errors='ignore') as f:
                    content = f.read()
                    is_template = 'template' in file
                    has_not_implemented = 'NotImplementedError' in content
                    has_logic = len(content.split('\n')) > 50

                    status = "Template" if is_template else ("Stub" if has_not_implemented else "Implementado")
                    results.append({
                        'agent': file,
                        'status': status,
                        'logic_lines': len(content.split('\n'))
                    })
    return results

readiness = check_agent_readiness()
print("| Agente | Estado | Líneas |")
print("| :--- | :--- | :--- |")
for r in sorted(readiness, key=lambda x: x['status']):
    print(f"| {r['agent']} | {r['status']} | {r['logic_lines']} |")
