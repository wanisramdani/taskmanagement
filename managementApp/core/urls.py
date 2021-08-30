from os import name
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.utils import cache

from rest_framework import routers, permissions
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views
from managementapp import views as vs

app_name = "core"

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        description="Test description",
        default_version="Version 0.0.1",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="")
        ),
    public=True,
    permission_classes= [permissions.AllowAny]
)

router = routers.DefaultRouter()
router.register('clients', vs.ClientViewSet)
router.register('subTasks', vs.SubTaskViewSet)
router.register('tasks', vs.TaskViewSet)
router.register('project', vs.ProjectViewSet)


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('clients/', include('managementapp.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.index),
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='docs'), name='docs'),
    url(r'^swagger(.P<format>\.json|.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-swagger-ui"),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name="schema-redoc"),
]
