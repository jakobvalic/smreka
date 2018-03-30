from django.urls import path

from . import views

urlpatterns = [
    path('izris/', views.izris_smreke, name='izris'),
    path('', views.pridobi_visino, name='vnos'),
]