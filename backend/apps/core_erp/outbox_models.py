from django.db import models
import uuid

class OutboxEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_type = models.CharField(max_length=100, db_index=True)
    domain = models.CharField(max_length=100, db_index=True)
    aggregate_root = models.CharField(max_length=100)
    payload = models.JSONField()
    version = models.IntegerField(default=1)
    status = models.CharField(max_length=20, default='PENDING') # PENDING, PROCESSED, ERROR
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        app_label = 'core_erp'


class EventAuditLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_type = models.CharField(max_length=100, db_index=True)
    correlation_id = models.CharField(max_length=100, db_index=True, null=True, blank=True)
    tenant_id = models.CharField(max_length=100, db_index=True, null=True, blank=True)
    payload = models.JSONField()
    status = models.CharField(max_length=20, default='EMITTED') # EMITTED, PROCESSED, PARTIAL_FAILURE, QUEUED_COMPLETED
    severity = models.CharField(max_length=20, default='info') # info, warning, critical, fatal
    error_details = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'core_erp'
        ordering = ['-timestamp']
