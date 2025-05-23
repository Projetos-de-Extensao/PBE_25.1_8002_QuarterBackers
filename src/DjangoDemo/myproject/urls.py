from django.contrib import admin
from django.urls import path, include
#streaming_platform/urls.py
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuração do Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API de Conteúdos",
        default_version='v1',
        description="Documentação da API para o app de streaming de áudio e vídeo",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="suporte@exemplo.com"),
        license=openapi.License(name="Licença BSD"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Suas outras URLs
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),  # Inclua as URLs do seu app

    # URLs do Swagger
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]