from django.urls import path

from space.views.mycreatedspaces import mycreatedspaces
from .views import homepage, signout, spaces, aboutus, mycreatedspaces, mymemberspaces, spacedetails, create_space, create_message, warning, create_step, update_space, delete_space, signout, change_password, edit_profile, register
from django.contrib.auth import views as auth_views

urlpatterns = [    
    path('', homepage, name='homepage'),
    path('spaces', spaces, name='spaces'),
    path('aboutus', aboutus, name='aboutus'),
    path('warning', warning, name='warning'),
    path('mycreatedspaces', mycreatedspaces, name='mycreatedspaces'),
    path('mymemberspaces', mymemberspaces, name='mymemberspaces'),
    path('spacedetails/<slug:slug>', spacedetails, name='spacedetails'),
    path('create-space', create_space, name='create-space'),
    path('create-message', create_message, name='create-message'),
    path('create-step', create_step, name='create-step'),
    path('update-space/<slug:slug>', update_space, name='update-space'),
    path('delete-space/<slug:slug>', delete_space, name='delete-space'),
    path('signout', signout, name='signout'),
    path('change-password', change_password, name='change-password'),
    path('edit-profile', edit_profile, name='edit-profile'),
    path('register', register, name='register'),
    path('signin', auth_views.LoginView.as_view(template_name='pages/signin.html'), name='signin'),
    
]