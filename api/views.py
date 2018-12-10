from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import escape

from .utils import get_location, save_location, calculate_geometric_distance

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
  geocode = get_location(location, 'address')

  if not 'found' in geocode:
    geocode = save_location(geocode)

  return render(request, 'api/single.html', geocode)

def reverseQuery(request):
  location = escape(request.GET.get('latitude')) + ',' + escape(request.GET.get('longitude'))
  reverseGeocode = get_location(location, 'latlng')

  if not 'found' in reverseGeocode:
    reverseGeocode = save_location(reverseGeocode)

  return render(request, 'api/reverse.html', reverseGeocode)

def distanceQuery(request):
  start = '+'.join(escape(request.GET.get('start')).split(' '))
  end = '+'.join(escape(request.GET.get('destination')).split(' '))
  
  geocodeStart = get_location(start, 'address')
  geocodeEnd = get_location(end, 'address')

  if not 'found' in geocodeStart:
    geocodeStart = save_location(geocodeStart)
  if not 'found' in geocodeEnd:
    geocodeEnd = save_location(geocodeEnd)

  geometricDistance = calculate_geometric_distance(
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

