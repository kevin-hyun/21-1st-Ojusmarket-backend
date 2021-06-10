from django.urls import path

from .views import UserIdentityCheck
from .views import UserSignUp
urlpatterns = [
    path('/id-check', UserIdentityCheck.as_view()),
    path('/sign-up', UserSignUp.as_view())
     ]