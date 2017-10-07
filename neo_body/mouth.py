from neo_body.agent import Agent


class Mouth(Agent):
    """The speaking agent of the program"""

    def __init__(self):
        """default constructor"""
        super(Mouth, self).__init__("mouth")

    def list_categories(self):
        print("I currently know about the following attributes: ")
        for color in self.ask("memory", "colors"):
            print(str(color) + " ")
        for weight_type in self.ask("memory", "weights"):
            print(str(weight_type) + " ")

    def report_visible_objects(self):
        visible_obj = self.ask("eyes", "num_vis_obj")
        if visible_obj != 1:
            print("I can see " + str(visible_obj) + " objects")
        else:
            print("I can see " + str(visible_obj) + " object")

