-- Movimientos Contables: Asientos (Traducción Directa de JournalEntry)
CREATE TABLE accounting.journal_entries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    period_id UUID NOT NULL, -- FK en 20_global
    created_by UUID NOT NULL, -- FK a users

    event_type TEXT NOT NULL, -- VENTA, PAGO, NOMINA
    financial_event_id TEXT, -- ID del documento fuente

    date DATE DEFAULT CURRENT_DATE,
    description TEXT,

    is_posted BOOLEAN DEFAULT false,
    posted_at TIMESTAMP,

    -- Inmutabilidad y Encadenamiento (Phase 3 Backend logic)
    system_hash VARCHAR(64),
    previous_hash VARCHAR(64),
    immutable_signature TEXT,

    created_at TIMESTAMP DEFAULT now()
);
