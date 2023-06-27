import string
from turtle import color
from typing import Optional

from cwruxr_sdk.common import Color, Vector2

class Parameters:
    """
    Parent class for all parameter types.
    """
    @classmethod
    def FromDict(cls, data: dict):
        """
        Method to create a Parameter from a dictionary.
        """
        if data == None:
            return cls()
            
        val = cls()
        for key in data.keys():
            setattr(val, key, data[key])
        return val

# Blending option cooresponding to Unity's Zero mode.
BLEND_ZERO = "Zero"
# Blending option cooresponding to Unity's One mode.
BLEND_ONE = "One"
# Blending option cooresponding to Unity's DstColor mode.
BLEND_DST_COLOR = "DstColor"
# Blending option cooresponding to Unity's SrcColor mode.
BLEND_SRC_COLOR ="SrcColor"
# Blending option cooresponding to Unity's OneMinusDstColor mode.
BLEND_ONE_MINUS_DST_COLOR ="OneMinusDstColor"
# Blending option cooresponding to Unity's SrcAlpha mode.
BLEND_SRC_ALPHA ="SrcAlpha"
# Blending option cooresponding to Unity's OneMinusSrcColor mode.
BLEND_ONE_MINUS_SRC_COLOR ="OneMinusSrcColor"
# Blending option cooresponding to Unity's DstAlpha mode.
BLEND_DST_ALPHA ="DstAlpha"
# Blending option cooresponding to Unity's OneMinusDstAlpha mode.
BLEND_ONE_MINUS_DST_ALPHA ="OneMinusDstAlpha"
# Blending option cooresponding to Unity's OneMinusSrcAlpha mode.
BLEND_ONE_MINUS_SRC_ALPHA ="OneMinusSrcAlpha"

class MaterialBlending:
    """
    Class defining how the foreground will render with the background for a material.
    """
    def __init__(
            self,
            srcBlend : str,
            dstBlend : str
        ):
        """
        Initialization function.

        Arguments:
        srcBlend -- The source blend, defining how to render this object.
        dstBlend -- The destination blend, defining how to render the background through this object.
        """
        self.srcBlend = srcBlend
        self.dstBlend = dstBlend

    @classmethod
    def FromDict(cls, data: dict):
        """
        Method to create a Material Blending instance from a dictionary.
        """
        if data == None:
            return cls()

        val = cls(data.get("srcBlend"), data.get("dstBlend"))
        return val

class MaterialRenderSettings:
    def __init__(
            self,
            blending : Optional[MaterialBlending] = None,
            zwrite : Optional[bool] = None,
            cull : Optional[str] = None,
            render_queue : Optional[int] = None
        ):
        """
        Initialization function.

        Arguments:
        blend -- The blending settings.
        zwrite -- Whether or not to render depth for this material.
        cull -- Culling options for this material, which determine what faces to render. Options are Front, Back, and Off.
        render_queue -- The order in which to render this material relative to others. ~2000 for opaque, and ~3000 for transparent. 
        """
        if blending != None:
            self.blending = blending
        if zwrite != None:
            self.zWrite = zwrite
        if cull != None:
            self.cull = cull
        if render_queue != None:
            self.renderQueue = render_queue

    @classmethod
    def FromDict(cls, data: dict):
        """
        Method to return a Metrial Render Settings instance from a dictionary.
        """
        if data == None:
            return cls()

        val = cls(
                zwrite = bool(data.get("zWrite")),
                cull = data.get("cull"),
                render_queue = data.get("renderQueue")
            )
        
        if data.get("blending") != None:
            val.blending = MaterialBlending.FromDict(data.get("blending"))

        return val

