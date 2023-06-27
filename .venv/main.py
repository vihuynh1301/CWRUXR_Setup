from cwruxr_sdk.common import *
from cwruxr_sdk.client import *
from cwruxr_sdk.object_message import *
from cwruxr_sdk.anchor_message import *
from cwruxr_sdk.material_message import *



ENDPOINT = "https://cwruxrstudents.azurewebsites.net/api/v2/"
ROOM_ID = "VI"
ANCHOR_ID = "test"

cwruxrClient = Client(ENDPOINT, ROOM_ID, ANCHOR_ID)

metalMaterial = MRTKMaterialMessage(
    id = "metalMat",
    color = Color(64,64,64,255),
    parameters = MRTKStandardParameters(
        metallic = 1,
        smoothness = .75,
        texture = TextureReference(
            source = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Grey_textured_cast_finish_clean_rough_seamless_metal_sheet_surface_texture.jpg/600px-Grey_textured_cast_finish_clean_rough_seamless_metal_sheet_surface_texture.jpg?20220827044816",
            tiling = Vector2(1,1),
            offset = Vector2(0,0)
        )
    ),
    render_settings= MaterialRenderSettings(
        blending = MaterialBlending(
            srcBlend = BLEND_ONE,
            dstBlend = BLEND_ZERO
        ),
        zwrite = True,
        cull = "Back",
        render_queue = 2000
    )
)

cwruxrClient.PostMaterial(metalMaterial)

sphere = PrimitiveMessage(
    id = "sphere1",
    source = PRIMITIVE_SPHERE,
    pose = Pose(
        position = Vector3(0, 1.25, 0),
        rotation = Quaternion(0,0,0,1),
        scale= Vector3(.25,.25,.25)),
    isManipulationOn = True,
    materialID = metalMaterial.id,
)
    
cwruxrClient.PostObject(sphere)

input("Press Enter to Delete")

deleteResponse = cwruxrClient.DeleteAllObjects()
deleteResponse = cwruxrClient.DeleteAllMaterials()
