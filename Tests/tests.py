import unittest
from app import *

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'UFO Sightings API', response.data)

    def test_valid_year_route(self):
        response = self.app.get('/sightings/year/1950')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_invalid_year_route(self):
        response = self.app.get('/sightings/year/banana')
        self.assertEqual(response.status_code, 404)  

if __name__ == '__main__':
    unittest.main()