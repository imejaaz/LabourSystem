from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['user', 'name', 'cnic', 'phone', 'gender', 'address', 'skill', 'work_experience']
