from rest_framework import viewsets, permissions, serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import StrategicRule, DecisionProposal
from .decision_engine import EnterpriseDecisionEngine

class StrategicRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategicRule
        fields = '__all__'

class DecisionProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecisionProposal
        fields = '__all__'

class DecisionProposalViewSet(viewsets.ModelViewSet):
    """
    Tor V2: UI for decision-making.
    Exposes strategic proposals and risks for the Super Admin dashboard.
    """
    queryset = DecisionProposal.objects.all()
    serializer_class = DecisionProposalSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(detail=True, methods=['post'])
    def approve_and_execute(self, request, pk=None):
        """
        Manually approves and triggers execution via GovernanceKernel.
        """
        proposal = self.get_object()

        try:
            result = EnterpriseDecisionEngine.execute_proposal(
                proposal_id=str(proposal.id),
                user=request.user
            )
            return Response(result)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_403_FORBIDDEN)

class StrategicRuleViewSet(viewsets.ModelViewSet):
    queryset = StrategicRule.objects.all()
    serializer_class = StrategicRuleSerializer
    permission_classes = [permissions.IsAdminUser]
