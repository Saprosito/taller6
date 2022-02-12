from django.urls import path, re_path, include
from apps.tipoDocumento.views import index

urlpatterns = [
   path('', index),
    
]
