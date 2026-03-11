import os
import re

def audit_platform(path):
    files = []
    for root, dirs, files_in_dir in os.walk(path):
        for file in files_in_dir:
            if file.endswith(('.ts', '.tsx', '.js', '.jsx')):
                files.append(os.path.join(root, file))
    return files

web_files = audit_platform('interfaz/src')
mobile_files = audit_platform('apps/mobile/src')
desktop_files = audit_platform('apps/desktop/main')

print(f"Web Source Files: {len(web_files)}")
print(f"Mobile Source Files: {len(mobile_files)}")
print(f"Desktop Main Files: {len(desktop_files)}")

# Look for specific production-ready features
features = ['offline', 'sync', 'auth', 'pos', 'payment']
for platform, path in [('Web', 'interfaz'), ('Mobile', 'apps/mobile'), ('Desktop', 'apps/desktop')]:
    print(f"\n--- {platform} Features ---")
    for f in features:
        # grep-like search
        count = 0
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(('.ts', '.tsx', '.js', '.jsx')):
                    with open(os.path.join(root, file), 'r', errors='ignore') as content_file:
                        if f in content_file.read().lower():
                            count += 1
        print(f"Feature '{f}': {count} files")
