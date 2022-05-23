from django.urls import path

from space.views.mycreatedspaces import mycreatedspaces
from .views import homepage, spaces, aboutus, mycreatedspaces, mymemberspaces, spacedetails, create_space, create_message, warning, create_step

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
    
    
]