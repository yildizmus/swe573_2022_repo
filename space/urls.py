from django.urls import path

from space.views.mycreatedspaces import mycreatedspaces
from .views import homepage, spaces, aboutus, mycreatedspaces, mymemberspaces, spacedetails

urlpatterns = [
    path('', homepage, name='homepage'),
    path('spaces', spaces, name='spaces'),
    path('aboutus', aboutus, name='aboutus'),
    path('mycreatedspaces', mycreatedspaces, name='mycreatedspaces'),
    path('mymemberspaces', mymemberspaces, name='mymemberspaces'),
    path('spacedetails/<slug:slug>', spacedetails, name='spacedetails'),
    
]