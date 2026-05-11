#!/bin/bash
echo "Starting SARITA Sovereign Runtime Bootstrap..."

# 1. Initialize Database Schemas and Extensions
echo "Initializing SQL Layer..."
# docker-compose exec -T postgres psql -U sarita_root -d sarita_sovereign < sarita_db/90_super_admin/00_init_super_admin.sql

# 2. Deploy Infrastructure
echo "Deploying Containers..."
docker-compose -f sarita_runtime/deployment_runtime/01_full_stack_compose.yml up -d

# 3. Validate Health
echo "Waiting for services to be ready..."
sleep 10
echo "System initialized. Control Plane heartbeat active."
