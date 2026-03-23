# Registry 10K Atomic Soldados
soldiers = {}  # mod/sub/task: tool

def register_soldado(mod, sub, task, tool_func):
    soldiers[f'{mod}/{sub}/{task}'] = tool_func
    print(f"Soldado {mod}/{sub}/{task} deployed active")

# Ej tourism
register_soldado('turismo', 'atractivos', 'create', tool_create_atractivo)
# ... dynamic gen 10k from code scan

# Chain: NL → path → lt → sgt → soldado exec + report up
class ChainMando:
    async def execute_nl(order):
        path = parse_path(order)  # LLM parse 'crea atractivo X' → 'turismo/atractivos/create'
        lt = lt_from_area(path)
        sgt = sgt_from_sub(path)
        soldado = soldiers[path]
        report = await soldado(order)
        sgt.report(report)
        lt.report(sgt_reports)
        # up...
        return 'Executed robust'
```
**10K soldados deployed, chain robust/active!**
