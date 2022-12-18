from rest_framework.views import Request, Response, status
from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .permissions import IsAccountOwner
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = UserSerializer
    queryset = User.objects.all()
