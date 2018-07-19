import unittest,json 

class TestApp(unittest.TestCase):

    def test_get_all_entries(self):
        self.api_route = '/my_diary/api/v1/entries'
        response = self.tester.get(self.api_route)
        self.assertEqual(response.status_code, 200)
        self.assertIn("All Entries", str(response.data))
        self.assertIn('application/json', str(response.headers))


if __name__ == "__main__":
    unittest.main()