from django.urls import path
from .views import object_list_view, object_detail_view

app_name = 'objects'

urlpatterns = [
        path('', object_list_view, name='objects_list'),
        path('<int:my_id>/', object_detail_view, name='objects_detail'),
        ]
