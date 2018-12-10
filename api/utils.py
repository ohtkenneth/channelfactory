import requests
import json

from math import cos, asin, sqrt
from .models import Geocode

GOOGLE_API_KEY = YOUR_API_KEY
GoogleApiBaseUrl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# checks db for location first before making api call
# type should either be address or latlng
def get_location(searchTerm, locationType):
  result = Geocode.objects.filter(search_term = searchTerm)

  if result.exists():
    return { 'search_term': searchTerm, 'result': result.first(), 'found': True }
  else: 
    # make api call
    googleApiUrl = GoogleApiBaseUrl + locationType + '=' + searchTerm + '&key=' + GOOGLE_API_KEY

    result = requests.get(googleApiUrl).json()['results']

    # return saveLocation(searchTerm, result)
    # use search_term as a key to follow db model
    return { 'search_term': searchTerm, 'result': result }

# extracts pertinent data from json response and saves to db
def save_location(data):
  # if geodata is empty, then save as None in database
  searchTerm = data['search_term']
  geodata = data['result']

  if not geodata:
    newGeocode = Geocode(
      search_term = searchTerm,
      address_string = None,
      latitude = None,
      longitude = None,
    )
    newGeocode.save()
    return { 'result': newGeocode }

  else:
    # extract address and coordinates from JSON response 
    formatted_address = None
    coordinates = None
    newGeocode = None

    for item in geodata:
      if 'formatted_address' in item:
        formatted_address = item['formatted_address']
      if 'geometry' in item:
        coordinates = item['geometry']['location']
      if formatted_address != None and coordinates != None:
        break

    newGeocode = Geocode(
      search_term = searchTerm, 
      address_string = formatted_address,
      latitude = coordinates['lat'],
      longitude = coordinates['lng']
    )

    newGeocode.save()

    return { 'result': newGeocode }

# returns distance in km
def calculate_geometric_distance(lat1, lon1, lat2, lon2):
  p = 0.017453292519943295 
  a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
  
  return 12742 * asin(sqrt(a))