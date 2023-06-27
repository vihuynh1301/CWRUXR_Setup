from time import sleep
import unittest
from cwruxr_sdk.material_message import *
import orjson as json

class TestMaterialBlending(unittest.TestCase):
    def test_init(self):
        blend1 = MaterialBlending(BLEND_ONE, BLEND_ZERO)
        self.assertEqual(blend1.srcBlend, BLEND_ONE)
        self.assertEqual(blend1.dstBlend, BLEND_ZERO)
        
        blend2 = MaterialBlending(BLEND_SRC_ALPHA, BLEND_ONE_MINUS_SRC_ALPHA)
        self.assertEqual(blend2.srcBlend, BLEND_SRC_ALPHA)
        self.assertEqual(blend2.dstBlend, BLEND_ONE_MINUS_SRC_ALPHA)

    def test_FromDict(self):
        j1 = '{"srcBlend":"One", "dstBlend":"Zero"}'
        b1 = MaterialBlending.FromDict(json.loads(j1))
        self.assertEqual(b1.srcBlend, BLEND_ONE)
        self.assertEqual(b1.dstBlend, BLEND_ZERO)
        
        j2 = '{"srcBlend":"SrcAlpha", "dstBlend":"OneMinusSrcAlpha"}'
        b2 = MaterialBlending.FromDict(json.loads(j2))
        self.assertEqual(b2.srcBlend, BLEND_SRC_ALPHA)
        self.assertEqual(b2.dstBlend, BLEND_ONE_MINUS_SRC_ALPHA)

class TestMaterialRenderSettings(unittest.TestCase):
    def test_init(self):
        b1 = MaterialBlending(BLEND_ONE, BLEND_ZERO)
        r1 = MaterialRenderSettings(b1, True, "Back", 3000)

        self.assertEqual(r1.blending.srcBlend, BLEND_ONE)
        self.assertEqual(r1.blending.dstBlend, BLEND_ZERO)
        self.assertEqual(r1.zWrite, True)
        self.assertEqual(r1.cull, "Back")
        self.assertEqual(r1.renderQueue, 3000)

        b2 = MaterialBlending(BLEND_SRC_ALPHA, BLEND_ONE_MINUS_SRC_ALPHA)
        r2 = MaterialRenderSettings(b2, False, "Off", 2000)

        self.assertEqual(r2.blending.srcBlend, BLEND_SRC_ALPHA)
        self.assertEqual(r2.blending.dstBlend, BLEND_ONE_MINUS_SRC_ALPHA)
        self.assertEqual(r2.zWrite, False)
        self.assertEqual(r2.cull, "Off")
        self.assertEqual(r2.renderQueue, 2000)

    def test_FromDict(self):
        j1 = '{"blending":{"srcBlend":"One","dstBlend":"Zero"},"zWrite":true,"cull":"Back","renderQueue":3000}'
        m1 = MaterialRenderSettings.FromDict(json.loads(j1))

        self.assertEqual(m1.blending.srcBlend, BLEND_ONE)
        self.assertEqual(m1.blending.dstBlend, BLEND_ZERO)
        self.assertEqual(m1.zWrite, True)
        self.assertEqual(m1.cull, "Back")
        self.assertEqual(m1.renderQueue, 3000)
        
        j2 = '{"blending":{"srcBlend":"SrcAlpha","dstBlend":"OneMinusSrcAlpha"},"zWrite":false,"cull":"Off","renderQueue":2000}'
        m2 = MaterialRenderSettings.FromDict(json.loads(j2))

        self.assertEqual(m2.blending.srcBlend, BLEND_SRC_ALPHA)
        self.assertEqual(m2.blending.dstBlend, BLEND_ONE_MINUS_SRC_ALPHA)
        self.assertEqual(m2.zWrite, False)
        self.assertEqual(m2.cull, "Off")
        self.assertEqual(m2.renderQueue, 2000)

