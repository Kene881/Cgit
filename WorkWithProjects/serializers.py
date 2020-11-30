from rest_framework import serializers
from WorkWithProjects.models import Project
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta():
        model = User
        fields = ['username', 'email']

class ProjectSerializer(serializers.ModelSerializer):

    authors = serializers.StringRelatedField(many=True)
    class Meta():
        model = Project
        fields = ['id','name', 'description', 'authors','file']