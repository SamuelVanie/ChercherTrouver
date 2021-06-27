from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import AddObjectForm

# Create your views here.
@login_required(login_url='accounts/login/')
def add_form_view(request):
    if request.method == 'POST':
        add_form = AddObjectForm(request.POST)
        if add_form.is_valid():
            instance = add_form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('{objects:objects_list}') # Rediriger vers la page qui affiche liste des elements 
    else:
        add_form =AddObjectForm()
    return render(request, 'add_form/add_form.html', {'add_form':add_form})
