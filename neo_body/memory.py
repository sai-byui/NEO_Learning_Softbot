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
        self.short_term_memory = None
        self.current_object_weight = None
        self.current_row_index = 1
        self.colors = {}
        self.weights = {}
        self.create_object_memory()

    def memorize(self):
        self.current_object_color = self.ask("eyes", "current_object_color")
        self.current_object_name = self.ask("brain", "current_object_name")
        self.current_object_weight = self.ask("hands", "current_object_weight")
        self.store_object_info()

    def store_object_info(self):
        conn = sqlite3.connect('neo_test.db')

        cursor = conn.cursor()

        # insert the object into the objects table along with its attributes
        cursor.execute("INSERT INTO OBJECTS (object_name, object_color, object_weight) VALUES (:name, :color, :weight)",
                       {'name': self.current_object_name, 'color': self.current_object_color,
                        'weight': self.current_object_weight})
        # insert the color into the adjective table
        cursor.execute("INSERT OR IGNORE INTO ADJECTIVES (adjective_name, category) VALUES (:name, 'color')",
                       {'name': self.current_object_color})
        cursor.execute("SELECT adjective_id FROM ADJECTIVES WHERE adjective_name = ?", (self.current_object_color,))
        adjective_id = cursor.fetchone()[0]

        cursor.execute("SELECT object_id FROM OBJECTS WHERE object_name = ?", (self.current_object_name,))
        object_id = cursor.fetchone()[0]

        # make the connection between the adjective and its relation to the object
        cursor.execute("""INSERT INTO OBJECT_DESCRIPTION (object_id, adjective_id)
                          VALUES (
                          ?,
                          ?)""", (object_id, adjective_id,))
        # cursor.execute("SELECT * FROM OBJECT_DESCRIPTION")
        # print(cursor.fetchall())

        cursor.execute("""SELECT * FROM OBJECTS WHERE OBJECT_NAME = :name""", {'name': self.current_object_name})
        print(cursor.fetchone())

        conn.commit()
        conn.close()


    def create_object_memory(self):
        conn = sqlite3.connect('neo_test.db')

        cursor = conn.cursor()

        cursor.execute("""DROP TABLE IF EXISTS OBJECTS""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS OBJECTS
                          (
                           object_id INTEGER PRIMARY KEY ,
                           OBJECT_NAME,
                           OBJECT_COLOR,
                           OBJECT_WEIGHT
                           )""")

        # create linking table between objects and adjectives
        cursor.execute("""DROP TABLE IF EXISTS OBJECT_DESCRIPTION""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS OBJECT_DESCRIPTION
                          (
                           object_id INTEGER REFERENCES OBJECTS (object_id) ON DELETE CASCADE ,
                           adjective_id INTEGER REFERENCES ADJECTIVES (adjective_id) ON DELETE CASCADE
                          )""")

        # creating adjective table
        cursor.execute("""DROP TABLE IF EXISTS ADJECTIVES""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS ADJECTIVES
                          (
                           adjective_id INTEGER PRIMARY KEY ,
                           adjective_name UNIQUE,
                           category,
                           less_than,
                           greater_than
                          )""")

        conn.commit()
        conn.close()

    def recall_objects(self):
        statement = self.ask("brain", "sql_statement")
        conn = sqlite3.connect('neo_test.db')

        cursor = conn.cursor()

        cursor.execute(statement)

        self.short_term_memory = cursor.fetchall()
        conn.close()





