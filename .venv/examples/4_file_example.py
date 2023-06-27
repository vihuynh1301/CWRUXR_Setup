from cwruxr_sdk.client import Client
from cwruxr_sdk.common import Pose, Vector3, Quaternion, Euler
from cwruxr_sdk.object_message import FileMessage, ContainerMessage, Interpolation, ImageMessage, ImageParameters

ENDPOINT = "https://cwruxrstudents.azurewebsites.net/api/v2/"
ROOM_ID = "VI"
ANCHOR_ID = "test"

cwruxrClient = Client(ENDPOINT, ROOM_ID, ANCHOR_ID)

terrain_parent = ContainerMessage(
    id = "example_parent",
    pose = Pose(
        position = Vector3(0,0,0),
        rotation = Quaternion(0,0,0,1),
        scale = Vector3(1,1,1)
    ),
    active = True,
    isManipulationOn = False,
    interpolation = Interpolation(
        moveSpeed = 15,
        rotateSpeed = 15,
        scaleSpeed = 15
    )
)

terrain = FileMessage(
    id = "terrain",
    parentID = "example_parent",
    source = "http://url.to.terrain.fbx",
    active = True,
    walkable =  True,
    pose = Pose(
        position = Vector3(0,-0.5,0),
        rotation = Quaternion(0,0,0,1),
        scale = Vector3(1,1,1)
    )
)

map = ImageMessage(
    id = "map",
    parentID = "example_parent",
    source = "http://url.to.map.png",
    pose = Pose(
        position = Vector3(0,1,0),
        rotation = Euler(Vector3(90,0,0)),
        scale = Vector3(0.5,0.5,0.5)
    ),
    params = ImageParameters(
        updateRate = 0.1
    )
)

cwruxrClient.PostObjectBulk([terrain_parent, terrain, map])

input("Press Enter to Delete")

deleteResponse = cwruxrClient.DeleteAllObjects()