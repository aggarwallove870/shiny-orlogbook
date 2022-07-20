from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from apps.authentication.models import NewUser
from .forms import *

from django.contrib.auth.hashers import make_password
from django.contrib import messages





def login_view(request):


    form = CustomUserLoginForm(request.POST )
    msg = None

    if request.method == "POST":

        if form.is_valid():
           
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("generate_bar_chart")
            else:
                msg = 'Invalid credentials provided'
            
    

    return render(request, "accounts/login.html", {"form": form, "msg": msg})



def change_password(request): 
    if request.method == "POST": 
        current_user = request.user.username
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        user = NewUser.objects.get(username= current_user)
        if user:
            if password == confirm_password:
                user.password = make_password(password)
                user.save()
                messages.success(request, "successfully saved")
                return redirect('change_password')
            else:
                messages.error(request, "password and confirm password not matched")
                return redirect('change_password')

        else:
            messages.error(request, "Invalid user")
            return redirect('change_password')
    else:
        return render(request, 'accounts/change_password.html')


def delete_user(request): 
    get_user= NewUser.objects.filter(is_superuser=False,is_supervisor=False).all()
    if request.method == "POST":
        get_user= NewUser.objects.filter(is_superuser=False,is_supervisor=False).all()
        get_data = request.POST.get("user_id")
        delete_user = NewUser.objects.filter(id=get_data)
        delete_user.delete()
        messages.success(request, "Successfully Deleted")
        return render(request,"accounts/remove_user.html", {'users':get_user})
    return render(request,"accounts/remove_user.html", {'users':get_user})