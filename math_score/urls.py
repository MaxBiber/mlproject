from django.urls import path
from math_score import views

urlpatterns = [
    path('', views.index, name='math_score'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('prediction', views.prediction, name='prediction')
]