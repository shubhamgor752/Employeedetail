from django.shortcuts import render,redirect
from Employee.models import Company,Employee,User
from Employee.form import CompanyForm,EmployeeForm
from django.contrib import messages



#       


# #Home page
def home(request):
    return redirect(request,"")


def signup(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            msg="Email Already Registered"
            return render(request,'signup.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                        fname=request.POST['fname'],
                       
                        email=request.POST['email'],
                       
                        password=request.POST['password'],
                    )
                msg="Sign up Succesfully"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="Password & Confirmpassword Does Not Matched"
            return render(request,'signup.html',{'msg':msg})
    else:
        return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        try:
            user=User.objects.get(
                email=request.POST['email'],
                password=request.POST['password']
                )
            request.session['email']=user.email
            request.session['fname']=user.fname
            return render(request,'home.html')
        except:
            msg="Email Or Password Is Incorrect"
            return render(request,'home.html',{'msg':msg})
    else:
        return render(request,'login.html')

def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        return render(request,'login.html')
    except:
        return render(request,'login.html')



# To create Company
def comp(request):
    if request.method == "POST":

        form = CompanyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = CompanyForm()
    return render(request, "index.html", {'form':form})

# To retrieve Company details
def show(request):
    companies = Company.objects.all()
    return render(request, "show.html", {'companies':companies})

# To Edit Company details
def edit(request, cName):
    company = Company.objects.get(cName=cName)
    return render(request, "edit.html", {'company':company})

# To Update Company
def update(request, cName):
    company = Company.objects.get(cName=cName)
    form = CompanyForm(request.POST, instance= company)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, "edit.html", {'company': company})

# To Delete Company details
def delete(request, cName):
    company = Company.objects.get(cName=cName)
    company.delete()
    return redirect("/show")


# To create employee
def emp(request):
    if request.method == "POST":

        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                
                form.save()
                return redirect("/showemp")
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "addemp.html", {'form':form})

# To show employee details
def showemp(request):
    employees = Employee.objects.all()
    return render(request, "showemp.html", {'employees':employees})

# To delete employee details
def deleteEmp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    employee.delete()
    return redirect("/showemp")

# To edit employee details
def editemp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    return render(request, "editemployee.html", {'employee':employee})

# To update employee details
def updateEmp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    form = EmployeeForm(request.POST, instance= employee)
    print('Hello1')
    if form.is_valid():
        
        form.save()
        return redirect("/showemp")
    return render(request, "editemployee.html", {'employee': employee})


