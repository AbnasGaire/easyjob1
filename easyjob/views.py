from django.shortcuts import HttpResponse,render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm
from jobseeker.models import JobSeeker,Skill,Experience
from company.models import Company,Job
from django.contrib.auth.models import User
from jobseeker.forms import JobseekerCreateProject,JobseekerExperienceForm,JobseekerSkill,Updateform,Updateprofile
from jobseeker.models import Project
from company.forms import CreateCompany
from general.models import Slider,Testimonial

def home(request):
    if request.method=='GET':
        context={
            'slider':Slider.objects.all()[:3],
            'testimonial':Testimonial.objects.all()[:4],
            'jobseeker':JobSeeker.objects.all()[:4]
        }
        return render(request,'home.html',context)

def signup(request):
    if request.method=='GET':

        context={

        'form':SignupForm()

            }
        return render(request,'signup.html',context)

    else:
        # form=UserCreationForm(request.POST)
        form=SignupForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Your Account is Created  Successfully')
            return redirect('signin')
        else:
            return render(request,'signup.html',{'form':form})



def signin(request):
    if request.method =='GET':
        return render(request,'login.html')
    else:

        u=request.POST.get('username')
        p=request.POST['password']
        user=authenticate(username=u,password=p)
       # print(request.POST)

        if user is not None:
            login(request,user)
            id=request.user.id
            #creating function to check the company or jobseeker
            b=checkJobseekerOrCompany(id)
            if b ==1:
              return redirect('dashboard')
            elif b==2:
                return redirect('companydashboard')
            else:
                return redirect('who')
        else:
            messages.error(request,'Your password does not match')
            return redirect ('signin')

@login_required(login_url='signin')

def dashboard(request):
    a = checkJobseekerOrCompany(request.user.id)
    if a == 2:
        return redirect('companydashboard')

    if request.method =='GET':
        a=User.objects.get(id=request.user.id)
        b=JobSeeker.objects.get(user_id=request.user.id)
        # ya bata aaja ko
        project=Project.objects.filter(jobseeker_id=b.id)[::-1]  #if more than on value is present we use filter
        skill =Skill.objects.filter(jobseeker_id=b.id)
        experience=Experience.objects.filter(jobseeker_id=b.id)
        context={
            'user':a,
            'jobseeker':b,
            'jobseeker_create_form':JobseekerCreateProject,
            'project':project,
            'jobseeker_experience_form':JobseekerExperienceForm,
            'jobseeker_skill':JobseekerSkill,
            'skill':skill,
            'expeirence':experience,
            'updateform':Updateform(instance=b) , # to render the data iin the form
            'update_profile':Updateprofile(instance=b)

        }
        return render(request,'dashboard.html',context)
    else:
        form = JobseekerCreateProject(request.POST)
        if  form.is_valid():
            data=form.save(commit=False)
            a=JobSeeker.objects.get(user_id=request.user.id)
            data.jobseeker_id =a.id
            data.save()
            return redirect('dashboard')
        else:
            return redirect('dashboard')

def companydashboard(request):
    a=User.objects.get(id=request.user.id)
    b=Company.objects.get(user_id=request.user.id)
    j=Job.objects.filter(company_id=b.id)[:3]
    context={
        'user1':a,
        'company':b,
        'updatecompany':CreateCompany(instance=b),
        'job':j
    }
    return render(request,'company_dashboard.html',context)
@login_required(login_url='signin')
def who(request):

    a= checkJobseekerOrCompany(request.user.id)
    if a==1:
        return redirect('dashboard')
    elif a==2 :
        return redirect('companydashboard')
    else:
        return render(request,'who.html')
def signout(request):
    logout(request)
    return redirect('signin')

def  checkJobseekerOrCompany(id):
    try:
        if JobSeeker.objects.get(user_id=id):
             return 1
    except:
        try:
            if Company.objects.get(user_id=id):
                return 2
        except:
            return 3

