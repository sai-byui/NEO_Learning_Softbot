from neo_body.agent import Agent
from neo_body.eyes import Eyes
from neo_body.hands import Hands
from neo_body.memory import Memory
from neo_body.mouth import Mouth
from neo_body.legs import Legs
from enum import Enum


class brain(Agent):
    """The driver Agent of the program, manages all other agents. The consciousness of NEO"""

    def __init__(self, environment):
        """default constructor"""
        super(brain, self).__init__("brain", environment)
        self.CURRENT_STATE = BEHAVIOR_STATE.SCANNING
        self.facing_direction = "RIGHT"
        self.finished = False
        self.position = 100
        self.eyes = Eyes()
        self.hands = Hands()
        self.memory = Memory()
        self.mouth = Mouth()
        self.legs = Legs()


    def scan_room(self):
        self.eyes.scan_area()
        self.mouth.report_visible_objects()


    def report_understanding(self):
        self.mouth.list_categories()

    def run_learning_program(self):
        if self.CURRENT_STATE == BEHAVIOR_STATE.SCANNING:
            self.scan_room()
            self.report_understanding()
            self.CURRENT_STATE = BEHAVIOR_STATE.APPROACHING
        elif self.CURRENT_STATE == BEHAVIOR_STATE.APPROACHING:
            while self.position != self.environment.object_list[0].position:
                self.legs.walk()
                self.position = self.ask("legs", "position")
                self.mouth.state_current_position()
            self.CURRENT_STATE = BEHAVIOR_STATE.FINISHED
        elif self.CURRENT_STATE == BEHAVIOR_STATE.INSPECTING:
            pass
        else:
            self.CURRENT_STATE = BEHAVIOR_STATE.FINISHED
            self.finished = True


class BEHAVIOR_STATE(Enum):
    SCANNING = 1
    APPROACHING = 2
    INSPECTING = 3
    FINISHED = 4
