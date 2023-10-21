from urllib.request import Request
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import  Person

#def home(request):
   
 #   return render(request,'index.html')

def save(request):   
    if request.method == "POST":
        firstname =request.POST.get("firstname")
        lastname =request.POST.get("lastname")
       
        reg = Person(firstname=firstname, lastname=lastname)
        reg.save()
        print('Data Save Successfully')
    return render(request,'index.html')
