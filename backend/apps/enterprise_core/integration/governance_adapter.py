from apps.admin_plataforma.services.governance_kernel import GovernanceKernel, AuthorityLevel

class GovernanceAdapter:
    """
    Ensures every EOS decision passes through the GovernanceKernel.
    Part of the Governance Validation Layer.
    """

    @staticmethod
    def validate_and_execute(intention: str, parameters: dict, user=None):
        kernel = GovernanceKernel(user=user)
        return kernel.resolve_and_execute(intention, parameters)
