from django.shortcuts import render,redirect
from .models import Contact


def home(request):
    return render(request, "home.html") 
def contact(request):
    return render(request,"contact.html")



def confirm_contact(request):
    if request.method=='GET':
        return redirect('info:Contact')
    elif request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,phone=phone,message=message)
        contact.save()
        return redirect('info:Contact')
        