class TestMaterialMessage(unittest.TestCase):
    def test_init(self):
        m1 = MaterialMessage(
            0,
            "MRTKStandard",
            Color(255,255,255,255),
            MaterialRenderSettings(
                MaterialBlending(BLEND_ONE,BLEND_ZERO),
                True,
                "Back",
                render_queue=3000
            ),
            MRTKStandardParameters(
                1,
                1,
                Color(255,0,0,255),
                4,
                Color(0,255,0,255),
                TextureReference("source", Vector2(1,1), Vector2(0,0),0),
                False
            )
        )

        self.assertEqual(m1.id, 0)
        self.assertEqual(m1.shader, "MRTKStandard")
        self.assertEqual(m1.color.r, 255)
        self.assertEqual(m1.color.g, 255)
        self.assertEqual(m1.color.b, 255)
        self.assertEqual(m1.color.a, 255)
        self.assertEqual(m1.renderSettings.blending.srcBlend, BLEND_ONE)
        self.assertEqual(m1.renderSettings.blending.dstBlend, BLEND_ZERO)
        self.assertEqual(m1.renderSettings.zWrite, True)
        self.assertEqual(m1.renderSettings.cull, "Back")
        self.assertEqual(m1.renderSettings.renderQueue, 3000)
        self.assertEqual(m1.parameters.metallic, 1)
        self.assertEqual(m1.parameters.smoothness, 1)
        self.assertEqual(m1.parameters.emissiveColor.r, 255)
        self.assertEqual(m1.parameters.emissiveColor.g, 0)
        self.assertEqual(m1.parameters.emissiveColor.b, 0)
        self.assertEqual(m1.parameters.emissiveColor.a, 255)
        self.assertEqual(m1.parameters.rimLightPower, 4)
        self.assertEqual(m1.parameters.rimLightColor.r, 0)
        self.assertEqual(m1.parameters.rimLightColor.g, 255)
        self.assertEqual(m1.parameters.rimLightColor.b, 0)
        self.assertEqual(m1.parameters.rimLightColor.a, 255)
        self.assertEqual(m1.parameters.texture.source, "source")
        self.assertEqual(m1.parameters.texture.tiling, Vector2(1,1))
        self.assertEqual(m1.parameters.texture.offset, Vector2(0,0))
        self.assertEqual(m1.parameters.texture.lastUpdate, 0)
        self.assertEqual(m1.parameters.triplanar, False)
        
        m2 = MaterialMessage(
            1,
            "Unlit",
            Color(0,0,255,255),
            MaterialRenderSettings(
                MaterialBlending(BLEND_SRC_ALPHA,BLEND_ONE_MINUS_SRC_ALPHA),
                False,
                "Off",
                render_queue=2000
            ),
            UnlitParameters(
                True, .5, None
            )
        )

        self.assertEqual(m2.id, 1)
        self.assertEqual(m2.shader, "Unlit")
        self.assertEqual(m2.color.r, 0)
        self.assertEqual(m2.color.g, 0)
        self.assertEqual(m2.color.b, 255)
        self.assertEqual(m2.color.a, 255)
        self.assertEqual(m2.renderSettings.blending.srcBlend, BLEND_SRC_ALPHA)
        self.assertEqual(m2.renderSettings.blending.dstBlend, BLEND_ONE_MINUS_SRC_ALPHA)
        self.assertEqual(m2.renderSettings.zWrite, False)
        self.assertEqual(m2.renderSettings.cull, "Off")
        self.assertEqual(m2.renderSettings.renderQueue, 2000)
        self.assertEqual(m2.parameters.alphaTest, True)
        self.assertEqual(m2.parameters.alphaCutoff, 0.5)

    def test_FromDict(self):
        j1 = '{"id":"mat1","shader":"MrtkStandard","color":{"r":255,"g":128,"b":255,"a":128},"renderSettings":{"blending":{"srcBlend":"One","dstBlend":"Zero"},"zWrite":true,"cull":"Back","renderQueue":2000},"parameters":{"metallic":1.0,"smoothness":1.0,"emissiveColor":{"r":255,"g":255,"b":255,"a":255},"rimLightPower":4,"rimLightColor":{"r":255,"g":255,"b":255,"a":255},"texture":{"source":"http://www.google.com","tiling":{"x":1,"y":1},"offset":{"x":0.5,"y":0.5}},"triplanar":false}}'
        m1 = MaterialMessage.FromDict(json.loads(j1))

        self.assertEqual(m1.id, "mat1")
        self.assertEqual(m1.shader, "MrtkStandard")
        self.assertEqual(m1.color.r, 255)
        self.assertEqual(m1.color.g, 128)
        self.assertEqual(m1.color.b, 255)
        self.assertEqual(m1.color.a, 128)
        self.assertEqual(m1.renderSettings.blending.srcBlend, BLEND_ONE)
        self.assertEqual(m1.renderSettings.blending.dstBlend, BLEND_ZERO)
        self.assertEqual(m1.renderSettings.zWrite, True)
        self.assertEqual(m1.renderSettings.cull, "Back")
        self.assertEqual(m1.renderSettings.renderQueue, 2000)
        self.assertEqual(m1.parameters.metallic, 1)
        self.assertEqual(m1.parameters.smoothness, 1)
        self.assertEqual(m1.parameters.emissiveColor.r, 255)
        self.assertEqual(m1.parameters.emissiveColor.g, 255)
        self.assertEqual(m1.parameters.emissiveColor.b, 255)
        self.assertEqual(m1.parameters.emissiveColor.a, 255)
        self.assertEqual(m1.parameters.rimLightPower, 4)
        self.assertEqual(m1.parameters.rimLightColor.r, 255)
        self.assertEqual(m1.parameters.rimLightColor.g, 255)
        self.assertEqual(m1.parameters.rimLightColor.b, 255)
        self.assertEqual(m1.parameters.rimLightColor.a, 255)
        self.assertEqual(m1.parameters.texture.source, "http://www.google.com")
        self.assertEqual(m1.parameters.texture.tiling, Vector2(1,1))
        self.assertEqual(m1.parameters.texture.offset, Vector2(0.5,0.5))
        self.assertEqual(m1.parameters.triplanar, False)
        
        j2 = '{"id":"mat2","shader":"Unlit","color":{"r":0,"g":0,"b":255,"a":255},"renderSettings":{"blending":{"srcBlend":"SrcAlpha","dstBlend":"OneMinusSrcAlpha"},"zWrite":false,"cull":"Off","renderQueue":3000},"parameters":{"alphaTest":true,"alphaCutoff":0.5,"texture":{"source":"http://www.test.com","tiling":{"x":2,"y":2},"offset":{"x":0,"y":0}}}}'
        m2 = MaterialMessage.FromDict(json.loads(j2))

        self.assertEqual(m2.id, "mat2")
        self.assertEqual(m2.shader, "Unlit")
        self.assertEqual(m2.color.r, 0)
        self.assertEqual(m2.color.g, 0)
        self.assertEqual(m2.color.b, 255)
        self.assertEqual(m2.color.a, 255)
        self.assertEqual(m2.renderSettings.blending.srcBlend, BLEND_SRC_ALPHA)
        self.assertEqual(m2.renderSettings.blending.dstBlend, BLEND_ONE_MINUS_SRC_ALPHA)
        self.assertEqual(m2.renderSettings.zWrite, False)
        self.assertEqual(m2.renderSettings.cull, "Off")
        self.assertEqual(m2.renderSettings.renderQueue, 3000)
        self.assertEqual(m2.parameters.alphaTest, True)
        self.assertEqual(m2.parameters.alphaCutoff, 0.5)
        self.assertEqual(m2.parameters.texture.source, "http://www.test.com")
        self.assertEqual(m2.parameters.texture.tiling, Vector2(2,2))
        self.assertEqual(m2.parameters.texture.offset, Vector2(0,0))

