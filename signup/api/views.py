from rest_framework import generics
from signup.models import User
from signup.api.serializers import UserSerializer


class UserViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    