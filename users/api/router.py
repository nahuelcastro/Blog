from django.urls import path
from users.api.views import *

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
]