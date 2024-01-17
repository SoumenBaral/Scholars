
from django.urls import path
from .views import RegistrationFormView, activate_account,UserLoginView,logOut

app_name = 'accounts'

urlpatterns = [
    path('register/',RegistrationFormView.as_view(),name='register'),
    path('activate/<uidb64>/<token>/', activate_account,name='activate'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',logOut,name='logout')
]