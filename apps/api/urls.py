from django.urls import path 
from .views import LearnTemplateViewset, LearnTemplateModelViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'objects', LearnTemplateModelViewSet, basename='learn-api')

urlpatterns = router.urls



