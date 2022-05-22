from django.shortcuts import redirect, render
from space.forms import CreateSpaceModelForm
from django.contrib.auth.decorators  import login_required

@login_required(login_url='/')
def create_space(request):
    form=CreateSpaceModelForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        space=form.save(commit=False)
        space.author=request.user
        space.save()
        form.save_m2m()
        return redirect('spacedetails', slug=space.slug)    

    return render(request,'pages/create-space.html', context={'form':form})