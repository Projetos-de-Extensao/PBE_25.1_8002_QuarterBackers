from rest_framework.routers import DefaultRouter
from .views_api import MoradorViewSet, DomicilioViewSet, FalecidoViewSet

router = DefaultRouter()
router.register(r'moradores', MoradorViewSet)
router.register(r'domicilios', DomicilioViewSet)
router.register(r'falecidos', FalecidoViewSet)

urlpatterns = router.urls