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
        self.current_object_name = None
        self.colors = {}
        self.weights = {}
        self.create_object_memory()

    def memorize(self):
        self.current_object_color = self.ask("eyes", "current_object_color")
        self.current_object_name = self.ask("brain", "current_object_name")
        self.store_object_color()

    def store_object_color(self):
        conn = sqlite3.connect('neo_test.db')

        cursor = conn.cursor()

        cursor.execute("INSERT INTO OBJECTS VALUES (:name, :color)",
                       {'name': self.current_object_name, 'color': self.current_object_color})

        cursor.execute("""SELECT * FROM OBJECTS WHERE OBJECT_NAME = :name""", {'name': self.current_object_name})
        print(cursor.fetchone())

        conn.commit()
        conn.close()



    def create_object_memory(self):
        conn = sqlite3.connect('neo_test.db')

        cursor = conn.cursor()

        cursor.execute("""DROP TABLE IF EXISTS OBJECTS""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS OBJECTS ( OBJECT_NAME, OBJECT_COLOR )""")

        conn.commit()
        conn.close()
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



