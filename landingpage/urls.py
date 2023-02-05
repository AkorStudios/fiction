from django.urls import path
from .views import *

urlpatterns =[
   path('', LandingPage.as_view(), name = 'landingpage'),
   path('registration/', Register, name = 'registration'),
]  
