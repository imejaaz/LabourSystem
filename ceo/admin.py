from django.contrib import admin
from .models import SalaryAdjustment, Salary, Project, Departments, Designations
from .forms import ProjectForm

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
    list_display = ('labor', 'month', 'days_worked', 'adjustment', 'status')
    list_filter = ('status', )
    search_fields = ('labor__name', 'month')
    list_per_page = 20



class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ('name', 'start_date', 'deadline', 'progress')
    search_fields = ('name',)
    filter_horizontal = ('members',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(SalaryAdjustment, SalaryAdjustmentAdmin)
admin.site.register(Salary, SalaryRecordAdmin)
admin.site.register(Departments)
admin.site.register(Designations)
