from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api import VisaApplicationViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

router = routers.DefaultRouter()
router.register(r'applications', VisaApplicationViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="VisaFlow API",
        default_version='v1',
        description="Documentation for VisaFlow project",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
