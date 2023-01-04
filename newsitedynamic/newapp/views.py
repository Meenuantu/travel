from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method=='POST':
        u_name=request.POST['username']
        passw=request.POST['password']
        user1=auth.authenticate(username=u_name,password=passw)
        if user1 is not None:
            auth.login(request,user1)
            return redirect('/')
        else:
            messages.info(request,"Invalid username or password")
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        U_NAME =request.POST['username']
        F_NAME = request.POST['first_name']
        L_NAME = request.POST['last_name']
        email = request.POST['email']
        passw = request.POST['password']
        passw_c = request.POST['ConfirmPassword']
        if passw == passw_c:
            if User.objects.filter(username=U_NAME).exists():
                messages.info(request,"Username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email address already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=U_NAME,password=passw,first_name=F_NAME,last_name=L_NAME,email=email )
                user.save();
                print("User created")
                return redirect('login')

        else :
            messages.info(request,"Passwords didnot match")
            return redirect('register')



    return render(request,"new.html")