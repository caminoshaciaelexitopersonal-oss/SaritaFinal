# Diagrama de Alto Nivel - Sistema SARITA

Este diagrama representa la interacción entre las 6 capas fundamentales de la arquitectura.

```mermaid
graph TD
    subgraph Capa_1_Presentacion [Capa 1: Presentación]
        UI[Web/Mobile Interface]
        API_Ext[APIs Externas / SDKs]
    end

    subgraph Capa_2_Orquestacion [Capa 2: Orquestación]
        GW[API Gateway / Agent Gateway]
        Rules[Motor de Reglas & Gobernanza]
    end

    subgraph Capa_3_Servicios_Dominio [Capa 3: Servicios de Dominio]
        ERP[Módulos ERP: Contabilidad, Nómina]
        Vert[Verticales: Hoteles, Transporte, Agencias]
    end

    subgraph Capa_4_Inteligencia_Artificial [Capa 4: Capa de IA - SADI]
        Agents[Agentes Especializados]
        Reasoning[Motor de Razonamiento]
        Memory_AI[Motor de Memoria & Aprendizaje]
    end

    subgraph Capa_5_Persistencia [Capa 5: Persistencia]
        DB_SQL[(DB Transaccional - PostgreSQL)]
        DB_OLAP[(DB Analítica - ClickHouse)]
        DB_Vect[(DB Vectorial - Embeddings)]
        Logs[(Logs Inmutables - Auditoría)]
    end

    subgraph Capa_6_Infraestructura [Capa 6: Infraestructura]
        K8s[Kubernetes Cluster]
        Docker[Contenedores Docker]
        LB[Balanceadores de Carga]
    end

    %% Relaciones
    UI --> GW
    API_Ext --> GW
    GW --> Rules
    Rules --> ERP
    Rules --> Vert
    ERP <--> Agents
    Vert <--> Agents
    Agents --> Reasoning
    Reasoning --> Memory_AI

    ERP --> DB_SQL
    Vert --> DB_SQL
    Agents --> DB_Vect
    Rules --> Logs

    Capa_5_Persistencia --- Capa_6_Infraestructura
```

## Descripción del Flujo
1. **Entrada:** El usuario o sistema externo interactúa a través de la **Capa 1**.
2. **Control:** La **Capa 2** recibe la solicitud, valida la autoridad del solicitante a través del Motor de Reglas y la redirige al servicio correspondiente.
3. **Ejecución:** La **Capa 3** procesa la lógica de negocio, interactuando con la **Capa 4** (Agentes AI) si se requiere automatización o razonamiento avanzado.
4. **Persistencia:** Todos los resultados se almacenan en la **Capa 5**, asegurando que cada acción deje un rastro inmutable en los logs de auditoría.
5. **Soporte:** Todo el sistema corre sobre la **Capa 6**, que garantiza alta disponibilidad y escalabilidad.
