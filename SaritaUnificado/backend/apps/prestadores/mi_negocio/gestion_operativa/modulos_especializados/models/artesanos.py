# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_especializados/models/artesanos.py
from django.db import models
from ...modulos_genericos.models.base import Perfil

class CategoriaProductoArtesanal(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class ProductoArtesanal(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='productos_artesanales')
    categoria = models.ForeignKey(CategoriaProductoArtesanal, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    foto = models.ImageField(upload_to='productos_artesanales/', blank=True, null=True)
    materiales = models.CharField(max_length=255, blank=True, help_text="Materiales principales (ej. 'Lana de oveja, tintes naturales')")
    tecnica = models.CharField(max_length=255, blank=True, help_text="Técnica de elaboración (ej. 'Tejido en telar vertical')")

    class Meta:
        verbose_name = "Producto Artesanal"
        verbose_name_plural = "Productos Artesanales"

    def __str__(self):
        return f"{self.nombre} - {self.perfil.nombre_comercial}"

class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente de Pago'),
        ('pagado', 'Pagado'),
        ('en_preparacion', 'En Preparación'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='pedidos')
    nombre_cliente = models.CharField(max_length=255)
    direccion_envio = models.TextField()
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Pedido #{self.id} para {self.nombre_cliente} - {self.get_estado_display()}"

    def calcular_total(self):
        total_calculado = sum(item.subtotal for item in self.detalles.all())
        self.total = total_calculado
        self.save()

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(ProductoArtesanal, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio al momento de la compra")
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)
        self.pedido.calcular_total()

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en Pedido #{self.pedido.id}"
