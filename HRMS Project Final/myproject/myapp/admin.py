from django.contrib import admin
from .models import Employee, EmployeeAttendance, EmployeeLeave

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ['username', 'email', 'role', 'is_staff']

# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUser)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'email', 'phone_no', 'joining_date']  
    
    search_fields = ['name', 'designation', 'email', 'phone_no']  

@admin.register(EmployeeAttendance)
class EmployeeAttendanceAdmin(admin.ModelAdmin):
    list_display = ['employee', 'date', 'check_in', 'check_out', 'manually_updated']
    search_fields = ['employee__name']
    list_filter = ['date', 'manually_updated']
    date_hierarchy = 'date'

@admin.register(EmployeeLeave)
class EmployeeLeaveAdmin(admin.ModelAdmin):
    list_display = ['employee', 'leave_type', 'duration','start_date', 'end_date']
    search_fields = ['employee__name','designation', 'leave_type']
    list_filter = ['leave_type']
    date_hierarchy = 'start_date'
