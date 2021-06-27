from django.urls import path
from .views import(
        accounts_signup_view,
        accounts_login_view,
        accounts_logout_view,
        ) 

app_name = 'accounts'

urlpatterns = [
        path('signup/', accounts_signup_view, name='accounts_signup'),
        path('login/', accounts_login_view, name='accounts_login'),
        path('logout/', accounts_logout_view, name='accounts_logout'),
]
