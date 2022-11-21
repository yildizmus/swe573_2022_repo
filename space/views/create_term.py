from django.shortcuts import redirect, render, get_object_or_404
from space.models import SpaceModel
from space.forms import CreateTermModelForm, CreateSpaceModelForm

def create_term(request):
    spaceform=CreateSpaceModelForm(request.POST or None, files=request.FILES or None)
    if spaceform.is_valid():
        space=spaceform.save(commit=False)
    form=CreateTermModelForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        term=form.save(commit=False)
        term.termwriter=request.user
        space=get_object_or_404(SpaceModel, slug= term.termspace.slug)
        if request.user in space.members.all() or request.user == space.author:
            term.save()
        
        return redirect('spacedetails', slug= term.termspace.slug)    

    return render(request,'pages/create-term.html', context={'form':form})