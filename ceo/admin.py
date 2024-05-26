from django.contrib import admin
from .models import SalaryAdjustment, SalaryRecord, Project

class SalaryAdjustmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'percentage', 'date', 'reason', 'type', 'added_by')
    list_filter = ('type', 'date')
    search_fields = ('reason',)
    date_hierarchy = 'date'
    list_per_page = 20

    # def get_labor_name(self, obj):
    #     return obj.labor.name if obj.labor else None
    # get_labor_name.short_description = 'Labor'
class SalaryRecordAdmin(admin.ModelAdmin):
    list_display = ('labor', 'amount', 'month', 'days_worked', 'extra_hours', 'adjustment', 'status')
    list_filter = ('status', )
    search_fields = ('labor__name', 'month')
    list_per_page = 20



class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'progress_report')
    search_fields = ('name',)
    filter_horizontal = ('members',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(SalaryAdjustment, SalaryAdjustmentAdmin)
admin.site.register(SalaryRecord, SalaryRecordAdmin)
