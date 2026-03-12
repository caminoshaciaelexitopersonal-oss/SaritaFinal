# Diagrama de Red y Segmentación - Sistema SARITA

## 1. Estructura de la VPC
Se implementa una **VPC (Virtual Private Cloud)** dedicada con un rango de red CIDR `10.0.0.0/16`.

```mermaid
graph TD
    subgraph VPC_SARITA [VPC: 10.0.0.0/16]
        subgraph Subred_Publica [Subred Pública - 10.0.1.0/24]
            IGW[Internet Gateway]
            ALB[Application Load Balancer]
            NAT[NAT Gateway]
        end

        subgraph Subred_Privada_App [Subred Privada App - 10.0.2.0/24]
            EKS_Nodes[Nodos Kubernetes - EKS]
            WPA[Web Presentation - Frontend]
            PCA[Core Processing - Microservicios]
        end

        subgraph Subred_Aislada_DB [Subred Aislada Datos - 10.0.3.0/24]
            RDS[(Base de Datos RDS)]
            Redis[(Redis Cache)]
            VectorDB[(Vector Store)]
        end
    end

    %% Flujos de Red
    Usuario((Usuario)) --> CloudFront[AWS CloudFront]
    CloudFront --> ALB
    ALB --> EKS_Nodes
    EKS_Nodes --> RDS
    EKS_Nodes --> Redis
    EKS_Nodes --> VectorDB

    %% Salida a Internet
    EKS_Nodes --> NAT
    NAT --> IGW
```

## 2. Segmentación y Reglas de Acceso

### 2.1 Subred Pública
- **Contenido:** Application Load Balancer (ALB), NAT Gateways.
- **Acceso:** Recibe tráfico HTTPS (Puerto 443) desde internet.
- **Seguridad:** Protegido por AWS WAF.

### 2.2 Subred Privada (Aplicaciones)
- **Contenido:** Nodos de EKS donde corren MCP, PCA y WPA.
- **Acceso:** Solo permite tráfico desde el ALB en la subred pública.
- **Salida:** Acceso a internet controlado a través del NAT Gateway (para parches y APIs externas).

### 2.3 Subred Aislada (Datos)
- **Contenido:** Instancias de base de datos y cache.
- **Acceso:** **ESTRICTAMENTE LIMITADO** a las IPs de la subred privada de aplicaciones. No tiene acceso a internet (sin ruta de salida).

## 3. Políticas de Red (Network Policies - K8s)
Dentro del clúster de Kubernetes, se aplican políticas para restringir el tráfico "East-West":
- **WPA (Frontend):** No puede hablar directamente con la Base de Datos. Debe pasar por el PCA (Backend).
- **PCA (Microservicios):** Puede hablar con la DB y otros microservicios autorizados.
- **MCP (Admin):** Acceso restringido a IPs administrativas/VPN.

## 4. Conectividad Externa (VPN/Direct Connect)
Para acceso administrativo y de mantenimiento, se utiliza un **AWS Client VPN** que conecta directamente a la subred privada de aplicaciones, evitando la exposición de puertos SSH o dashboards de administración a internet pública.
