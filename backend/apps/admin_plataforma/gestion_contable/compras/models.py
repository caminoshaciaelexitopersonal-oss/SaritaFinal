from django.db import models
from apps.admin_plataforma.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

class Proveedor(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='admin_proveedores')
    nombre = models.CharField(max_length=200)
    nit = models.CharField(max_length=20, blank=True)

    class Meta:
        app_label = 'admin_compras'

class FacturaCompra(models.Model):
    perfil = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='admin_facturas_compra')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='admin_facturas')
    numero = models.CharField(max_length=50)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        app_label = 'admin_compras'
