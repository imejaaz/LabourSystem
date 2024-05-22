from django.contrib import admin
from .models import Application, ApplicationDocument, ReviewerComment

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('labor', 'title', 'status', 'date_submitted')
    list_filter = ('status',)
    search_fields = ('labor__name', 'title', 'description')
    readonly_fields = ('date_submitted',)

@admin.register(ReviewerComment)
class ReviewerCommentAdmin(admin.ModelAdmin):
    list_display = ('application', 'date_added', 'comment')
    search_fields = ('application__title', 'application__labor__name', 'comment')
    date_hierarchy = 'date_added'

@admin.register(ApplicationDocument)
class ApplicationDocumentAdmin(admin.ModelAdmin):
    list_display = ('application', 'uploaded_at')
    search_fields = ('application__title', 'application__labor__name')
