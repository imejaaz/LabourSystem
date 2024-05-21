from django.urls import path
from . import views
urlpatterns = [
    path('', views.ceo_dashboard_view, name= 'dashboard'),
]
