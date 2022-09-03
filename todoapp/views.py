from random import randint
from unicodedata import name
from django.shortcuts import render,redirect
from todoapp.models import Registration,TasksModel
# Create your views here.
def taketomainpage(request):
    emailidlog = request.POST['email']
    passwordlog = request.POST['pass']
    try:
        user = Registration.objects.get(emailid = emailidlog)
    except: 
        msg4 = "Not Registered"
        return render(request,"loginpage.html",{'msg4':msg4})
    if user:
        if user.password==passwordlog:
            request.session['username'] = user.name
            msg1 = "Succesfully Logged In"
            return render(request,"loginpage.html",{'msg1':msg1})
        else:
            msg2 = "Password Incorrect"
            return render(request,"loginpage.html",{'msg2':msg2})
    else:
        msg4 = "Not Registered"
        return render(request,"loginpage.html",{'msg4':msg4})
    
def taketoRegisterpage(request):
    return render(request,"registrationpage.html")

def registered(request):
    if request.method=="POST":
        namereg = request.POST['name']
        emailidreg = request.POST['email']
        mob = request.POST['mobno']
        passwordreg = request.POST['pass']
        user = Registration.objects.filter(emailid = emailidreg)
        if user :
            msg1 = "User is Already Registered"
            return render(request,"registrationpage.html",{'msg1':msg1})
        else:
            msg2 = "User is Successfully Registered"
            reg = Registration.objects.create(name=namereg,mobno=mob,emailid=emailidreg,password=passwordreg)
            return render(request,"registrationpage.html",{'msg2':msg2})

def taketoLoginpage(request):
    return render(request,"loginpage.html")

def MainPage(request,pk):
    db = TasksModel.objects.filter(name=pk)
    return render(request,"mainpage.html",{'username':pk,'db':db})

def Addtask(request,pk):
    if request.method == "POST":
        idd = randint(1,10000)    
        titlee = request.POST['title']
        desc = request.POST['desc']
        prio = request.POST['ans']
        addedtask = TasksModel.objects.create(id=idd,name=pk,title=titlee,description=desc,priority=prio)
        return redirect('logintoMain',pk)

def DeleteTask(request,pk):
    deletetask = TasksModel.objects.get(id=pk)
    deletetask.delete()
    return redirect('logintoMain',deletetask.name)

def Logout(request):
    del request.session['username']
    return render(request,"loginpage.html")