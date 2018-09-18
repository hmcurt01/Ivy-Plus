from rec import Rec
from mentee import Mentee


# student class
class Student:
    def __init__(self, act, gpa, race, name, email, passw, lastmeet, nextmeet, meetamount, menteehours, grade, Class, cogat, firstgen, lowincome, house, classrank,
                 minority, parentoneemail, parentonenum, parenttwoemail, parenttwonum):
        self.act = act
        self.gpa = gpa
        self.race = race
        self.name = name
        self.email = email
        self.passw = passw
        self.lastmeet = lastmeet
        self.nextmeet = nextmeet
        self.meetamount = meetamount
        self.menteehours = menteehours
        self.collegeAmount = 0
        self.colleges = {}
        self.grade = grade
        self.Class = Class
        self.mentees = {}
        self.recs = {}
        self.cogat = cogat
        self.firstgen = firstgen
        self.lowincome = lowincome
        self.house = house
        self.classrank = classrank
        self.minority = minority
        self.parentoneemail = parentoneemail
        self.parentonenum = parentonenum
        self.parenttwoemail = parenttwoemail
        self.parenttwonum = parenttwonum

    # change attritubes of object
    def change_attr(self, value, new, key):
        if value == "act":
            self.act = new
        elif value == "gpa":
            self.gpa = new
        elif value == "race":
            self.race = new
        elif value == "name":
            self.name = new
        elif value == "email":
            self.email = new
        elif value == "passw":
            self.passw = new
        elif value == "lastmeet":
            self.lastmeet = new
        elif value == "nextmeet":
            self.nextmeet = new
        elif value == "meetamount":
            self.meetamount = new
        elif value == "menteehours":
            self.menteehours = new
        elif value == "college":
            self.colleges[key] = new
        elif value == "grade":
            self.grade = new
        elif value == "Class":
            self.Class = new
        elif value == "mentees":
            self.mentees[str(key)] = Mentee(0, new)
        elif value == "recs":
            self.recs[str(key)] = Rec(new, "")
        elif value == "cogat":
            self.cogat = new
        elif value == "firstgen":
            self.firstgen = new
        elif value == "lowincome":
            self.lowincome = new
        elif value == "house":
            self.house = new
        elif value == "classrank":
            self.classrank = new
        elif value == "minority":
            self.minority = new
        elif value == "parentoneemail":
            self.parentoneemail = new
        elif value == "parentonenum":
            self.parentonenum = new
        elif value == "parenttwoemail":
            self.parenttwoemail = new
        elif value == "parenttwonum":
            self.parenttwonum = new
            
