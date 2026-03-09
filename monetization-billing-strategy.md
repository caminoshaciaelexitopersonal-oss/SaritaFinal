# Estrategia de Monetización y Billing SARITA v1.0

## 1. Modelos de Ingresos (Monetización)
SARITA opera bajo un esquema híbrido que garantiza la sostenibilidad de la plataforma y el fomento del ecosistema regional.

*   **SaaS (Software as a Service)**: Suscripciones mensuales/anuales por el uso del ERP "Mi Negocio" (Tiers: Free, Pro, Enterprise).
*   **Transaction Fees**: Comisiones por pagos procesados vía Wallet o Pasarelas integradas.
*   **API Usage (Pay-as-you-go)**: Facturación por consumo excedente de recursos de IA y llamadas a APIs de alto volumen.
*   **Marketplace Commission**: Porcentaje sobre la venta de plugins y extensiones de terceros.

## 2. Sistema de Billing y Suscripciones (Fase 9)
Implementación nativa en el módulo `usage_billing` para el control automático de ingresos.

### 2.1 Niveles de Servicio (Planes)
| Plan | Cuota API (Mensual) | Funciones Incluidas |
| :--- | :--- | :--- |
| **Free** | 10,000 req | ERP Básico, Notificaciones limitadas. |
| **Pro** | 100,000 req | IA Avanzada, Gestión de Inventario, Webhooks. |
| **Enterprise** | Ilimitado | Soporte dedicado, Auditoría SHA-256, mTLS. |

## 3. Medición de Consumo (Usage Collector)
*   Recolección en tiempo real de métricas de uso de CPU, almacenamiento y peticiones de IA.
*   Generación de facturas automáticas al cierre del ciclo contable regional.

---
**Estrategia aprobada para el crecimiento financiero sostenible.**
*Jules, Lead AI & Business Architect.*
