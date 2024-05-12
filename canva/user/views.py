from django.shortcuts import render,redirect
from .forms import registerForm,LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


def login_view(request):
    if request.method== 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=User.objects.filter(username=username).first()
            if user and user.check_password(password):
                login(request,user)
                return redirect('info:home')
            return render(request,'login.html',context={'form':form,'invalid_cred':True})
        return render(request,'login.html',context={'form':form})
    else:
        form=LoginForm()
        return render(request,'login.html',context={'form':form})
    


def register_view(request):
    form=registerForm()
    if request.method=='POST':
        form=registerForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('info:home')

        return render(request,'register.html',context={'form':form})
    else:
        form=registerForm
        return render(request,'register.html',context={'form':form})


def logout_view(request):
    logout(request)
    return redirect('user:login')