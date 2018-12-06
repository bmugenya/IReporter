import unittest
from app import create_app


class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        self.data = {

            "id": "flag_id",
            "createdOn": "created_on",
            "createdBy": "flag_id",
            "type": "flag_type",
            "location": "location",
            "status": "pending",
            "photo": "bribe.jpg",
            "video": "bribe.mp4",
            "comments": "incident"

        }

        self.user = {
            "id": "user_id",
            "firstname": "firstname",
            "lastname": "lastname",
            "othernames": "othernames",
            "email": "email",
            "phoneNumber": "phoneNumbe",
            "username": "username",
            "registered": "time",
            "isAdmin": "False"

        }

    def tearDown(self):
        del self.data
        del self.user

    def test_can_create_post(self):
        response = self.client.post('/api/v1/record', json=self.data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()['message'], 'Successfully created red flag')

    def test_can_create_account(self):
        response = self.client.post('/api/v1/user', json=self.user, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_can_get_post(self):
        response = self.client.get('/api/v1/record/1')
        self.assertEqual(response.status_code, 200)

    def test_can_get_posts(self):
        response = self.client.get('/api/v1/record')
        result = response.get_json()
        self.assertEqual(0, len(result["data"]))
        self.assertEqual(response.status_code, 200)

    def test_can_edit_post(self):
        resp = self.client.patch('/api/v1/record/1')
        self.assertEqual(resp.status_code, 200)

    def test_can_delete_post(self):
        resp = self.client.delete('/api/v1/record/1')
        self.assertEqual(resp.status_code, 200)
