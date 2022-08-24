from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('dual', views.dual),
    path('dual/manual', views.dual_manual_post),
    path('test', views.test),

]