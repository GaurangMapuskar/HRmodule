from django.contrib import admin
from django.urls import path
from employee import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[
path("",views.base,name='base'),
path("addemployee",views.addemployee,name='addemployee'),
path("addattendance",views.addattendance,name='addattendance'),
path("interviewscheduler/<int:id>",views.interviewscheduler,name='interviewscheduler'),
path("interviewschedule",views.interviewschedule,name='interviewschedule'),
path("jobposting",views.jobposting,name='jobposting'),
path("employeeDB",views.employeeDB,name='employeeDB'),
path("attendancetracker",views.attendancetracker,name='attendancetracker'),
path("officeschedular",views.officeschedular,name='officeschedular'),
path("updateemployee<int:id>",views.updateemployee,name='updateemployee'),
path("updaterecord<int:id>",views.updaterecord,name='updaterecord'),
path("deleteemployee<int:id>",views.deleteemployee,name='deleteemployee'),
path("profile<int:id>",views.profile,name='profile'),
path("leaveapproval",views.leaveapproval,name='leaveapproval'),
path("leavedeny<int:id>",views.leavedeny,name='leavedeny'),
path("leaveapprove<int:id>",views.leaveapprove,name='leaveapprove'),

path("test",views.test,name='test')
]

if settings.DEBUG:
    urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 