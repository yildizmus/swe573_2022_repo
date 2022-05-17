from django.shortcuts import render
from space.models import SpaceModel
from django.core.paginator import Paginator


def homepage(request): 

    allspaces=SpaceModel.objects.order_by('-id')

    page=request.GET.get('page')
    paginator=Paginator(allspaces,3)

    return render(request,'pages/homepage.html', context={'allspaces':paginator.get_page(page)})
