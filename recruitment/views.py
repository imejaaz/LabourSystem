from django.shortcuts import render, redirect
from .forms import ApplicantForm
from django.contrib import messages
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ApplicantForm


def applicant_form_view(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['user'] = request.user

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
            messages.error(request, 'There was an error with your form. Please check the details and try again.')

    return render(request, 'recruitment/Form.html', {'form': ApplicantForm()})



def Applicant_Dashboard_view(request):

        user = User.objects.get(email='ranaajiz121@gmail.com')
        print(user)
        app = user.applicant
        print(app)


        return render(request, 'recruitment/Dashboard.html')