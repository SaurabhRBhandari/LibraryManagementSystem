from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_home,name='index'),#redirect the user to user home page
    path('<int:ISBN>/',views.detail,name='detail'),#give details for a book with given ISBN
    path('all/',views.booklist,name='booklist'),#give details of all books registered in the library system
]
