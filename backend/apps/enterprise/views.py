from rest_framework import viewsets, permissions
from .domain.policy import EnterprisePolicy
from .domain.strategic_objective import StrategicObjective
from .domain.budget import CorporateBudget
from .domain.workflow import EnterpriseWorkflow
from .domain.logs import DecisionLog
from .serializers import (
    EnterprisePolicySerializer, StrategicObjectiveSerializer,
    CorporateBudgetSerializer, EnterpriseWorkflowSerializer,
    DecisionLogSerializer
)
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from api.permissions import IsSuperAdmin

class EnterprisePolicyViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    queryset = EnterprisePolicy.objects.all()
    serializer_class = EnterprisePolicySerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

class StrategicObjectiveViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    queryset = StrategicObjective.objects.all()
    serializer_class = StrategicObjectiveSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

class CorporateBudgetViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    queryset = CorporateBudget.objects.all()
    serializer_class = CorporateBudgetSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

class EnterpriseWorkflowViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    queryset = EnterpriseWorkflow.objects.all()
    serializer_class = EnterpriseWorkflowSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

class DecisionLogViewSet(SystemicERPViewSetMixin, viewsets.ReadOnlyModelViewSet):
    queryset = DecisionLog.objects.all()
    serializer_class = DecisionLogSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]
