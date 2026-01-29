# main_config/views.py
from django.http import JsonResponse
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from api.permissions import IsSuperAdmin

def healthcheck(request):
    """
    A simple health check endpoint that returns a JSON response indicating the server is running.
    """
    return JsonResponse({"status": "ok"})
