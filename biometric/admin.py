
from django.contrib import admin

from . import models
from . import forms

class NonAcademicStaffAdmin(admin.ModelAdmin):
    search_fields = ['staff_name', 'address', 'phone_no']
    list_filter = ['enrolment_date', 'staff_name']
    list_display = ['staff_id', 'staff_name', 'address', 'phone_no', 'enrolment_date']


class AdministratorAdmin(admin.ModelAdmin):
    form = forms.AdministratorForm
    search_fields = ['username']
    list_display = ['staff_id', 'username', 'password']


class AttendanceStationAdmin(admin.ModelAdmin):
    list_filter = ['num_hours', 'attendance_date_time', 'staff_id']
    list_display = ['staff_id', 'num_hours', 'attendance_date_time']


class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ['dept_name']
    list_filter = ['dept_name', 'staff_id']
    list_display = ['staff_id', 'dept_id', 'dept_name']

class DesignationAdmin(admin.ModelAdmin):
    search_fields = ['job_name']
    list_filter = ['job_name', 'dept_id', 'staff_id']
    list_display = ['staff_id', 'job_id', 'dept_id', 'job_name']


class FingerprintAdmin(admin.ModelAdmin):
    list_filter = ['x_cord', 'y_cord', 'angle']
    list_display = ['staff_id', 'x_cord', 'y_cord', 'angle', 'hash']

class ServerAdmin(admin.ModelAdmin):
    list_filter = ['report', 'staff_id']
    list_display = ['staff_id', 'report']

admin.site.register(models.NonAcademicStaff, NonAcademicStaffAdmin)
admin.site.register(models.Administrator, AdministratorAdmin)
admin.site.register(models.AttendanceStation, AttendanceStationAdmin)
admin.site.register(models.Department, DepartmentAdmin)
admin.site.register(models.Designation, DesignationAdmin)
admin.site.register(models.Fingerprint, FingerprintAdmin)
admin.site.register(models.Server, ServerAdmin)
