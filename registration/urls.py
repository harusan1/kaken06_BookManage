from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import index,login,signup

urlpatterns = [
    path('', index.IndexView.as_view(), name="index"),
    path('login/', login.LoginView.as_view(), name="login"),
    path("signup/", signup.SignUpView.as_view(), name="signup"),
]