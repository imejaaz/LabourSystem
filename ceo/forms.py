from django import forms
from .models import Project, Labor

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supervisor'].queryset = Labor.objects.filter(post='supervisor')
        self.fields['members'].queryset = Labor.objects.filter(post='labor')
