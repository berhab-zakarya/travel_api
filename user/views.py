from django.shortcuts import render
from rest_framework import viewsets, permissions, status, filters
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Adjust according to your security needs
