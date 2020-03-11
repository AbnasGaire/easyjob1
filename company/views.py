from django.shortcuts import render,redirect
from .forms import CreateCompany,Updatejob
from django.contrib.auth.models import User
from .models import Job,Company
from .forms import Addpost
from easyjob.views import checkJobseekerOrCompany
# Create your views here.

def create(request):

    if request.method=='GET':
        context={
            'form':CreateCompany()
        }
        return render(request,'companycreate.html',context)
    else:
        form=CreateCompany(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user_id=request.user.id
            data.save()
            return redirect('companydashboard')
        else:
            return render(request,'companycreate.html',{'form':form})

def addvacancy(request):
    if request.method=='GET':
        context={
            'addvacancypost':Addpost()
        }
        return render(request,'addvacancy.html',context)
    else:
        form=Addpost(request.POST,request.FILES or None)
        if form.is_valid():
            data=form.save(commit=False)
            a=User.objects.get(id=request.user.id)
            b=Company.objects.get(user_id=request.user.id)
            data.company_id=b.id
            data.save()
            return redirect('companydashboard')

def viewpost(request):
    if request.method=='GET':
        a = Company.objects.get(user_id=request.user.id)
        b = Job.objects.filter(company_id=a.id)[::-1]
        context = {
            'job': b
        }
        return  render(request,'viewpost.html',context)


def updatecompany(request):

    a=request.POST.get('fname')
    b=request.POST.get('lname')
    c=User.objects.get(id=request.user.id)
    c.first_name=a
    c.last_name=b
    c.save()
    return redirect('companydashboard')

def updatecompanydetail(request):
    if request.method=='GET':
        return redirect('companydashboard')
    else:
        a=Company.objects.get(user_id=request.user.id)
        form=CreateCompany(request.POST or None ,instance=a)
        if form.is_valid():
            form.save()
            return redirect('companydashboard')




def deletepost(request,x):
    a=Job.objects.get(id=x)
    a.delete()
    return redirect('viewpost')

def updatepost(request,x):

    a=Job.objects.get(id=x)
    form=Updatejob(request.POST or None ,instance=a)
    context={
        'updatepostform':form
    }

    if form.is_valid():
        form.save()
        return redirect('viewpost')
    return render(request, 'updatepost.html', context)

def viewdetail(request,x):
    if request.method =='GET':
        a=Job.objects.filter(id=x)
        context={
            'view':a
        }
        return render(request,'viewdetails.html',context)


