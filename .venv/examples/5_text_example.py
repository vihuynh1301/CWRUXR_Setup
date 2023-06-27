from cwruxr_sdk.common import *
from cwruxr_sdk.object_message import *
from cwruxr_sdk.client import *

ENDPOINT = "https://cwruxrstudents.azurewebsites.net/api/v2/"
ROOM_ID = "VI"
ANCHOR_ID = "test"

cwruxrClient : Client = Client(ENDPOINT, ROOM_ID, ANCHOR_ID)

text_object = TextMessage(
    id = "end1",
    pose = Pose(
        position=Vector3(0,1,0),
        euler=Vector3(0,0,0),
        scale=Vector3(1,1,1)
    ),
    active = True,
    params = TextParameters(
        text = "Hello World",
        fontSize = 1,
        width= 2,
        height= 1,
        color= Color(255,255,0,255)
    )
)

cwruxrClient.PostObject(text_object)

input("Press Enter to Delete")

deleteResponse = cwruxrClient.DeleteAllObjects()