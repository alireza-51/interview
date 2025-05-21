from django.urls import path
from signup.api.views import UserViewSet

urlpatterns = [
    path('signup/user', UserViewSet.as_view()),
]
