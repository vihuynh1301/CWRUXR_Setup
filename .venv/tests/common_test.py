from time import sleep
import unittest
import orjson as json

from cwruxr_sdk.common import *

class TestVector3(unittest.TestCase):
    def test_init(self):
        v1 = Vector3(0, 0, 0)
        self.assertEqual(v1.x, 0)
        self.assertEqual(v1.y, 0)
        self.assertEqual(v1.z, 0)

        v2 = Vector3(1, 2, 3)
        self.assertEqual(v2.x, 1)
        self.assertEqual(v2.y, 2)
        self.assertEqual(v2.z, 3)

    def test_FromDict(self):
        j1 = '{"x": 0, "y": 0, "z": 0}'
        v1 = Vector3.FromDict(json.loads(j1))
        self.assertEqual(v1.x, 0)
        self.assertEqual(v1.y, 0)
        self.assertEqual(v1.z, 0)
        
        j2 = '{"x": 1, "y": 2, "z": 3}'
        v2 = Vector3.FromDict(json.loads(j2))
        self.assertEqual(v2.x, 1)
        self.assertEqual(v2.y, 2)
        self.assertEqual(v2.z, 3)

    def test_eq(self):
        v1 = Vector3(0, 0, 0)
        j1 = '{"x": 0, "y": 0, "z": 0}'
        v2 = Vector3.FromDict(json.loads(j1))

        self.assertEqual(v1, v2)
        self.assertEqual(v2, v1)

        v3 = Vector3(1, 2, 3)
        j2 = '{"x": 1, "y": 2, "z": 3}'
        v4 = Vector3.FromDict(json.loads(j2))

        self.assertEqual(v3, v4)
        self.assertEqual(v4, v3)

        self.assertNotEqual(v1, v3)
        self.assertNotEqual(v2, v3)
        self.assertNotEqual(v1, v4)
        self.assertNotEqual(v2, v4)

        v5 = Vector3(1,0,0)
        v6 = Vector3(0,1,0)
        v7 = Vector3(0,0,1)

        self.assertNotEqual(v5, v6)
        self.assertNotEqual(v6, v7)
        self.assertNotEqual(v7, v5)
        
        self.assertNotEqual(v1, v5)
        self.assertNotEqual(v1, v6)
        self.assertNotEqual(v1, v7)

class TestVector2(unittest.TestCase):
    def test_init(self):
        v1 = Vector2(0,0)
        self.assertEqual(v1.x, 0)
        self.assertEqual(v1.y, 0)

        v2 = Vector2(1,2)
        self.assertEqual(v2.x, 1)
        self.assertEqual(v2.y, 2)

    def test_FromDict(self):
        j1 = '{"x": 0, "y": 0}'
        v1 = Vector2.FromDict(json.loads(j1))
        self.assertEqual(v1.x, 0)
        self.assertEqual(v1.y, 0)
        
        j2 = '{"x": 1, "y": 2}'
        v2 = Vector2.FromDict(json.loads(j2))
        self.assertEqual(v2.x, 1)
        self.assertEqual(v2.y, 2)

    def test_eq(self):
        v1 = Vector2(0, 0)
        j1 = '{"x": 0, "y": 0}'
        v2 = Vector2.FromDict(json.loads(j1))

        self.assertEqual(v2, v1)
        self.assertEqual(v1, v2)

        v3 = Vector2(1, 2)
        j2 = '{"x": 1, "y": 2}'
        v4 = Vector2.FromDict(json.loads(j2))

        self.assertEqual(v3, v4)
        self.assertEqual(v4, v3)

        self.assertNotEqual(v1, v3)
        self.assertNotEqual(v2, v3)
        self.assertNotEqual(v1, v4)
        self.assertNotEqual(v2, v4)

        v5 = Vector3(1,0,0)
        v6 = Vector3(0,1,0)

        self.assertNotEqual(v5, v6)
        
        self.assertNotEqual(v1, v5)
        self.assertNotEqual(v1, v6)

