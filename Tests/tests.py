import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test client for the Flask app."""
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        """Test that home route returns status 200 and contains expected text."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the UFO Sightings', response.data)

    def test_valid_year_route(self):
        """Test valid year route returns 200 and JSON list."""
        response = self.app.get('/sightings/year/1950')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_invalid_year_route(self):
        """Test invalid year route returns 404 for bad URL segment."""
        response = self.app.get('/sightings/year/banana')
        self.assertEqual(response.status_code, 404)  

if __name__ == '__main__':
    unittest.main()