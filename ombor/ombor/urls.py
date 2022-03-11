from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from omborapp.views import OmborLC, OmborRUD, ProductLC, ProductRUD, ClientLC, ClientRUD
from rest_framework.authtoken.views import obtain_auth_token
from statisticaapp.views import StatsLC, StatsRUD


schema_view = get_schema_view(
   openapi.Info(
      title="Ombor API",
      default_version='v1',
      description="Ombor",
      contact=openapi.Contact("Sukhrobbek Mukhammadjonov <surobbekmuxammadjonov@gmail.com>, <+998993930242>"),
   ),
   public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', OmborLC.as_view()),
    path('/<int:pk>/', OmborRUD.as_view()),
    path('product/', ProductLC.as_view()),
    path('product/<int:pk>/', ProductRUD.as_view()),
    path('client/', ClientLC.as_view()),
    path('client/<int:pk>/', ClientRUD.as_view()),

    path('stats/', StatsLC.as_view()),
    path('stats/<int:pk>/', StatsRUD.as_view()),

    path('get-token/', obtain_auth_token),
    path('docs/', schema_view.with_ui("swagger", cache_timeout=0), name="swagger-doc"),
    path('doc/', schema_view.with_ui("redoc", cache_timeout=0), name="redoc-doc"),

]
