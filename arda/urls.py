from django.urls import path
from . import views

urlpatterns = [
    path('<language>', views.multimedia_recommendation, name="multimedia_recommendation"),
]
