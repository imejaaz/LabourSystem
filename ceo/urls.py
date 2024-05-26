from django.urls import path
from . import views
urlpatterns = [
    path('', views.ceo_dashboard_view, name= 'dashboard'),
    path('applicants/', views.applicants_view, name='applicants'),
    path('applicant_record/<int:id>', views.applicant_record, name='applicant_record'),
    # path('register_employee/>', views.register_employee, name='register_employee'),
]

app_name = 'ceo'