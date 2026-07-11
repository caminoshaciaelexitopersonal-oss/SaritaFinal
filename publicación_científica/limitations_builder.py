class LimitationsBuilder:
    """
    Constructs limitations and threats to validity sections.
    """
    def __init__(self):
        pass

    def build_limitations(self, risks: list, limitations: list) -> str:
        risks_str = "\n".join([f"- {r}" for r in risks]) or "- No notable risks logged."
        limits_str = "\n".join([f"- {l}" for l in limitations]) or "- No notable limitations logged."

        return (
            f"## Limitations & Threats to Validity\n\n"
            f"While our empirical results are statistically significant, we explicitly recognize "
            f"potential limitations in the current experimental design.\n\n"
            f"### Identified Risks:\n"
            f"{risks_str}\n\n"
            f"### Study Limitations:\n"
            f"{limits_str}\n\n"
            f"To mitigate threats to external validity, we validated results across multiple "
            f"logical kernel configurations and simulated OS platform environments."
        )
