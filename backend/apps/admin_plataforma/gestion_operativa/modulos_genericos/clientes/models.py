from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    class Meta:
        app_label = 'admin_operativa'
