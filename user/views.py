from django.shortcuts import render,redirect
from user.models import Employee
from django.contrib import messages
from user.models import attendance
from user.models import  schedule
from user.models import  Jobposting
from user.models import  leave

code = 100

# Create your views here.
def test(request):
   # emp = Employee.objects.get(EmpSSN=id)
    return render (request,'test.html')

def base(request,id):
    emp = Employee.objects.get(EmpSSN=id)
    return render (request,'base(user).html',{'emp':emp,'emp':emp})

def attendancetracker(request,id):
    emp = Employee.objects.get(EmpSSN=id)
    att = attendance.objects.filter(employee=id)
    return render (request,'attendancetracker(user).html',{'att':att,'emp':emp})

def scheduleuser(request,id):
    emp = Employee.objects.get(EmpSSN=id)
    sch = schedule.objects.filter(EmpSSN=id)
    return render (request,'schedule(user).html',{'sch':sch,'emp':emp})

def jobvacany(request,id):
    emp = Employee.objects.get(EmpSSN=id)
    job = Jobposting.objects.all()
    return render (request,'jobvacany.html',{'job':job,'emp':emp})

def profile(request,id):
    emp = Employee.objects.get(EmpSSN=id)
    profile = Employee.objects.get(EmpSSN=id)
    return render (request,'profile(user).html',{'profile':profile,'emp':emp})

def leaverequest(request,id):
    if request.method == "POST":
        if  id!=leave.EmpSSN:
            emp = Employee.objects.get(EmpSSN=id)
            sdate=request.POST.get("sdate")
            edate=request.POST.get("edate")
            leavetype=request.POST.get("leavetype")
            reason=request.POST.get("reason")
            EmpSSN = request.POST.get("EmpSSN")
            name = request.POST.get("Fname")

            leaverequest = leave(sdate=sdate,edate=edate,leavetype=leavetype,reason=reason,EmpSSN=EmpSSN,name=name)
            leaverequest.save()
            #return redirect ('leaverequest{{emp.EmpSSN}}')
            messages.success(request, 'Leave request has been sent.')
        else:
            messages.info(request, 'You already have pending leave request')
        return render (request,'leaverequest.html',{'emp':emp})
        

    emp = Employee.objects.get(EmpSSN=id)
    return render (request,'leaverequest.html',{'emp':emp})

def project(request,id):
    emp = Employee.objects.get(EmpSSN=id)
    sch = schedule.objects.filter(EmpSSN=id)
    return render (request, 'project(user).html',{'emp':emp,'sch':sch})

def jobapplication(request,id):
    #emp = Employee.objects.get(EmpSSN=id)
    job = Jobposting.objects.all()
    emp = Employee.objects.get(EmpSSN=id)
    return render (request, 'jobapplication.html',{'job':job,'emp':emp})


