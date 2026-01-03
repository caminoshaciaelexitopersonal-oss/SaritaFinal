# backend/apps/prestadores/mi_negocio/gestion_comercial/signals.py
from django.dispatch import Signal

# Señal emitida cuando una factura comercial se confirma y está lista para
# pasar al siguiente módulo en el pipeline de facturación.
factura_comercial_confirmada = Signal()
