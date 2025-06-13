from django.contrib import admin
from django.urls import path, include
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

# Configuração do Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API do Censo",
        default_version='v1',
        description="Documentação da API para o app do censo",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="estevaotevico@exemplo.com"),
        license=openapi.License(name="Licença BSD"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include('censo_ilhaprimeira.urls_api')),
    path('api/token/', obtain_auth_token, name='api_token_auth'),

    # URLs do Swagger
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]