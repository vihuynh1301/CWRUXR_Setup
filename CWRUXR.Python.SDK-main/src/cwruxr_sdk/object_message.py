from optparse import Option
from typing import Optional, Union
from cwruxr_sdk.common import Color, Pose

class Parameters:
    """
    Parent class for all object parameter classes.
    """
    @classmethod
    def FromDict(cls, data: dict):
        """
        Method to return object parameters from a dictionary.
        """
        if data == None:
            return cls()
        val = cls()
        for key in data.keys():
            setattr(val, key, data[key])
        return val

class Interpolation:
    """
    Class which defines how to interpolate the pose of an object.
    """
    def __init__(
            self,
            on : Optional[bool] = True,
            moveSpeed : Optional[float] = 15,
            rotateSpeed : Optional[float] = 10,
            scaleSpeed : Optional[float] = 15,
        ):
        """
        Initialization function.

        Arguments:
        on -- Whether or not to interpolate this object.
        moveSpeed -- How fast to interpolate this object's position.
        rotateSpeed -- How fast to interpolate this object's rotation.
        scaleSpeed -- How fast to interpolate this object's scale.
        """
        if(on != None):
            self.on = on
        if(moveSpeed != None):
            self.moveSpeed = moveSpeed
        if(rotateSpeed != None):
            self.rotateSpeed = rotateSpeed
        if(scaleSpeed != None):
            self.scaleSpeed = scaleSpeed
    
    @classmethod
    def FromDict(cls, data: dict):
        """
        Method to get interpolation settings from a dictionary.
        """
        if data == None:
            return cls()

        val = cls()
        for key in data.keys():
            setattr(val, key, data[key])
        return val


class ObjectMessage:
    """
    A message type which holds information about a single object under an anchor.
    """
    def __init__(
            self,
            id : Optional[str] = None,
            anchorID : Optional[str] = None,
            parentID : Optional[str] = None, 
            type : Optional[str] = None, 
            source : Optional[str] = None,
            active : Optional[bool] = None,
            materialID : Optional[str] = None,
            pose : Optional[Pose] = None,
            isManipulationOn : Optional[bool] = None,
            walkable : Optional[bool] = None,
            interpolation : Optional[Interpolation] = None,
        ):
        """
        Initialization function.

        Arguments:
        id -- The name of the object.
        anchorID -- The anchor to place this object under.
        parentID -- The id of the object to parent this object to.
        type -- The type of object that this object is.
        source -- The source to use for the object. Differs depending on the type.
        active -- Whether or not to render this object.
        materialID -- The name of the material to use for this object.
        pose -- The pose of this object. Contains the position, rotation, and scale.
        isManipulationOn -- Whether or not this object is grabbable and movable.
        walkable -- Whether or not to place object to below your feet.
        interpolation -- The interpolation settings to use for this object.
        """
        if id != None:
            self.id = id
        if anchorID != None:
            self.anchorID = anchorID
        if parentID != None:
            self.parentID = parentID
        if type != None:
            self.type = type
        if source != None:
            self.source = source
        if active != None:
            self.active = active
        if materialID != None:
            self.materialID = materialID
        if pose != None:
            self.pose = pose
        if isManipulationOn != None:
            self.isManipulationOn = isManipulationOn
        if walkable != None:
            self.walkable = walkable
        if interpolation != None:
            self.interpolation = interpolation
    
    @classmethod
    def FromDict(cls, data : dict):
        """
        Method to get an object message out of a dictionary.
        """
        if data == None:
            return cls()
            
        val = cls(
                data.get("id"),
                data.get("anchorID"),
                data.get("parentID"),
                data.get("type"),
                data.get("source"),
                data.get("active"),
                data.get("materialID"),
                Pose.FromDict(data.get("pose")),
                data.get("isManipulationOn"),
                data.get("walkable"),
                Interpolation.FromDict(data.get("interpolation")),
            )
        if data.get("isManipulating") != None:
            val.isManipulating = data["isManipulating"]
        if data.get("parameters") != None:
            val.parameters = Parameters.FromDict(data["parameters"])

        return val

class TextParameters(Parameters):
    """
    An extension to Parameters to use with Text object types.
    """
    def __init__(
            self,
            text : Optional[str] = None,
            fontSize : Optional[float] = None,
            width : Optional[float] = None,
            height : Optional[float] = None,
            color : Optional[Color] = None,
        ):
        """
        Initialization function.

        Arguments:
        text -- The text to display.
        fontSize -- The size for the displayed text.
        width -- The width of the box within which the text is displayed. Will determine when it wraps.
        height -- The height of the box within which the text is displayed.
        color -- The color of the text.
        """
        if text != None:
            self.text = text
        if fontSize != None:
            self.fontSize = fontSize
        if width != None:
            self.width = width
        if height != None:
            self.height = height
        if color != None:
            self.color = color

