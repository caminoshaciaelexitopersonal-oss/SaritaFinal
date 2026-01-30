from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import FinancialEventRecord, FinancialMetric
from django.db.models import Sum, Count, Avg
from api.permissions import IsSuperAdmin

class FinancialDashboardViewSet(viewsets.ViewSet):
    """
    Vista para el ERP del Super Admin con métricas de rentabilidad en tiempo real.
    """
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def list(self, request):
        # Resumen Global
        total_sessions = FinancialEventRecord.objects.filter(event_type='voice_session_started').count()
        total_costs = FinancialEventRecord.objects.filter(event_type='voice_minute_consumed').aggregate(total=Sum('value'))['total'] or 0.0

        # CAC Promedio
        avg_cac = total_costs / total_sessions if total_sessions > 0 else 0.0

        return Response({
            "summary": {
                "total_sessions": total_sessions,
                "total_adq_costs": total_costs,
                "avg_cac": avg_cac
            },
            "recent_events": FinancialEventRecord.objects.all()[:10].values()
        })

    @action(detail=False, methods=['get'])
    def roi_analysis(self, request):
        """Métricas de ROI por tipo de usuario."""
        # En una implementación real esto consultaría FinancialMetric
        return Response([
            {"dimension": "user_type:prestador", "roi": 4.5, "cac": 0.85, "ltv": 4.67},
            {"dimension": "user_type:gobierno", "roi": 12.2, "cac": 2.10, "ltv": 27.7}
        ])
