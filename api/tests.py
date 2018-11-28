from django.test import TestCase
from .models import Geocode

from .utils import getLocation, saveLocation, calculateGeometricDistance
# Create your tests here.

class UtilityFunctionsTests(TestCase):
  def test_getLocation_return_dictionary(self):
    """
      getLocation should return a dictionary with fields searchTerm and result
    """

    searchTerm = 'test'
    result = getLocation(searchTerm, 'address')

    self.assertIs('search_term' in result, True)
    self.assertIs('result' in result, True)

  def test_getLocation_return_args(self):
    """
      getLocation should return the original search term
    """

    searchTerm = 'originalSearchTerm'
    result = getLocation(searchTerm, 'address')

    self.assertIs(result['search_term'], searchTerm)

  def test_saveLocation_Geocode_instantiation(self):
    """
      saveLocation should return an instantiation of Geocode class model
    """

    model = saveLocation(getLocation('Los+Angeles', 'address'))['result']

    self.assertIs(isinstance(model, Geocode), True)

  def test_saveLocation_None(self):
    """
      saveLocation should return result Geocode with None values if no search results
    """

    model = saveLocation(getLocation('***', 'address'))['result']

    self.assertIs(model.search_term, '***')
    self.assertIs(model.address_string, None)
    self.assertIs(model.latitude, None)
    self.assertIs(model.longitude, None)