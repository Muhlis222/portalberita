from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('api/', include('appberita.urls'), name='appberita'),
    path('api-token-auth/', obtain_auth_token)
]
