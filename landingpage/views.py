from django.shortcuts import render
from django.views.generic import TemplateView
from .models import EarlyUser
from django.http import HttpResponse                                                                             

# Create your views here.

class LandingPage(TemplateView):
    template_name = 'landingpage.html'
    
    
def Register(request):
    if request.method == 'POST':
        name = request.POST['name']
        storytype = request.POST['storytype']
        phone = request.POST['phone']
        
        if len(phone) < 11:
            return HttpResponse("Use a valid Whatsapp Phone Number")
        elif len(phone) > 11:
            return HttpResponse("Use a valid Whatsapp Phone Number")
        else:
            new_user = EarlyUser(name=name, storytype=storytype, phone=phone)
            new_user.save()
            return HttpResponse("Registered Successfully")
            
        
        
    return render(request, "registration.html")
        
        
