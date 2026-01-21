
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer, InitiatePaymentSerializer
from .services import PaymentService
from apps.cart.models import Cart

class PaymentViewSet(viewsets.GenericViewSet):
    """
    API endpoint para el proceso de pago.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Un usuario solo puede ver sus propios pagos
        return Payment.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'], url_path='init')
    def initiate_payment(self, request):
        """
        Inicia un proceso de pago para el carro del usuario actual.
        """
        serializer = InitiatePaymentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            cart = Cart.objects.get(user=request.user)
            if cart.items.count() == 0:
                return Response({'error': 'El carro está vacío.'}, status=status.HTTP_400_BAD_REQUEST)
        except Cart.DoesNotExist:
            return Response({'error': 'No se encontró un carro para este usuario.'}, status=status.HTTP_404_NOT_FOUND)

        provider = serializer.validated_data['provider']
        payment = PaymentService.initiate_payment(cart=cart, provider=provider)

        response_serializer = self.get_serializer(payment)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'], url_path='status')
    def get_status(self, request, pk=None):
        """
        Obtiene el estado de un pago específico.
        """
        try:
            payment = self.get_object()
            return Response({'status': payment.status})
        except Payment.DoesNotExist:
            return Response({'error': 'Pago no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

# Vista para webhooks (sin autenticación de sesión)
# Se debería proteger con un mecanismo de firma de webhook en producción
class PaymentWebhookViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'], url_path='confirm')
    def confirm_payment(self, request):
        """
        Endpoint para que los proveedores de pago confirmen el estado de una transacción.
        """
        # La lógica de validación del webhook iría aquí
        transaction_id = request.data.get('transaction_id')
        payment_status = request.data.get('status') # 'PAID', 'FAILED', etc.

        if not transaction_id or not payment_status:
            return Response({'error': 'transaction_id y status son requeridos'}, status=status.HTTP_400_BAD_REQUEST)

        PaymentService.confirm_payment(transaction_id, payment_status)

        return Response(status=status.HTTP_200_OK)
