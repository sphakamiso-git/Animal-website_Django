from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .decorators import user_not_authenticated



# Create your views here.
@user_not_authenticated
def register(request):
    # Logged in user can't register a new account
    #if request.user.is_authenticated:
    #   return redirect('/')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'New account created: {user.username}')
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            #    print(request, error)
    
    else:
        form = UserRegistrationForm()

    return render(request=request, template_name='users/register.html', context={'form':form})

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, 'Logged out successfullly!')
    return redirect('homepage')

"""
@user_not_authenticated
def custom_login(request):
    #if request.user.is_authenticated:
    #    return redirect('homepage')
    
    if request.method == 'POST':
        #form = AuthenticationForm(request=request, data=request.POST)
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f'Hello <b>{user.username}</b>! You have been logged in')
                return redirect('homepage')
        
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    form = AuthenticationForm()

    return render(request=request, template_name='users/login.html', context={'form': form })
    """
@user_not_authenticated
def custom_login(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("homepage")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, 'You must pass the reCAPTCHA test')
                    continue
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="users/login.html",
        context={"form": form}
        )
