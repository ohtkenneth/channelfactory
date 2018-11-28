from django.urls import path

from . import views

urlpatterns = [
  path('geocode', views.index, name = 'index'),
  path('geocode/single', views.single, name = 'single'),
  path('geocode/single/query', views.singleQuery, name = 'singleQuery'),
  path('geocode/reverse', views.reverse, name = 'reverse'),
  path('geocode/reverse/query', views.reverseQuery, name = 'reverseQuery'),
  path('geocode/distance', views.distance, name = 'distance'),
  path('geocode/distance/query', views.distanceQuery, name = 'distanceQuery')
]