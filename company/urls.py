from django.urls import path
from . import views

urlpatterns=[
    path('create/',views.create,name='companycreate'),
    path('addvacancy/',views.addvacancy,name='addvacancy'),
    path('viewpost/',views.viewpost,name='viewpost'),
    path('updatecompany/',views.updatecompany,name='updatecompany'),
    path('updatecompanydetail/',views.updatecompanydetail,name='updatecompanydetail'),
    path('deletepost/<int:x>',views.deletepost,name='deletepost'),
    path('updatepost/<int:x>',views.updatepost,name='updatepost'),
    path('viewdetail/<int:x>',views.viewdetail,name='viewdetail'),


]