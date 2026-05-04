-- Núcleo Transaccional del ERP (Base de Operaciones)
CREATE TYPE core.operation_type AS ENUM ('venta', 'servicio', 'reserva', 'orden');
CREATE TYPE core.operation_status AS ENUM ('creada', 'confirmada', 'ejecutada', 'cancelada');

CREATE TABLE core.business_operations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    tipo_operacion core.operation_type NOT NULL,
    estado core.operation_status DEFAULT 'creada',

    cliente_id UUID NOT NULL, -- FK en 20_global
    provider_id UUID NOT NULL, -- FK en 20_global

    fecha_operacion TIMESTAMP DEFAULT now(),
    total_bruto DECIMAL(18,2) DEFAULT 0.00,
    total_impuestos DECIMAL(18,2) DEFAULT 0.00,
    total_neto DECIMAL(18,2) DEFAULT 0.00,

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
