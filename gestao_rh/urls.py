from django.contrib import admin
from rest_framework import routers
from apps.core import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include('apps.core.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('horas-extras/', include('apps.registro_hora_extra.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

