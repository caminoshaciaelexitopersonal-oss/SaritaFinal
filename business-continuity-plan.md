# Plan de Continuidad del Negocio y Chaos Engineering SARITA v1.0

## 1. Escenarios de Continuidad Crítica
| Escenario | Estrategia de Mitigación | Objetivo (RTO) |
| :--- | :--- | :--- |
| **Fallo de Región Cloud** | Conmutación automática a región secundaria (Passive Hot-Standby). | < 15 min |
| **Ataque DDoS Masivo** | Escalado elástico infinito y filtrado en el borde (Cloudflare). | < 5 min |
| **Corrupción de DB** | Recuperación Point-in-Time mediante logs transaccionales (WAL). | < 1 hora |

## 2. Programa de Chaos Engineering
Para asegurar la resiliencia sistémica, SARITA realiza experimentos controlados de fallo en su entorno de Pre-Producción.

*   **Experimento A (Kill-Worker)**: Eliminación aleatoria de nodos de procesamiento durante picos de carga.
*   **Experimento B (Latency-Injection)**: Inyección de retardo en la comunicación con bases de datos para probar timeouts y circuit breakers.
*   **Experimento C (Security-Stress)**: Simulación de acceso concurrente masivo con credenciales inválidas para validar el Rate Limiting.

---
**El sistema está diseñado para fallar con elegancia y recuperarse con velocidad.**
*Jules, Lead AI & Software Architect.*
