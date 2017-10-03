from neo_body.agent import Agent


class Hands(Agent):
    """Holds objects and gathers info about weight, temp, etc."""

    def __init__(self):
        """default constructor"""
        super(Hands, self).__init__("hands")
        self.current_object_weight = None
        self.current_object_temperature = None


