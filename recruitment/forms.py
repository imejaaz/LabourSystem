from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['user', 'first_name', 'last_name', 'cnic', 'dob', 'phone', 'gender', 'address', 'skill', 'work_experience']
