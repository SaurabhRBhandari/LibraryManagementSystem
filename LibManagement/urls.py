
from django.contrib import admin
from django.urls import path,include
import libmansys

from views import Home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/google/login/callback/libmansys/home',include('libmansys.urls')),
    path('accounts/', include('allauth.urls')),
    path('', Home.as_view(), name='home'),
    path('lib/',include('libmansys.urls'))
    
]
