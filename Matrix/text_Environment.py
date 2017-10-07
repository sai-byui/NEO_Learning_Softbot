from Matrix.environment import Environment
from Object.Object import Object
from neo_body.brain import brain

class Text_Environment(Environment):

    def __init__(self):
        self.object_list = []
        self.left_wall_x_pos = 0
        self.right_wall_x_pos = 500

    def add_object(self, object):
        self.object_list.append(object)

text_matrix = Text_Environment()
test_object = Object("apple", (255, 0, 0), 1, 300)
text_matrix.add_object(test_object)
print("adding " + text_matrix.object_list[0].name + " into the matrix")
print("adding neo into the matrix")
neo = brain(text_matrix)
while not neo.finished:
    neo.run_learning_program()
