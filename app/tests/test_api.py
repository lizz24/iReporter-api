import unittest
import json
from app.views.incidents import app


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
                    "id": 1,
                    "createdOn": "Date",  
                    "createdBy": 1, 
                    "type": "red-flags",       
                    "location": "Nlat:2375812 long:4556",   
                    "status": "draft",     
                    "comment": "delete this flag",
                    "Images": "images",
                    "Videos": "videos"
            }
        self.client.post('/api/v1/red-flags',
                         content_type='application/json',
                         json=redflag_details)
        redflag_details = {
                    "id": 1,
                    "createdOn": "Date",  
                    "createdBy": 1, 
                    "type": "red-flags",       
                    "location": "lat:237 long:455",   
                    "status": "Rejected",     
                    "comment": "delete this flag",
                    "Images": "images",
                    "Videos": "videos"
        }
        response = self.client.delete('/api/v1/red-flags/1',
                                      json=redflag_details)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['data']), 1)
        self.assertEqual(data["data"][0]["message"], 
                         "red-flag record id has been deleted")

    def test_delete_redflag_with_id_not_found(self): 
            redflag_details = {
                        "id": 1,
                        "createdOn": "Date",  
                        "createdBy": 1, 
                        "type": "red-flags",       
                        "location": "Nlat:2375812 long:4556",   
                        "status": "draft",     
                        "comment": "delete this flag",
                        "Images": "images",
                        "Videos": "videos"
                }
            self.client.post('/api/v1/red-flags',
                             content_type='application/json',
                             json=redflag_details)
            redflag_details = {
                    "id": 1,
                    "createdOn": "Date",  
                    "createdBy": 1, 
                    "type": "red-flags",       
                    "location": "lat:237 long:455",   
                    "status": "Rejected",     
                    "comment": "delete this flag",
                    "Images": "images",
                    "Videos": "videos"
                    }
            response = self.client.delete('/api/v1/red-flags/10',
                                          json=redflag_details)
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 404)
            self.assertEqual(data["error"], 
                             "redflag id doesnot exist")
                         
    def test_wrong_url(self):
        redflag_details = {
                        "id": 1,
                        "createdOn": "Date", 
                        "createdBy": 1,
                        "type": "red-flags",    
                        "location": "wakiso, lat:111 long:222", 
                        "status": "draft",   
                        "comment": "fix holes",
                        "Images": "images",
                        "Videos": "videos"
                }
        self.client.post('/api/v1/red-flags',
                         content_type='application/json',
                         json=redflag_details)

        location = {"location": "Kampala"}
        response = self.client.patch(
            "/api/v1/red_flags/1/locagvgvht",
            json=location)   
        self.assertTrue(404, response.status_code)      

    def test_method_not_allowed(self):
        redflag_details = {
                        "id": 1,
                        "createdOn": "Date",  
                        "createdBy": 1, 
                        "type": "red-flags",       
                        "location": "wakiso, lat:111 long:222",   
                        "status": "draft",     
                        "comment": "fix holes",
                        "Images": "images",
                        "Videos": "videos"
                }
        self.client.post('/api/v1/red-flags',
                         content_type='application/json',
                         json=redflag_details)
        response = self.client.patch("/api/v1/red_flags")
        self.assertTrue(response.status_code, 405)
    
    def test_patchredflag_comment_with_nonexistant_id(self):
        redflag_details = {
                        "id": 1,
                        "createdOn": "Date",  
                        "createdBy": 1, 
                        "type": "red-flags",       
                        "location": "lat:2375812 long:4556",   
                        "status": "draft",     
                        "comment": "fix holes",
                        "Images": "images",
                        "Videos": "videos"
                }
        self.client.post('/api/v1/red-flags',
                         content_type='application/json',
                         json=redflag_details)  
        comment = {
            "comment": "testing change"
        }
        response = self.client.patch('/api/v1/red-flags/10/comment',
                                     json=comment)  
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["error"], "The redflag record id doest exist")

    def test_patchredflag_location_with_nonexistant_id(self):
        redflag_details = {
                        "id": 1,
                        "createdOn": "Date",  
                        "createdBy": 1, 
                        "type": "red-flags",       
                        "location": "wakiso, lat:111 long:222",   
                        "status": "draft",     
                        "comment": "fix holes",
                        "Images": "images",
                        "Videos": "videos"
                }
        self.client.post('/api/v1/red-flags',
                         content_type='application/json',
                         json=redflag_details)
        location = {
            "location": "lat:2375812 long:4556"
        }
        response = self.client.patch('/api/v1/red-flags/10/location',
                                     json=location)  
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["error"], "Redflag record id doesnot exist")

    def test_get_single_redflag_With_negative(self):
            """ Tests that the end point with zero integer"""
            redflag_details = {
                        "id": 1,
                        "createdOn": "Date",  
                        "createdBy": 1, 
                        "type": "red-flags",       
                        "location": "wakiso",   
                        "status": "draft",     
                        "comment": "fix holes",
                        "Images": "images",
                        "Videos": "videos"
                }
            self.client.post('/api/v1/red-flags',
                             json=redflag_details)
            redflag_details = {
                    "id": 1,
                    "createdOn": "Date",  
                    "createdBy": 1, 
                    "type": "red-flags",       
                    "location": "lat:237 long:455",   
                    "status": "Rejected",     
                    "comment": "delete this flag",
                    "Images": "images",
                    "Videos": "videos"
                       }
            response = self.client.get('/api/v1/red-flags/0',
                                        json=redflag_details)
            data = json.loads(response.data)  
            self.assertEqual(response.status_code, 400)
            self.assertEqual(data["error"], "No recorded redflags to display, please create redflag")
           
    def test_get_empty_redflaglist(self):
            """ Tests that the end point returns a single record"""
            redflag_details = {
                
            }
            self.client.post('/api/v1/red-flags',
                             json=redflag_details)
            response = self.client.get('/api/v1/red-flags',
                                       content_type='application/json')
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 404)
            self.assertEqual(data["error"], "Empty redflag list")