class LineParameters(Parameters):
    """
    An extension to Parameters to use with Line object types.
    """
    def __init__(
            self,
            startId : str,
            endId : str,
            width : Optional[float] = .01
        ):
        """
        Initialization function.

        Arguments:
        startId -- The name of the object to start the line from.
        endId -- The name of the object at the end of the line.
        width -- The width of the line.
        """
        self.startId = startId
        self.endId = endId
        self.width = width

class ImageParameters(Parameters):
    """
    A parameter class to be used for Image object types.
    """
    def __init__(
            self,
            updateRate : Optional[float] = None,
        ):
            
        """
        Initialization function.

        Arguments:
        updateRate -- The rate at which the image will be re-acquired.
        """
        if updateRate != None:
            self.updateRate = updateRate

class ContainerMessage(ObjectMessage):
    """
    A type of ObjectMessage which will have no visual.
    This is best used as a parent object, which will allow for groups of other objects to be transformed as one.
    """
    def __init__(
            self,
            id : Optional[str] = None,
            parentID : Optional[str] = None,
            pose : Optional[Pose] = None,
            active : Optional[bool] = None,
            isManipulationOn : Optional[bool] = None,
            interpolation : Optional[Interpolation] = None,
        ):
        """
        Initialization function.

        Arguments:
        id -- The name of the object.
        parentID -- The name of the object to parent this object to.
        pose -- The pose to display this object with.
        active -- The pose of this object. Contains the position, rotation, and scale.
        isManipulationOn -- Whether or not this object is grabbable and movable.
        interpolation -- The interpolation settings to use for this object.
        """
        super().__init__(
            id = id,
            type = "Container",
            parentID = parentID,
            pose = pose,
            active = active,
            isManipulationOn = isManipulationOn,
            interpolation = interpolation
        )

PRIMITIVE_CUBE = "Cube"
PRIMITIVE_SPHERE = "Sphere"
PRIMITIVE_CAPSULE = "Capsule"
PRIMITIVE_CYLINDER = "Cylinder"
PRIMITIVE_PLANE = "Plane"
PRIMITIVE_QUAD = "Quad"
PRIMITIVE_ARROW = "Arrow"
PRIMITIVE_HOOK = "Hook"
PRIMITIVE_DIAMOND = "Diamond"
PRIMITIVE_STAR = "Star"
PRIMITIVE_TORUS = "Torus"

class PrimitiveMessage(ObjectMessage):
    """
    A type of Object Message which will display a simple mesh.
    The "source" string will dictate what type of mesh will be displayed.
    PRIMITIVE_* constants are provided for all of the possible mesh types.
    """
    def __init__(
            self,
            id : Optional[str] = None,
            source : Optional[str] = PRIMITIVE_CUBE,
            parentID : Optional[str] = None,
            pose : Optional[Pose] = None,
            materialID : Optional[str] = None,
            active : Optional[bool] = None,
            isManipulationOn : Optional[bool] = None,
            interpolation : Optional[Interpolation] = None,
        ):
        """
        Initialization function.

        Arguments:
        id -- The name of the object.
        source -- The type of primitive to render. Use the "PRIMITIVE_XXXX" strings defined in this file.
        parentID -- The name of the object to parent this object to.
        pose -- The pose to display this object with.
        materialID -- The material to use for this object.
        active -- The pose of this object. Contains the position, rotation, and scale.
        isManipulationOn -- Whether or not this object is grabbable and movable.
        interpolation -- The interpolation settings to use for this object.
        """
        super().__init__(
                id = id,
                type = "Primitive",
                source = source,
                parentID = parentID,
                pose = pose,
                materialID=materialID,
                active = active,
                isManipulationOn = isManipulationOn,
                interpolation = interpolation,
            )

class TextMessage(ObjectMessage):
    """
    A type of ObjectMessage which will display a textbox.
    """
    def __init__(
            self,
            id : Optional[str] = None,
            parentID : Optional[str] = None,
            pose : Optional[Pose] = None, 
            active : Optional[bool] = None,
            params : Optional[TextParameters] = None,
            isManipulationOn : Optional[bool] = None,
            interpolation : Optional[Interpolation] = None,
        ):
        """
        Initialization function.

        Arguments:
        id -- The name of the object.
        parentID -- The name of the object to parent this object to.
        pose -- The pose to display this object with.
        active -- The pose of this object. Contains the position, rotation, and scale.
        params -- Parameters to use for rendering the text for this object.
        isManipulationOn -- Whether or not this object is grabbable and movable.
        interpolation -- The interpolation settings to use for this object.
        """
        super().__init__(
                id = id,
                parentID = parentID,
                pose = pose,
                active = active,
                type = "Text",
                isManipulationOn = isManipulationOn,
                interpolation = interpolation,
            )
        if params != None:
            self.parameters = params

