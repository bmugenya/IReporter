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
            "incident": "flag_type",
            "location": "location",
            "status": "pending",
            "photo": "bribe.jpg",
            "video": "bribe.mp4",
            "comment": "incident"

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
        response = self.client.post('/api/v1/auth/register', json=self.user, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_can_get_post(self):
        response = self.client.get('/api/v1/record/1')
        self.assertEqual(response.status_code, 200)

    def test_can_get_posts(self):
        response = self.client.get('/api/v1/record')
        self.assertEqual(response.status_code, 200)
