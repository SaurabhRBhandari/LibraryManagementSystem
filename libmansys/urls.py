from django.urls import path
from . import views

app_name = 'libmansys'
urlpatterns = [
    # redirect the user to user home page
    path('', views.user_home, name='user_home'),
    # give details for a book with given ISBN
    path('<int:ISBN>/', views.detail, name='detail'),
    # give details of all books registered in the library system
    path('all/', views.booklist, name='booklist'),
    #for changing user profile
    path('profile/',views.edit_profile,name='profile')
]
