from django.urls import path
from . import views
urlpatterns = [
    path('', views.supervisor_dashboard, name= 'dashboard'),
    path('manage_application', views.labor_application_view, name='manage_application'),
    path('process_application/<int:id>', views.process_application_view, name='process_application'),
    path('reject_application/<int:id>', views.reject_application_view, name='reject_application'),
]
app_name = 'supervisor'