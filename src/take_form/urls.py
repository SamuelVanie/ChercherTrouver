from django.urls import path
from .views import take_form_view 

app_name = 'take_form'

urlpatterns = [
        path('<int:id>/', take_form_view, name='take_form'),
        ]
