from django.shortcuts import render

def homepage(request):
    return render(request,'pages/homepage.html', context={})

def space(request):
    return render(request,'pages/space.html', context={})

