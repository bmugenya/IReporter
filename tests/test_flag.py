import unittest
from app import create_app, create_tables


class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.store = create_tables()
        self.client = self.app.test_client()
        self.client = self.store.test_client()

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

    def tearDown(self):
        del self.data

    def test_can_create_post(self):
        response = self.client.post('/api/v1/record', json=self.data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()['message'], 'Successfully created red flag')
