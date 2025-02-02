from django.urls import path
from users.views import show_users

urlpatterns = [
    path('show-users/', show_users)
]
