-- Validación de balance cero en transacciones (Doble Entrada)
CREATE OR REPLACE FUNCTION ledger.fn_validate_transaction_balance()
RETURNS TRIGGER AS $$
DECLARE
    v_balance DECIMAL(18,2);
BEGIN
    SELECT SUM(debit - credit) INTO v_balance
    FROM ledger.ledger_entries
    WHERE transaction_id = NEW.transaction_id;

    IF v_balance != 0 THEN
        RAISE EXCEPTION 'Inconsistencia financiera: El balance de la transacción % no es cero (%)', NEW.transaction_id, v_balance;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
