from django.db import models

class DocumentoOperativo(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        app_label = 'admin_operativa'
