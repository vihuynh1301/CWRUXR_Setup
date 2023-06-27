from time import sleep
import unittest
from cwruxr_sdk.anchor_message import *
import orjson as json

test_id = "test"
test_guid = "abc-123"

class TestAnchorMessage(unittest.TestCase):
    def test_init(self):
        asa = [ASAAnchor(0, test_guid)]
        a = AnchorMessage(id = test_id, asaAnchors = asa)
        self.assertEqual(a.id, test_id)
        self.assertEqual(a.asaAnchors[0].id, 0)
        self.assertEqual(a.asaAnchors[0].asaGuid, test_guid)

        b = AnchorMessage(id = test_id)
        self.assertEqual(b.id, test_id)
        self.assertFalse(hasattr(b,"asaAnchors"))

    def test_FromDict(self):
        text1 = '{"id" : "test", "asaAnchors" : [{"id" : 0, "asaGuid" : "abc-123"}]}'
        a = AnchorMessage.FromDict(json.loads(text1))
        self.assertEqual(a.id, test_id)
        self.assertTrue(hasattr(a,"asaAnchors"))
        self.assertEqual(len(a.asaAnchors), 1)
        self.assertEqual(a.asaAnchors[0].id, 0)
        self.assertEqual(a.asaAnchors[0].asaGuid, test_guid)

        text2 = '{"id" : "test", "asaAnchors" : []}'
        b = AnchorMessage.FromDict(json.loads(text2))
        self.assertEqual(b.id, test_id)
        self.assertTrue(hasattr(b,"asaAnchors"))
        self.assertEqual(len(b.asaAnchors), 0)
        

        text3 = '{"id" : "test", "asaAnchors" : [{"id" : 0, "asaGuid" : "abc-123"}, {"id" : 1, "asaGuid" : "def-456"}]}'
        c = AnchorMessage.FromDict(json.loads(text3))
        self.assertEqual(c.id, test_id)
        self.assertTrue(hasattr(c,"asaAnchors"))
        self.assertEqual(len(c.asaAnchors), 2)
        self.assertEqual(c.asaAnchors[0].id, 0)
        self.assertEqual(c.asaAnchors[1].id, 1)
        
        self.assertEqual(c.asaAnchors[0].asaGuid, test_guid)
        self.assertEqual(c.asaAnchors[1].asaGuid, "def-456")

class TestASAAnchor(unittest.TestCase):
    def test_init(self):
        a = ASAAnchor(id = 0, asaGuid = test_guid)
        self.assertEqual(a.id, 0)
        self.assertEqual(a.asaGuid, test_guid)

        b = ASAAnchor(id = 1)
        self.assertEqual(b.id, 1)
        self.assertIsNone(b.asaGuid)

    def test_FromDict(self):
        text1 = '{"id" : 0, "asaGuid" : "abc-123"}'
        a = ASAAnchor.FromDict(json.loads(text1))

        self.assertEqual(a.id, 0)
        self.assertEqual(a.asaGuid, "abc-123")
        
        text2 = '{"id" : 1}'
        with self.assertRaises(KeyError):
            b = ASAAnchor.FromDict(json.loads(text2))
        