import os
import sys

def check_purity():
    forbidden_patterns = [".pyc", "__pycache__"]
    found = []
    for root, dirs, files in os.walk("."):
        for d in dirs:
            if d == "__pycache__":
                found.append(os.path.join(root, d))
        for f in files:
            if f.endswith(".pyc") or f.endswith(".db"):
                # Ignore legit dbs if any, but test dbs should be in /tmp
                found.append(os.path.join(root, f))

    if found:
        # Filter out __pycache__ if it's currently being accessed by the validator itself
        # but actually we want absolute purity.
        print(f"Purity Violation! Found: {found}")
        return False
    print("Repository is Pure.")
    return True

if __name__ == "__main__":
    if not check_purity():
        sys.exit(1)
