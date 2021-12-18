from django.shortcuts import render
from django.http import HttpResponse
from .models import Parcle
# Create your views here.
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return render(request , 'login_page/logout.html')

def check_view(request):
    try:
       
        user = request.user.email
        parcles = Parcle.objects.filter(email = user)
        for parcle in parcles:
            print(parcle.ems)
        return render(request , 'login_page/check.html' ,{'parcles':parcles})
        
    except:
       return render(request , 'login_page/check.html')
    
    
    
def history_view(request):
    return render(request , 'login_page/history.html')