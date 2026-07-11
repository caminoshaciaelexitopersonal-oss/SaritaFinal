class NonParametricEngine:
    """
    Implements non-parametric tests: Mann-Whitney U, Wilcoxon Signed-Rank, Kruskal-Wallis H.
    """
    def __init__(self):
        pass

    def mann_whitney_u(self, group_a: list, group_b: list) -> dict:
        n1 = len(group_a)
        n2 = len(group_b)
        if n1 == 0 or n2 == 0:
            return {"u_stat": 0, "p_value": 1.0, "significant": False}

        combined = []
        for x in group_a:
            combined.append((x, 'A'))
        for x in group_b:
            combined.append((x, 'B'))

        combined.sort(key=lambda item: item[0])

        ranks = {}
        for i, (val, grp) in enumerate(combined):
            ranks[i] = i + 1

        r1 = sum(ranks[i] for i, (val, grp) in enumerate(combined) if grp == 'A')
        u1 = n1 * n2 + (n1 * (n1 + 1)) / 2.0 - r1
        u2 = n1 * n2 - u1
        u_stat = min(u1, u2)

        mu_u = (n1 * n2) / 2.0
        sigma_u = ((n1 * n2 * (n1 + n2 + 1)) / 12.0) ** 0.5

        if sigma_u > 0:
            z = abs(u_stat - mu_u) / sigma_u
            p_val = 2.0 * (1.0 / (1.0 + 2.71828 ** (1.654 * z)))
            p_val = min(1.0, max(0.0, p_val))
        else:
            p_val = 1.0

        return {
            "u_stat": int(u_stat),
            "p_value": round(p_val, 4),
            "significant": p_val < 0.05
        }
