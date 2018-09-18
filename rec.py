class Rec:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def change_attr(self, value, new):
        if value == "name":
            self.name = new
        elif value == "status":
            self.value = new