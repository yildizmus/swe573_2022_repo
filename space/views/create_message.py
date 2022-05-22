from django.shortcuts import redirect, render
from space.forms import CreateMessageModelForm, CreateSpaceModelForm
from django.contrib.auth.decorators  import login_required

@login_required(login_url='/')
def create_message(request):
    spaceform=CreateSpaceModelForm(request.POST or None, files=request.FILES or None)
    if spaceform.is_valid():
        space=spaceform.save(commit=False)
    form=CreateMessageModelForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        message=form.save(commit=False)
        message.sender=request.user
        message.save()
        
        return redirect('spacedetails', slug= message.memberspace.slug)    

    return render(request,'pages/create-message.html', context={'form':form})