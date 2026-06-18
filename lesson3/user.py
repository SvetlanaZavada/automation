class User:

    def __init__(self, first_name, last_name):
        self.name = first_name
        self.secondName = last_name

    def sayName(self):
        print(self.name)

    def saySecondName(self):
        print(self.secondName)

    def Name_and_secondName(self):
        print(self.name, self.secondName)
