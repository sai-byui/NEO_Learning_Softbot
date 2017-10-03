from neo_body.agent import Agent
from neo_body.eyes import Eyes
from neo_body.hands import Hands
from neo_body.memory import Memory
from neo_body.mouth import Mouth


class Brain(Agent):
    """The driver Agent of the program, manages all other agents. The consciousness of NEO"""

    def __init__(self):
        """default constructor"""
        super(Brain, self).__init__("brain")
        self.eyes = Eyes()
        self.hands = Hands()
        self.memory = Memory()
        self.mouth = Mouth()




