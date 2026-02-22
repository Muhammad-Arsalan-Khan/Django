from django.shortcuts import render

def home(request):
    return render(request, 'main/app.html')

def about(request):
    return render(request, 'main/app2.html')
