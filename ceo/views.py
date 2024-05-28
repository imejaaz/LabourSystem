from django.shortcuts import render, get_object_or_404, redirect
from recruitment.models import Applicant
from labor.models import Labor
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import get_user_model
User = get_user_model()
from ceo.utility import register_labor


def ceo_dashboard_view(request):
    applicants = Applicant.objects.all()
    labors = Labor.objects.all()
    regi_user = User.objects.all()

    context = {
        'applicants': applicants,
        'labors': labors,
        'users' : regi_user
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
