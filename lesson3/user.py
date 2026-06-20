class User:

    def __init__(self, first_name, last_name):
        self.name = first_name
        self.secondName = last_name

    def FirstName(self):
        print(self.name)

    def LastName(self):
        print(self.secondName)

    def FirstName_and_LastName(self):
        print(self.name, self.secondName)
