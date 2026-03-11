import os
import re

# 1. Fix backend/api/serializers.py syntax error
path_ser = 'backend/api/serializers.py'
with open(path_ser, 'r') as f:
    content = f.read()

# Fix the broken line: return {"status": "success", "message": f"Method update executed"}word = validated_data.pop('password', None)
content = content.replace("return {\"status\": \"success\", \"message\": f\"Method update executed\"}word = validated_data.pop('password', None)",
                          "password = validated_data.pop('password', None)")

with open(path_ser, 'w') as f:
    f.write(content)
print("Fixed syntax in serializers.py")

# 2. Fix contract violations in backend/apps/sadi_agent/voice_providers.py
path_voice = 'backend/apps/sadi_agent/voice_providers.py'
with open(path_voice, 'r') as f:
    content = f.read()

# Restore abstract methods to use 'pass'
content = re.sub(r'def transcribe\(self, audio_path: Path\) -> Tuple\[str, str\]:.*?return {.*?}',
                 'def transcribe(self, audio_path: Path) -> Tuple[str, str]:\n        pass', content, flags=re.DOTALL)
content = re.sub(r'def speak\(self, text: str, output_path: Path\):.*?return {.*?}',
                 'def speak(self, text: str, output_path: Path):\n        pass', content, flags=re.DOTALL)

with open(path_voice, 'w') as f:
    f.write(content)
print("Fixed contract violations in voice_providers.py")

# 3. Clean up root directory from audit scripts
scripts = [
    'audit_results.py', 'detailed_audit.py', 'detailed_audit_v2.py',
    'detailed_db_audit.py', 'detailed_db_audit_core.py', 'tech_debt_audit.py',
    'platform_audit.py', 'agent_readiness.py', 'generate_stub_inventory.py',
    'generate_stub_inventory_v2.py', 'fix_p1_stubs.py', 'fix_p1_stubs_v2.py',
    'fix_p1_stubs_v3.py', 'fix_p2_stubs.py', 'fix_p3_stubs.py', 'fix_p3_stubs_v2.py',
    'fix_p5_stubs.py', 'fix_p5_stubs_v2.py', 'fix_p8_stubs.py', 'fix_p8_stubs_v2.py',
    'test_implemented_stubs.py', 'check_stubs_final.py', 'check_stubs_final_v2.py',
    'fix_remaining_stubs.py', 'fix_remaining_stubs_v2.py', 'fix_remaining_stubs_v3.py',
    'final_stub_fixer.py', 'final_stub_fixer_v2.py', 'test_load.py'
]

for s in scripts:
    if os.path.exists(s):
        os.remove(s)
        print(f"Removed temporary script: {s}")
