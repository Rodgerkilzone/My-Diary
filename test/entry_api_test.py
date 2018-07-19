# import unittest,json 
# from app import create_app
# class TestApp(unittest.TestCase):
#      def Variables(self):
#          app = create_app('testing')
#          self.tester = app.test_client(self)
#          self.api_route = '/mydiary/api/v1/entries'
#          self.api_route_2 = '/mydiary/api/v1/entries/1'
#          self.payload = {'title':'beach','content':'today i had fun at the beach'}
#          self.entry = {
#                             "id":1,
#                             'title':"airport",
#                             'content':'i love travelling and adventure',
#                             "date":'5-8-2018'
#             }
#          self.entry_update= {'title':'school','content':'today school was amaizing'}
#          Entry().save(self.entry)
# # TEST FOR GETTING ALL ENTRIES
#      def test_get_all_entries(self):
#             # self.api_route = '/my_diary/api/v1/entries'
#          response = self.tester.get(self.api_route)
#          self.assertEqual(response.status_code, 200)
#          self.assertIn("All Entries", str(response.data))
#          self.assertIn('application/json', str(response.headers))
# # TEST FOR GETTING SPECIFIC ENTRY BY ID
#      def test_get_entry_by_id(self):
#             # self.api_route_2= '/my_diary/api/v1/entries/1'
#         response = self.tester.get(self.api_route_2)
#         self.assertEqual(response.status_code, 200)
#  # TEST FOR ENTRY POST
#      def test_entry_post(self):
#         response = self.tester.post(self.api_route,data=json.dumps(self.payload),
#         content_type="application/json")
#         self.assertEquals(response.status_code,201)
#         response_data = json.loads(response.data.decode('utf8'))
#         self.assertEqual("today i had fun at the beach",response_data['content'])
# # TEST FOR UPDATING ENTRY
#      def test_entry_update(self):
#         response = self.tester.put(self.api_route_2,data=json.dumps(self.entry_update),
#         content_type="application/json")
#         self.assertEqual(response.status_code, 200)
#         self.assertIn("school", str(response.data))
# # TEST FOR DELETING ENTRY
#      def test_delete_entry_by _id(self):
#         response = self.tester.delete(self.api_route_2)
#         self.assertEqual(response.status_code, 200)

# if __name__ == "__main__":
#     unittest.main()