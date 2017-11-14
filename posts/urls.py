from rest_framework import routers
from django.conf.urls import url, include
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
