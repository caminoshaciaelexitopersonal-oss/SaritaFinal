import os
import sys

def enforce_repository_lockdown():
    """
    Enforces absolute repository purity (Phase 81.9).
    """
    forbidden_extensions = [".pyc", ".db-wal", ".db-shm"]
    forbidden_directories = ["__pycache__"]

    violations = []
    for root, dirs, files in os.walk("."):
        for d in dirs:
            if d in forbidden_directories:
                violations.append(os.path.join(root, d))
        for f in files:
            for ext in forbidden_extensions:
                if f.endswith(ext):
                    violations.append(os.path.join(root, f))

    if violations:
        print("CONSTITUTIONAL REPOSITORY LOCKDOWN: Violations detected!")
        for v in violations:
            print(f" - {v}")
        return False

    print("Repository Constitutional Lockdown: Verified Pure.")
    return True

if __name__ == "__main__":
    if not enforce_repository_lockdown():
        sys.exit(1)