class MaterialMessage:
    """
    Class representing a generic material message.
    While this can be used, UnlitMaterialMessage and MRTKMaterialMessage provide an easier to use alternative.
    """
    def __init__(
            self,
            id : Optional[str],
            shader : str,
            color : Optional[Color],
            render_settings : Optional[MaterialRenderSettings] = None,
            parameters = None
        ):
        """
        Initialization function.

        Arguments:
        id -- The name of the material.
        shader -- Whether or not to render depth for this material.
        color -- The base color of the material.
        render_settings -- The render settings to use for this material. 
        parameters -- The shader specific parameters to use for this material.
        """
        if id != None:
            self.id = id
        self.shader = shader
        if color != None:
            self.color = color

        self.renderSettings = render_settings

        self.parameters = parameters
    
    @classmethod
    def FromDict(cls, data : dict):
        """
        Method to return a Material Message from a dictionary.
        """
        val = cls(
                id = data.get("id"),
                shader = data.get("shader"),
                color = Color.FromDict(data.get("color"))
            )
        
        if data.get("renderSettings") != None:
            val.renderSettings = MaterialRenderSettings.FromDict(data["renderSettings"])

        if data.get("parameters") != None:
            if val.shader.casefold() == "MrtkStandard".casefold():
                val.parameters = MRTKStandardParameters.FromDict(data["parameters"])
            elif val.shader.casefold() == "Unlit".casefold():
                val.parameters = UnlitParameters.FromDict(data["parameters"])
            else:
                val.parameters = Parameters.FromDict(data["parameters"])
        return val

class TextureReference():
    """
    Class to reference an external texture, and how to render it.
    """
    def __init__(
        self,
        source : Optional[str] = None,
        tiling : Optional[Vector2] = None,
        offset : Optional[Vector2] = None,
        lastUpdate : Optional[float] = None
    ):
        """
        Initialization function.

        Arguments:
        source -- The url to download this texture from.
        tiling -- How much to tile this texture.
        offset -- The amount to displace the texture.
        lastUpdate -- The last time this texture was changed. Changing this value causes the texture to be reloaded from the source.
        """
        if source != None:
            self.source = source
        if tiling != None:
            self.tiling = tiling
        if offset != None:
            self.offset = offset
        if lastUpdate != None:
            self.lastUpdate = lastUpdate
    
    @classmethod
    def FromDict(cls, data: dict):
        """
        Method to return a texture reference from a dictionary.
        """
        if data == None:
            return cls()
        val = cls(
            source = data.get("source"),
            tiling = Vector2.FromDict(data.get("tiling")),
            offset = Vector2.FromDict(data.get("offset")),
            lastUpdate = data.get("lastUpdate")
        )
        return val


class UnlitParameters(Parameters):
    """
    Extension to Parameters which supports the Unlit shader.
    """
    def __init__(
        self,
        alphaTest : Optional[bool] = None,
        alphaCutoff : Optional[float] = None,
        texture : Optional[TextureReference] = None,
    ):
        """
        Initialization function.

        Arguments:
        alphaTest -- Whether or not to use alpha test for this material.
        alphaCutoff -- The cutoff value to use when the material uses alpha test.
        texture -- The texture reference to use for the albedo.
        """
        if alphaTest != None:
            self.alphaTest = alphaTest
        if alphaCutoff != None:
            self.alphaCutoff = alphaCutoff
        if texture != None:
            self.texture = texture

    @classmethod
    def FromDict(cls, data: dict):
        """
        Method to return unlit parameters from a dictionary.
        """
        if data == None:
            return cls()
        val = cls()
        val.alphaTest = data.get("alphaTest")
        val.alphaCutoff = data.get("alphaCutoff")
        val.texture = TextureReference.FromDict(data.get("texture"))
        return val

