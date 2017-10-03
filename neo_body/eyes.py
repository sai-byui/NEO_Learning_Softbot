from neo_body.agent import Agent


class Eyes(Agent):
    """views objects and gathers visual information"""
    def __init__(self):
        """default constructor"""
        super(Eyes, self).__init__("eyes")
        self.current_object_color = None
        self.current_object_size = None

    def look_at_object(self):
        self.determine_color()
        self.determine_size()