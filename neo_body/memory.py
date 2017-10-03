from enum import Enum

from neo_body.agent import Agent


class Memory(Agent):
    """Keeps track of objects NEO has interacted with and their associations based on attributes"""

    def __init__(self):
        """default constructor"""
        super(Memory, self).__init__("memory")
        self.colors = {}






SMALL_MIN_LENGTH = 0.1
SMALL_MAX_LENGTH = 10
MED_MIN_LENGTH = 10
MED_MAX_LENGTH = 36
LARGE_MIN_LENGTH = 36
LARGE_MAX_LENGTH = 240


class Size(Enum):
    SMALL = (SMALL_MIN_LENGTH, SMALL_MAX_LENGTH)
    MEDIUM = (MED_MIN_LENGTH, MED_MAX_LENGTH)
    LARGE = (LARGE_MIN_LENGTH, LARGE_MAX_LENGTH)


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


