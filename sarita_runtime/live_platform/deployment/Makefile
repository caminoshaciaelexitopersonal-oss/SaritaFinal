.PHONY: up down status ps logs

up:
	docker-compose -f sarita_runtime/live_platform/kafka_cluster/docker-compose.yml up -d
	docker-compose -f sarita_runtime/live_platform/observability/docker-compose.yml up -d

down:
	docker-compose -f sarita_runtime/live_platform/kafka_cluster/docker-compose.yml down
	docker-compose -f sarita_runtime/live_platform/observability/docker-compose.yml down

status:
	docker-compose -f sarita_runtime/live_platform/kafka_cluster/docker-compose.yml ps
	docker-compose -f sarita_runtime/live_platform/observability/docker-compose.yml ps

logs:
	docker-compose -f sarita_runtime/live_platform/kafka_cluster/docker-compose.yml logs -f
