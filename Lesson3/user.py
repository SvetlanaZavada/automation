class User:

    def __init__(self, first_name, last_name):
        self.name = first_name
        self.secondName = last_name

    def firstName(self):
        print(self.name)

    def lastName(self):
        print(self.secondName)

    def firstName_and_lastName(self):
        print(self.name, self.secondName)