class TestTextureReference(unittest.TestCase):
    def test_init(self):
        t1 = TextureReference("source", Vector2(1,1), Vector2(0,0))
        self.assertEqual(t1.source, "source")
        self.assertEqual(t1.tiling.x, 1)
        self.assertEqual(t1.tiling.y, 1)
        self.assertEqual(t1.offset.x, 0)
        self.assertEqual(t1.offset.y, 0)
        
        t1 = TextureReference("source2", Vector2(2,2), Vector2(0.5,0.5))
        self.assertEqual(t1.source, "source2")
        self.assertEqual(t1.tiling.x, 2)
        self.assertEqual(t1.tiling.y, 2)
        self.assertEqual(t1.offset.x, 0.5)
        self.assertEqual(t1.offset.y, 0.5)

    def test_FromDict(self):
        j1 = '{"source":"s1","tiling":{"x":1.0,"y":1.0},"offset":{"x":0,"y":0}}'
        t1 = TextureReference.FromDict(json.loads(j1))

        self.assertEqual(t1.source, "s1")
        self.assertEqual(t1.tiling.x, 1)
        self.assertEqual(t1.tiling.y, 1)
        self.assertEqual(t1.offset.x, 0)
        self.assertEqual(t1.offset.y, 0)
        
        j2 = '{"source":"s2","tiling":{"x":2.0,"y":2.0},"offset":{"x":0.5,"y":0.5}}'
        t2 = TextureReference.FromDict(json.loads(j2))

        self.assertEqual(t2.source, "s2")
        self.assertEqual(t2.tiling.x, 2)
        self.assertEqual(t2.tiling.y, 2)
        self.assertEqual(t2.offset.x, 0.5)
        self.assertEqual(t2.offset.y, 0.5)

