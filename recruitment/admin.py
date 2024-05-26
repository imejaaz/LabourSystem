from django.contrib import admin
from .models import Applicant, InterViewResults

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'application_id', 'cnic', 'phone',)
    search_fields = ('first_name', 'application_id', 'cnic', 'phone')
    list_filter = ('gender',)

@admin.register(InterViewResults)
class InterviewResultAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'score', 'is_selected')
    search_fields = ('applicant','score')
    list_filter = ('is_selected', 'score',)
