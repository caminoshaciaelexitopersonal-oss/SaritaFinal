from django.db import models
import uuid

# This file fulfills the requirement of having proposal_model.py
# Although DecisionProposal is in models.py, we can provide specialized logic here.

class ProposalAnalytic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    proposal = models.OneToOneField('enterprise_core.DecisionProposal', on_delete=models.CASCADE, related_name='analytics')

    simulation_data = models.JSONField(default=dict, help_text="Impact simulation results")
    confidence_level = models.FloatField(default=0.95)

    created_at = models.DateTimeField(auto_now_add=True)

    __schema_version__ = "v2.1"

    class Meta:
        app_label = 'enterprise_core'
