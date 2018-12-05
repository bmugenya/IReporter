import json

from .test_case import BaseCase


class TestproductResource(BaseCase):


    def test_can_create_post(self):
        response = self.client.post('api/v1/record', json=self.data)
        result = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()['message'], 'Successfully created red flag')


    def test_can_get_post(self):
        response = self.client.get('api/v1/record/1')
        result = response.get_json()
        self.assertEqual(response.status_code, 200)

    def test_can_get_posts(self):
        response = self.client.get('api/v1/record')
        result = response.get_json()
        self.assertEqual(0, len(result["data"]))
        self.assertEqual(response.status_code, 200)

    def test_can_edit_post(self):
        resp = self.client.patch('/api/v1/record/1')
        self.assertEqual(resp.status_code, 200)

    def test_can_delete_post(self):
        resp = self.client.delete('api/v1/record/1')
        self.assertEqual(resp.status_code, 200)
