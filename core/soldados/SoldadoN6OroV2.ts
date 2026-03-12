// core/soldados/SoldadoN6OroV2.ts

export interface ContextoEjecucion {
    user_id: string;
    tenant_id: string;
    correlation_id: string;
    idempotent_key: string;
    params: any;
}

export interface ResultadoOperacion {
    status: 'READY' | 'FAILED';
    entity_id?: string;
    audit_id?: string;
    event_emitted: boolean;
    error?: string;
}

export abstract class SoldadoN6OroV2 {
    // Propiedades obligatorias
    public abstract dominio: string;
    public abstract agregadoRaiz: string;
    public version: number = 1;
    public abstract permisosRequeridos: string[];

    public requiereIdempotencia: boolean = true;
    public requiereOutbox: boolean = true;
    public requiereAuditoria: boolean = true;
    public requiereMultiTenant: boolean = true;

    constructor(
        protected repo: any,
        protected permisos: any,
        protected idempotencia: any,
        protected outbox: any,
        protected auditoria: any,
        protected tenant: any,
        protected eventBus: any
    ) {
        this.validarInyeccion();
    }

    private validarInyeccion() {
        if (!this.repo || !this.permisos || !this.idempotencia || !this.outbox || !this.auditoria || !this.tenant || !this.eventBus) {
            throw new Error("Faltan dependencias obligatorias para el Soldado N6 Oro V2");
        }
    }

    /**
     * MÉTODO DE EJECUCIÓN PROTEGIDO
     */
    public async ejecutar(contexto: ContextoEjecucion): Promise<ResultadoOperacion> {
        console.log(`N6-ORO-V2: Ejecutando ${this.constructor.name} [${contexto.correlation_id}]`);

        try {
            // 1. Validaciones
            await this.validarTenant(contexto.tenant_id);
            await this.validarPermisos(contexto.user_id);

            // 2. Idempotencia
            if (this.requiereIdempotencia) {
                const prev = await this.idempotencia.verificar(contexto.idempotent_key, this.dominio);
                if (prev) return prev;
            }

            // 3. Transacción y Ejecución
            const resultado = await this.repo.transaction(async () => {
                // 4. Lógica de Dominio
                const entidad = await this.ejecutarDominio(contexto.params);

                // 5. Persistencia y Auditoría
                await this.repo.save(entidad);
                const audit = await this.auditoria.registrar(contexto, entidad);

                // 6. Outbox
                if (this.requiereOutbox) {
                    await this.outbox.insertar({
                        tipo: `${this.dominio.toUpperCase()}_ACTION`,
                        payload: entidad,
                        cid: contexto.correlation_id
                    });
                }

                return { entidad, audit_id: audit.id };
            });

            // 7. Marcar éxito idempotencia
            if (this.requiereIdempotencia) {
                await this.idempotencia.confirmar(contexto.idempotent_key, resultado);
            }

            return {
                status: 'READY',
                entity_id: resultado.entidad.id,
                audit_id: resultado.audit_id,
                event_emitted: this.requiereOutbox
            };

        } catch (error: any) {
            console.error(`N6-ORO-V2 ERROR: ${error.message}`);
            return { status: 'FAILED', error: error.message, event_emitted: false };
        }
    }

    protected abstract ejecutarDominio(params: any): Promise<any>;

    private async validarTenant(id: string) {
        if (this.requiereMultiTenant && !id) throw new Error("Violación Multi-tenant");
    }

    private async validarPermisos(user: string) {
        const has = await this.permisos.check(user, this.permisosRequeridos);
        if (!has) throw new Error("Permisos insuficientes");
    }
}
