from django.urls import path
from backend.views import TextGenerationView, ChatCompletionView

urlpatterns = [
    path('text', TextGenerationView.as_view(), name='ai_text_generation'),
    path('chat/', ChatCompletionView.as_view(), name='ai_chat_completion'),
]
