from django.shortcuts import render, get_object_or_404, redirect
from recruitment.models import Applicant
from labor.models import Labor
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import get_user_model
User = get_user_model()
from ceo.utility import register_labor
from supervisor.models import Application, ReviewerComment


def ceo_dashboard_view(request):
    user = request.user
    try:
        obj = get_object_or_404(Labor, user=user)
    except Labor.DoesNotExist:
        raise Http404("No CEO matches the given query.")

    applicants = Applicant.objects.all()
    labors = Labor.objects.all()
    regi_user = User.objects.all()
    applications = Application.objects.filter(status='under_review')
    context = {
        'use' : request.user,
        'applicants': applicants,
        'labors': labors,
        'users' : regi_user,
        'applications' : applications
    }

    return render(request, 'ceo/dashboard.html',context)

def applicants_view(request):
    applicants = Applicant.objects.all()
    return render(request, 'ceo/applicants.html', context={'applicants':applicants})

def applicant_record(request, id):

    if request.method == 'POST':
        salary = request.POST.get('salary')
        post = request.POST.get('post')
        applicant = get_object_or_404(Applicant, id=id)

        labor = register_labor(applicant, salary, post)
        if labor:
            applicant.delete()
            messages.success(request, 'Labor registered successfully')
        else:
            messages.error(request, 'Failed to register labor')
        return redirect('ceo:applicants')

    applicant = get_object_or_404(Applicant, id=id)
    return render(request, 'ceo/applicant_profile.html', context={'applicant':applicant})

def labor_applications_view(request):
    applications = Application.objects.filter(status='under_review')
    return render(request, 'ceo/applications_view.html', context={'applications':applications})
def open_application(request, id):
    application = Application.objects.get(id=id)
    if request.method == 'POST':
        decision = request.POST.get('decision')
        review = request.POST.get('review')
        comment = ReviewerComment.objects.create(
            application=application,
            comment=review
        )
        application.status = decision
        application.save()
        return redirect('ceo:labor_application')

    return render(request, 'ceo/open_application.html', context={'application':application})
