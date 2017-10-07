from enum import Enum

from neo_body.agent import Agent


class Memory(Agent):
    """Keeps track of objects NEO has interacted with and their associations based on attributes"""

    def __init__(self):
        """default constructor"""
        super(Memory, self).__init__("memory")
        self.colors = {}
        self.create_color_categories()
        self.weights = {}
        self.create_weight_categories()

    def create_color_categories(self):
        for color_name in Color:
            self.colors[color_name] = color_name.value

    def create_weight_categories(self):
        for weight_category in Weight:
            self.weights[weight_category] = weight_category.value



class Color(Enum):
    RED = ((230, 0, 0), (255, 20, 20))
    BLUE = ((0, 0, 145), (40, 40, 255))
    GREEN = ((0, 100, 0), (65, 100, 65))

LIGHT_MIN_WEIGHT = 0.1
LIGHT_MAX_WEIGHT = 20
HEAVY_MIN_WEIGHT = 20
HEAVY_MAX_WEIGHT = 1000


class Weight(Enum):
    LIGHT = (LIGHT_MIN_WEIGHT, LIGHT_MAX_WEIGHT)
    HEAVY = (HEAVY_MIN_WEIGHT, HEAVY_MAX_WEIGHT)