class TestQuaternion(unittest.TestCase):
    def test_init(self):
        q1 = Quaternion(0,0,0,1)
        self.assertAlmostEqual(q1.x, 0)
        self.assertAlmostEqual(q1.y, 0)
        self.assertAlmostEqual(q1.z, 0)
        self.assertAlmostEqual(q1.w, 1)

        q2 = Quaternion(.7,.7,.7,.7)
        self.assertAlmostEqual(q2.x, .7)
        self.assertAlmostEqual(q2.y, .7)
        self.assertAlmostEqual(q2.z, .7)
        self.assertAlmostEqual(q2.w, .7)

    def test_FromDict(self):
        j1 = '{"x": 0, "y": 0, "z": 0, "w": 1}'
        q1 = Quaternion.FromDict(json.loads(j1))
        self.assertAlmostEqual(q1.x, 0)
        self.assertAlmostEqual(q1.y, 0)
        self.assertAlmostEqual(q1.z, 0)
        self.assertAlmostEqual(q1.w, 1)
        
        j2 = '{"x": 0.7, "y": 0.7, "z": 0.7, "w": 0.7}'
        q2 = Quaternion.FromDict(json.loads(j2))
        self.assertAlmostEqual(q2.x, .7)
        self.assertAlmostEqual(q2.y, .7)
        self.assertAlmostEqual(q2.z, .7)
        self.assertAlmostEqual(q2.w, .7)

class TestEuler(unittest.TestCase):
    pass

class TestPose(unittest.TestCase):
    def test_init(self):
        p1 = Pose(position = Vector3(0,0,0), rotation = Quaternion(0,0,0,1), scale = Vector3(1,1,1))
        self.assertEqual(p1.position.x, 0)
        self.assertEqual(p1.position.y, 0)
        self.assertEqual(p1.position.z, 0)
        
        self.assertEqual(p1.rotation.x, 0)
        self.assertEqual(p1.rotation.y, 0)
        self.assertEqual(p1.rotation.z, 0)
        self.assertEqual(p1.rotation.w, 1)
        
        self.assertEqual(p1.scale.x, 1)
        self.assertEqual(p1.scale.y, 1)
        self.assertEqual(p1.scale.z, 1)

        p2 = Pose(position = Vector3(1,2,3), rotation = Quaternion(4,5,6,7), scale = Vector3(8,9,0))
        self.assertEqual(p2.position.x, 1)
        self.assertEqual(p2.position.y, 2)
        self.assertEqual(p2.position.z, 3)
        
        self.assertEqual(p2.rotation.x, 4)
        self.assertEqual(p2.rotation.y, 5)
        self.assertEqual(p2.rotation.z, 6)
        self.assertEqual(p2.rotation.w, 7)
        
        self.assertEqual(p2.scale.x, 8)
        self.assertEqual(p2.scale.y, 9)
        self.assertEqual(p2.scale.z, 0)

    def test_FromDict(self):
        j1 = '{"position" : {"x" : 0, "y" : 0, "z" : 0}, "rotation" : {"x" : 0, "y" : 0, "z" : 0, "w" : 1}, "scale" : {"x" : 1, "y" : 1, "z" : 1}}'
        p1 = Pose.FromDict(json.loads(j1))
        self.assertEqual(p1.position.x, 0)
        self.assertEqual(p1.position.y, 0)
        self.assertEqual(p1.position.z, 0)
        
        self.assertEqual(p1.rotation.x, 0)
        self.assertEqual(p1.rotation.y, 0)
        self.assertEqual(p1.rotation.z, 0)
        self.assertEqual(p1.rotation.w, 1)
        
        self.assertEqual(p1.scale.x, 1)
        self.assertEqual(p1.scale.y, 1)
        self.assertEqual(p1.scale.z, 1)
        
        j2 = '{"position" : {"x" : 1, "y" : 2, "z" : 3}, "rotation" : {"x" : 4, "y" : 5, "z" : 6, "w" : 7}, "scale" : {"x" : 8, "y" : 9, "z" : 0}}'
        p2 = Pose.FromDict(json.loads(j2))
        self.assertEqual(p2.position.x, 1)
        self.assertEqual(p2.position.y, 2)
        self.assertEqual(p2.position.z, 3)
        
        self.assertEqual(p2.rotation.x, 4)
        self.assertEqual(p2.rotation.y, 5)
        self.assertEqual(p2.rotation.z, 6)
        self.assertEqual(p2.rotation.w, 7)
        
        self.assertEqual(p2.scale.x, 8)
        self.assertEqual(p2.scale.y, 9)
        self.assertEqual(p2.scale.z, 0)

