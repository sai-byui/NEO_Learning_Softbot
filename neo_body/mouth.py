from neo_body.agent import Agent


class Mouth(Agent):
    """The speaking agent of the program"""

    def __init__(self):
        """default constructor"""
        super(Mouth, self).__init__("mouth")

    def list_similar_objects(self):
        object_list = self.ask("brain", "list_of_objects")
        for object in object_list:
            print(object[0])

    def report_visible_objects(self):
        visible_obj = self.ask("eyes", "num_vis_obj")
        if visible_obj != 1:
            print("I can see " + str(visible_obj) + " objects")
        else:
            print("I can see " + str(visible_obj) + " object")

    def state_current_position(self):
        position = self.ask("brain", "position")
        print("My current position is " + str(position))

