from cwruxr_sdk.common import *
from cwruxr_sdk.object_message import *
from cwruxr_sdk.client import *

ENDPOINT = "https://cwruxrstudents.azurewebsites.net/api/v2/"
ROOM_ID = "VI"
ANCHOR_ID = "test"

cwruxrClient : Client = Client(ENDPOINT, ROOM_ID, ANCHOR_ID)

end1 = PrimitiveMessage(
    id = "end1",
    source = PRIMITIVE_SPHERE,
    materialID = "Lit:White",
    pose = Pose(Vector3(0,1,-1),scale=Vector3(.1,.1,.1)),
    isManipulationOn=True
)
end2 = PrimitiveMessage(
    id = "end2",
    source = PRIMITIVE_SPHERE,
    materialID = "Lit:White",
    pose = Pose(Vector3(0,1,1),scale=Vector3(.1,.1,.1)),
    isManipulationOn=True
)
line = LineMessage(
    id = "line1",
    source = LINE_CYLINDER,
    params= LineParameters(
        startId="end1",
        endId="end2",
        width=0.01,
    ),
)

cwruxrClient.PostObjectBulk([end1,end2,line])

input("Press Enter to Delete")

deleteResponse = cwruxrClient.DeleteAllObjects()