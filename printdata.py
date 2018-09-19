from data import student_dict
def printdict(value, grade):
    datastring = ""
    studentamt = 0
    if value == "stats":
        label = "NAME   " + "|ACT    |" + "C/RANK |" + "COGAT  |" + "F/GEN  |" + "GPA    |" + "HOUSE  |" +\
                     "L/I    |" + "MINOR  |" + "RACE   |"
        print(label + "\n")
        for i in student_dict:
            if student_dict[i].grade == grade:
                studentamt += 1
                if studentamt > 20:
                    studentamt = 0
                    datastring = datastring + label + "\n\n"
                datastring = datastring + short_string(student_dict[i].name)
                for key, char in sorted(student_dict[i].__dict__.items()):
                    if key == "act" or key == "classrank" or key == "cogat" or key == "firstgen" or key == "gpa"\
                            or key == "house" or key == "lowincome" or key == "minority" or key == "race":
                        datastring = datastring + "|" + short_string(str(char))
                datastring = datastring + "|" + "\n" + "\n"
    else:
        datastring = ""
        for i in student_dict:
            if student_dict[i].grade == grade:
                datastring = datastring + student_dict[i].name + ": \n"
                for key, char in sorted(student_dict[i].__dict__.items()):
                    if key != "act" and key != "classrank" and key != "cogat" and key != "firstgen" and key != "gpa" \
                            and key != "house" and key != "lowincome" and key != "minority" and key != "race" and key\
                            != "colleges" and key != "mentees" and key != "recs":
                        datastring = datastring + key.upper() + ": " + str(char) +"\n"
                    if key == "colleges":
                        datastring = datastring + "COLLEGES: "
                        for p in student_dict[i].colleges:
                            datastring = datastring + student_dict[i].colleges[p].name + ", "
                        datastring = datastring + "\n"
                    if key == "mentees":
                        datastring = datastring + "MENTEES: "
                        for p in student_dict[i].mentees:
                            datastring = datastring + student_dict[i].mentees[p].name + ", "
                        datastring = datastring + "\n"
                    if key == "recs":
                        datastring = datastring + "RECS: "
                        for p in student_dict[i].recs:
                            datastring = datastring + student_dict[i].recs[p].name + ", "
                        datastring = datastring + "\n"
            datastring = datastring + "\n"
        print(datastring)

def short_string(str):
    if len(str) < 8:
        while len(str) < 7:
            str = str + " "
        return str
