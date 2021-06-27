from django.urls import path 
from .views import add_form_view


app_name = 'add_form'

urlpatterns = [
        path('create/', add_form_view, name='add_form')
]
