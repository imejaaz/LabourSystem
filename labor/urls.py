from django.urls import path
from . import views

urlpatterns = ([
    path('', views.dashboard, name= 'dashboard'),
    path('application/', views.labor_application_view, name='application'),
    path('submit_application/<int:id>', views.submit_application_view, name='submit_application'),
    path('delete_application/<int:id>', views.delete_application_view, name='delete_application'),
    path('application_report/<int:id>', views.application_detail_view, name='application_report'),

]+[

    path('attendance/', views.attendance_view, name='attendance'),

])
app_name='labor'