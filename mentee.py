class Mentee:
    def __init__(self, hours, name):
        self.hours = hours
        self.name = name

    def change_attr(self, value, new):
        if value == "hours":
            self.hours = new
        elif value == "name":
            self.name = new