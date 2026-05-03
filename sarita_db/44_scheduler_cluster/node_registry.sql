CREATE TABLE scheduler.cluster_nodes (
    node_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    node_name TEXT,
    last_heartbeat TIMESTAMP DEFAULT now(),
    is_active BOOLEAN DEFAULT true
);

CREATE OR REPLACE FUNCTION scheduler.fn_node_heartbeat(p_node_id UUID)
RETURNS VOID AS $$
BEGIN
    INSERT INTO scheduler.cluster_nodes (node_id, last_heartbeat)
    VALUES (p_node_id, now())
    ON CONFLICT (node_id) DO UPDATE SET last_heartbeat = now();
END;
$$ LANGUAGE plpgsql;
