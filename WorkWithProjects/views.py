from django.shortcuts import render
from rest_framework import viewsets
from WorkWithProjects.models import Project
from WorkWithProjects.serializers import (
    ProjectSerializer,
    UserSerializer
)
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
#BasicAuth, IsAuth
#
#

class ProjectVewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class UserVewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer