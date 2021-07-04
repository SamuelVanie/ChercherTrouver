from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserCustomForm, UserProfileForm 

# Create your views here.
def accounts_signup_view(request):
    if request.method == 'POST':
        user_form = UserCustomForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form = user_form.save()
            profile_form.save()
            login(request, user_form)
            return redirect('objects:objects_list')     
    else:
        user_form = UserCustomForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.profile)
    return render(request, 'accounts/accounts_signup.html', {'user_form':user_form, 'profile_form':profile_form})


def accounts_login_view(request):
    if request.method == 'POST':
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():
            user = form.get_user()
            login(request, user)
            redirect('objects:objects_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/accounts_login.html', {'form':form})

def accounts_logout_view(request):
   if request.method == 'POST':
       logout(request)
       return redirect('objects:objects_list')
