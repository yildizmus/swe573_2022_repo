from django.shortcuts import redirect, render, get_object_or_404
from space.forms import UpdateSpaceModelForm
from space.models import SpaceModel
from django.contrib.auth.decorators  import login_required

@login_required(login_url='/')
def update_space(request, slug):
    space=get_object_or_404(SpaceModel, slug=slug, author=request.user)
    form=UpdateSpaceModelForm(request.POST or None, files=request.FILES or None, instance=space)
    if form.is_valid():
        form.save()
        return redirect('spacedetails', slug=space.slug)    

    return render(request,'pages/update-space.html', context={'form':form})