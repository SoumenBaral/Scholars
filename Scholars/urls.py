
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Core.urls')),
    path('auth/',include('Account.urls')),
    path('course/',include('Course.urls')),
]
