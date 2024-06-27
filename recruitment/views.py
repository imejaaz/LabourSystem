from django.shortcuts import render, redirect
from .forms import ApplicantForm
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ApplicantForm


def applicant_form_view(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['user'] = request.user
        print("data coming from form: ", data)
        form = ApplicantForm(data)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Application has been submitted!')
                return redirect('recruitment:dashboard')
            except Exception as e:
                messages.error(request, getattr(e, 'message', str(e)))
                return redirect('recruitment:apply')
        else:
            print("Form errors: ", form.errors)
            messages.error(request, 'There was an error with your form. ', form.errors)

    return render(request, 'recruitment/application_form.html', {'form': ApplicantForm()})


@login_required(login_url='login')
def Applicant_Dashboard_view(request):

        user = request.user
        application = False
        if Applicant.objects.filter(user=user).exists():
            application = True

        return render(request, 'recruitment/dashboard.html', {'application': application})