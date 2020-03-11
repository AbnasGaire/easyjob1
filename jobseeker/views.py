from django.shortcuts import render,redirect
from .forms import JobseekerForm,JobseekerSkill,JobseekerExperienceForm,Updateform,JobseekerCreateProject,Updateprofile
from .models import JobSeeker,Skill,Project,Experience
from django.contrib.auth.models import User
# Create your views here.

def create(request):
    if request.method == 'GET':
        context={
            'form':JobseekerForm()
        }
        return render(request,'jobseekercreate.html',context)
    else:
        form = JobseekerForm(request.POST,request.FILES or None)
        if form.is_valid():
            data=form.save(commit=False)
            data.user_id=request.user.id
            data.save()
            return redirect('dashboard')
        else:
            return render(request,'jobseekercreate.html',{'form':form})



def skill_store(request):
    if request.method=='GET':

        return redirect('dashboard')

    else:
        form=JobseekerSkill(request.POST)
        if form.is_valid:
            data=form.save(commit=False)
            a=JobSeeker.objects.get(user_id=request.user.id)
            data.jobseeker_id=a.id
            data.save()
            return redirect('dashboard')


def experience(request):
    if request.method=='GET':
        return redirect('dashboard')
    else:
        form=JobseekerExperienceForm(request.POST)
        if form.is_valid():
            data =form.save(commit=False)
            a=JobSeeker.objects.get(user_id=request.user.id)
            data.jobseeker_id=a.id
            data.save()
            return redirect('dashboard')


def remove(request,x):
    a=Skill.objects.get(id=x)
    a.delete()
    return redirect('dashboard')

def updateuser(request):
    if request.method =='GET':
        return redirect('dashboard')
    else:
        f=request.POST.get('fname')
        l=request.POST.get('lname')
        a=User.objects.get(id=request.user.id)
        a.first_name=f
        a.last_name=l
        a.save()
        return redirect('dashboard')

def updatedetail(request):
    if request.method=='GET':
        return redirect('dashboard')
    else:
        b=JobSeeker.objects.get(user_id=request.user.id)
        form=Updateform(request.POST or None,instance=b) # for id
        if form.is_valid:
            form.save()
            return redirect('dashboard')




def editdata(request,x):

         jobseeker=JobSeeker.objects.get(user_id=request.user.id)
         project=Project.objects.get(id=x)
         if jobseeker.id==project.jobseeker_id:
             form= JobseekerCreateProject(request.POST or None,instance=project)
             if form.is_valid():
                 form.save()
                 return redirect('dashboard')
             context={
                    'form':form
                }
             return render(request,'edit.html',context)
         else:
             return render(request,'error.html',{'error':'You cannot delete this post'})


def deleteproject(request,x):

    a=Project.objects.get(id=x)

    a.delete()
    return redirect('dashboard')

def updateexperience(request,x):
    a=Experience.objects.get(id=x)
    form= JobseekerExperienceForm(request.POST or None ,instance=a)
    context = {
        'updateexperienceform': form
    }
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request,'updateexperience.html',context)

def  deleteexperience(request,x):
    a=Experience.objects.get(id=x)
    a.delete()
    return redirect('dashboard')



def updateprofile(request):
    if request.method=='GET':
        return redirect('dashboard')
    else:
        c=JobSeeker.objects.get(user_id=request.user.id)
        form=Updateprofile(request.POST , request.FILES,instance=c)
        if form.is_valid:
            form.save()
        return redirect('dashboard')