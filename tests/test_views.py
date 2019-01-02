import unittest
import json
from app import app


class test_redflag(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_redflags(self):
        # Tests that the end point fetches all records
        response = self.client.get('/api/v1/red-flags',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_single_redflag(self):
            # Tests that the end point returns a single record
            redflag_details = {
                        "id" : 1,
                        "createdOn" : "Date",  
                        "createdBy" : 1, 
                        "type" : "red-flags",       
                        "location" : "wakiso",   
                        "status" : "draft",     
                        "comment" : "fix holes",
                        "Images" : "images",
                        "Videos" : "videos"
                }
            self.client.post('/api/v1/red-flags',
                            json=redflag_details)
            response = self.client.get('/api/v1/red-flags/1',
                                    content_type='application/json')
           
            self.assertEqual(response.status_code, 200)

    def test_patch_redflag_location(self):
        redflag_details = {
            "location": "lat:2375812 long:4556"
        }
        self.client.patch('/api/v1/red-flags/1/location', json=redflag_details)  
        response = self.client.get('/api/v1/red-flags/1',
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['data']), 1)

    def test_patch_redflag_comment(self):
        redflag_details = {
            "comment": "testing change"
        }
        self.client.patch('/api/v1/red-flags/1/comment', json=redflag_details)  
        response = self.client.get('/api/v1/red-flags/1',
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['data']), 1)
        
        

       

    
