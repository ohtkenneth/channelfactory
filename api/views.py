from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import escape

from .utils import getLocation, saveLocation, calculateGeometricDistance

def index(request):
  return render(request, 'api/index.html')

def single(request):
  return render(request, 'api/single.html')

def reverse(request):
  return render(request, 'api/reverse.html')

def distance(request):
  return render(request, 'api/distance.html')

def singleQuery(request):
  location = '+'.join(escape(request.GET.get('location')).split(' '))
  geocode = getLocation(location, 'address')

  if not 'found' in geocode:
    geocode = saveLocation(geocode)

  return render(request, 'api/single.html', geocode)

def reverseQuery(request):
  location = escape(request.GET.get('latitude')) + ',' + escape(request.GET.get('longitude'))
  reverseGeocode = getLocation(location, 'latlng')

  if not 'found' in reverseGeocode:
    reverseGeocode = saveLocation(reverseGeocode)

  return render(request, 'api/reverse.html', reverseGeocode)

def distanceQuery(request):
  start = '+'.join(escape(request.GET.get('start')).split(' '))
  end = '+'.join(escape(request.GET.get('destination')).split(' '))
  
  geocodeStart = getLocation(start, 'address')
  geocodeEnd = getLocation(end, 'address')

  if not 'found' in geocodeStart:
    geocodeStart = saveLocation(geocodeStart)
  if not 'found' in geocodeEnd:
    geocodeEnd = saveLocation(geocodeEnd)

  geometricDistance = calculateGeometricDistance(
    geocodeStart['result'].latitude, 
    geocodeStart['result'].longitude,
    geocodeEnd['result'].latitude,
    geocodeEnd['result'].longitude
  )

  context = {
    'start': geocodeStart['result'],
    'end': geocodeEnd['result'], 
    'distance': ("%.2f" % geometricDistance) + ' km'
  }
  
  return render(request, 'api/distance.html', context)

