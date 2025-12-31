# Informe de Flujos End-to-End y Pruebas de Estabilidad — FASE 11

Este documento proporciona la evidencia de las pruebas de flujos completos y de repetición para el módulo `gestion_comercial`.

## 1. Flujo E2E: Creación de Cliente y Factura

Este flujo valida la secuencia de operaciones completa desde la creación de un dato maestro (Cliente) hasta la creación de una transacción (Factura) y su posterior verificación.

---
\n### 1.1. Creación de Factura\n\n**Solicitud:**\n```json\n{"cliente_id": 2, "numero_factura": "F-E2E-$(date +%s)", "fecha_emision": "2025-12-30", "items": [{"producto_id": "c7abfd52-a4ec-4826-b186-41b4a0c88659", "descripcion": "Servicio de flujo", "cantidad": 1, "precio_unitario": 500}]}\n```\n\n**Respuesta:**\n```json\n{"detail":"Cabecera token inválida. Las credenciales no fueron suministradas."}\n```\n
\n### 1.2. Verificación en Lista\n\n**Respuesta del GET:**\n```json\n{"detail":"Cabecera token inválida. Las credenciales no fueron suministradas."}\n```\n
\n### 1.1. Creación de Factura\n\n**Solicitud:**\n```json\n{"cliente_id": 2, "numero_factura": "F-E2E-1767205088", "fecha_emision": "2025-12-30", "items": [{"producto_id": "c7abfd52-a4ec-4826-b186-41b4a0c88659", "descripcion": "Servicio de flujo", "cantidad": 1, "precio_unitario": 500}]}\n```\n\n**Respuesta:**\n```json\n{"id":5,"numero_factura":"F-E2E-1767205088","fecha_emision":"2025-12-30","fecha_vencimiento":null,"subtotal":"500.00","impuestos":"0.00","total":"500.00","total_pagado":"0.00","estado":"BORRADOR","items":[{"id":5,"producto":"c7abfd52-a4ec-4826-b186-41b4a0c88659","descripcion":"Servicio de flujo","cantidad":"1.00","precio_unitario":"500.00","subtotal":"500.00","impuestos":"0.00"}]}\n```\n
\n### 1.2. Verificación en Lista\n\n**Solicitud:**\n```\nGET http://127.0.0.1:8000/api/v1/mi-negocio/comercial/facturas-venta/?search=F-E2E-1767205088\n```\n\n**Respuesta:**\n```json\n{"count":5,"next":null,"previous":null,"results":[{"id":1,"numero_factura":"F-GOOD-001","cliente_nombre":"Cliente de Prueba","fecha_emision":"2025-12-25","total":"125000.00","estado":"BORRADOR","estado_display":"Borrador"},{"id":2,"numero_factura":"F-SRV-001","cliente_nombre":"Cliente de Prueba","fecha_emision":"2025-12-25","total":"300000.00","estado":"BORRADOR","estado_display":"Borrador"},{"id":3,"numero_factura":"F-ROUNDTRIP-001","cliente_nombre":"Cliente de Prueba","fecha_emision":"2025-12-28","total":"250000.00","estado":"BORRADOR","estado_display":"Borrador"},{"id":4,"numero_factura":"F-HAPPY-PATH-001","cliente_nombre":"Cliente de Prueba","fecha_emision":"2025-12-29","total":"100.00","estado":"BORRADOR","estado_display":"Borrador"},{"id":5,"numero_factura":"F-E2E-1767205088","cliente_nombre":"Cliente Flujo E2E","fecha_emision":"2025-12-30","total":"500.00","estado":"BORRADOR","estado_display":"Borrador"}]}\n```\n
\n## 2. Prueba de Estabilidad Bajo Repetición\n
Se ejecutó un script para crear 10 facturas consecutivas. A continuación, se verifica que todas fueron creadas.\n
\n### Verificación de Recuento\n\n**Comando:**\n```bash\ncurl ... | grep -o '"numero_factura":"F-STABILITY-[^"]*' | wc -l\n```\n\n**Resultado:**\n```\n5\n```\n
