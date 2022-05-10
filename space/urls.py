from django.urls import path
from .views import homepage, space

urlpatterns = [
    path('', homepage),
    path('space', space),
    
    
]