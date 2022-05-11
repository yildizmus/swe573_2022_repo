from django.shortcuts import render

def homepage(request):
    return render(request,'pages/homepage.html', context={})

def spaces(request):
    return render(request,'pages/spaces.html', context={})

def aboutus(request):
    return render(request,'pages/aboutus.html', context={})
