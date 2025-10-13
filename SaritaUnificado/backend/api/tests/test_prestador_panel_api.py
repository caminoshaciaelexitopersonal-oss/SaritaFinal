from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import CustomUser, PrestadorServicio, ServicioTuristico, CategoriaPrestador, Booking, Factura
from core.auth.jwt_utils import generate_jwt_for_user
from datetime import datetime

class PrestadorPanelAPITests(APITestCase):
    """
    Pruebas para los endpoints del panel del prestador de servicios.
    """

    def setUp(self):
        # Crear un usuario con rol PRESTADOR
        self.prestador_user = CustomUser.objects.create_user(
            'prestador_test', 'prestador@example.com', 'password123', role=CustomUser.Role.PRESTADOR
        )
        # Crear el perfil de PrestadorServicio asociado
        self.categoria = CategoriaPrestador.objects.create(nombre="Hoteles", slug="hoteles")
        self.prestador_profile = PrestadorServicio.objects.create(
            usuario=self.prestador_user,
            nombre_negocio="Hotel de Prueba",
            categoria=self.categoria,
            aprobado=True
        )

        # Generar token JWT para autenticación
        self.prestador_token = generate_jwt_for_user(self.prestador_user)

        # URLs
        self.servicios_list_url = reverse('prestador-servicio-list')
        self.bookings_list_url = reverse('prestador-booking-list')
        self.facturas_list_url = reverse('prestador-factura-list')

    def _get_auth_header(self, token_data):
        return {'HTTP_AUTHORIZATION': f'Bearer {token_data["access"]}'}

    def test_prestador_can_list_own_servicios(self):
        """Un PRESTADOR puede listar sus propios servicios."""
        # Crear un servicio para este prestador
        ServicioTuristico.objects.create(
            prestador=self.prestador_profile,
            nombre="Habitación Doble",
            descripcion="Una habitación cómoda.",
            precio=150.00
        )
        self.client.credentials(**self._get_auth_header(self.prestador_token))
        response = self.client.get(self.servicios_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['nombre'], "Habitación Doble")

    def test_prestador_cannot_list_other_servicios(self):
        """Un PRESTADOR no puede listar servicios de otros prestadores."""
        # Crear otro prestador y su servicio
        other_user = CustomUser.objects.create_user('otro_prestador', 'otro@example.com', 'password123', role=CustomUser.Role.PRESTADOR)
        other_profile = PrestadorServicio.objects.create(usuario=other_user, nombre_negocio="Otro Hotel", categoria=self.categoria)
        ServicioTuristico.objects.create(prestador=other_profile, nombre="Suite Presidencial", descripcion="Lujo total.", precio=500.00)

        self.client.credentials(**self._get_auth_header(self.prestador_token))
        response = self.client.get(self.servicios_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0) # No debería ver el servicio del otro prestador

    def test_prestador_can_create_servicio(self):
        """Un PRESTADOR puede crear un nuevo servicio."""
        data = {
            "nombre": "Habitación Sencilla",
            "descripcion": "Ideal para viajeros solos.",
            "precio": 100.00
        }
        self.client.credentials(**self._get_auth_header(self.prestador_token))
        response = self.client.post(self.servicios_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(ServicioTuristico.objects.filter(nombre="Habitación Sencilla").exists())
        # Verificar que se asoció al prestador correcto
        servicio = ServicioTuristico.objects.get(nombre="Habitación Sencilla")
        self.assertEqual(servicio.prestador, self.prestador_profile)

    def test_prestador_can_update_own_servicio(self):
        """Un PRESTADOR puede actualizar su propio servicio."""
        servicio = ServicioTuristico.objects.create(
            prestador=self.prestador_profile,
            nombre="Servicio a actualizar",
            descripcion="Descripción original.",
            precio=200.00
        )
        url = reverse('prestador-servicio-detail', kwargs={'pk': servicio.pk})
        data = {'precio': 250.00}
        self.client.credentials(**self._get_auth_header(self.prestador_token))
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        servicio.refresh_from_db()
        self.assertEqual(servicio.precio, 250.00)

    def test_prestador_can_delete_own_servicio(self):
        """Un PRESTADOR puede eliminar su propio servicio."""
        servicio = ServicioTuristico.objects.create(
            prestador=self.prestador_profile,
            nombre="Servicio a eliminar",
            descripcion="Descripción.",
            precio=100.00
        )
        url = reverse('prestador-servicio-detail', kwargs={'pk': servicio.pk})
        self.client.credentials(**self._get_auth_header(self.prestador_token))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ServicioTuristico.objects.filter(pk=servicio.pk).exists())

    def test_prestador_can_list_own_bookings(self):
        """Un PRESTADOR puede listar las reservas de sus servicios."""
        servicio = ServicioTuristico.objects.create(
            prestador=self.prestador_profile,
            nombre="Servicio con reserva",
            descripcion="Descripción.",
            precio=100.00
        )
        turista = CustomUser.objects.create_user('turista_test', 'turista@example.com', 'password123', role=CustomUser.Role.TURISTA)
        Booking.objects.create(
            servicio=servicio,
            cliente=turista,
            fecha_reserva=datetime.now(),
            valor_total=100.00
        )
        self.client.credentials(**self._get_auth_header(self.prestador_token))
        response = self.client.get(self.bookings_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['servicio'], servicio.pk)

    def test_prestador_can_create_factura_for_booking(self):
        """Un PRESTADOR puede crear una factura para una reserva."""
        servicio = ServicioTuristico.objects.create(
            prestador=self.prestador_profile,
            nombre="Servicio para facturar",
            descripcion="Descripción.",
            precio=300.00
        )
        turista = CustomUser.objects.create_user('turista_factura', 'turista_factura@example.com', 'password123', role=CustomUser.Role.TURISTA)
        booking = Booking.objects.create(
            servicio=servicio,
            cliente=turista,
            fecha_reserva=datetime.now(),
            valor_total=300.00
        )
        data = {
            "booking": booking.pk,
            "monto": 300.00,
            "metodo_pago": "TARJETA"
        }
        self.client.credentials(**self._get_auth_header(self.prestador_token))
        response = self.client.post(self.facturas_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Factura.objects.filter(booking=booking).exists())