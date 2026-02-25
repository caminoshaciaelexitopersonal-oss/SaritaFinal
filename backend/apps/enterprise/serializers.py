from rest_framework import serializers
from .domain.policy import EnterprisePolicy
from .domain.strategic_objective import StrategicObjective
from .domain.budget import CorporateBudget
from .domain.workflow import EnterpriseWorkflow, WorkflowStep
from .domain.logs import DecisionLog, PolicyEvaluationLog

class EnterprisePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterprisePolicy
        fields = '__all__'

class StrategicObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategicObjective
        fields = '__all__'

class CorporateBudgetSerializer(serializers.ModelSerializer):
    variance_revenue = serializers.SerializerMethodField()

    class Meta:
        model = CorporateBudget
        fields = '__all__'

    def get_variance_revenue(self, obj):
        return obj.actual_revenue - obj.revenue_target

class EnterpriseWorkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterpriseWorkflow
        fields = '__all__'

class DecisionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecisionLog
        fields = '__all__'
