from data import student_dict
import pyperclip

#convert student dict into text
def printdict(value, grade):
    studentamt = 0
    sortednames = {}
    for o in student_dict:
        if student_dict[o].grade == grade:
            sortednames[o] = student_dict[o].name
    if value == "stats":
        label = "NAME                    " + "|ACT    |" + "C/RANK |" + "COGAT  |" + "F/GEN  |" + "GPA    |" + "HOUSE  |" +\
                     "L/I    |" + "MINOR  |" + "RACE   |"
        datastring = "Class of " + grade + ": \n\n" + label + "\n\n"
        for i in sorted(sortednames.items(), key=lambda kv: (kv[1], kv[0])):
            i = i[0]
            if student_dict[i].grade == grade:
                studentamt += 1
                if studentamt > 20:
                    studentamt = 0
                    datastring = datastring + label + "\n\n"
                datastring = datastring + short_string(student_dict[i].name[:24], 25)
                for key, char in sorted(student_dict[i].__dict__.items()):
                    if key == "act" or key == "classrank" or key == "cogat" or key == "firstgen" or key == "gpa"\
                            or key == "house" or key == "lowincome" or key == "minority" or key == "race":
                        datastring = datastring + "|" + short_string(str(char), 8)
                datastring = datastring + "|" + "\n" + "\n"
    else:
        datastring = "Class of " + grade + ": \n\n"
        for i in sorted(sortednames.items(), key=lambda kv: (kv[1], kv[0])):
            i = i[0]
            if student_dict[i].grade == grade:
                datastring = datastring + student_dict[i].name + ": \n"
                for key, char in student_dict[i].__dict__.items():
                    if key != "act" and key != "classrank" and key != "cogat" and key != "firstgen" and key != "gpa" \
                            and key != "house" and key != "lowincome" and key != "minority" and key != "race" and key\
                            != "colleges" and key != "mentees" and key != "recs" and key != "name" and key != "grade"\
                            and key != "Class":
                        if str(char).strip() == "Designate Class":
                            char == "Undesignated"
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
    pyperclip.copy(datastring)

#add blank space to short string
def short_string(str, length):
        if len(str) < length:
            while len(str) < length-1:
                str = str + " "
            return str
        return str
