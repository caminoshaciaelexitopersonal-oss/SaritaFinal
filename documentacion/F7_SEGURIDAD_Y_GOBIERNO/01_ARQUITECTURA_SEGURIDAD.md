# Arquitectura de Seguridad en 6 Niveles - Sistema SARITA

## 1. Nivel 1: Seguridad de Identidad (IAM Avanzado)
El acceso al sistema se rige por el principio de **Zero Trust** y **Mínimo Privilegio**.

- **Multi-Factor Authentication (MFA):** Requerido para todos los roles administrativos y de provisión.
- **RBAC & ABAC:** Combinación de Control de Acceso basado en Roles y Atributos (e.g., hora, ubicación, nivel de riesgo del dispositivo).
- **Identidad de Servicio para Agentes:** Cada agente SADI posee una identidad digital única basada en certificados X.509, permitiendo la autenticación mutua (mTLS) en el PCA.
- **Separación de Funciones:** Las capacidades de "Aprobación" y "Ejecución" están estrictamente separadas en diferentes identidades de servicio.

## 2. Nivel 2: Seguridad de Red
Segmentación física y lógica para evitar movimientos laterales.

- **Micro-segmentación:** Network Policies en Kubernetes que restringen el tráfico entre Pods. Un microservicio solo puede hablar con los servicios declarados explícitamente.
- **Firewall por Microservicio:** Reglas de entrada/salida específicas para cada componente.
- **Inspección de Tráfico (DPI):** Monitoreo de anomalías en el tráfico interno para detectar exfiltración de datos.

## 3. Nivel 3: Seguridad de Datos
Blindaje de la información en todos sus estados.

- **Cifrado en Tránsito:** TLS 1.3 forzado para toda comunicación.
- **Cifrado en Reposo:** AES-256 para bases de datos y almacenamiento de objetos.
- **Tokenización:** Datos sensibles (e.g., tarjetas de crédito, IDs personales) se reemplazan por tokens fuera del dominio operativo.
- **Mascaramiento Dinámico:** Los datos sensibles se ocultan parcialmente en la UI basándose en el rol del usuario.
- **Clasificación de Datos:**
  - **Público:** Información general de turismo.
  - **Interno:** Reportes operativos.
  - **Confidencial:** Datos de perfil de usuario.
  - **Crítico:** Llaves criptográficas, transacciones financieras, registros de auditoría.

## 4. Nivel 4: Seguridad de Código (DevSecOps)
Protección desde la concepción del software.

- **SAST (Static Application Security Testing):** Análisis automático de vulnerabilidades en el código fuente.
- **DAST (Dynamic Application Security Testing):** Pruebas de penetración automatizadas en el entorno de Staging.
- **SCA (Software Composition Analysis):** Escaneo de dependencias y librerías para detectar vulnerabilidades conocidas (CVE).
- **Firmado de Artefactos:** Solo imágenes Docker firmadas por el CI/CD corporativo pueden ejecutarse en el clúster.

## 5. Nivel 5: Seguridad de Agentes AI
Control ético y técnico sobre la inteligencia artificial.

- **Explainability Log:** Cada decisión de agente debe incluir el "razonamiento" y las "fuentes" utilizadas.
- **Detección de Desviación:** Monitoreo de respuestas incoherentes o cambios abruptos de comportamiento (Drift detection).
- **Validación Cruzada:** El PCA requiere que al menos dos agentes de diferentes dominios validen acciones críticas.

## 6. Nivel 6: Seguridad Operativa
Resiliencia y respuesta ante incidentes.

- **WORM (Write Once, Read Many):** Los registros de auditoría se almacenan en sistemas que impiden su modificación o borrado.
- **Monitoreo 24/7:** Centro de Operaciones de Seguridad (SOC) simulado mediante alertas automatizadas en Grafana/CloudWatch.
- **Plan de Respuesta a Incidentes (IRP):** Protocolos predefinidos para contención de ataques o brechas de datos.
