from neo_body.agent import Agent


class Hands(Agent):
    """Holds objects and gathers info about weight, temp, etc."""

    def __init__(self):
        """default constructor"""
        super(Hands, self).__init__("hands")
        self.current_object_weight = None
        self.current_object_temperature = None

    def pick_up_object(self):
        self.current_object_weight = self.ask("brain", "uninspected_objects")[0].weight




