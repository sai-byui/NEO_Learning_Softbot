from neo_body.agent import Agent
import Matrix


class Eyes(Agent):
    """views objects and gathers visual information"""
    def __init__(self):
        """default constructor"""
        super(Eyes, self).__init__("eyes")
        self.current_object_color = None
        self.FACING_DIRECTION = None
        self.position = self.ask("brain", "position")
        self.num_vis_obj = 0
        self.visible_object_list = []

    def look_at_object(self):
        self.determine_color()



    def determine_color(self):
       self.current_object_color = self.visible_object_list[0].color
       self.visible_object_list.pop(0)


    def scan_area(self):
        self.FACING_DIRECTION = self.ask("brain", "facing_direction")
        if self.FACING_DIRECTION == "RIGHT":
            for object in Agent.environment.object_list:
                if object.position > self.position:
                    self.num_vis_obj += 1
                    self.visible_object_list.append(object)
        elif self.FACING_DIRECTION == "LEFT":
            for object in Agent.environment.object_list:
                if object.position > self.position:
                    self.num_vis_obj += 1
                    self.visible_object_list.append(object)