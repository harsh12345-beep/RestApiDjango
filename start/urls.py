from django.urls import path
from . import views

from .views import (
    Pract,
)
urlpatterns = [
    path('api',Pract.as_view() ),
]