class TestUnlitParameters(unittest.TestCase):
    def test_init(self):
        p1 = UnlitParameters(True, 0.5, TextureReference("source", Vector2(1,1), Vector2(0,0)))
        self.assertTrue(p1.alphaTest)
        self.assertEqual(p1.alphaCutoff, 0.5)
        self.assertEqual(p1.texture.source, "source")
        self.assertEqual(p1.texture.tiling.x, 1)
        self.assertEqual(p1.texture.tiling.y, 1)
        self.assertEqual(p1.texture.offset.x, 0)
        self.assertEqual(p1.texture.offset.y, 0)

        p2 = UnlitParameters(False, 1.0, TextureReference("source2", Vector2(2,2), Vector2(0.5,0.5)))
        self.assertFalse(p2.alphaTest)
        self.assertEqual(p2.alphaCutoff, 1.0)
        self.assertEqual(p2.texture.source, "source2")
        self.assertEqual(p2.texture.tiling.x, 2)
        self.assertEqual(p2.texture.tiling.y, 2)
        self.assertEqual(p2.texture.offset.x, 0.5)
        self.assertEqual(p2.texture.offset.y, 0.5)

    def test_FromDict(self):
        j1 = '{"alphaTest":true,"alphaCutoff":0.5,"texture":{"source":"s1","tiling":{"x":1.0,"y":1.0},"offset":{"x":0,"y":0}}}'
        p1 = UnlitParameters.FromDict(json.loads(j1))
        self.assertTrue(p1.alphaTest)
        self.assertEqual(p1.alphaCutoff, 0.5)
        self.assertEqual(p1.texture.source, "s1")
        self.assertEqual(p1.texture.tiling.x, 1)
        self.assertEqual(p1.texture.tiling.y, 1)
        self.assertEqual(p1.texture.offset.x, 0)
        self.assertEqual(p1.texture.offset.y, 0)
        
        j2 = '{"alphaTest":false,"alphaCutoff":1.0,"texture":{"source":"s2","tiling":{"x":2.0,"y":2.0},"offset":{"x":0.5,"y":0.5}}}'
        p2 = UnlitParameters.FromDict(json.loads(j2))
        self.assertFalse(p2.alphaTest)
        self.assertEqual(p2.alphaCutoff, 1.0)
        self.assertEqual(p2.texture.source, "s2")
        self.assertEqual(p2.texture.tiling.x, 2)
        self.assertEqual(p2.texture.tiling.y, 2)
        self.assertEqual(p2.texture.offset.x, 0.5)
        self.assertEqual(p2.texture.offset.y, 0.5)

