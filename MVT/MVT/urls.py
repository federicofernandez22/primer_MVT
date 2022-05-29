
from django.contrib import admin
from django.urls import path, include
from MVT.views import plantilla

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plantilla/', plantilla),
    path('Familia/', include('Familia.urls') ),
]
