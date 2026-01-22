from django.urls import path
from .views import SadiCommandView

app_name = 'sadi_agent'

urlpatterns = [
    path('command/', SadiCommandView.as_view(), name='sadi_command'),
]
