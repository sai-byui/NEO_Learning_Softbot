
class Object:

    """Objects are any items that are placed in NEO's environment which it can interact with

    name: the name of the object, string value
    color: a rgb tuple (eg. (255,255,255))
    size: an integer length
    weight: an integer value
    position: x coordinate int value (y coordinates will be added later)
    """
    def __init__(self, name, color, size, weight, position):

        self.name = name
        self.color = color
        self.size = size
        self.weight = weight
        self.position = position
