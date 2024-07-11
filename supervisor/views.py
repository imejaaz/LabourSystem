from django.shortcuts import render, get_object_or_404, redirect
from .models import Labor, Application
from django.http import HttpResponse
from datetime import datetime, date
from labor.models import Attendance, HourlyAttendance
from django.contrib import messages
from ceo.models import Project, Departments
def supervisor_dashboard(request):
    user = request.user
    try:
        supervisorObj = get_object_or_404(Labor, user=user, post="supervisor")
    except Labor.DoesNotExist:
        raise Http404("No Supervisor matches the given query.")
    
    department = supervisorObj.department
    projectsCount = Project.objects.filter(supervisor=supervisorObj).count() 
    projects = Project.objects.filter(supervisor=supervisorObj)
    membersCount = Labor.objects.filter(post='labor', department=department).count()
    membersList = Labor.objects.filter(post='labor', department=department)
    print("projects count: ", projectsCount)
    
    context = {
        "department": department,
        "projectsCount": projectsCount,
        "projects": projects,
        "membersCount": membersCount,
        "membersList": membersList,
        "supervisorObj": supervisorObj
    }
    

    return render(request, 'supervisor/dashboard.html', context)

def labor_application_view(request):
    applications = Application.objects.filter(status='submitted')
    return render(request, 'supervisor/labor_applications.html', context={'applications':applications})
def process_application_view(request, id):
    application = get_object_or_404(Application, id=id)
    application.status='under_review'
    application.save()
    return redirect('supervisor:manage_application')
def reject_application_view(request, id):
    application = get_object_or_404(Application, id=id)
    application.status='rejected'
    application.save()
    return redirect('supervisor:manage_application')

# attendance management by supervisor

def attendacne_view(request):
    today_rec = Attendance.objects.filter(date=date.today())
    return render(request, 'supervisor/attandance.html', context={'attendance_records': today_rec})

def edit_attandacne_view(request, id):
    attandance = Attendance.objects.get(id=id)
    if request.method == 'POST':
        extra_hours = request.POST.get('extra_hours')
        record, created = HourlyAttendance.objects.get_or_create(attendance=attandance)
        record.hours = extra_hours
        record.save()
        messages.success(request, 'Extra hours are added')
        return redirect('supervisor:attandance')
    return render(request,'supervisor/attandance_edit.html' ,context={'attandance':attandance})