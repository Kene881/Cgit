from django.urls import path, include

from rest_framework import routers

from WorkWithProjects.views import ProjectVewSet, UserVewSet

router = routers.DefaultRouter()
router.register('Project', ProjectVewSet)
router.register('Users', UserVewSet)

urlpatterns = [
    path('', include(router.urls)),
]
