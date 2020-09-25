from django.contrib import admin

# Register your models here.
from .models import Users, Attendance_log

admin.site.register(Users)

admin.site.register(Attendance_log)