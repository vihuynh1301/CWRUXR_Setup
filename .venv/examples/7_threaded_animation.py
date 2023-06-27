from cwruxr_sdk.common import *
from cwruxr_sdk.object_message import *
from cwruxr_sdk.client import *
from threading import Thread
import math
import time

ENDPOINT = "https://cwruxrstudents.azurewebsites.net/api/v2/"
ROOM_ID = "VI"
ANCHOR_ID = "test"

cwruxrClient : Client = Client(ENDPOINT, ROOM_ID, ANCHOR_ID)

thread_running = True

def move_sphere():
    last_time = time.time()
    move_speed = 1
    t = 0
    while(thread_running):
        current_time = time.time()
        time_difference = current_time - last_time

        t += move_speed * time_difference

        sphere = PrimitiveMessage(
            id = "sphere1",
            source = PRIMITIVE_SPHERE,
            pose = Pose(
                position = Vector3(0, math.sin(t) * .5 + 1, 0),
                rotation = Quaternion(0,0,0,1),
                scale= Vector3(.1,.1,.1)),
            isManipulationOn = True,
            interpolation = Interpolation(
                on = True,
                moveSpeed = 5
            )
        )
        
        cwruxrClient.PostObject(sphere)
        last_time = current_time
        time.sleep(.2)

movement_thread = Thread(target = move_sphere)
movement_thread.start()

input("Press Enter to Delete")

thread_running = False
movement_thread.join()

deleteResponse = cwruxrClient.DeleteAllObjects()