from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def accounts_signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # return redirect('objects:objects_list') after I'll create my objects
    else:
        form = UserCreationForm()
    return render(request, 'accounts/accounts_signup.html', {'form':form})


def accounts_login_view(request):
    if request.method == 'POST':
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():
            user = form.get_user()
            login(request, user)
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/accounts_login.html', {'form':form})

def accounts_logout_view(request):
   if request.method == 'POST':
       logout(request)
       # return redirect('objects:objects_list')
