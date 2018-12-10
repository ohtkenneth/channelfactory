from django.test import TestCase
from .models import Geocode

from .utils import get_location, save_location, calculate_geometric_distance
# Create your tests here.

class UtilityFunctionsTests(TestCase):
  def test_getLocation_return_dictionary(self):
    """
      getLocation should return a dictionary with fields searchTerm and result
    """

    searchTerm = 'test'
    result = get_location(searchTerm, 'address')

    self.assertIs('search_term' in result, True)
    self.assertIs('result' in result, True)

  def test_getLocation_return_args(self):
    """
      getLocation should return the original search term
    """

    searchTerm = 'originalSearchTerm'
    result = get_location(searchTerm, 'address')

    self.assertIs(result['search_term'], searchTerm)

  def test_saveLocation_Geocode_instantiation(self):
    """
      saveLocation should return an instantiation of Geocode class model
    """

    model = save_location(get_location('Los+Angeles', 'address'))['result']

    self.assertIs(isinstance(model, Geocode), True)

  def test_saveLocation_None(self):
    """
      saveLocation should return result Geocode with None values if no search results
    """

    model = save_location(get_location('***', 'address'))['result']

    self.assertIs(model.search_term, '***')
    self.assertIs(model.address_string, None)
    self.assertIs(model.latitude, None)
    self.assertIs(model.longitude, None)