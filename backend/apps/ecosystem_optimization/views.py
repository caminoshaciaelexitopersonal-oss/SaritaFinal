from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import OptimizationProposal, PerformanceMetric
from .serializers import OptimizationProposalSerializer
from .services.optimization_engine import OptimizationEngine
from .services.governance_optimizer import GovernanceOptimizer
from api.permissions import IsSuperAdmin

class OptimizationProposalViewSet(viewsets.ModelViewSet):
    queryset = OptimizationProposal.objects.all()
    serializer_class = OptimizationProposalSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    @action(detail=False, methods=['post'])
    def run_cycle(self, request):
        """Ejecuta el ciclo de optimización del ecosistema."""
        engine = OptimizationEngine()
        proposals = engine.run_optimization_cycle()
        return Response({
            "message": f"Ciclo completado. {len(proposals)} nuevas optimizaciones propuestas.",
            "proposals": OptimizationProposalSerializer(proposals, many=True).data
        })

    @action(detail=True, methods=['post'])
    def apply(self, request, pk=None):
        """Aprueba y ejecuta la optimización."""
        optimizer = GovernanceOptimizer(user=request.user)
        justification = request.data.get("justificacion", "Aplicado vía Consola de Optimización.")
        try:
            optimizer.approve_optimization(pk, justification)
            optimizer.execute_optimization(pk)
            return Response({"status": "EXECUTED", "message": "Ajuste sistémico aplicado correctamente."})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def rollback(self, request, pk=None):
        """Revierte la optimización."""
        optimizer = GovernanceOptimizer(user=request.user)
        try:
            optimizer.rollback_optimization(pk)
            return Response({"status": "REVERTED", "message": "Sistema restaurado al estado previo."})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
