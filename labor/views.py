from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404
from .models import Labor
from supervisor.models import Application, ApplicationDocument
def dashboard(request):
    user = request.user
    try:
        obj = get_object_or_404(Labor, user=user)
    except Labor.DoesNotExist:
        raise Http404("No Labor matches the given query.")
    return render(request, 'labor/dashboard.html',{'labor':obj})

def labor_application_view(request):
    if request.method == 'POST':
        user = request.user
        labor = get_object_or_404(Labor, user=user)
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        doc1 = request.FILES.get('doc_file1')
        doc2 = request.FILES.get('doc_file2')
        doc3 = request.FILES.get('doc_file3')
        app = Application.objects.create(labor = labor, title=title, description=desc)
        print(app)
        if doc1:
            ApplicationDocument.objects.create(application=app, document=doc1)
        if doc2:
            ApplicationDocument.objects.create(application=app, document=doc2)
        if doc3:
            ApplicationDocument.objects.create(application=app, document=doc3)
        return redirect('labor:application')
    user = request.user
    labor = get_object_or_404(Labor, user=user)
    application = labor.applications.all()

    return render(request, 'labor/application.html', context={'labor':labor, 'applications':application})
def application_detail_view(request, id):
    application = get_object_or_404(Application, id=id)
    user = request.user
    labor = get_object_or_404(Labor, user=user)
    return render(request, 'labor/application_report.html', context={'application':application, 'labor':labor})
def submit_application_view(request, id):
    application = get_object_or_404(Application, id=id)
    application.status = 'submitted'
    application.save()
    return redirect('labor:application')

def delete_application_view(request, id):
    application = get_object_or_404(Application, id=id)
    application.delete()
    return redirect('labor:application')