class TestColor(unittest.TestCase):
    def test_init(self):
        c1 = Color(1,1,1,1)
        self.assertAlmostEqual(c1.r, 1)
        self.assertAlmostEqual(c1.g, 1)
        self.assertAlmostEqual(c1.b, 1)
        self.assertAlmostEqual(c1.a, 1)
        
        c2 = Color(0,.25,.5,.75)
        self.assertAlmostEqual(c2.r, 0)
        self.assertAlmostEqual(c2.g, .25)
        self.assertAlmostEqual(c2.b, .5)
        self.assertAlmostEqual(c2.a, .75)

    def test_FromDict(self):
        j1 = '{"r" : 1, "g" : 1, "b" : 1, "a" : 1}'
        c1 = Color.FromDict(json.loads(j1))
        self.assertAlmostEqual(c1.r, 1)
        self.assertAlmostEqual(c1.g, 1)
        self.assertAlmostEqual(c1.b, 1)
        self.assertAlmostEqual(c1.a, 1)
        
        j2 = '{"r" : 0, "g" : 0.25, "b" : 0.5, "a" : 0.75}'
        c2 = Color.FromDict(json.loads(j2))
        self.assertAlmostEqual(c2.r, 0)
        self.assertAlmostEqual(c2.g, .25)
        self.assertAlmostEqual(c2.b, .5)
        self.assertAlmostEqual(c2.a, .75)

class TestJson(unittest.TestCase):
    def test_ToJson(self):
        v3 = Vector3(0,0,0)
        j1 = ToJson(v3)
        self.assertEqual(j1, b'{"x":0,"y":0,"z":0}')

        v2 = Vector2(1,1)
        j2 = ToJson(v2)
        self.assertEqual(j2, b'{"x":1,"y":1}')

        q1 = Quaternion(0,0,0,1)
        j3 = ToJson(q1)
        self.assertEqual(j3, b'{"x":0,"y":0,"z":0,"w":1}')
        
        p1 = Pose(position=Vector3(0,1,0),rotation=Quaternion(0,0,0,1),scale=Vector3(.5,.5,.5))
        p1string = b'{"position":{"x":0,"y":1,"z":0},"rotation":{"x":0,"y":0,"z":0,"w":1},"scale":{"x":0.5,"y":0.5,"z":0.5}}'
        j4 = ToJson(p1)
        self.assertEqual(j4, p1string)
        
        c1 = Color(.25,.5,.75,1)
        j5 = ToJson(c1)
        self.assertEqual(j5, b'{"r":0.25,"g":0.5,"b":0.75,"a":1}')

    def test_FromJson(self):
        v3 = FromJson('{"x":0,"y":0,"z":0}')
        v3 = Vector3.FromDict(v3)
        self.assertEqual(v3.x, 0)
        self.assertEqual(v3.y, 0)
        self.assertEqual(v3.z, 0)
        
        v2 = FromJson('{"x":1,"y":1}')
        v2 = Vector2.FromDict(v2)
        self.assertEqual(v2.x, 1)
        self.assertEqual(v2.y, 1)

        q1 = FromJson('{"x":0,"y":0,"z":0,"w":1}')
        q1 = Quaternion.FromDict(q1)
        self.assertEqual(q1.x, 0)
        self.assertEqual(q1.y, 0)
        self.assertEqual(q1.z, 0)
        self.assertEqual(q1.w, 1)
        
        p1 = FromJson('{"position":{"x":0,"y":1,"z":0},"rotation":{"x":0,"y":0,"z":0,"w":1},"scale":{"x":0.5,"y":0.5,"z":0.5}}')
        p1 = Pose.FromDict(p1)
        self.assertEqual(p1.position.x, 0)
        self.assertEqual(p1.position.y, 1)
        self.assertEqual(p1.position.z, 0)

        self.assertEqual(p1.rotation.x, 0)
        self.assertEqual(p1.rotation.y, 0)
        self.assertEqual(p1.rotation.z, 0)
        self.assertEqual(p1.rotation.w, 1)

        self.assertEqual(p1.scale.x, 0.5)
        self.assertEqual(p1.scale.y, 0.5)
        self.assertEqual(p1.scale.z, 0.5)
        
        c1 = FromJson('{"r":0.25,"g":0.5,"b":0.75,"a":1}')
        c1 = Color.FromDict(c1)
        self.assertEqual(c1.r, 0.25)
        self.assertEqual(c1.g, 0.5)
        self.assertEqual(c1.b, 0.75)
        self.assertEqual(c1.a, 1)