class TestMRTKStandardParameters(unittest.TestCase):
    def test_init(self):
        p1 = MRTKStandardParameters(1.0,1.0,Color(255,255,255,255),4,Color(255,255,255,255),TextureReference("source", Vector2(1,1), Vector2(0,0)),False)
        
        self.assertEqual(p1.metallic, 1.0)
        self.assertEqual(p1.smoothness, 1.0)
        self.assertEqual(p1.emissiveColor.r, 255)
        self.assertEqual(p1.emissiveColor.g, 255)
        self.assertEqual(p1.emissiveColor.b, 255)
        self.assertEqual(p1.emissiveColor.a, 255)
        self.assertEqual(p1.rimLightPower, 4)
        self.assertEqual(p1.rimLightColor.r, 255)
        self.assertEqual(p1.rimLightColor.g, 255)
        self.assertEqual(p1.rimLightColor.b, 255)
        self.assertEqual(p1.rimLightColor.a, 255)
        self.assertEqual(p1.texture.source, "source")
        self.assertEqual(p1.texture.tiling.x, 1)
        self.assertEqual(p1.texture.tiling.y, 1)
        self.assertEqual(p1.texture.offset.x, 0)
        self.assertEqual(p1.texture.offset.y, 0)
        self.assertEqual(p1.triplanar, False)
        
        p1 = MRTKStandardParameters(0.5,0.5,Color(128,0,128,64),2,Color(64,128,32,64),TextureReference("source2", Vector2(2,2), Vector2(0.5,0.5)),True)
        
        self.assertEqual(p1.metallic, 0.5)
        self.assertEqual(p1.smoothness, 0.5)
        self.assertEqual(p1.emissiveColor.r, 128)
        self.assertEqual(p1.emissiveColor.g, 0)
        self.assertEqual(p1.emissiveColor.b, 128)
        self.assertEqual(p1.emissiveColor.a, 64)
        self.assertEqual(p1.rimLightPower, 2)
        self.assertEqual(p1.rimLightColor.r, 64)
        self.assertEqual(p1.rimLightColor.g, 128)
        self.assertEqual(p1.rimLightColor.b, 32)
        self.assertEqual(p1.rimLightColor.a, 64)
        self.assertEqual(p1.texture.source, "source2")
        self.assertEqual(p1.texture.tiling.x, 2)
        self.assertEqual(p1.texture.tiling.y, 2)
        self.assertEqual(p1.texture.offset.x, 0.5)
        self.assertEqual(p1.texture.offset.y, 0.5)
        self.assertEqual(p1.triplanar, True)
        
    def test_FromDict(self):
        j1 = '{"metallic":1.0,"smoothness":1.0,"emissiveColor":{"r":255,"g":255,"b":255,"a":255},"rimLightPower":4,"rimLightColor":{"r":255,"g":255,"b":255,"a":255},"triplanar":true,"texture":{"source":"s1","tiling":{"x":1.0,"y":1.0},"offset":{"x":0,"y":0}}}'
        p1 = MRTKStandardParameters.FromDict(json.loads(j1))
        self.assertEqual(p1.metallic, 1.0)
        self.assertEqual(p1.smoothness, 1.0)
        self.assertEqual(p1.emissiveColor.r, 255)
        self.assertEqual(p1.emissiveColor.g, 255)
        self.assertEqual(p1.emissiveColor.b, 255)
        self.assertEqual(p1.emissiveColor.a, 255)

        self.assertEqual(p1.rimLightPower, 4)
        self.assertEqual(p1.rimLightColor.r, 255)
        self.assertEqual(p1.rimLightColor.g, 255)
        self.assertEqual(p1.rimLightColor.b, 255)
        self.assertEqual(p1.rimLightColor.a, 255)
        
        self.assertEqual(p1.texture.source, "s1")
        self.assertEqual(p1.texture.tiling.x, 1)
        self.assertEqual(p1.texture.tiling.y, 1)
        self.assertEqual(p1.texture.offset.x, 0)
        self.assertEqual(p1.texture.offset.y, 0)
        self.assertEqual(p1.triplanar, True)
        
        j2 = '{"metallic":0.5,"smoothness":0.5,"emissiveColor":{"r":128,"g":0,"b":128,"a":0},"rimLightPower":2,"rimLightColor":{"r":32,"g":64,"b":128,"a":0},"triplanar":false,"texture":{"source":"s2","tiling":{"x":2.0,"y":2.0},"offset":{"x":0.5,"y":0.5}}}'
        p2 = MRTKStandardParameters.FromDict(json.loads(j2))
        self.assertEqual(p2.metallic, 0.5)
        self.assertEqual(p2.smoothness, 0.5)
        self.assertEqual(p2.emissiveColor.r, 128)
        self.assertEqual(p2.emissiveColor.g, 0)
        self.assertEqual(p2.emissiveColor.b, 128)
        self.assertEqual(p2.emissiveColor.a, 0)

        self.assertEqual(p2.rimLightPower, 2)
        self.assertEqual(p2.rimLightColor.r, 32)
        self.assertEqual(p2.rimLightColor.g, 64)
        self.assertEqual(p2.rimLightColor.b, 128)
        self.assertEqual(p2.rimLightColor.a, 0)
        
        self.assertEqual(p2.texture.source, "s2")
        self.assertEqual(p2.texture.tiling.x, 2)
        self.assertEqual(p2.texture.tiling.y, 2)
        self.assertEqual(p2.texture.offset.x, 0.5)
        self.assertEqual(p2.texture.offset.y, 0.5)
        self.assertEqual(p2.triplanar, False)

