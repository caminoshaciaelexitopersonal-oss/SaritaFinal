from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .models import AlgorithmicCertificate, TrustSignal
from .serializers import AlgorithmicCertificateSerializer, TrustSignalSerializer
from .services import TrustCertificateService, TrustSignalService

class InternationalInteropViewSet(viewsets.ViewSet):
    """
    Gateway Diplomático de Sarita (Z-TRUST-NET).
    Maneja el intercambio de certificados y señales con otros nodos.
    """
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['post'], url_path='generate-certificate')
    def generate_cert(self, request):
        cert_type = request.data.get('type', 'GOVERNANCE')
        node_id = "SARITA_NATIONAL_NODE_01" # Configurable por env

        if cert_type == 'GOVERNANCE':
            cert = TrustCertificateService.generate_governance_certificate(node_id)
        elif cert_type == 'SECURITY':
            cert = TrustCertificateService.generate_security_certificate(node_id)
        else:
            return Response({"error": "Tipo de certificado no soportado"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(AlgorithmicCertificateSerializer(cert).data)

    @action(detail=False, methods=['post'], url_path='verify-external-certificate')
    def verify_external(self, request):
        is_valid = TrustCertificateService.verify_external_certificate(request.data)
        return Response({"is_valid": is_valid})

    @action(detail=False, methods=['post'], url_path='emit-signal')
    def emit_signal(self, request):
        category = request.data.get('category')
        level = request.data.get('level')
        description = request.data.get('description')

        signal = TrustSignalService.emit_threat_signal(category, level, description)
        return Response(TrustSignalSerializer(signal).data)

    @action(detail=False, methods=['get'], url_path='active-signals')
    def list_signals(self, request):
        signals = TrustSignal.objects.order_by('-timestamp')[:50]
        return Response(TrustSignalSerializer(signals, many=True).data)

    @action(detail=False, methods=['post'], url_path='receive-external-signal')
    def receive_signal(self, request):
        TrustSignalService.receive_external_signal(request.data)
        return Response({"status": "SIGNAL_PROCESSED"})
