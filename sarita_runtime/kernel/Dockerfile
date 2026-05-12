FROM python:3.11-slim
WORKDIR /app
COPY sarita_runtime/kernel/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONPATH=/app
CMD ["python", "sarita_runtime/kernel/runtime_supervisor.py"]
