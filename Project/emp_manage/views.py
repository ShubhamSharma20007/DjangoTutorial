from django.shortcuts import render,redirect
from django.http import HttpResponse
from  .models import Emp ,testimonial
from .forms import feedbackForm
# Create your views here.
def home(request):
    return render(request,"emp_tem/home.html")


def addemp(request):
    if request.method =="POST":
        name = request.POST.get('name')
        empid = request.POST.get('empid')
        number = request.POST.get('mobile')
        address = request.POST.get('address')
        working = request.POST.get('work')
        department = request.POST.get('depart') 
        # the boolean field take always True and false condition parameter 
        # if working is None:
        #     working =  False
        # else:
        #     working = True
        # or
        working =  True if working else False
        employee = Emp(name=name,emp_id=empid,phone=number,address =address,department=department,working =working)
        employee.save()
    return render(request,"emp_tem/addemp.html")



def userdata(request):
    empdata = Emp.objects.all()
    context ={
        'data' :empdata
    }
    return render(request,"emp_tem/userdata.html",context=context)

def delete_user(request, emp_id):
    userdelete = Emp.objects.filter(emp_id=emp_id)
    userdelete.delete()
    return redirect('userdata')

def updateuser(request,emp_id):
    empdata =  Emp.objects.filter(emp_id=emp_id)
    
    context = {
        'employeedata': empdata
    }
    return render(request,"emp_tem/updateuser.html",context=context)



def updation(request,emp_id):
    #getting a data from userupdate html file
    if request.method =="POST":
        name = request.POST.get('name')
        empid = request.POST.get('empid')
        number = request.POST.get('mobile')
        address = request.POST.get('address')
        working = request.POST.get('work')
        department = request.POST.get('depart')
        print(name,emp_id, "1234")
        # here i replace the data to new update values
        working =  True if working else False
        empshu = Emp.objects.filter(emp_id=emp_id)
        for emp in empshu:
            emp.name = name
            emp.emp_id = empid
            emp.phone = number
            emp.address =  address
            emp.department = department
            emp.save()
    

    return redirect('userdata')



def testi(request):
    testi=  testimonial.objects.all()
    context = {
        'testidata' : testi
    }
    
    return render(request, "emp_tem/testimonial.html" , context=context)



def feedback(request):
    if request.method ==  "POST":
        form = feedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']  #here we getting a data from form 
            print(name)
        else:
            return render(request,"userdata")
        
        
    else:
        form = feedbackForm()
    
    return render(request, "emp_tem/feedback.html",{'form':form})