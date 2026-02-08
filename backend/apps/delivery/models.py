import uuid
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class DeliveryCompany(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    company = models.OneToOneField('companies.Company', on_delete=models.CASCADE, related_name='delivery_profile')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Driver(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='driver_profile')
    delivery_company = models.ForeignKey(DeliveryCompany, on_delete=models.CASCADE, related_name='drivers')
    license_number = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.delivery_company.name}"

class Vehicle(models.Model):
    class VehicleType(models.TextChoices):
        MOTO = "MOTO", _("Motocicleta")
        MOTOCARRO = "MOTOCARRO", _("Motocarro")
        AUTO = "AUTO", _("Automóvil")
        VAN = "VAN", _("Camioneta / Van")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plate = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=20, choices=VehicleType.choices)
    delivery_company = models.ForeignKey(DeliveryCompany, on_delete=models.CASCADE, related_name='vehicles')
    current_driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name='current_vehicles')
    is_active = models.BooleanField(default=True)

    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.plate} ({self.vehicle_type})"

class DeliveryService(models.Model):
    class Status(models.TextChoices):
        REQUESTED = "REQUESTED", _("Solicitado")
        ASSIGNED = "ASSIGNED", _("Asignado")
        IN_PROGRESS = "IN_PROGRESS", _("En Curso")
        COMPLETED = "COMPLETED", _("Completado")
        CANCELLED = "CANCELLED", _("Cancelado")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tourist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='delivery_requests')

    # Desacoplamiento de dominio via UUID
    provider_id = models.UUIDField(null=True, blank=True, help_text="ID del ProviderProfile asociado")

    delivery_company = models.ForeignKey(DeliveryCompany, on_delete=models.SET_NULL, null=True, blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)

    origin_address = models.CharField(max_length=500)
    destination_address = models.CharField(max_length=500)

    estimated_price = models.DecimalField(max_digits=18, decimal_places=2)
    final_price = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True)

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.REQUESTED)

    wallet_transaction = models.UUIDField(null=True, blank=True, help_text="ID de la transacción en apps.wallet")
    governance_intention_id = models.CharField(max_length=255, null=True, blank=True)

    # Interoperabilidad (FASE 9)
    related_operational_order_id = models.UUIDField(null=True, blank=True, help_text="ID de la Reserva/Orden Operativa vinculada")

    # Feedback
    rating = models.PositiveIntegerField(null=True, blank=True)
    tourist_comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Delivery {self.id} - {self.status}"

class DeliveryEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service = models.ForeignKey(DeliveryService, on_delete=models.CASCADE, related_name='events')
    event_type = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
