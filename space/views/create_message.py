from django.shortcuts import redirect, render, get_object_or_404
from space.forms import CreateMessageModelForm, CreateSpaceModelForm
from space.models import SpaceModel
from django.contrib.auth.decorators  import login_required

@login_required(login_url='/')
def create_message(request):     
    spaceform=CreateSpaceModelForm(request.POST or None, files=request.FILES or None)
    if spaceform.is_valid():
        space=spaceform.save(commit=False)    
    form=CreateMessageModelForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        message=form.save(commit=False)
        space=get_object_or_404(SpaceModel, slug= message.memberspace.slug)
        message.sender=request.user
        if request.user in space.members.all() or request.user == space.author:            
            message.save()
            
        return redirect('spacedetails', slug= message.memberspace.slug)    

    return render(request,'pages/create-message.html', context={'form':form})