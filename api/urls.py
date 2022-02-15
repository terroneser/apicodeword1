import imp
from django.urls import URLPattern, path
from .views import restaurantesview, usuariosview

urlpatterns = [

    path('usuarios/', usuariosview.as_view(), name='lista_usuarios'),
    path('usuarios/<int:id>', usuariosview.as_view(), name='usuarios_actions'),
    path('restaurantes/', restaurantesview.as_view(), name='lista_restaurantes'),
    path('restaurantes/<int:id>', restaurantesview.as_view(), name='restaurantes_actions')
            ]