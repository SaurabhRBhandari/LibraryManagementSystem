from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('<int:ISBN>/',views.detail,name='detail'),
    path('all/',views.booklist,name='booklist'),
]
