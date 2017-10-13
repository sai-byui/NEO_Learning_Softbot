from neo_body.agent import Agent


class Legs(Agent):
    """Allows NEO to move in its environment"""

    def __init__(self):
        """default constructor"""
        super(Legs, self).__init__("legs")
        self.position = self.ask("brain", "position")

    def walk(self):
        direction = self.ask("brain", "facing_direction")
        if direction == "RIGHT":
            self.position += 1
        else:
            self.position -= 1
