
from django.contrib import admin
from django.urls import path,include

from views import Home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', Home.as_view(), name='home'),
    path('accounts/google/login/callback/libmansys/home',include('libmansys.urls'),name='libmansys/home')
]
