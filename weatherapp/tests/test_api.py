import unittest
from app.services.weather_service import get_weather_for_city

class TestWeatherAPI(unittest.TestCase):
    def test_get_weather_for_city(self):
        data = get_weather_for_city(-15.7939, -47.8828)  # Brasília
        self.assertIn("current", data)

if __name__ == "__main__":
    unittest.main()
