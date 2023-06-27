from cwruxr_sdk.client import Client
from cwruxr_sdk.common import Pose, Vector3, Quaternion
from cwruxr_sdk.object_message import PrimitiveMessage, PRIMITIVE_CUBE

ENDPOINT = "https://cwruxrstudents.azurewebsites.net/api/v2/"
ROOM_ID = "VI"
ANCHOR_ID = "test"

cwruxrClient = Client(ENDPOINT, ROOM_ID, ANCHOR_ID)

cube = PrimitiveMessage(
    id = "cube1",
    source = PRIMITIVE_CUBE,
    pose = Pose(
        position = Vector3(0, 1.25, 0),
        rotation = Quaternion(0,0,0,1),
        scale= Vector3(.1,.1,.1)),
    isManipulationOn = True,
)
    
createResponse = cwruxrClient.PostObject(cube)

input("Press Enter to Delete")

deleteResponse = cwruxrClient.DeleteObject(cube.id)