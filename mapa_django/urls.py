
from django.contrib import admin
from django.urls import path, include
from puntos.views import index
from rest_framework.routers import DefaultRouter
from puntos.api import PuntoViewSet

router = DefaultRouter()
router.register(r'puntos', PuntoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', index, name='index'),
]

