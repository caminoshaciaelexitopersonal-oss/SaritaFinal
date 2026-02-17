# Políticas IAM y Gestión de Secretos - Sistema SARITA

## 1. Modelo de Identidad IAM
Se sigue el principio de **Mínimo Privilegio**. Ningún componente tiene más permisos de los que necesita estrictamente para operar.

### 1.1 IRSA (IAM Roles for Service Accounts)
En lugar de dar permisos a los nodos físicos de Kubernetes, se asignan roles de AWS directamente a las `ServiceAccounts` de los Pods.
- **`Role-PCA-Backend`**: Permiso de lectura/escritura solo en su bucket de S3 específico y acceso a su base de datos en Secrets Manager.
- **`Role-SADI-Agents`**: Permiso para invocar servicios de Bedrock/OpenAI y acceso a la Vector DB.
- **`Role-Infrastructure`**: Permisos para gestionar el clúster (solo para el CI/CD).

## 2. Gestión de Secretos
**PROHIBIDO** guardar secretos en variables de entorno fijas o en código.

### 2.1 AWS Secrets Manager
Se utiliza para almacenar:
- Credenciales de base de datos.
- API Keys de servicios externos (OpenAI, Stripe).
- Certificados y llaves privadas.

### 2.2 Inyección de Secretos
Los secretos se inyectan en los contenedores mediante:
- **Secrets Store CSI Driver:** Monta los secretos como archivos en un volumen temporal (memory-backed).
- **External Secrets Operator:** Sincroniza los secretos de AWS con `Secrets` nativos de Kubernetes para configuraciones rápidas.

## 3. Rotación Automática
- Las credenciales de base de datos rotan cada 30 días de forma automática mediante una función Lambda integrada con Secrets Manager.
- El PCA está diseñado para reconectar y refrescar las credenciales sin necesidad de reinicio manual.

## 4. Auditoría de Accesos
- **AWS CloudTrail:** Registra todas las llamadas a la API de AWS (quién accedió a qué secreto y cuándo).
- **K8s Audit Logs:** Registra quién modificó configuraciones en el clúster.

## 5. Acceso Humano (IAM Users vs SSO)
- **Cero IAM Users:** No se crean usuarios permanentes con llaves de acceso estáticas.
- **AWS IAM Identity Center (SSO):** Acceso federado para desarrolladores y administradores basado en sus roles en el directorio corporativo.
- **MFA Mandatorio:** El segundo factor de autenticación es obligatorio para cualquier acceso administrativo.
