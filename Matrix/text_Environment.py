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


    def query_neo(self, neo):
        query = ""
        finished = False
        while not finished:
            answer = input("Would you like to query NEO?(y/n)").lower()
            if answer == 'y':
                query = input("Enter a color (red, orange, yellow)").lower()
                neo.find_objects(query)
            else:
                finished = True




text_matrix = Text_Environment()
object_file = open("list_of_objects.txt", "r")
line = object_file.readline()
while line:
    object_name = object_file.readline().rstrip()
    object_color = object_file.readline().rstrip()
    object_weight = float(object_file.readline().rstrip())
    object_position = int(object_file.readline().rstrip())
    test_object = Object(object_name, object_color, object_weight, object_position)
    text_matrix.add_object(test_object)
    print("adding " + object_name + " into the matrix")
    line = object_file.readline()
object_file.close()
print("adding neo into the matrix")
neo = brain(text_matrix)
while not neo.finished:
    neo.run_learning_program()
text_matrix.query_neo(neo)
