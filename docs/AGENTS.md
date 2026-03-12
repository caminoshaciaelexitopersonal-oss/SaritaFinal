# Sarita - Instrucciones para Agentes (IA)

## Arquitectura de Frontend: Duplicación Estratégica
Debido a requerimientos específicos de despliegue y visibilidad para el embudo de marketing conversacional (Fase 6), se ha creado un proyecto de frontend separado en `web-ventas-frontend`.

### Directrices Importantes:
1. **No considerar como bug:** La duplicación de contextos (`AuthContext`, `EntityContext`) y hooks entre `interfaz` y `web-ventas-frontend` es intencional por ahora para asegurar independencia operativa del embudo de ventas.
2. **Mantenimiento:** Al realizar cambios en la lógica de autenticación o resolución de entidades en `interfaz`, **deben replicarse** en `web-ventas-frontend` hasta que se implemente una librería de componentes/hooks compartida.
3. **Perspectiva de Triple Vía:**
   - `interfaz`: Dashboard operativo para Vía 1 (Gobierno) y Vía 2 (Empresarios).
   - `web-ventas-frontend`: Interfaz conversacional SADI para adquisición de nuevos usuarios (Prospectos).
   - `interfaz/src/app/descubre`: Interfaz pública para Vía 3 (Turistas).

## Convención de Eventos
Todos los eventos del `EventBus` deben seguir la convención **UPPER_SNAKE_CASE** en inglés.
- Correcto: `SALE_CREATED`, `PAYROLL_LIQUIDATED_V2`.
- Incorrecto: `VentaCreada`, `nomina_liquidada`.

## Integridad Contable (LedgerEngine)
El sistema utiliza hashing encadenado (SHA-256). Cualquier modificación directa a las tablas de `JournalEntry` o `LedgerEntry` romperá la cadena. Usar siempre `LedgerEngine.post_event` o servicios de reversión.
