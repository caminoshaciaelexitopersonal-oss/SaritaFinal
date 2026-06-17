import os
import sys

phases = ["111", "112", "113", "114", "115"]
for phase in phases:
    print(f"\n>>> VERIFYING PHASE {phase}...")
    res = os.system(f"python3 verify_phase_{phase}.py > /dev/null 2>&1")
    if res == 0:
        print(f"PHASE {phase} SUCCESS")
    else:
        print(f"PHASE {phase} FAILED")
        sys.exit(1)

demos = [
    "demonstrate_real_evolution.py",
    "demonstrate_scientific_reproducibility.py",
    "demonstrate_architectural_novelty.py",
    "demonstrate_constitutional_integrity.py",
    "demonstrate_evolutionary_chain.py",
    "demonstrate_causal_reconstruction.py",
    "retrospective_index_audit.py"
]
for demo in demos:
    print(f"\n>>> EXECUTING DEMO: {demo}...")
    res = os.system(f"python3 {demo} > /dev/null 2>&1")
    if res == 0:
        print(f"DEMO {demo} SUCCESS")
    else:
        print(f"DEMO {demo} FAILED")
        sys.exit(1)

print("\nSOVEREIGN EVOLUTION OPTIMALITY CERTIFICATION COMPLETE.")
