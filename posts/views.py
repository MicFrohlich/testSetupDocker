# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from posts.models import *
from rest_framework import viewsets
from posts.serializers import *


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
