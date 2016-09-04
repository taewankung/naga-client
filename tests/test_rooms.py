import unittest
from nagaclient.client import NagaClient

class UserManagerTest(unittest.TestCase):
    def setUp(self):
        self.client = NagaClient(rpc_server=True)
        self.client.initial()

        self.client.user.loggedin_info = {'token': 'test_token'}

    def tearDown(self):
        self.client.disconnect()

    def test_list_rooms(self):
        result = self.client.room.list_rooms()
        self.assertIn('rooms', result['responses'])

