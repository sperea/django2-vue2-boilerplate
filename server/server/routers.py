# -*- coding: utf-8 -*-
# @Author: Sergio Perea

from rest_framework import routers
from mainapp.viewsets import NoticiaViewSet

router = routers.DefaultRouter()
router.register(r'noticia', NoticiaViewSet)