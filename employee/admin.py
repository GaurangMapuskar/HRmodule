from django.contrib import admin
from employee.models import Employee
from employee.models import Jobposting
from employee.models import attendance
from employee.models import schedule
from employee.models import leave

# Register your models here.
admin.site.register(Employee)
admin.site.register(Jobposting)
admin.site.register(attendance)
admin.site.register(schedule)
admin.site.register(leave)