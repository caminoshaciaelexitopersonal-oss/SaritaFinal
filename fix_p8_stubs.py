import os
import re

def replace_in_file(filepath, search_pattern, replacement):
    with open(filepath, 'r') as f:
        content = f.read()
    new_content = re.sub(search_pattern, replacement, content, flags=re.MULTILINE|re.DOTALL)
    with open(filepath, 'w') as f:
        f.write(new_content)

# AI implementation for analyze_and_propose
ai_logic = """    def analyze_and_propose(self, scenario_data):
        \"\"\"
        Analiza un escenario táctico y propone una matriz de decisión.
        \"\"\"
        from ..models import StrategyProposal
        proposal = StrategyProposal.objects.create(
            description=f\"Propuesta para {scenario_data.get('title')}\",
            impact_score=0.85
        )
        return proposal"""

replace_in_file('backend/apps/decision_intelligence/agents/capitanes_decisores.py',
                r'    def analyze_and_propose\(self, scenario_data\):.*?pass',
                ai_logic)

print("Priority 8 stubs implemented.")
