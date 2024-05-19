from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.Applicant_Dashboard_view, name='dashboard'),
    path('apply/', views.applicant_form_view, name='apply'),
]
app_name = 'recruitment'
