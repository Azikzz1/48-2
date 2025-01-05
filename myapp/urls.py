from django.urls import path
from .views import text_response, html_response

urlpatterns = [
    path('text/', text_response),
    path('html/', html_response),
]
