from django.db import models

class Restaurante(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        app_label = 'admin_operativa'

class Menu(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='admin_menus')
    nombre = models.CharField(max_length=100)

    class Meta:
        app_label = 'admin_operativa'

class CategoriaPlato(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        app_label = 'admin_operativa'

class Plato(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='admin_platos')
    categoria = models.ForeignKey(CategoriaPlato, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        app_label = 'admin_operativa'
