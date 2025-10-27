# backend/apps/contabilidad/views_reports.py
from rest_framework.views import APIView; from rest_framework.response import Response; from . import services_reports
class ReportBaseView(APIView):
    def get(self, request):
        perfil = request.user.perfil_prestador
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        # Lógica simplificada
        if 'libro-diario' in request.path: data = services_reports.get_libro_diario(perfil, start_date, end_date)
        # ... más lógica para otros informes ...
        return Response([]) # Placeholder
