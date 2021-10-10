from django.shortcuts import render
from django.db.models import Q


from django.http import HttpResponse
from faker import Faker


fake=Faker()
from .models import employee


def employeedata(request):
    for i in range(100):
        firstname=fake.first_name()
        lastname=fake.last_name()
        email=fake.email()
        job=fake.random_element(elements=('SW','Training','HR','Salesman','Teacher'))
        salary=fake.random_int(min=25000,max=100000)
        city=fake.random_element(elements=('Guntur','Vijayawada','Prakasam','Nellore','Chittor'))
        state=fake.random_element(elements=('AP','TN','KERALA','KARNATAKA','MAHARASHTRA','GUJARAT'))
        employee(firstname=firstname,lastname=lastname,email=email,job=job,salary=salary,city=city,state=state).save()
    return HttpResponse("DataSaved")



def fetchingdata(request):
    if(request.method=="POST"):
        job1=request.POST.get('job')
        employees=employee.objects.filter(Q(job=str(job1)) | Q(state=str(job1)) | Q(firstname=(job1)) | Q(lastname=job1) | Q(city=job1) | Q(state=job1))
        return render(request,'employeedata.html',{'employees':employees})
    else:
        employees=employee.objects.all()
        return render(request,'employeedata.html',{'employees':employees})


def gunturdata(request):
    if(request.method=="POST"):
        job1=request.POST.get('job')
        employees=employee.objects.filter(city='Guntur') & employee.objects.filter(job=job1)
        return render(request,'guntur.html',{'employees':employees})
    else:
        employees=employee.objects.filter(city='Guntur')
        return render(request,'guntur.html',{'employees':employees})


def vijaywadadata(request):
    if(request.method=="POST"):
        job1=request.POST.get('job')
        employees=employee.objects.filter(city='Vijayawada') & employee.objects.filter(job=job1)
        return render(request,'guntur.html',{'employees':employees})
    else:
        employees=employee.objects.filter(city='Vijayawada')
        return render(request,'vij.html',{'employees':employees})


def prakasamdata(request):
    if(request.method=="POST"):
        job1=request.POST.get('job')
        employees=employee.objects.filter(city='Prakasam') & employee.objects.filter(job=job1)
        return render(request,'guntur.html',{'employees':employees})
    else:
        employees=employee.objects.filter(city='Prakasam')
        return render(request,'prakasam.html',{'employees':employees})


def chittordata(request):
    if(request.method=="POST"):
        job1=request.POST.get('job')
        employees=employee.objects.filter(city='Chittor') & employee.objects.filter(job=job1)
        return render(request,'guntur.html',{'employees':employees})
    else:
        employees=employee.objects.filter(city='Chittor')
        return render(request,'chittor.html',{'employees':employees})


def nelloredata(request):
    if(request.method=="POST"):
        job1=request.POST.get('job')
        employees=employee.objects.filter(city='Nellore') & employee.objects.filter(job=job1)
        return render(request,'guntur.html',{'employees':employees})
    else:
        employees=employee.objects.filter(city='Nellore')
        return render(request,'nellore.html',{'employees':employees})
