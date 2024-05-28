from django.urls import path
from . import views
urlpatterns = [
    path('', views.supervisor_dashboard, name= 'dashboard'),
]
app_name = 'supervisor'