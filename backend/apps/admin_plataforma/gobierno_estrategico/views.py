from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from api.permissions import IsSuperAdmin
from .services import GovernanceMetricsService
from apps.audit.models import AuditLog

class GlobalAuditLogView(APIView):
    """
    Vista para que el Super Admin supervise eventos críticos en todo el sistema.
    """
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get(self, request):
        logs = AuditLog.objects.all()[:50] # Top 50 logs recientes
        data = [{
            "timestamp": log.timestamp,
            "username": log.username,
            "action": log.get_action_display(),
            "details": log.details
        } for log in logs]
        return Response(data)

class GovernanceSummaryView(APIView):
    """
    Endpoint para el resumen ejecutivo global de gobernanza.
    """
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get(self, request):
        summary = GovernanceMetricsService.get_global_summary()
        return Response(summary)

class ComparativeAnalysisView(APIView):
    """
    Análisis comparativo de rendimiento entre segmentos de prestadores.
    """
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get(self, request):
        analysis = GovernanceMetricsService.get_comparative_analysis()
        return Response(analysis)

class ProviderRankingView(APIView):
    """
    Ranking de los top performers del sistema.
    """
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get(self, request):
        limit = int(request.query_params.get('limit', 10))
        ranking = GovernanceMetricsService.get_provider_ranking(limit=limit)
        return Response(ranking)
