# backend/apps/inventario/services.py
from django.db import transaction
from .models import Producto, MovimientoInventario
from apps.compras.models import FacturaProveedor
from apps.comercial.models import FacturaVenta

@transaction.atomic
def registrar_entrada_inventario(factura: FacturaProveedor):
    """
    Crea movimientos de entrada para cada item de una factura de proveedor
    y actualiza el costo promedio ponderado del producto.
    """
    for item in factura.items.all():
        producto = item.producto

        # Crear el movimiento de inventario (Kardex)
        MovimientoInventario.objects.create(
            producto=producto,
            tipo='ENTRADA',
            fecha=factura.fecha_emision,
            cantidad=item.cantidad,
            costo_unitario=item.costo_unitario
        )

        # Actualizar stock y costo promedio ponderado
        nuevo_stock = producto.cantidad_en_stock + item.cantidad
        nuevo_costo_total = (producto.cantidad_en_stock * producto.costo_promedio_ponderado) + (item.cantidad * item.costo_unitario)

        producto.cantidad_en_stock = nuevo_stock
        if nuevo_stock > 0:
            producto.costo_promedio_ponderado = nuevo_costo_total / nuevo_stock

        producto.save()

@transaction.atomic
def registrar_salida_inventario(factura: FacturaVenta):
    """
    Crea movimientos de salida para cada item de una factura de venta
    y actualiza el stock.
    """
    for item in factura.items.all():
        producto = item.producto

        if item.cantidad > producto.cantidad_en_stock:
            raise ValueError(f"No hay stock suficiente para el producto '{producto.nombre}'.")

        # Crear el movimiento de salida al costo promedio actual
        MovimientoInventario.objects.create(
            producto=producto,
            tipo='SALIDA',
            fecha=factura.fecha_emision,
            cantidad=item.cantidad,
            costo_unitario=producto.costo_promedio_ponderado # Salida se registra al costo
        )

        # Actualizar stock
        producto.cantidad_en_stock -= item.cantidad
        producto.save()
