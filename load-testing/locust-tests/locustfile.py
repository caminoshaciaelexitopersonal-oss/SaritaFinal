from locust import HttpUser, task, between, SequentialTaskSet

class TouristBehavior(SequentialTaskSet):
    @task
    def explore_destinations(self):
        self.client.get("/api/v1/atractivos/")

    @task
    def search_providers(self):
        self.client.get("/api/v1/mi-negocio/prestadores/?search=hotel")

    @task
    def consult_services(self):
        # Simulamos consulta de un servicio específico
        self.client.get("/api/v1/mi-negocio/productos-servicios/")

    @task
    def make_reservation(self):
        payload = {
            "service_id": "893699c3-982b-497d-944a-10f84428841a",
            "start_date": "2026-05-01",
            "end_date": "2026-05-02",
            "customer_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        }
        self.client.post("/api/v1/operativa/reservas/", json=payload)

class ProviderBehavior(SequentialTaskSet):
    @task
    def view_dashboard(self):
        self.client.get("/api/v1/mi-negocio/dashboard-resumen/")

    @task
    def consult_bookings(self):
        self.client.get("/api/v1/operativa/reservas/")

    @task
    def register_sale(self):
        # Simulación de uso de POS
        payload = {"items": [{"id": 1, "qty": 1}], "total": 50000}
        self.client.post("/api/v1/sales/orders/", json=payload)

class AdminBehavior(SequentialTaskSet):
    @task
    def view_control_tower(self):
        self.client.get("/api/v1/admin-control-tower/global/")

    @task
    def monitor_providers(self):
        self.client.get("/api/v1/mi-negocio/prestadores/")

    @task
    def view_risk_panel(self):
        self.client.get("/api/v1/admin-control-tower/risk/")

class SaritaUser(HttpUser):
    wait_time = between(1, 5)

    # Probabilidades de cada perfil de usuario
    tasks = {
        TouristBehavior: 70, # 70% Turistas
        ProviderBehavior: 25, # 25% Prestadores
        AdminBehavior: 5      # 5% Admins
    }
