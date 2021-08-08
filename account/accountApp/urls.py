from rest_framework.routers import DefaultRouter

from .api import SpentViewSet, ImageViewSet

router = DefaultRouter()
router.register('api', SpentViewSet, 'API')
router.register('image', ImageViewSet, 'image')

urlpatterns = router.urls

