from django.shortcuts import render, get_object_or_404, redirect
from .models import Labor, Application
from django.http import HttpResponse
def supervisor_dashboard(request):
    user = request.user
    try:
        user = get_object_or_404(Labor, user=user)
    except Labor.DoesNotExist:
        raise Http404("No Supervisor matches the given query.")

    return render(request, 'supervisor/dashboard.html', context={'user':user})

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