class TestSkyboxParameters(unittest.TestCase):
    def test_init(self):
        self.skipTest("Not Yet Implemented")

class TestUnlitMaterialMessage(unittest.TestCase):
    def test_init(self):
        m1 = UnlitMaterialMessage("mat1", Color(255,255,255,255),UnlitParameters(True, 0.5, TextureReference("s1", Vector2(1,1), Vector2(0,0))))
        self.assertEqual(m1.id, "mat1")
        self.assertEqual(m1.color.r, 255)
        self.assertEqual(m1.color.g, 255)
        self.assertEqual(m1.color.b, 255)
        self.assertEqual(m1.color.a, 255)
        self.assertEqual(m1.parameters.alphaTest, True)
        self.assertEqual(m1.parameters.alphaCutoff, 0.5)
        self.assertEqual(m1.parameters.texture.source, "s1")
        self.assertEqual(m1.parameters.texture.tiling.x, 1)
        self.assertEqual(m1.parameters.texture.tiling.y, 1)
        self.assertEqual(m1.parameters.texture.offset.x, 0)
        self.assertEqual(m1.parameters.texture.offset.y, 0)

        m2 = UnlitMaterialMessage("mat2", Color(128,64,32,16),UnlitParameters(False, 1.0, TextureReference("s2", Vector2(2,2), Vector2(0.5,0.5))))
        self.assertEqual(m2.id, "mat2")
        self.assertEqual(m2.color.r, 128)
        self.assertEqual(m2.color.g, 64)
        self.assertEqual(m2.color.b, 32)
        self.assertEqual(m2.color.a, 16)
        self.assertEqual(m2.parameters.alphaTest, False)
        self.assertEqual(m2.parameters.alphaCutoff, 1)
        self.assertEqual(m2.parameters.texture.source, "s2")
        self.assertEqual(m2.parameters.texture.tiling.x, 2)
        self.assertEqual(m2.parameters.texture.tiling.y, 2)
        self.assertEqual(m2.parameters.texture.offset.x, 0.5)
        self.assertEqual(m2.parameters.texture.offset.y, 0.5)

