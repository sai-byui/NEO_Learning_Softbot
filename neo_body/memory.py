from enum import Enum
import sqlite3
from Object.Object import Object

from neo_body.agent import Agent


class Memory(Agent):
    """Keeps track of objects NEO has interacted with and their associations based on attributes"""

    def __init__(self):
        """default constructor"""
        super(Memory, self).__init__("memory")
        self.current_object_color = None
        self.colors = {}
        self.create_color_categories()
        self.weights = {}
        self.create_weight_categories()
        self.create_object_memory()

    def create_color_categories(self):
        for color_name in Color:
            self.colors[color_name] = color_name.value

    def create_weight_categories(self):
        for weight_category in Weight:
            self.weights[weight_category] = weight_category.value

    def memorize(self):
        self.current_object_color = self.ask("eyes", "current_object_color")
        self.store_object_color()

    def store_object_color(self):
        conn = sqlite3.connect('neo_test.db')

        cursor = conn.cursor()

        cursor.execute("INSERT INTO OBJECTS VALUES (:name, :color)", {'name': "apple", 'color': self.current_object_color})

        cursor.execute("""SELECT * FROM OBJECTS""")
        print(cursor.fetchone())

        conn.commit()
        conn.close()



    def create_object_memory(self):
        conn = sqlite3.connect('neo_test.db')

        cursor = conn.cursor()

        # cursor.execute("""CREATE REPLACE TABLE OBJECTS ( OBJECT_NAME, OBJECT_COLOR )""")
        #
        # apple = Object("apple", (255, 0, 0), 1, 300)
        #
        # color = apple.color
        #
        # object_name = apple.name
        #
        # cursor.execute("INSERT INTO OBJECTS VALUES ( {}, {} )".format(object_name, color))
        #
        # cursor.execute("""SELECT * FROM OBJECTS""")
        #
        # print(cursor.fetchone())
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


