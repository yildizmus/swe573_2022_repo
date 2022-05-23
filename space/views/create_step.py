from django.shortcuts import redirect, render
from space.forms import CreateStepModelForm, CreateSpaceModelForm

def create_step(request):
    spaceform=CreateSpaceModelForm(request.POST or None, files=request.FILES or None)
    if spaceform.is_valid():
        space=spaceform.save(commit=False)
    form=CreateStepModelForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        step=form.save(commit=False)
        step.stepcreator=request.user
        step.save()
        
        return redirect('spacedetails', slug= step.stepspace.slug)    

    return render(request,'pages/create-step.html', context={'form':form})