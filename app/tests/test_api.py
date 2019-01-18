import unittest
import json
from app.views.routes import app


class test_redflag(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_redflags(self):
        """ Tests that the end point fetches all records"""
        response = self.client.get('/api/v1/red-flags',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_single_redflag(self):
            """ Tests that the end point returns a single record"""
            redflag_details = {
                        "Images": "images.jpg",
                        "Videos": "videos.mp4",
                        "comment": "fix holes",
                        "createdBy": 1,
                        "createdOn": "2019-01-05 01:47:40",
                        "id": 1,
                        "location": "lat:242 long:568",
                        "status": "draft",
                        "type": "red-flag"
                }
            self.client.post('/api/v1/red-flags',
                            json=redflag_details)
            response = self.client.get('/api/v1/red-flags/1',
                                    content_type='application/json')
            self.assertEqual(response.status_code, 200)

    def test_patch_redflag_location(self):
        redflag_details = {
                        "Images": "images.jpg",
                        "Videos": "videos.mp4",
                        "comment": "fix holes",
                        "createdBy": 1,
                        "createdOn": "2019-01-05 01:47:40",
                        "id": 1,
                        "location": "lat:242 long:568",
                        "status": "draft",
                        "type": "red-flag"
                }
        self.client.post('/api/v1/red-flags',
                            content_type='application/json',
                            json=redflag_details)
        location = {
            "location": "lat:2375812 long:4556"
        }
        response = self.client.patch('/api/v1/red-flags/1/location', json=location)  
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['data']), 1)
        self.assertEqual(data["data"][0]["message"], "Updated red-flag record’s location")
        

    def test_patch_redflag_comment(self):
        redflag_details = {
                        "Images": "images.jpg",
                        "Videos": "videos.mp4",
                        "comment": "fix holes",
                        "createdBy": 1,
                        "createdOn": "2019-01-05 01:47:40",
                        "id": 1,
                        "location": "lat:242 long:568",
                        "status": "draft",
                        "type": "red-flag"
                }
        self.client.post('/api/v1/red-flags',
                            content_type='application/json',
                            json=redflag_details)  
        comment = {
            "comment": "testing change"
        }
        response = self.client.patch('/api/v1/red-flags/1/comment',
                                json=comment)  
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['data']), 1)
        self.assertEqual(data["data"][0]["message"], "Updated red-flag record’s comment")
        
             
    def test_delete_redflag(self):
        
        redflag_details = {
                        "Images": "images.jpg",
                        "Videos": "videos.mp4",
                        "comment": "fix holes",
                        "createdBy": 1,
                        "createdOn": "2019-01-05 01:47:40",
                        "id": 1,
                        "location": "lat:242 long:568",
                        "status": "draft",
                        "type": "red-flag"
                }
        self.client.post('/api/v1/red-flags',
                                    content_type='application/json',
                                    json=redflag_details)
        redflag_details = {
                        "Images": "images.jpg",
                        "Videos": "videos.mp4",
                        "comment": "fix holes",
                        "createdBy": 1,
                        "createdOn": "2019-01-05 01:47:40",
                        "id": 1,
                        "location": "lat:242 long:568",
                        "status": "rejected",
                        "type": "red-flag"
                }
        response = self.client.delete('/api/v1/red-flags/1',
                                      json=redflag_details)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['data']), 1)
        self.assertEqual(data["data"][0]["message"], "red-flag record has been deleted")
