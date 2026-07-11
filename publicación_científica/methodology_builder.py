class MethodologyBuilder:
    """
    Constructs methodology sections detailing experimental protocols, independent/dependent variables, and blocking controls.
    """
    def __init__(self):
        pass

    def build_methodology(self, design_type: str, variables: dict) -> str:
        indep = ", ".join([v["name"] for v in variables.get("independent", [])]) or "None"
        dep = ", ".join([v["name"] for v in variables.get("dependent", [])]) or "None"
        ctrl = ", ".join([v["name"] for v in variables.get("control", [])]) or "None"

        return (
            f"## Methodology\n\n"
            f"The study adopts a standard **{design_type}** protocol managed by SARITA's "
            f"autonomous `ScientificMethodEngine`. In order to validate operational performance changes "
            f"without risk of system-wide side-effects, the experimental platform is partitioned "
            f"using randomized blocking controls.\n\n"
            f"### Variables definition:\n"
            f"- **Independent Variable(s):** {indep}\n"
            f"- **Dependent Variable(s):** {dep}\n"
            f"- **Control Variable(s):** {ctrl}\n\n"
            f"The physical environment metrics (OS platform, thread counts, kernel tick timing, "
            f"and CPU frequencies) are monitored at high frequency via `EnvironmentRebuilder` "
            f"to calculate exact environmental hashes, ensuring that all trials are completed "
            f"under uniform sandbox constraints."
        )
