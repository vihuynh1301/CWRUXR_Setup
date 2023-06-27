from cwruxr_sdk.client import Client

ENDPOINT = "https://cwruxrstudents.azurewebsites.net/api/v2/"
ROOM_ID = "VI"
ANCHOR_ID = "test"

cwruxrClient = Client(ENDPOINT, ROOM_ID, ANCHOR_ID)

allObjects = cwruxrClient.GetAllObjects()
print(allObjects)