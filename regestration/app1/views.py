from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        # Check if passwords match
        if pass1 != pass2:
            return HttpResponse("Passwords do not match")

        try:
            # Creating the user
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()

            return redirect('login')

        except IntegrityError:
            return HttpResponse("Username already exists. Please choose a different username.")
        
    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('username or password is incorrect!!!')

    return render(request, 'login.html')


def Logout(request):
    logout(request)
    return redirect('login')