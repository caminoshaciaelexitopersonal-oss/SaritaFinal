import uuid

class TraceContext:
    @staticmethod
    def generate_context(tenant_id):
        return {
            "trace_id": str(uuid.uuid4()),
            "correlation_id": str(uuid.uuid4()),
            "tenant_id": tenant_id,
            "span_id": str(uuid.uuid4())
        }

    @staticmethod
    def propagate(header):
        # Extract and return existing trace from header
        return {
            "trace_id": header.get("trace_id"),
            "correlation_id": header.get("correlation_id"),
            "tenant_id": header.get("tenant_id"),
            "span_id": str(uuid.uuid4()) # New span
        }

if __name__ == "__main__":
    ctx = TraceContext.generate_context("tenant-abc")
    print(f"New context: {ctx}")
    new_span = TraceContext.propagate(ctx)
    print(f"Propagated: {new_span}")
