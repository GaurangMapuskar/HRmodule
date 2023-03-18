from datetime import datetime, time
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.urls import reverse

from employee.models import Employee
from employee.models import attendance
from employee.models import Jobposting
from employee.models import schedule
from employee.models import leave

# Create your views here.
def base(request):
    return render (request,'base.html')

def leaveapproval(request):
    app = leave.objects.filter(approval="pending")
    return render (request,'leaveapproval.html',{'app':app})

def employeeDB(request):
    emp = Employee.objects.all()
    return render (request,'employeeDB.html',{'emp':emp})

def attendancetracker(request):
    att = attendance.objects.all()
    return render (request,'attendancetracker.html',{'att':att})
    
def officeschedular(request):

    if request.method =="POST":
        EmpSSN=request.POST.get('EmpSSN')
        deadlinedate=request.POST.get('deadlinedate')
        deadlinetime=request.POST.get('deadlinetime')
        task=request.POST.get('task')
        
        officeschedular = schedule(EmpSSN=EmpSSN,deadlinedate=deadlinedate,deadlinetime=deadlinetime,task=task)
        officeschedular.save()
        messages.success(request, 'Schedule has been set.')
    emp = Employee.objects.all()
    return render (request,'officeschedular.html',{'emp':emp})

def jobposting(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        time=request.POST.get('time')
        date=request.POST.get('date')
        comments=request.POST.get('comments')
        minqualification=request.POST.get('minqualification')
        vacany=request.POST.get('vacany')

        jobposting = Jobposting(name=name,email=email,contact=contact,time=time,date=date,comments=comments,minqualification=minqualification,vacany=vacany)
        jobposting.save()
        messages.success(request, 'Vacany has been posted.')


    return render (request,'jobposting.html')

def interviewscheduler(request,id):
    if request.method =="POST":
        time=request.POST.get('time')
        date=request.POST.get('date')
        
        schedule=Jobposting.objects.get(vacany=id)
        schedule.time=time
        schedule.date=date
        schedule.schedule=True
        schedule.save()
    messages.success(request, 'Interview has been schedule.')
    return render (request,'interviewscheduler.html')

def interviewschedule(request):
    vac=Jobposting.objects.all()
    return render (request,'interviewscheduler.html',{'vac':vac})

def test(request):
    return render (request,'test.html')

def updateemployee(request,id):
    #if request.method == "POST":
     
    update = Employee.objects.get(EmpSSN=id)
    return render (request,'updateemployee.html',{'update':update})

def addattendance(request):
    if request.method == "POST":
        employee=request.POST.get('employee')
        intime=request.POST.get('intime')
        outtime=request.POST.get('outtime')
        date=request.POST.get('date')
        

        
        t1=datetime.strptime(intime , '%H:%M').time()
        t2=datetime.strptime(outtime , '%H:%M').time()
        #time = attendance.objects.get()
        workinghours=t2.hour-t1.hour
        if(workinghours<7):
            messages.warning(request, 'Employee has not met daily working hours')
            remark="Half-Day"
        
        if(t1.hour>8):
            messages.warning(request, 'Late Mark')
            remark="Late"
        else:remark="Present"

        
        addattendance = attendance(employee=employee,intime=intime,outtime=outtime,date=date,remark=remark)
        addattendance.save()
        messages.success(request, 'Attendence has been added.')
    att = Employee.objects.all()

    return render (request,'addattendance.html',{'att':att})

def addemployee(request):
    if request.method == "POST":
        Fname=request.POST.get('Fname')
        Mname=request.POST.get('Mname')
        Lname=request.POST.get('Lname')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        address=request.POST.get('address')
        state=request.POST.get('state')
        city=request.POST.get('city')
        zip=request.POST.get('zip')
        Bankname=request.POST.get('Bankname')
        Bankbranch=request.POST.get('Bankbranch')
        IFSCCode=request.POST.get('IFSCCode')
        BankAC=request.POST.get('BankAC')
        EmpSSN=request.POST.get('EmpSSN')
        post=request.POST.get('post')
        #joining_date=request.POST.get('joining_date')
        branch=request.POST.get('branch')
        description=request.POST.get('description')
        EFname=request.POST.get('EFname')
        EMname=request.POST.get('EMname')
        ELname=request.POST.get('ELname')
        Eemail=request.POST.get('Eemail')
        Econtact=request.POST.get('Econtact')
        Eaddress=request.POST.get('Eaddress')
        aadhaar=request.POST.get('aadhar')
        religion=request.POST.get('religion')
        subcaste=request.POST.get('subcaste') 
        mothertounge=request.POST.get('mothertounge') 
        school=request.POST.get('school') 
        tenboard=request.POST.get('tenboard') 
        tenyear=request.POST.get('tenyear')
        tenpercentage=request.POST.get('tenpercentage')
        twelveboard=request.POST.get('twelveboard') 
        twelveyear=request.POST.get('twelveyear')
        twelvepercentage=request.POST.get('twelvepercentage') 
        degree=request.POST.get('degree') 
        year=request.POST.get('year')
        percentage=request.POST.get('percentage')
        face=request.POST.get('face')

        addemployee = Employee(Fname=Fname, Mname=Mname, Lname=Lname,email=email,contact=contact,address=address,state=state,city=city,zip=zip,Bankname=Bankname,Bankbranch=Bankbranch,IFSCCode=IFSCCode,BankAC=BankAC,EmpSSN=EmpSSN,post=post,branch=branch,description=description,EFname=EFname,EMname=EMname,ELname=ELname,Eemail=Eemail,Econtact=Econtact,Eaddress=Eaddress,
        aadhaar=aadhaar,religion=religion,subcaste=subcaste,mothertounge=mothertounge,school=school,tenboard=tenboard,tenyear=tenyear,
        tenpercentage=tenpercentage,twelveboard=twelveboard,twelveyear=twelveyear,twelvepercentage=twelvepercentage,degree=degree,year=year,percentage=percentage,face=face)
        addemployee.save()
        messages.success(request, 'Profile details updated.')
        return redirect ('addemployee')


    return render (request,'addemployee.html')

def updaterecord(request,id):
    if request.method == "POST":
        Fname=request.POST.get('Fname')
        Mname=request.POST.get('Mname')
        Lname=request.POST.get('Lname')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        address=request.POST.get('address')
        state=request.POST.get('state')
        city=request.POST.get('city')
        zip=request.POST.get('zip')
        Bankname=request.POST.get('Bankname')
        Bankbranch=request.POST.get('Bankbranch')
        IFSCCode=request.POST.get('IFSCCode')
        BankAC=request.POST.get('BankAC')
        EmpSSN=request.POST.get('EmpSSN')
        post=request.POST.get('post')
        #joining_date=request.POST.get('joining_date')
        branch=request.POST.get('branch')
        description=request.POST.get('description')
        EFname=request.POST.get('EFname')
        EMname=request.POST.get('EMname')
        ELname=request.POST.get('ELname')
        Eemail=request.POST.get('Eemail')
        Econtact=request.POST.get('Econtact')
        Eaddress=request.POST.get('Eaddress')
        aadhaar=request.POST.get('aadhar')
        religion=request.POST.get('religion')
        subcaste=request.POST.get('subcaste') 
        mothertounge=request.POST.get('mothertounge') 
        school=request.POST.get('school') 
        tenboard=request.POST.get('tenboard') 
        tenyear=request.POST.get('tenyear')
        tenpercentage=request.POST.get('tenpercentage')
        twelveboard=request.POST.get('twelveboard') 
        twelveyear=request.POST.get('twelveyear')
        twelvepercentage=request.POST.get('twelvepercentage') 
        degree=request.POST.get('degree') 
        year=request.POST.get('year')
        percentage=request.POST.get('percentage')
        

        update = Employee.objects.get(EmpSSN=id)
        update.Fname=Fname
        update.Mname=Mname
        update.Lname=Lname
        update.email=email
        update.contact=contact
        update.address=address
        update.state=state
        update.city=city
        update.zip=zip
        update.Bankname=Bankname
        update.Bankbranch=Bankbranch
        update.IFSCCode=IFSCCode
        update.BankAC=BankAC
        update.EmpSSN=EmpSSN
        update.post=post
        #joining_date=joining_date
        update.branch=branch
        update.description=description
        update.EFname=EFname
        update.EMname=EMname
        update.ELname=ELname
        update.Eemail=Eemail
        update.Econtact=Econtact
        update.Eaddress=Eaddress
        aadhaar=aadhaar
        religion=religion
        subcaste=subcaste
        mothertounge=mothertounge
        school=school
        tenboard=tenboard
        tenyear=tenyear
        tenpercentage=tenpercentage
        twelveboard=twelveboard
        twelveyear=twelveyear
        twelvepercentage=twelvepercentage
        degree=degree
        year=year
        percentage=percentage

        update.save()
    return redirect (reverse('employeeDB'))
        
def deleteemployee(request,id):
    delete = Employee.objects.get(EmpSSN=id)
    delete.delete()
    return redirect (reverse('employeeDB'))

def profile(request,id):
    profile = Employee.objects.get(EmpSSN=id)
    
    return render (request,'profile.html',{'profile':profile})

def leaveapprove(request,id):
   approval="yes"
   app=leave.objects.get(EmpSSN=id)
   app.approval=approval
   app.save()
   messages.success(request, 'Leave request was Approved.')
   return render (request,'leaveapproval.html')
   
def leavedeny(request,id):
    approval="no"
    app=leave.objects.get(EmpSSN=id)
    app.approval=approval
    app.save()
    messages.success(request, 'Leave request was denyed.')
    return render (request,'leaveapproval.html')
   