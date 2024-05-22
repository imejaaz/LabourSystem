from django.contrib import admin
from .models import SalaryAdjustment, SalaryRecord

class SalaryAdjustmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'percentage', 'date', 'reason', 'type', 'added_by', 'get_labor_name')
    list_filter = ('type', 'date')
    search_fields = ('reason',)
    date_hierarchy = 'date'
    list_per_page = 20

    def get_labor_name(self, obj):
        return obj.labor.name if obj.labor else None

    get_labor_name.short_description = 'Labor'
class SalaryRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'labor', 'amount', 'start_date', 'end_date', 'month', 'days_worked', 'extra_hours', 'adjustment', 'status')
    list_filter = ('status', 'start_date', 'end_date')
    search_fields = ('labor__name', 'month')
    date_hierarchy = 'start_date'
    list_per_page = 20

admin.site.register(SalaryAdjustment, SalaryAdjustmentAdmin)
admin.site.register(SalaryRecord, SalaryRecordAdmin)
