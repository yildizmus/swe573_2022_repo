from django.urls import path
from .views import homepage, spaces, aboutus

urlpatterns = [
    path('', homepage, name='homepage'),
    path('spaces', spaces, name='spaces'),
    path('aboutus', aboutus, name='aboutus'),
    
    
]