LINE_CUBE = "Cube"
LINE_SPHERE = "Sphere"
LINE_CYLINDER = "Cylinder"
LINE_CAPSULE = "Capsule"
LINE_DEFAULT = ""

class LineMessage(ObjectMessage):
    """
    A type of ObjectMessage which will draw a line between two other objects.
    """
    def __init__(
            self,
            id : Optional[str] = None,
            source : Optional[str] = None,
            parentID : Optional[str] = None,
            active : Optional[bool] = None,
            params : Optional[LineParameters] = None,
            interpolation : Optional[Interpolation] = None,
        ):
        """
        Initialization function.

        Arguments:
        id -- The name of the object.
        source -- The type of line to render. Use the "LINE_XXXX" strings defined in this file.
        parentID -- The name of the object to parent this object to.
        active -- The pose of this object. Contains the position, rotation, and scale.
        params -- Parameters to use for rendering the line for this object.
        interpolation -- The interpolation settings to use for this object.
        """
        super().__init__(
                id = id,
                source = source,
                parentID = parentID,
                active = active,
                type="Line",
                isManipulationOn = False,
                interpolation = interpolation,
            )
        if params != None:
            self.parameters = params

class FileMessage(ObjectMessage):
    """
    A type of ObjectMessage which will load a model from an outside source.
    """
    def __init__(
            self,
            id : Optional[str] = None,
            parentID : Optional[str] = None,
            source : Optional[str] = None,
            pose : Optional[Pose] = None,
            materialID : Optional[str] = None,
            active : Optional[bool] = None,
            isManipulationOn : Optional[bool] = None,
            walkable : Optional[bool] = None,
            interpolation : Optional[Interpolation] = None,
        ):
        """
        Initialization function.

        Arguments:
        id -- The name of the object.
        parentID -- The name of the object to parent this object to.
        source -- The URL for the external file to load.
        pose -- The pose to display this object with.
        materialID -- The material to use with this object. Will override the default material, and if it has a texture it will also override the texture.
        active -- The pose of this object. Contains the position, rotation, and scale.
        isManipulationOn -- Whether or not this object is grabbable and movable.
        walkable -- Whether or not to place object to below your feet.
        interpolation -- The interpolation settings to use for this object.
        """
        super().__init__(
                id = id,
                parentID = parentID,
                type="File",
                source = source,
                materialID = materialID,
                pose=pose,
                active = active,
                isManipulationOn = isManipulationOn,
                walkable = walkable,
                interpolation = interpolation
            )

class AddressableMessage(ObjectMessage):
    """
    A type of ObjectMessage which will load an object from the Unity Addressables package.
    """
    def __init__(
            self,
            id : Optional[str] = None,
            parentID : Optional[str] = None,
            source : Optional[str] = None,
            pose : Optional[Pose] = None,
            materialID : Optional[str] = None,
            active : Optional[bool] = None,
            isManipulationOn : Optional[bool] = None,
            walkable : Optional[bool] = None,
            interpolation : Optional[Interpolation] = None,
        ):
        super().__init__(
                id = id,
                parentID = parentID,
                type="Addressable",
                source = source,
                materialID = materialID,
                pose=pose,
                active = active,
                isManipulationOn = isManipulationOn,
                walkable = walkable,
                interpolation = interpolation,
            )

class ImageMessage(ObjectMessage):
    """
    A type of ObjectMessage which will load an image from a url.
    """
    def __init__(
            self,
            id : Optional[str] = None,
            parentID : Optional[str] = None,
            source : Optional[str] = None,
            pose : Optional[Pose] = None,
            materialID : Optional[str] = None,
            active : Optional[bool] = None,
            params : Optional[ImageParameters] = None,
            isManipulationOn : Optional[bool] = None,
            interpolation : Optional[Interpolation] = None,
        ):
        """
        Initialization function.

        Arguments:
        id -- The name of the object.
        parentID -- The name of the object to parent this object to.
        source -- The URL for the external file to load.
        pose -- The pose to display this object with.
        materialID -- The material to use with this object. Will override the default material, and if it has a texture it will also override the texture.
        active -- The pose of this object. Contains the position, rotation, and scale.
        params -- The image parameters to use for rendering this object.
        isManipulationOn -- Whether or not this object is grabbable and movable.
        interpolation -- The interpolation settings to use for this object.
        """
        super().__init__(
                id = id,
                parentID = parentID,
                type="Image",
                source = source,
                materialID = materialID,
                pose=pose,
                active = active,
                isManipulationOn = isManipulationOn,
                interpolation = interpolation,
            )
        if params != None:
            self.parameters = params