import math

class BayesianEngine:
    """
    Implements Bayesian parameter estimation, prior-posterior updates, and Bayes Factor calculation.
    """
    def __init__(self):
        pass

    def compute_posterior(self, prior_mean: float, prior_variance: float, sample_mean: float, sample_variance: float, n: int) -> dict:
        # Prevent division by extreme small values for microsecond uniform variances
        safe_variance = max(0.001, sample_variance)

        if n == 0 or safe_variance == 0:
            return {"posterior_mean": prior_mean, "posterior_variance": prior_variance, "bayes_factor": 1.0, "evidence_strength": "ANECDOTAL"}

        precision_prior = 1.0 / prior_variance
        precision_data = n / safe_variance

        precision_posterior = precision_prior + precision_data
        posterior_variance = 1.0 / precision_posterior

        posterior_mean = (prior_mean * precision_prior + sample_mean * precision_data) / precision_posterior

        exponent = 0.5 * (posterior_mean - prior_mean) ** 2 / posterior_variance
        exponent = min(700.0, exponent)  # Protect against float overflow in exponential projection
        bayes_factor = math.exp(exponent)

        return {
            "posterior_mean": round(posterior_mean, 4),
            "posterior_variance": round(posterior_variance, 4),
            "bayes_factor": round(bayes_factor, 4),
            "evidence_strength": "STRONG" if bayes_factor > 10 else ("MODERATE" if bayes_factor > 3 else "ANECDOTAL")
        }
