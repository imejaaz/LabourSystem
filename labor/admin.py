from django.contrib import admin
from .models import Labor, Attendance, HourlyAttendance

class LaborAdmin(admin.ModelAdmin):
    list_display = ('labor_id', 'first_name', 'last_name', 'post', 'basic_pay', 'date_of_hire')
    search_fields = ('labor_id', 'first_name', 'last_name', 'cnic', 'phone')
    list_filter = ('post', 'gender')
    ordering = ('first_name', 'last_name')
    readonly_fields = ('labor_id',)
    fieldsets = (
        (None, {
            'fields': ('user', 'labor_id', 'first_name', 'last_name', 'cnic', 'phone', 'gender', 'address', 'post', 'basic_pay', 'date_of_birth', )
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.labor_id:
            obj.labor_id = obj.generate_labor_id()
        super().save_model(request, obj, form, change)

admin.site.register(Labor, LaborAdmin)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('labor', 'date', 'check_in', 'check_out',  'status')
    list_filter = ('status', 'date')
    search_fields = ('labor__name', 'date')
    date_hierarchy = 'date'
    readonly_fields = ('check_in',)  # To make check_in field read-only in admin

@admin.register(HourlyAttendance)
class HourlyAttendanceAdmin(admin.ModelAdmin):
    list_display = ('attendance', 'check_in')
    search_fields = ('attendance__labor__name', 'attendance__date')
    date_hierarchy = 'attendance__date'
    readonly_fields = ('check_in',)