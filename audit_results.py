import os
import re

def audit_endpoints():
    endpoints = []
    # Simplified scan of urls.py files
    for root, dirs, files in os.walk('backend'):
        if 'urls.py' in files:
            with open(os.path.join(root, 'urls.py'), 'r') as f:
                content = f.read()
                matches = re.findall(r"path\(['\"](.+?)['\"],", content)
                for m in matches:
                    endpoints.append({'path': m, 'module': root})
    return endpoints

def audit_debt():
    debt = []
    patterns = ['TODO', 'FIXME', 'NotImplementedError']
    for root, dirs, files in os.walk('backend/apps'):
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(root, file)
                with open(path, 'r', errors='ignore') as f:
                    for i, line in enumerate(f):
                        for p in patterns:
                            if p in line:
                                debt.append({'file': path, 'line': i+1, 'type': p, 'content': line.strip()})
    return debt

endpoints = audit_endpoints()
debt = audit_debt()

print(f"Total Endpoints Found: {len(endpoints)}")
print(f"Total Technical Debt Markers: {len(debt)}")
