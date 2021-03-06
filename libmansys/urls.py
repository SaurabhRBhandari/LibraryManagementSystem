from django.urls import path
from . import views
from .views import (
    BookListView,
    BookRequestView,
)

app_name = "libmansys"
urlpatterns = [
    # redirect the user to user home page
    path("", views.user_home, name="user_home"),
    # give details for a book with given ISBN
    path("<int:ISBN>/", views.detail, name="detail"),
    # give details of all books registered in the library system
    path("all/", BookListView.as_view(), name="booklist"),
    # request a new book
    path("request/", BookRequestView.as_view(), name="request"),
    # for changing user profile
    path("profile/", views.edit_profile, name="profile"),
    # give details of pending requests by the user
    path("requests/pending", views.pending_requests, name="pending_requests"),
    # give details of books issued to the user
    path("requests/issued", views.issued_books, name="issued_books"),
]
