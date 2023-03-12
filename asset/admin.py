from django.contrib import admin
from .models import Company, Employee, Device,DeviceLog
# Register your models here.
@admin.register(Company)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display =['name',]
@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display =['user', 'company']
@admin.register(Device)
class DeviceModelAdmin(admin.ModelAdmin):
    list_display =['name','serial_number','company','current_employee']

@admin.register(DeviceLog)
class DeviceLogModelAdmin(admin.ModelAdmin):
    list_display =['device','employee','checked_out','checked_in','condition']