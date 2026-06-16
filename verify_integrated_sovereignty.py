import os
import sys

# Run phase scripts
for phase in ["111", "112", "113"]:
    print(f"\n>>> VERIFYING PHASE {phase}...")
    res = os.system(f"python3 verify_phase_{phase}.py > /dev/null 2>&1")
    if res == 0:
        print(f"PHASE {phase} SUCCESS")
    else:
        print(f"PHASE {phase} FAILED")
        sys.exit(1)

# Run integrated causal audit
print("\n>>> VERIFYING INTEGRATED CAUSAL CHAIN...")
res = os.system("python3 integrated_causal_audit.py > /dev/null 2>&1")
if res == 0:
    print("INTEGRATED CAUSAL CHAIN SUCCESS")
else:
    print("INTEGRATED CAUSAL CHAIN FAILED")
    sys.exit(1)

print("\nALL SOVEREIGN EVOLUTION LAYERS VERIFIED.")
