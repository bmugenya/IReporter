import unittest
from app import create_app
from app.db_con import database_setup


class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.dummy = database_setup()

        self.dummy.create_tables()

        self.data = {

            "id": 1,
            "createdOn": "created_on",
            "createdBy": "flag_id",
            "post_type": "flag_type",
            "location": "location",
            "status": "pending",
            "photo": "bribe.jpg",
            "video": "bribe.mp4",
            "comment": "incident"

        }

        self.user = {
            "id": 1,
            "firstname": "firstname",
            "lastname": "lastname",
            "othernames": "othernames",
            "email": "email",
            "phoneNumber": "phoneNumbe",
            "username": "username",
            "registered": "time",
            "isAdmin": "False",
            "password": "password"

        }

    def tearDown(self):
        self.dummy.destroy_tables()

    def test_can_create_post(self):
        response = self.client.post('/api/v1/red-flag', json=self.data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()['message'], 'Success')

    def test_can_create_account(self):
        response = self.client.post('/api/v1/auth/register/admin', json=self.user, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_can_get_post(self):
        response = self.client.get('/api/v1/red-flag/1')
        self.assertEqual(response.status_code, 200)

    def test_can_get_posts(self):
        response = self.client.get('/api/v1/red-flags')
        self.assertEqual(response.status_code, 200)

    def test_can_delete_post(self):
        resp = self.client.delete('/api/v1/red-flag/1')
        self.assertEqual(resp.status_code, 200)
