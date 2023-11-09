import datetime
from functools import partial
from django.db import models

# Create your models here.
class Employee(models.Model):
    Fname=models.CharField(null=True,max_length=15)
    Mname=models.CharField(null=True,max_length=15) 
    Lname=models.CharField(null=True,max_length=15)
    email=models.EmailField(null=True, max_length=254)
    gender=models.CharField(null=True, max_length=50)
    contact=models.IntegerField(null=True)
    address=models.TextField(null=True)
    state=models.CharField(null=True,max_length=20)
    city=models.CharField(null=True,max_length=20)
    zip=models.IntegerField(null=True)
    Bankname=models.CharField(null=True,max_length=50)
    Bankbranch=models.CharField(null=True,max_length=5)
    BankAC=models.IntegerField(null=True)
    IFSCCode=models.CharField(null=True,max_length=20)
    EmpSSN=models.IntegerField(primary_key=True)
    post=models.CharField(null=True,max_length=50)
    branch=models.CharField(null=True,max_length=20)
    joining_date=models.DateField(null=True, auto_now=False, auto_now_add=False)
    description=models.CharField(null=True,max_length=20)
    EFname=models.CharField(null=True,max_length=15)
    EMname=models.CharField(null=True,max_length=15)
    ELname=models.CharField(null=True,max_length=15)
    Eemail=models.EmailField(null=True, max_length=254)
    Econtact=models.IntegerField(null=True)
    Eaddress=models.TextField(null=True,max_length=15)
    Egender=models.CharField(null=True, max_length=50)
    aadhaar=models.IntegerField(null=True)
    religion=models.CharField(null=True,max_length=50)
    subcaste=models.CharField(null=True, max_length=50)
    mothertounge=models.CharField(null=True, max_length=50)
    school=models.CharField(null=True, max_length=50)
    tenboard=models.CharField(null=True, max_length=50)
    tenyear=models.IntegerField(null=True)
    tenpercentage=models.DecimalField( null=True,max_digits=3, decimal_places=2)
    twelveboard=models.CharField(null=True, max_length=50)
    twelveyear=models.IntegerField(null=True)
    twelvepercentage=models.DecimalField(null=True, max_digits=3, decimal_places=2)
    degree=models.CharField(null=True, max_length=50)
    year=models.IntegerField(null=True)
    percentage=models.IntegerField(null=True)
    face=models.FileField(upload_to="face/",max_length=256,null=True)

class Jobposting(models.Model):
    name=models.CharField(null=True,max_length=50)
    email=models.EmailField(null=True,max_length=254)
    contact=models.IntegerField(null=True)
    comments=models.TextField(null=True)
    time=models.TimeField(auto_now_add=False, null=True)
    date=models.DateField(auto_now_add=False, null=True)
    minqualification=models.CharField(null=True,max_length=50)
    vacany=models.CharField(null=True,max_length=50)
    schedule=models.BooleanField(default=False)

class attendance(models.Model):
    #EmpSSN = models.ForeignKey("Employee", on_delete=models.CASCADE,default=Employee.objects.get_or_create(EmpSSN=100)[0])
    #fk = models.ForeignKey('Employee',on_delete=models.CASCADE,null=True)
    
    employee=models.CharField(null=True,max_length=50)
    date=models.DateField(auto_now=False, auto_now_add=False,null=True)
    intime=models.TimeField(auto_now=False, auto_now_add=False,null=True)
    outtime=models.TimeField(auto_now=False, auto_now_add=False, null=True)
    remark=models.CharField(null=True, max_length=50)

class schedule(models.Model):
    EmpSSN=models.IntegerField(null=True)
    deadlinedate=models.DateField( auto_now=False, auto_now_add=False, null=True )
    deadlinetime=models.TimeField( auto_now=False, auto_now_add=False, null=True)
    task=models.TextField(null=True)

class leave(models.Model):
    EmpSSN=models.IntegerField(null=True)
    sdate=models.DateField(null=True, auto_now=False, auto_now_add=False)
    edate=models.DateField(null=True, auto_now=False, auto_now_add=False)
    leavetype=models.CharField(null=True, max_length=50)
    reason=models.TextField(null=True)
    name=models.CharField(null=True, max_length=50)
    approval=models.CharField(default="pending", max_length=50)

#drishti module integrate


class Salary(models.Model):
    month_year = models.DateTimeField()
    base_salary = models.DecimalField(max_digits=19, decimal_places=2)
    house_rent_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    conveyance_allowance = models.DecimalField(max_digits=10, decimal_places=2, default=1600) # type: ignore
    medical_allowance = models.DecimalField(max_digits=10, decimal_places=2, default=1250) # type: ignore
    special_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    provided_fund = models.DecimalField(max_digits=10, decimal_places=2)
    health_insurance = models.DecimalField(max_digits=10, decimal_places=2)
    professional_tax = models.DecimalField(max_digits=10, decimal_places=2, default=200) # type: ignore
    tds = models.DecimalField(max_digits=10, decimal_places=2)
    other_reductions = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True) # type: ignore
    total_deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)  # type: ignore
    # total_deductions = provided_fund + health_insurance + professional_tax + tds + other_reductions
    gross_salary = models.DecimalField(max_digits=19, decimal_places=2, default=0, null=True) # type: ignore
    # gross_salary = base_salary + house_rent_allowance + conveyance_allowance + medical_allowance + special_allowance
    net_salary = models.DecimalField(max_digits=19, decimal_places=2, default=0, null=True) # type: ignore
    # net_salary = gross_salary - total_dedecutions
