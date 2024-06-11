from django.urls import path
from . import views
urlpatterns = [
    path('', views.ceo_dashboard_view, name= 'dashboard'),
    path('applicants/', views.applicants_view, name='applicants'),
    path('applicant_record/<int:id>', views.applicant_record, name='applicant_record'),
    path('labor_application/', views.labor_applications_view, name='labor_application'),
    path('open_application/<int:id>/', views.open_application, name='open_application'),
]+[
    path('calculate-salaries/', views.calculate_monthly_salaries, name='calculate-salaries'),
    path('salaries/', views.salaries_view, name='salaries'),
]

app_name = 'ceo'
