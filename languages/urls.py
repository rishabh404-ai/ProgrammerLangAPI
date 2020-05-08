from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('paradigm', views.paradigmViewSet)
router.register('languages', views.languagesViewSet)
router.register('programmer', views.programmerViewSet)

urlpatterns = [
     path('', include(router.urls))]
