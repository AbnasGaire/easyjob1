from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.
gender =(('male','Male'),('female','Female'),('other','Other'))
class JobSeeker(models.Model):
    fulname=models.CharField(max_length=100,default='Abinash')
    address= models.CharField(max_length=100)
    experience_year= models.IntegerField(default=0,null=True,blank=True)
    cv= models.FileField(upload_to='cv/')
    profile=models.ImageField(upload_to='profile/')
    professional_title=models.CharField(max_length=100,null=True,blank=True)
    contact_no = PhoneField(null=True,blank=True,unique=True)
    description = models.TextField(null=True,blank=True,help_text="About Yourself")
    url=models.URLField(blank=True,null=True,unique=True)
    gender=models.CharField(choices=gender,max_length=10)
    qualification= models.CharField(max_length=100,help_text="Your Heighest Degree")
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Skill(models.Model):
    skill_title=models.CharField(max_length=100)
    proficiency_level= models.IntegerField()
    jobseeker=models.ForeignKey(JobSeeker,on_delete=models.CASCADE)

    def __str__(self):
        return self.skill_title

class Experience(models.Model):
    company=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField(null=True,blank=True)
    jobseeker=models.ForeignKey(JobSeeker,on_delete=models.CASCADE)

    def __str__(self):
        return self.jobseeker.user.username

class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    link=models.URLField(null=True,blank=True,unique=True)
    jobseeker=models.ForeignKey(JobSeeker,on_delete=models.CASCADE)

    def __str__(self):
        return self.jobseeker.user.username
