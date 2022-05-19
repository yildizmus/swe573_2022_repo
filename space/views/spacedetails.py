from django.shortcuts import render, get_object_or_404
from space.models import SpaceModel, message
#from django.contrib.auth.decorators  import login_required

#@login_required(login_url='/')
def spacedetails(request, slug): 
    space=get_object_or_404(SpaceModel, slug=slug)
    messages=space.messages.all()
    
    return render(request,'pages/spacedetails.html', context={
        'space':space,
        'messages':messages,
        
    })