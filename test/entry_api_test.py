import unittest,json 
from app.app import app
class TestApp(unittest.TestCase):
# TEST FOR GETTING ALL ENTRIES
     def test_get_all_entries(self):
         self.tester = app.test_client(self)
         self.api_route= 'http://127.0.0.1:5000/mydiary/api/v1/entries'
         response = self.tester.get(self.api_route)
         self.assertEqual(response.status_code, 200)
         self.assertIn("movies", str(response.data))
         self.assertIn('application/json', str(response.headers))
# TEST FOR GETTING SPECIFIC ENTRY BY ID
     def test_get_entry_by_id(self):
        self.tester = app.test_client(self)
        self.api_route= 'http://127.0.0.1:5000/mydiary/api/v1/entries'
        response = self.tester.get(self.api_route)
        self.assertEqual(response.status_code, 200)
 # TEST FOR ENTRY POST
     def test_entry_post(self):
        self.tester = app.test_client(self)
        self.api_route= 'http://127.0.0.1:5000/mydiary/api/v1/entries'
        self.payload = {'title':'beach','content':'today i had fun at the beach'}
        response = self.tester.post(self.api_route,data=json.dumps(self.payload),
        content_type="application/json")
        self.assertEquals(response.status_code,201)
        self.assertIn("beach", str(response.data))
# TEST FOR UPDATING ENTRY
     def test_entry_update(self):
        self.tester = app.test_client(self)
        self.api_route= 'http://127.0.0.1:5000/mydiary/api/v1/entries/1'
        self.entry_update= {'title':'school','content':'today school was amaizing'}
        response = self.tester.put(self.api_route,data=json.dumps(self.entry_update),
        content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("school", str(response.data))
# TEST FOR DELETING ENTRY
     def test_delete_entry(self):
        self.tester = app.test_client(self)
        self.api_route= 'http://127.0.0.1:5000/mydiary/api/v1/entries/2'
        response = self.tester.delete(self.api_route)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()