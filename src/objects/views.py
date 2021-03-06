from django.shortcuts import render, get_object_or_404
from .models import objetPerdu
from django.http import HttpResponse

# Create your views here.
def object_list_view(request):
    objets = objetPerdu.objects.all().order_by('date')
    context = {'objets':objets}
    return render(request, 'objects/object_list.html', context)

def object_detail_view(request, id):
    obj = get_object_or_404(objetPerdu, id=id)
    context = {
            'object':obj,
    }
    return render(request, 'objects/objects_detail.html', context)
