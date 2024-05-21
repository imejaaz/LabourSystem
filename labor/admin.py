from django.contrib import admin
from .models import Labor

class LaborAdmin(admin.ModelAdmin):
    list_display = ('labor_id', 'first_name', 'last_name', 'post', 'basic_pay', 'date_of_hire')
    search_fields = ('labor_id', 'first_name', 'last_name', 'cnic', 'phone')
    list_filter = ('post', 'gender')
    ordering = ('first_name', 'last_name')
    readonly_fields = ('labor_id',)
    fieldsets = (
        (None, {
            'fields': ('user', 'labor_id', 'first_name', 'last_name', 'cnic', 'phone', 'gender', 'address', 'post', 'basic_pay', 'date_of_birth', 'date_of_hire')
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.labor_id:
            obj.labor_id = obj.generate_labor_id()
        super().save_model(request, obj, form, change)

admin.site.register(Labor, LaborAdmin)
