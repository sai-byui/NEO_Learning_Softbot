from neo_body.agent import Agent


class Legs(Agent):
    """Allows NEO to move in its environment"""

    def __init__(self):
        """default constructor"""
        super(Legs, self).__init__("legs")

    def walk(self):
        pass
