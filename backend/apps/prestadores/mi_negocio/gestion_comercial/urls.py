from django.urls import path
from .views import PlaceholderView

urlpatterns = [
    path('', PlaceholderView.as_view(), name='placeholder'),
]
