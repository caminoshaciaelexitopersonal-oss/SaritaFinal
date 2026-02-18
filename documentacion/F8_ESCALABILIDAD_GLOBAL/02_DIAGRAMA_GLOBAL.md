# Diagrama Global de Infraestructura - Sistema SARITA

## 1. Topología Mundial

```mermaid
graph TB
    subgraph Internet_Global [Internet Global]
        User_EU[Usuario Europa]
        User_AM[Usuario América]
        User_AS[Usuario Asia]
    end

    subgraph Entry_Layer [Capa de Entrada Global]
        R53[Route 53 - Intelligent DNS]
        GA[AWS Global Accelerator]
        CF[CloudFront CDN]
    end

    subgraph Regiones_Activas [Regiones Activas]
        subgraph Region_US [Región: us-east-1]
            EKS_US[EKS Cluster US]
            RDS_US[(PostgreSQL US)]
            Vect_US[(Vector Store US)]
        end

        subgraph Region_EU [Región: eu-central-1]
            EKS_EU[EKS Cluster EU]
            RDS_EU[(PostgreSQL EU)]
            Vect_EU[(Vector Store EU)]
        end

        subgraph Region_AS [Región: ap-southeast-1]
            EKS_AS[EKS Cluster AS]
            RDS_AS[(PostgreSQL AS)]
            Vect_AS[(Vector Store AS)]
        end
    end

    %% Ruteo
    User_EU --> CF
    User_AM --> CF
    User_AS --> CF
    CF --> R53
    R53 --> GA

    GA -- Latencia Baja --> EKS_US
    GA -- Latencia Baja --> EKS_EU
    GA -- Latencia Baja --> EKS_AS

    %% Replicación
    RDS_US <--> |Replicación Asíncrona| RDS_EU
    RDS_EU <--> |Replicación Asíncrona| RDS_AS
    Vect_US -.-> |Sync Lotes| Vect_EU
    Vect_EU -.-> |Sync Lotes| Vect_AS
```

## 2. Flujo de Solicitud Internacional
1. El usuario accede a `app.sarita.com`.
2. **CloudFront** sirve los componentes de la UI (WPA) desde el punto de presencia más cercano.
3. **Route 53** resuelve la IP del **Global Accelerator** basándose en la latencia.
4. La solicitud viaja por la red privada de AWS hacia el microservicio correspondiente en la región óptima.
5. Si los datos requeridos no están en la región local, el microservicio realiza una consulta inter-regional protegida por mTLS.

## 3. Aislamiento y Resiliencia
- Cada región es **Self-Healing**. Un fallo en el clúster de US no afecta el funcionamiento de EU o AS.
- Los planos de control de Kubernetes son independientes por región para evitar fallos de orquestación en cascada.
