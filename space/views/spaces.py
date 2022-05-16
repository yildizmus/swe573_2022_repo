from django.shortcuts import render

def spaces(request):
    return render(request,'pages/spaces.html', context={})