import unittest
from nagaclient.client import NagaClient

class UserManagerTest(unittest.TestCase):
    def setUp(self):
        self.client = NagaClient(rpc_server=True)
        self.client.initial()

    def tearDown(self):
        self.client.disconnect()

    def test_login_with_username_should_pass(self):
        username = 'test'
        password = 'testpasswd'
        result = self.client.user.login(username, password)

        self.assertTrue(result['responses']['loggedin'])
