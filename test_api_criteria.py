import unittest  # Import the unittest framework for writing and running tests
import requests  # Import the requests library for making HTTP requests

class TestAPICriteria(unittest.TestCase):

    def setUp(self):
        self.api_url = "https://api.tmsandbox.co.nz/v1/Categories/6329/Details.json?catalogue=false"
        # Set up the API URL to be used in all test methods

    def test_name(self):
        response = requests.get(self.api_url)
        # Send a GET request to the API URL
        data = response.json()
        # Parse the response JSON into a Python dictionary
        self.assertEqual(data['Name'], "Home & garden")
        # Assert that the 'Name' in the response matches the expected value

    def test_can_relist(self):
        response = requests.get(self.api_url)
        data = response.json()
        self.assertTrue(data['CanRelist'])
        # Assert that the 'CanRelist' value in the response is True

    def test_promotion_description(self):
        response = requests.get(self.api_url)
        data = response.json()
        promotions = data['Promotions']
        # Get the list of promotions from the response
        feature_promotion = next((promo for promo in promotions if promo['Name'] == "Feature"), None)
        # Find the promotion with the name 'Feature' in the list, or set to None if not found
        self.assertIsNotNone(feature_promotion)
        # Assert that the 'Feature' promotion is found
        self.assertIn("Better position in category", feature_promotion['Description'])
        # Assert that the description of the 'Feature' promotion contains the expected text

if __name__ == '__main__':
    unittest.main()
    # Run the tests if the script is executed as the main program