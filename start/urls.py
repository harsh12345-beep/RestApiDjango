from django.urls import path
from . import views

from .views import (
    Pract,
)
urlpatterns = [
    path('/',Pract.as_view() ),
]
