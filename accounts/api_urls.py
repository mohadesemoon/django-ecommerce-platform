from django.urls import path
from .api_view import RegisterAPIView

app_name = 'accounts_api'

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
]