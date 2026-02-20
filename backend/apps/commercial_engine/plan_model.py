import uuid
from django.db import models

class SaaSPlan(models.Model):
    """
    Modelo único de Plan para el ecosistema SaaS.
    """
    class Frecuencia(models.TextChoices):
        MENSUAL = 'MENSUAL', 'Mensual'
        ANUAL = 'ANUAL', 'Anual'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    monthly_price = models.DecimalField(max_digits=12, decimal_places=2)
    yearly_price = models.DecimalField(max_digits=12, decimal_places=2)

    # Límites
    user_limit = models.IntegerField(default=1)
    storage_limit_gb = models.IntegerField(default=5)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        verbose_name = "Plan SaaS"
        verbose_name_plural = "Planes SaaS"
