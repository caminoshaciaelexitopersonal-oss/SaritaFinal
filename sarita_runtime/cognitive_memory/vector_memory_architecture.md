# ARQUITECTURA DE MEMORIA VECTORIAL
**Stack Sugerido:** Pinecone / Milvus / PGVector

## 1. TIPOS DE MEMORIA
- **Episodic Memory:** Registro de acciones pasadas de los agentes (almacenado como vectores de eventos).
- **Semantic Memory:** Conocimiento base del ecosistema (reglas, manuales, leyes).
- **Long-term Memory:** Resúmenes consolidados de la historia del tenant.

## 2. MEMORY LIFECYCLE
1. **Ingestion:** Los eventos relevantes se convierten en embeddings (ej. `text-embedding-3`).
2. **Indexing:** Almacenamiento en la Vector DB segmentado por `tenant_id`.
3. **Retrieval:** Búsqueda por similitud semántica durante el razonamiento del agente.
4. **Decay/Summarization:** Los recuerdos antiguos se resumen para ahorrar espacio y mantener la relevancia.
