from django.shortcuts import render, get_object_or_404
from .models import objetPerdu
from django.http import HttpResponse

# Create your views here.
def object_list_view(request):
    objets = objetPerdu.objects.all().order_by('date')
    return render(request, 'objects/object_list.html', {'objets':objets})

def object_detail_view(request, my_id):
    obj = get_object_or_404(objetPerdu, id=my_id)
    context = {
            'object':obj,
            }
    return render(request, 'objects/objects_detail.html', context)
