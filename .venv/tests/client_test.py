from time import sleep
import unittest

from cwruxr_sdk.client import Client

fake_endpoint = "test_endpoint"
fake_room_id = "test_room_id"
fake_anchor_id = "test_anchor_id"

real_endpoint = "test_endpoint"
real_room_id = "test_room_id"
real_anchor_id = "test_anchor_id"

class TestClientCreation(unittest.TestCase):
    def test_initialize(self):
        client = Client(fake_endpoint, fake_room_id, fake_anchor_id)
        self.assertEqual(client._endpointDefault, fake_endpoint)
        self.assertEqual(client._roomIdDefault, fake_room_id)
        self.assertEqual(client._anchorIdDefault, fake_anchor_id)
        pass

class TestAnchor(unittest.TestCase):
    def setUp(self):
        self.client = Client(real_endpoint, real_room_id, real_anchor_id)

    def tearDown(self) -> None:
        pass

    def test_post(self):
        self.fail("Not Yet Implemented")

    def test_get(self):
        self.fail("Not Yet Implemented")

    def test_get_all(self):
        self.fail("Not Yet Implemented")

    def test_delete(self):
        self.fail("Not Yet Implemented")

    def test_delete_all(self):
        self.fail("Not Yet Implemented")

class TestObject(unittest.TestCase):
    def setUp(self):
        self.client = Client(real_endpoint, real_room_id, real_anchor_id)
        self.client.PostAnchor(real_anchor_id)

    def tearDown(self):
        self.client.DeleteAnchor(real_anchor_id)

    def test_post(self):
        self.fail("Not Yet Implemented")

    def test_get(self):
        self.fail("Not Yet Implemented")

    def test_get_all(self):
        self.fail("Not Yet Implemented")

    def test_delete(self):
        self.fail("Not Yet Implemented")

    def test_delete_all(self):
        self.fail("Not Yet Implemented")

    def test_delete_bulk(self):
        self.fail("Not Yet Implemented")
    
class TestMaterial(unittest.TestCase):
    def setUp(self):
        self.client = Client(real_endpoint, real_room_id, real_anchor_id)

    def tearDown(self):
        pass
        
    def test_post(self):
        self.fail("Not Yet Implemented")

    def test_get(self):
        self.fail("Not Yet Implemented")

    def test_get_all(self):
        self.fail("Not Yet Implemented")

    def test_delete(self):
        self.fail("Not Yet Implemented")

    def test_delete_all(self):
        self.fail("Not Yet Implemented")