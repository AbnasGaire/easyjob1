
from django.urls import path
from . import views
urlpatterns=[

    path('create/',views.create,name='create'),
    path('skillproject/',views.skill_store,name='skillpro'),
    path('experience/',views.experience,name='experience'),
    path('delete/<int:x>',views.remove,name='delete'),
    path('update/',views.updateuser,name='updateuser'),
    path('updatedetail/',views.updatedetail,name='updatedetails'),
    path('edit_data/<int:x>',views.editdata,name='edit_data'),
    path('deleteproject/<int:x>',views.deleteproject,name='deleteproject'),
    path('updateexperience/<int:x>',views.updateexperience,name='updateexperience'),
    path('deleteexperience/<int:x>',views.deleteexperience,name='deleteexperience'),
    path('updateprofile',views.updateprofile,name='updateprofile')
]