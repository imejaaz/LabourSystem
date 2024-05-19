from django.contrib import admin
from .models import Applicant, InterViewResults

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnic', 'phone', 'gender', 'address', 'skill', 'work_experience')
    search_fields = ('name', 'cnic', 'phone')
    list_filter = ('gender',)

@admin.register(InterViewResults)
class InterviewResultAdmin(admin.ModelAdmin):
    list_display = ('name', 'score', 'is_selected')
    search_fields = ('name','score')
    list_filter = ('is_selected', 'name', 'score',)
