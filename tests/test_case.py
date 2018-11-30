'''Base test class.'''
import json
from unittest import TestCase
from app.api.v1.models import reported_flags


from app import create_app


class BaseCase(TestCase):

    def setUp(self):

        self.app = create_app()

        self.client = self.app.test_client()

        self.data = {

            "id": 'flag_id',
            "title": 'title',
            "flag_type": 'flag_type',
            "location": 'location',
            "incident": 'incident',
            "date": 'created_on'

        }

    def tearDown(self):
        del reported_flags[:]
