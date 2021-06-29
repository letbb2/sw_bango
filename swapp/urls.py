from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('display/<int:counter>/<str:filename>', views.display, name='display')
]