class MRTKStandardParameters(Parameters):
    """
    Extension to Parameters which supports the MRTK shader.
    """
    def __init__(
        self,
        metallic : Optional[float] = None,
        smoothness : Optional[float] = None,
        emissiveColor : Optional[Color] = None,
        rimLightPower : Optional[float] = None,
        rimLightColor : Optional[Color] = None,
        texture : Optional[TextureReference] = None,
        triplanar : Optional[bool] = None
    ):
        """
        Initialization function.

        Arguments:
        metallic -- How metallic the material should appear.
        smoothness -- How smooth the material should appear.
        emissiveColor -- The color to use for emission. Ignores shading.
        rimLightPower -- How fast the rim light should falloff.
        rimLightColor -- The color to use for the fresnel outline.
        texture -- The texture reference to use for the albedo.
        triplanar -- Whether or not to render the texure with triplanar projection.
        """
        if metallic != None:
            self.metallic = metallic
        if smoothness != None:
            self.smoothness = smoothness
        if emissiveColor != None:
            self.emissiveColor = emissiveColor
        if rimLightPower != None:
            self.rimLightPower = rimLightPower
        if rimLightColor != None:
            self.rimLightColor = rimLightColor
        if texture != None:
            self.texture = texture
        if triplanar != None:
            self.triplanar = triplanar
    
    @classmethod
    def FromDict(cls, data: dict):
        """
        Method to return an MRTKStandardParameters from a dictionary.
        """
        if data == None:
            return cls()
        val = cls()
        val.metallic = float(data.get("metallic"))
        val.smoothness = float(data.get("smoothness"))
        val.rimLightPower = float(data.get("rimLightPower"))
        val.emissiveColor = Color.FromDict(data.get("emissiveColor"))
        val.rimLightColor = Color.FromDict(data.get("rimLightColor"))
        val.texture = TextureReference.FromDict(data.get("texture"))
        val.triplanar = bool(data.get("triplanar"))
        return val

class SkyboxParameters(Parameters):
    """
    Extension to parameters to handle skybox materials.
    """
    def __init__(
        self,
        exposure : Optional[bool],
        rotation : Optional[float]
    ):
        """
        Initialization function.

        Arguments:
        exposure -- The exposure to use for the texture.
        rotation -- The amount to rotation the texture. Use to line up the skybox to the scene.
        """
        if exposure != None:
            self.exposure = exposure
        if rotation != None:
            self.alphaCutoff = rotation

class UnlitMaterialMessage(MaterialMessage):
    """
    Extension to MaterialMessage to create Unlit Materials.
    """
    def __init__(
        self,
        id : Optional[str],
        color : Optional[Color],
        parameters : UnlitParameters,
        render_settings : Optional[MaterialRenderSettings] = None,
    ):
        """
        Initialization function.

        Arguments:
        id -- The name of the material.
        color -- The base color to use for the material.
        parameters -- The Unlit parameters to use for the material.
        render_settings -- The render settings to use for the material.      
        """
        super().__init__(
            id,
            "Unlit",
            color,
            render_settings,
            parameters,
            )

class MRTKMaterialMessage(MaterialMessage):
    """
    Extension to MaterialMessage to create MRTK Standard Materials.
    """
    def __init__(
        self,
        id : Optional[str],
        color : Optional[Color],
        parameters : MRTKStandardParameters,
        render_settings : Optional[MaterialRenderSettings] = None,
    ):
        """
        Initialization function.

        Arguments:
        id -- The name of the material.
        color -- The base color to use for the material.
        parameters -- The MRTK Standard parameters to use for the material.
        render_settings -- The render settings to use for the material.      
        """
        super().__init__(
            id,
            "MrtkStandard",
            color,
            render_settings,
            parameters,
            )

class SkyboxMaterialMessage(MaterialMessage):
    """
    Extension to MaterialMessage to create Skybox Materials.
    """
    def __init__(
        self,
        id : Optional[str],
        color : Optional[Color],
        parameters : SkyboxParameters,
        render_settings : Optional[MaterialRenderSettings] = None,
    ):
        """
        Initialization function.

        Arguments:
        id -- The name of the material.
        color -- The base color to use for the material.
        parameters -- The Skybox parameters to use for the material.
        render_settings -- The render settings to use for the material.      
        """
        super().__init__(
            id,
            "Skybox",
            color,
            render_settings,
            parameters,
            )