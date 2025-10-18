from django.db import models
from django.utils.translation import gettext_lazy as _
from api.models import PrestadorServicio

class CategoriaMenu(models.Model):
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='categorias_menu')
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría de Menú"
        verbose_name_plural = "Categorías de Menú"

class ProductoMenu(models.Model):
    categoria = models.ForeignKey(CategoriaMenu, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto del Menú"
        verbose_name_plural = "Productos del Menú"

class Mesa(models.Model):
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.CASCADE, related_name='mesas')
    numero_mesa = models.CharField(max_length=50)
    capacidad = models.PositiveIntegerField(default=4)

    class Estado(models.TextChoices):
        DISPONIBLE = 'DISPONIBLE', _('Disponible')
        OCUPADA = 'OCUPADA', _('Ocupada')
        RESERVADA = 'RESERVADA', _('Reservada')

    estado = models.CharField(max_length=50, choices=Estado.choices, default=Estado.DISPONIBLE)

    def __str__(self):
        return f"Mesa {self.numero_mesa}"

    class Meta:
        verbose_name = "Mesa"
        verbose_name_plural = "Mesas"

class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL, null=True, blank=True, related_name='pedidos')
    productos = models.ManyToManyField(ProductoMenu, through='ItemPedido')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Pedido {self.id} - Mesa {self.mesa.numero_mesa if self.mesa else 'N/A'}"

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(ProductoMenu, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"