from django.contrib import admin
from django.urls import path, include
from views import Home


urlpatterns = [
    path("admin/", admin.site.urls),  # loads the admin window
    # redirecting user to user home after successfull login
    path("accounts/google/login/callback/libmansys/home", include("libmansys.urls")),
    path("accounts/", include("allauth.urls")),
    path("", Home.as_view(), name="home"),  # Website's home page
    path("lib/", include("libmansys.urls")),  # libmansys's home page
]