class TestMRTKMaterialMessage(unittest.TestCase):
    def test_init(self):
        m1 = UnlitMaterialMessage("mat1", Color(255,255,255,255),MRTKStandardParameters(1.0,1.0,Color(255,255,255,255),4,Color(255,255,255,255),TextureReference("source", Vector2(1,1), Vector2(0,0)),False))
        self.assertEqual(m1.id, "mat1")
        self.assertEqual(m1.color.r, 255)
        self.assertEqual(m1.color.g, 255)
        self.assertEqual(m1.color.b, 255)
        self.assertEqual(m1.color.a, 255)
        self.assertEqual(m1.parameters.metallic, 1.0)
        self.assertEqual(m1.parameters.smoothness, 1.0)
        self.assertEqual(m1.parameters.emissiveColor.r, 255)
        self.assertEqual(m1.parameters.emissiveColor.g, 255)
        self.assertEqual(m1.parameters.emissiveColor.b, 255)
        self.assertEqual(m1.parameters.emissiveColor.a, 255)
        self.assertEqual(m1.parameters.rimLightPower, 4)
        self.assertEqual(m1.parameters.rimLightColor.r, 255)
        self.assertEqual(m1.parameters.rimLightColor.g, 255)
        self.assertEqual(m1.parameters.rimLightColor.b, 255)
        self.assertEqual(m1.parameters.rimLightColor.a, 255)
        self.assertEqual(m1.parameters.texture.source, "source")
        self.assertEqual(m1.parameters.texture.tiling.x, 1)
        self.assertEqual(m1.parameters.texture.tiling.y, 1)
        self.assertEqual(m1.parameters.texture.offset.x, 0)
        self.assertEqual(m1.parameters.texture.offset.y, 0)
        self.assertEqual(m1.parameters.triplanar, False)

        m2 = UnlitMaterialMessage("mat2", Color(128,64,32,16),MRTKStandardParameters(0.5,0.5,Color(128,0,128,64),2,Color(64,128,32,64),TextureReference("source2", Vector2(2,2), Vector2(0.5,0.5)),True))
        
        self.assertEqual(m2.id, "mat2")
        self.assertEqual(m2.color.r, 128)
        self.assertEqual(m2.color.g, 64)
        self.assertEqual(m2.color.b, 32)
        self.assertEqual(m2.color.a, 16)
        self.assertEqual(m2.parameters.metallic, 0.5)
        self.assertEqual(m2.parameters.smoothness, 0.5)
        self.assertEqual(m2.parameters.emissiveColor.r, 128)
        self.assertEqual(m2.parameters.emissiveColor.g, 0)
        self.assertEqual(m2.parameters.emissiveColor.b, 128)
        self.assertEqual(m2.parameters.emissiveColor.a, 64)
        self.assertEqual(m2.parameters.rimLightPower, 2)
        self.assertEqual(m2.parameters.rimLightColor.r, 64)
        self.assertEqual(m2.parameters.rimLightColor.g, 128)
        self.assertEqual(m2.parameters.rimLightColor.b, 32)
        self.assertEqual(m2.parameters.rimLightColor.a, 64)
        self.assertEqual(m2.parameters.texture.source, "source2")
        self.assertEqual(m2.parameters.texture.tiling.x, 2)
        self.assertEqual(m2.parameters.texture.tiling.y, 2)
        self.assertEqual(m2.parameters.texture.offset.x, 0.5)
        self.assertEqual(m2.parameters.texture.offset.y, 0.5)
        self.assertEqual(m2.parameters.triplanar, True)

class TestSkyboxMaterialMessage(unittest.TestCase):
    def test_init(self):
        self.skipTest("Not Yet Implemented")