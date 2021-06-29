from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('display/<str:filename>', views.display, name='display')
]
