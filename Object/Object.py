
class Object:

    """Objects are any items that are placed in NEO's environment which it can interact with

    name: the name of the object, string value
    color: string of color name
    size: an integer length
    weight: an integer value
    position: x coordinate int value (y coordinates will be added later)
    """
    def __init__(self, name, color, weight, position):

        self.name = name
        self.color = color
        self.weight = weight
        self.position = position
