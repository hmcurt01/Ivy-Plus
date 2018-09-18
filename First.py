class student:
    def __init__(self, id, name, act, menteeHours, race, gpa, rank, nextMeet, lastMeet, meetAmount, email, password):
        self.id = 0
        self.name = name
        self.act = act
        self.menteeHours = menteeHours
        self.race = race
        self.gpa = gpa
        self.rank = rank
        self.nextMeet = nextMeet
        self.lastMeet = lastMeet
        self.meetAmount = meetAmount
        self.email = email
        self.password = password

    def changeAttribute(self, var, update):
        variables = {
            "act":self.act, "name":self.name, "id":self.id
        }
        variables[var] = update
