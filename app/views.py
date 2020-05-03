from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from app.forms import userform,userinfoform
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
def userpage(request):
    return render(request,'app/userpage.html')

#######################################################################################   register information  ###############################

def register(request):
    registered = False

    if request.method=='POST':

        user_form=userform(data=request.POST)
        info_form=userinfoform(data=request.POST)

        if user_form.is_valid() and info_form.is_valid():

            user=user_form.save()

            user.set_password(user.password)
            user.save()
            info=info_form.save(commit=False)
            info.user=user
            info.save()
            registered=True

            return redirect('user_login')

        else:

            print(user_form.errors,info_form.errors)

    else:
        user_form=userform()
        info_form=userinfoform()
    return render(request,'app/register.html',
                                {
                                    'user_form':user_form,
                                    'info_form':info_form,
                                    'registered':registered})

#######################################################################################   login information  ###############################


def user_login(request):
    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('/')
            else:
                return HttpResponse("Your account is not active.")
        else:
            
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request,'app/login.html',{})

#######################################################################################   logout information  ###############################


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('userpage'))

#######################################################################################   profile information  ###############################

def profile_view(request):
    return render(request,'app/profile.html')


def profile(request):
    return HttpResponseRedirect(reverse('profile_view'))

