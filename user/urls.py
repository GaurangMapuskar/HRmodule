from django.contrib import admin
from django.urls import path
from user import views
urlpatterns =[
  path("test",views.test,name='test'),
  path("<int:id>",views.base,name='base'),
  path("profile(user)<int:id>",views.profile,name='profile'),
  path("attendancetracker(user)<int:id>",views.attendancetracker,name='attendancetracker'),
  path("leaverequest<int:id>",views.leaverequest,name='leaverequest'),
  path("scheduleuser<int:id>",views.scheduleuser,name='scheduleuser'),
  path("project(user)<int:id>",views.project,name='project'),
  path("jobvacany<int:id>",views.jobvacany,name='jobvacany'),
  path("jobapplication<int:id>",views.jobapplication,name='jobapplication'),
  # path("profile(user)/<int:id>",views.profile,name='profile'),
  # path("profile(user)/<int:id>",views.profile,name='profile'),
]