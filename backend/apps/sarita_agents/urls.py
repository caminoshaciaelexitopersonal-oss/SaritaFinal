# backend/apps/sarita_agents/urls.py
from django.urls import path
from backend. import views

urlpatterns = [
    path('directive/', views.DirectiveView.as_view(), name='sarita_directive'),
    path('missions/<uuid:id>/', views.MissionStatusView.as_view(), name='sarita_mission_status'),
]
