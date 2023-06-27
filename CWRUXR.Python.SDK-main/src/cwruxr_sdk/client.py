from logging import exception
from typing import Optional, Any
import requests
from cwruxr_sdk.anchor_message import AnchorMessage
from cwruxr_sdk.common import FromJson, ToJson
from cwruxr_sdk.material_message import MaterialMessage
from cwruxr_sdk.object_message import ObjectMessage
from cwruxr_sdk import endpoints

class Client:
    """
    Client class which exposes methods for interacting with the api.
    """

    _endpointDefault = ""
    _roomIdDefault = ""
    _anchorIdDefault = ""

    _session = None

    def __init__(
            self,
            endpoint : str,
            roomId : str,
            anchorId : str
        ):
        """
        Initialization function.

        Arguments:
        endpoint -- The Api endpoint to connect to.
        roomId -- The Room to write to and read from.
        anchorId -- The anchor in the room to write to and read from.
        """
        if endpoint != None:
            self._endpointDefault = endpoint
        if roomId != None:
            self._roomIdDefault = roomId
        if anchorId != None:
            self._anchorIdDefault = anchorId
        self._session = requests.Session()

    ### POST ###
    def PostAnchor(
            self,
            message : AnchorMessage,
        ) -> requests.Response:
        """
        Post an anchor message to the API.
        """
        result = self._session.post(
            self._endpointDefault + endpoints.ANCHOR_ENDPOINT,
            data = ToJson(message),
            headers = { 
                    "Content-Type" : "application/json",
                    "RoomId" : self._roomIdDefault
                }
        )
        if result.status_code != 200:
            raise Exception(result.reason)
        return result

    def PostObject(
            self,
            message : ObjectMessage,
        ) -> requests.Response:
        """
        Post an object message to the API.
        """
        result = self._session.post(
            self._endpointDefault + endpoints.OBJECT_ENDPOINT,
            data = ToJson(message),
            headers = { 
                    "Content-Type" : "application/json",
                    "RoomId" : self._roomIdDefault,
                    "AnchorId" : self._anchorIdDefault
                }
        )
        if result.status_code != 200:
            raise Exception(result.reason)
        return result

    def PostObjectBulk(
            self,
            message,
        ) -> requests.Response:
        """
        Post a list of object messages to the API.
        """

        result = self._session.post(
            self._endpointDefault + endpoints.OBJECT_BULK_ENDPOINT,
            data = ToJson(message),
            headers = { 
                    "Content-Type" : "application/json",
                    "RoomId" : self._roomIdDefault,
                    "AnchorId" : self._anchorIdDefault
                }
        )
        if result.status_code != 200:
            raise Exception(result.reason)
        return result

    def PostMaterial(
            self,
            message : MaterialMessage,
        ) -> requests.Response:
        """
        Post a material message to the API.
        """

        data = ToJson(message)

        result = self._session.post(
            self._endpointDefault + endpoints.MATERIAL_ENDPOINT,
            data = data,
            headers = { 
                    "Content-Type" : "application/json",
                    "RoomId" : self._roomIdDefault
                }
        )
        if result.status_code != 200:
            raise Exception(result.reason)
        return result

    def PostMaterialBulk(
            self,
            message,
        ) -> requests.Response:
        """
        Post a list of material messages to the API.
        """

        result = self._session.post(
            self._endpointDefault + endpoints.MATERIAL_BULK_ENDPOINT,
            data = ToJson(message),
            headers = { 
                    "Content-Type" : "application/json",
                    "RoomId" : self._roomIdDefault
                }
        )
        if result.status_code != 200:
            raise Exception(result.reason)
        return result

    ### GET ###
    def GetAllAnchors(
            self,
        ) -> list[dict[str, Any]]:
        """
        Get all anchors for the room.
        """

        result = self._session.get(
            self._endpointDefault + endpoints.ANCHOR_ENDPOINT,
            headers = { 
                    "Content-Type" : "application/json",
                    "RoomId" : self._roomIdDefault
                }
        )
        if result.status_code != 200:
            raise Exception(result.reason)
        l = []
        for data in FromJson(result.content):
            l.append(data)
        return l
    
    def GetAnchor(
            self,
            id : str,
        ) -> dict[str, Any]:
        """
        Get an anchor in the room by the ID.
        """
        
        result = self._session.get(
            self._endpointDefault + endpoints.ANCHOR_ENDPOINT + id,
            headers = { 
                    "Content-Type" : "application/json",
                    "RoomId" : self._roomIdDefault
                }
        )
        if result.status_code != 200:
            raise Exception(result.reason)
        return FromJson(result.content)

    def GetAllObjects(
            self,
        ) -> list[dict[str, Any]]:
        """
        Get all objects under the anchor.
        """

        result = self._session.get(
            self._endpointDefault + endpoints.OBJECT_ENDPOINT,
            headers = { 
                    "Content-Type" : "application/json",
                    "RoomId" : self._roomIdDefault,
                    "AnchorId" : self._anchorIdDefault
                }
        )
        if result.status_code != 200:
            raise Exception(result.reason)
        l = []
        for data in FromJson(result.content):
            l.append(data)
        return l
    
    def GetObject(
            self,
            id : str,
        ) ->  dict[str, Any]:
        """
        Get an object under the anchor by its ID.
        """
        
        result = self._session.get(
            self._endpointDefault + endpoints.OBJECT_ENDPOINT + id,
            headers = { 
                    "Content-Type" : "application/json",
                    "RoomId" : self._roomIdDefault,
                    "AnchorId" : self._anchorIdDefault
                }
        )
        if result.status_code != 200:
            raise Exception(result.reason)
        data = FromJson(result.content)
        return data

    def GetAllMaterials(
            self,
        ) -> list[dict[str, Any]]:
        """
        Get all materials in the room.
        """

        result = self._session.get(
            self._endpointDefault + endpoints.MATERIAL_ENDPOINT,
            headers = { 
                    "Content-Type" : "application/json",
                    "RoomId" : self._roomIdDefault
                }
        )
        if result.status_code != 200:
            raise Exception(result.reason)
        l = []
        for data in FromJson(result.content):
            l.append(data)
        return l

    def GetMaterial(
            self,
            id : str
        ) ->  dict[str, Any]:
        """
        Get a material by the id.
        """
        
        result = self._session.get(
            self._endpointDefault + endpoints.MATERIAL_ENDPOINT + id,
            headers = { 
                    "Content-Type" : "application/json",
                    "RoomId" : self._roomIdDefault
                }
        )
        if result.status_code != 200:
            raise Exception(result.reason)
        data = FromJson(result.content)

        return data

    ### Delete ###
    def DeleteAllAnchors(
            self,
        ):
        """
        Delete all anchors in the room.
        """
        
        result = self._session.delete(
            self._endpointDefault + endpoints.ANCHOR_ENDPOINT,
            headers = { 
                    "Content-Type" : "application/json",
                    "RoomId" : self._roomIdDefault,
                    "AnchorId" : self._anchorIdDefault
                }
        )
        if result.status_code != 200:
            raise Exception(result.reason)
        pass

    def DeleteAnchor(
            self,
            id : str,
        ):
        """
        Delete an anchor with the given ID.
        """

        result = self._session.delete(
            self._endpointDefault + endpoints.ANCHOR_ENDPOINT + id,
            headers = { 
                    "Content-Type" : "application/json",
                    "RoomId" : self._roomIdDefault,
                    "AnchorId" : self._anchorIdDefault
                }
        )
        if result.status_code != 200:
            raise Exception(result.reason)
        pass

    def DeleteAllMaterials(
            self,
        ):
        """
        Delete all materials in this room.
        """

        result = self._session.delete(
            self._endpointDefault + endpoints.MATERIAL_ENDPOINT,
            headers = { 
                    "Content-Type" : "application/json",
                    "RoomId" : self._roomIdDefault,
                    "AnchorId" : self._anchorIdDefault
                }
        )
        if result.status_code != 200:
            raise Exception(result.reason)
        pass

    def DeleteMaterial(
            self,
            id : str,
        ):
        """
        Delete the material with the given ID.
        """

        result = self._session.delete(
            self._endpointDefault + endpoints.MATERIAL_ENDPOINT + id,
            headers = { 
                    "Content-Type" : "application/json",
                    "RoomId" : self._roomIdDefault
                }
        )
        if result.status_code != 200:
            raise Exception(result.reason)
        pass

    def DeleteAllObjects(
            self,
        ):
        """
        Delete all objects under the anchor.
        """
        
        result = self._session.delete(
            self._endpointDefault + endpoints.OBJECT_ENDPOINT,
            headers = { 
                    "Content-Type" : "application/json",
                    "RoomId" : self._roomIdDefault,
                    "AnchorId" : self._anchorIdDefault
                }
        )
        if result.status_code != 200:
            raise Exception(result.reason)
        pass

    def DeleteObjectBulk(
            self,
            ids : list[str]
        ):
        """
        Delete all objects with the given IDs.
        """
        result = self._session.delete(
            self._endpointDefault + endpoints.OBJECT_BULK_ENDPOINT,
            data = ToJson(ids),
            headers = { 
                    "Content-Type" : "application/json",
                    "RoomId" : self._roomIdDefault,
                    "AnchorId" : self._anchorIdDefault
                }
        )
        if result.status_code != 200:
            raise Exception(result.reason)
        pass

    def DeleteObject(
            self,
            id : str,
        ):
        """
        Delete the object with the given ID.
        """
        
        result = self._session.delete(
            self._endpointDefault + endpoints.OBJECT_ENDPOINT + id,
            headers = { 
                    "Content-Type" : "application/json",
                    "RoomId" : self._roomIdDefault,
                    "AnchorId" : self._anchorIdDefault
                }
        )
        if result.status_code != 200:
            raise Exception(result.reason)
        pass