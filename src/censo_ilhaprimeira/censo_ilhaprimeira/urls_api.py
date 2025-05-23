from rest_framework.routers import DefaultRouter
from .views_api import MoradorViewSet, DomicilioViewSet

router = DefaultRouter()
router.register(r'moradores', MoradorViewSet)
router.register(r'domicilios', DomicilioViewSet)

urlpatterns = router.urls