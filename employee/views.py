from datetime import datetime, time
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.urls import reverse

import time
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import *


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
        

        
        t1=datetime.strftime(intime , '%H:%M').time()  # type: ignore
        t2=datetime.strftime(outtime , '%H:%M').time() # type: ignore
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
   

#Drishti module intergated
def samp(request):
    return render(request, "samp.html")

def index(request):
    return render(request, "index.html")

def tables(request):
    # baseSalary = Salary.objects.only('base_salary')
    # houseRentAllowance = Salary.objects.only('house_rent_allowance')
    # conveyanceAllowance = Salary.objects.only('conveyance_allowance')
    # medicalAllowance = Salary.objects.only('medical_allowance')
    # specialAllowance = Salary.objects.only('special_allowance')
    # grossSalary = (baseSalary+houseRentAllowance+conveyanceAllowance+medicalAllowance+specialAllowance)
    # salary = Salary(
    #     gross_salary = grossSalary
    # )
    # salary.save(update_fields=['gross_salary'])
    # print(grossSalary)
    salary = Salary.objects.all()
    return render(request, "salary.html", {'salary': salary})

def createSalaryRecord(request):
    time.sleep(2)
    if request.method=="POST":
        salary = Salary()
        salary.month_year = request.POST["Date"]
        salary.base_salary = request.POST["BaseSalary"]
        # salary.house_rent_allowance = request.POST["HRA"]
        hra = (40/100) * float(request.POST["BaseSalary"])
        salary.house_rent_allowance = hra # type: ignore
        # salary.conveyance_allowance = request.POST["CA"]
        ca = 1600
        salary.conveyance_allowance = ca
        # salary.medical_allowance = request.POST["MA"]
        ma = 1250
        salary.medical_allowance = ma
        salary.special_allowance = request.POST["SA"]
        # salary.provided_fund = request.POST["PF"]
        pf = (12/100) * float(request.POST["BaseSalary"])
        salary.provided_fund = pf # type: ignore
        salary.health_insurance = request.POST["HealthInsurance"]
        # salary.professional_tax = request.POST["Tax"]
        tax = 200
        salary.professional_tax = tax
        salary.tds = request.POST["TDS"]
        salary.other_reductions = request.POST["Other"]
        gross_salary = float(request.POST["BaseSalary"]) + hra + ca + ma + float(request.POST["SA"])
        total_deductions = pf + float(request.POST["HealthInsurance"]) + tax + float(request.POST["TDS"]) + float(request.POST["Other"])
        salary.gross_salary = gross_salary
        salary.total_deductions = total_deductions
        salary.net_salary = gross_salary - total_deductions
        salary.save()
        return redirect('tables')
    else:
        return redirect('tables')

def updateSalary(request, pk):
    time.sleep(2)
    if request.method=="POST":
        salary = Salary.objects.get(id=pk)
        salary.base_salary = request.POST["BaseSalary1"]
        hra = (40/100) * float(request.POST["BaseSalary1"])
        salary.house_rent_allowance = hra # type: ignore
        # salary.house_rent_allowance = request.POST["HRA1"]
        salary.conveyance_allowance = request.POST["CA1"]
        salary.medical_allowance = request.POST["MA1"]
        salary.special_allowance = request.POST["SA1"]
        # salary.provided_fund = request.POST["PF1"]
        pf = (12/100) * float(request.POST["BaseSalary1"])
        salary.provided_fund = pf # type: ignore
        salary.health_insurance = request.POST["HealthInsurance1"]
        salary.professional_tax = request.POST["Tax1"]
        salary.tds = request.POST["TDS1"]
        salary.other_reductions = request.POST["Other1"]
        gross_salary = float(request.POST["BaseSalary1"]) + hra + float(request.POST["CA1"]) + float(request.POST["MA1"]) + float(request.POST["SA1"])
        total_deductions = pf + float(request.POST["HealthInsurance1"]) + float(request.POST["Tax1"]) + float(request.POST["TDS1"]) + float(request.POST["Other1"])
        salary.gross_salary = gross_salary
        salary.total_deductions = total_deductions
        salary.net_salary = gross_salary - total_deductions
        salary.save()
        return redirect('tables')

def viewUpdateData(request, pk):
    print('------>>>-----')
    getdata = Salary.objects.get(id=pk)
    data = []
    item = {
        'baseSalary1': getdata.base_salary,
        'hra1': getdata.house_rent_allowance,
        'ca1': getdata.conveyance_allowance,
        'ma1': getdata.medical_allowance,
        'sa1': getdata.special_allowance,
        'pf1': getdata.provided_fund,
        'healthInsurance1': getdata.health_insurance,
        'tax1': getdata.professional_tax,
        'tds1': getdata.tds,
        'other1': getdata.other_reductions,
        'date1': getdata.month_year

    }
    data.append(item)
    return JsonResponse({'data': data})

def mail(request, pk):
    if request.method == "POST":
        salary = Salary.objects.get(id=pk)
        html_content = render_to_string("copy.html", {'content': salary})
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            "Testing",#subject
            text_content,#content
            'prabhapamula12@gmail.com',#from_email
            ['2020.drishti.samvedi@ves.ac.in']#to email
        )
        email.attach_alternative(html_content,"text/html")
        email.send()
        print('email sent')
        return redirect('tables')
    
    # return render(request, 'mailslip.html')

def format(request):
    return render(request, 'copy.html')