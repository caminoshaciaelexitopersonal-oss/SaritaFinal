from django.db import models
import uuid

class AuditLog(models.Model):
    class Action(models.TextChoices):
        USER_LOGIN_SUCCESS = 'USER_LOGIN_SUCCESS', 'Inicio de sesión exitoso'
        USER_LOGIN_FAILED = 'USER_LOGIN_FAILED', 'Intento de inicio de sesión fallido'
        DOCUMENT_CREATED = 'DOCUMENT_CREATED', 'Creó concepto de documento'
        VERSION_UPLOADED = 'VERSION_UPLOADED', 'Subió nueva versión'
        VERSION_DOWNLOADED = 'VERSION_DOWNLOADED', 'Descargó versión'
        VERSION_DELETED = 'VERSION_DELETED', 'Eliminó versión'
        VERSION_VERIFIED = 'VERSION_VERIFIED', 'Verificó integridad de versión'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('api.CustomUser', on_delete=models.SET_NULL, null=True, blank=True)
    username = models.CharField(max_length=150)
    company = models.ForeignKey('companies.Company', on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=50, choices=Action.choices, db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    details = models.JSONField(default=dict)

    class Meta:
        verbose_name = "Audit Log Entry"
        verbose_name_plural = "Audit Log"
        ordering = ['-timestamp']

    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {self.username} -> {self.get_action_display()}"
