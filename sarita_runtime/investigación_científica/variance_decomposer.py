class VarianceDecomposer:
    """
    Decomposes total experimental variance into within-group (internal noise) and between-group (treatment effect) components.
    """
    def __init__(self):
        pass

    def decompose(self, groups: list) -> dict:
        total_elements = [x for g in groups for x in g]
        n_total = len(total_elements)
        if n_total < 2:
            return {"within_variance": 0.0, "between_variance": 0.0, "total_variance": 0.0}

        grand_mean = sum(total_elements) / n_total
        ss_total = sum((x - grand_mean)**2 for x in total_elements)

        ssb = 0.0
        for g in groups:
            n_g = len(g)
            if n_g == 0:
                continue
            mean_g = sum(g) / n_g
            ssb += n_g * ((mean_g - grand_mean) ** 2)

        ssw = 0.0
        for g in groups:
            if len(g) == 0:
                continue
            mean_g = sum(g) / len(g)
            ssw += sum((x - mean_g)**2 for x in g)

        df_total = n_total - 1
        total_variance = ss_total / df_total if df_total > 0 else 0.0

        return {
            "within_variance": round(ssw / df_total, 4) if df_total > 0 else 0.0,
            "between_variance": round(ssb / df_total, 4) if df_total > 0 else 0.0,
            "total_variance": round(total_variance, 4)
        }
