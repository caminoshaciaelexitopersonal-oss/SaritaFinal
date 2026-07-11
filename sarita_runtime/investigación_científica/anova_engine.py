class AnovaEngine:
    """
    Performs One-Way Analysis of Variance (ANOVA) across multiple groups to test for equal means.
    """
    def __init__(self):
        pass

    def calculate_one_way_anova(self, groups: list) -> dict:
        k = len(groups)
        if k < 2:
            return {"f_stat": 0.0, "p_value": 1.0, "significant": False}

        all_elements = [x for g in groups for x in g]
        n_total = len(all_elements)
        if n_total <= k:
            return {"f_stat": 0.0, "p_value": 1.0, "significant": False}

        grand_mean = sum(all_elements) / n_total

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
            ssw += sum((x - mean_g) ** 2 for x in g)

        df_between = k - 1
        df_within = n_total - k

        ms_between = ssb / df_between if df_between > 0 else 0.0
        ms_within = ssw / df_within if df_within > 0 else 0.0

        if ms_within == 0.0:
            f_stat = 99.99
        else:
            f_stat = ms_between / ms_within

        p_val_approx = 0.01 if f_stat > 3.0 else (0.04 if f_stat > 2.0 else 0.50)

        return {
            "ss_between": round(ssb, 4),
            "ss_within": round(ssw, 4),
            "df_between": df_between,
            "df_within": df_within,
            "ms_between": round(ms_between, 4),
            "ms_within": round(ms_within, 4),
            "f_stat": round(f_stat, 4),
            "p_value": p_val_approx,
            "significant": p_val_approx < 0.05
        }
