import imp
from django.urls import URLPattern, path
from .views import usuariosview

urlpatterns = [

    path('usuarios/', usuariosview.as_view(), name='lista_usuarios'),
    path('usuarios/<int:id>', usuariosview.as_view(), name='usuarios_actions')
    
            ]