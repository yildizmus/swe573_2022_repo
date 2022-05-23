from django.shortcuts import render, get_object_or_404
from space.models import SpaceModel
from django.core.paginator import Paginator

def spacedetails(request, slug): 
    space=get_object_or_404(SpaceModel, slug=slug)
    messages=space.messages.all().order_by('-id')
    steps=space.steps.all()


    page=request.GET.get('page')
    paginator=Paginator(messages,3)
    return render(request,'pages/spacedetails.html', context={
        'space':space,
        'messages':paginator.get_page(page),
        'steps':steps,
        
    })