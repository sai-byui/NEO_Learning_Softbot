from neo_body.agent import Agent


class Wernicke_Area(Agent):
    """This agent forms the query from natural language into SQL"""

    def __init__(self):
        """default constructor"""
        super(Wernicke_Area, self).__init__("wernicke_area")

        self.original_sentence = None
        self.query = None
        self.word_array = []
        self.select_statement = None
        self.from_statement = None
        self.where_statement = None

    def analyze_query(self):
        self.original_sentence = self.ask("brain", "sentence")
        self.word_array = self.original_sentence.split()
        self.determine_inter()
        self.determine_table()
        self.find_qualifiers()
        self.create_where_statement()

    def determine_inter(self):
        if self.word_array[0].lower() == "which":
            self.create_select_statement()

    def determine_table(self):
        self.from_statement = "FROM " + self.word_array[1].upper()

    def find_qualifiers(self):
        pass

    def create_select_statement(self):
        pass
