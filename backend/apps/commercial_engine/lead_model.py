import uuid
from django.db import models

class SaaSLead(models.Model):
    class Status(models.TextChoices):
        NEW = 'NEW', 'Nuevo'
        QUALIFIED = 'QUALIFIED', 'Calificado'
        CONVERTED = 'CONVERTED', 'Convertido'
        REJECTED = 'REJECTED', 'Rechazado'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=255)
    contact_email = models.EmailField(unique=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    score = models.IntegerField(default=0)

    source = models.CharField(max_length=100, default='web')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Lead SaaS"
        verbose_name_plural = "Leads SaaS"
