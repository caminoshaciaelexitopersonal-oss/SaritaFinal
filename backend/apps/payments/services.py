
from decimal import Decimal
from .models import Payment
from apps.cart.models import Cart

class PaymentService:
    """
    Servicio para manejar la lógica de pagos de forma agnóstica al proveedor.
    """

    @staticmethod
    def initiate_payment(cart: Cart, provider: str) -> Payment:
        """
        Inicia un proceso de pago para un carro de compras.
        Crea un registro de Pago en la base de datos con estado 'INIT'.
        """
        total_price = sum(item.total_price for item in cart.items.all())

        payment = Payment.objects.create(
            cart=cart,
            user=cart.user,
            amount=total_price,
            provider=provider,
            status='INIT'
        )

        # Lógica futura:
        # 1. Llamar a la API del proveedor de pago (ej. Wompi, Stripe).
        # 2. Obtener una URL de pago o un ID de transacción.
        # 3. Guardar el ID de transacción y actualizar el estado a 'PENDING'.
        # 4. Devolver el objeto Payment con la información necesaria.

        print(f"Iniciando pago para el carro {cart.id} por ${total_price} con {provider}")

        return payment

    @staticmethod
    def confirm_payment(transaction_id: str, status: str):
        """
        Confirma el resultado de un pago basado en un webhook o callback del proveedor.
        """
        try:
            payment = Payment.objects.get(transaction_id=transaction_id)

            if status.upper() == 'PAID':
                payment.status = 'PAID'
                # Lógica futura:
                # - Crear la suscripción para el usuario.
                # - Vaciar el carro de compras.
                # - Enviar email de confirmación.
            elif status.upper() in ['FAILED', 'CANCELLED']:
                payment.status = status.upper()

            payment.save()
            print(f"Pago {payment.id} actualizado a estado {payment.status}")
            return payment

        except Payment.DoesNotExist:
            print(f"Error: No se encontró un pago con transaction_id {transaction_id}")
            return None

    @staticmethod
    def get_payment_status(payment_id: int):
        """
        Verifica el estado de un pago en nuestro sistema.
        """
        try:
            payment = Payment.objects.get(id=payment_id)
            return payment.status
        except Payment.DoesNotExist:
            return None
