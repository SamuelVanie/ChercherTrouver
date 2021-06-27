from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from objects.models import objetPerdu
from django.contrib.auth.decorators import login_required
from .forms import TakeObjectForm

@login_required(login_url='accounts/login')
def take_form_view(request, my_id):
    obj = get_object_or_404(objetPerdu, id=my_id)
    if request.method == 'POST':
        take = TakeObjectForm(request.POST)
        if take.is_valid():
            instance = take.save(commit=False)
            take.objet = obj
            instance.save()
            return redirect('{objects:objects_list}') # Rediriger vers la page qui affiche liste des elements 
    else:
        take = TakeObjectForm()
    
    return render(request, 'take_form/take_form.html', {'object':obj, 'take':take})
