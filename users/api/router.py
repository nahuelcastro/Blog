from django.urls import path
from users.api.views import *

urlpatterns = [
    path('auth/signup/', SignUpView.as_view(), name='signup'),
]