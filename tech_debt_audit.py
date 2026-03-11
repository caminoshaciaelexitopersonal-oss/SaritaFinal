import os
import re

def audit_debt():
    debt_items = []
    patterns = {
        'TODO': r'TODO:',
        'FIXME': r'FIXME:',
        'pass': r'pass',
        'NotImplementedError': r'NotImplementedError'
    }

    for root, dirs, files in os.walk('backend'):
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(root, file)
                with open(path, 'r', errors='ignore') as f:
                    for i, line in enumerate(f):
                        for label, pattern in patterns.items():
                            if re.search(pattern, line):
                                # Filter out false positives for 'pass'
                                if label == 'pass' and not re.match(r'^\s*pass\s*$', line):
                                    continue
                                if label == 'pass' and 'backend/apps' not in root:
                                    continue

                                debt_items.append({
                                    'file': path,
                                    'line': i + 1,
                                    'type': label,
                                    'context': line.strip()
                                })
    return debt_items

debt = audit_debt()
print("| Archivo | Línea | Tipo | Contexto |")
print("| :--- | :--- | :--- | :--- |")
for d in debt[:100]:
    print(f"| {d['file']} | {d['line']} | {d['type']} | {d['context']} |")
