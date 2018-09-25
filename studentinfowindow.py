from tkinter import *
from college import College
from studentpagewindow import StudentPageWindow
from data import root
from data import student_dict

# student info class, displays information for selected student
class StudentInfoWindow:
    def __init__(self, value, currentgrade):
        self.currentgrade=currentgrade
        self.widgets = {"main": {}, "colleges": {"clist": [], "others": []}, "mentees": {}, "recs": {}}
        self.widgetList = []
        self.value = value
        self.draw_main(value)

    #entry validation - only allow floats
    def callback(self, P):
        try:
            if P == "":
                return True
            float(P)
            return True
        except ValueError:
            return False

    #goes to student in dictionary one place from current student based on which
    def next_student(self, which):
        self.save_and_erase()
        allstudents = []
        for i in student_dict:
            if student_dict[i].grade == self.currentgrade:
                allstudents.append(i)
        if allstudents.index(self.value) == len(allstudents) - 1 and which == 1:
            StudentInfoWindow(allstudents[0], self.currentgrade)
        else:
            StudentInfoWindow(allstudents[allstudents.index(self.value) + which], self.currentgrade)

    # changes the color and value of a selected college attr
    def change_color(self, value, college, attr, char):
        newcolor = ""
        if char == "Yes":
            student_dict[value].colleges[college].change_attr(attr, "No")
            newcolor = "tomato"
        elif char == "No":
            if attr == "accept":
                student_dict[value].colleges[college].change_attr(attr, "Wait")
                newcolor = "yellow"
            else:
                student_dict[value].colleges[college].change_attr(attr, "Yes")
                newcolor = "springgreen"
        elif char == "Wait":
            newcolor = "SystemButtonFace"
            student_dict[value].colleges[college].change_attr(attr, "")
        elif char == "":
            newcolor = "springgreen"
            student_dict[value].colleges[college].change_attr(attr, "Yes")
        self.widgets["colleges"][college][str(college) + attr].config(bg=newcolor)
        newfuncdict = {"springgreen": "Yes", "tomato": "No", "yellow": "Wait", "SystemButtonFace": ""}
        self.widgets["colleges"][college][str(college) + attr].config(
            command=lambda: self.change_color(value, college, attr,
                                              newfuncdict[newcolor]))

    #saves aid of all colleges
    def save_aid(self):
        for i in self.widgets["colleges"]:
            if i != "clist" and i != "others":
                if self.widgets["colleges"][i]["aidentry"].get() == "":
                    student_dict[self.value].colleges[i].aid = 0
                else:
                    student_dict[self.value].colleges[i].aid = \
                    self.widgets["colleges"][i]["aidentry"].get().replace(" ", "")

    # erases all colleges
    def erase_colleges(self):
        for i in self.widgets["colleges"]:
            for o in self.widgets["colleges"][i]:
                if i != "clist" and i != "others":
                    self.widgets["colleges"][i][o].destroy()
        self.widgets["colleges"].clear()
        self.widgets["colleges"]["clist"] = []
        self.widgets["colleges"]["others"] = []

    # draws all colleges
    def draw_college(self, value, college):
        self.widgets["colleges"][college] = {}
        colordict = {"Yes": "springgreen", "No": "tomato", "Wait": "yellow", "": "SystemButtonFace"}
        if len(self.widgets["colleges"]["clist"]) >= 1:
            self.widgets["colleges"][college][str(college) + "accept"] = Button(root, text=student_dict[value].colleges[
                college].name, width=14, bg=colordict[ student_dict[value].colleges[college].accept],
                command=lambda: self.change_color(value, college, "accept",
                                                  student_dict[ value].colleges[college].accept))
            self.widgets["colleges"]["clist"].append(self.widgets["colleges"][college][str(college) + "accept"])
            self.widgets["colleges"][college][str(college) + "accept"].place(
                in_=self.widgets["colleges"]["clist"][self.widgets["colleges"]["clist"]
                                                          .index(
                    self.widgets["colleges"][college][str(college) + "accept"]) - 1], rely=2, relx=0, anchor=SW,
                bordermode="outside")
        else:
            self.widgets["colleges"][college][str(college) + "accept"] = Button(root, bg=colordict[
                student_dict[value].colleges[college].accept], text=student_dict[value].colleges[college].name,
                width=14, command=lambda: self.change_color(value, college, "accept", student_dict[value].colleges[
                college].accept))
            self.widgets["colleges"][college][str(college) + "accept"].place(relx=0, rely=.1, anchor=SW,
                                                                             bordermode="outside")
            self.widgets["colleges"]["clist"].append(self.widgets["colleges"][college][str(college) + "accept"])

        self.count = 1
        for key, char in sorted(student_dict[value].colleges[college].__dict__.items()):
            if key == "name" or key == "accept" or key == "aid":
                pass
            else:
                self.draw_college_info(key, char, value, college, colordict[char])
        self.widgets["colleges"][college]["aidentry"] = Entry(root, width=13)
        self.widgets["colleges"][college]["aidentry"].insert(0, student_dict[self.value].colleges[college].aid)
        self.widgets["colleges"][college]["aidentry"].place(in_=self.widgets["colleges"][college][str(college) + "ty"],
                                                            relx=1, rely=1, anchor=SW, bordermode="outside")
        vcmd = (root.register(self.callback))
        self.widgets["colleges"][college]["aidentry"].config(validate="key")
        self.widgets["colleges"][college]["aidentry"].config(validatecommand=(vcmd, "%P"))

    # draws information for each college object
    def draw_college_info(self, key, char, student, college, color):
        self.widgets["colleges"][college][str(college) + key] = Button(root, text=key.upper(), width=7, bg=color)
        self.widgets["colleges"][college][str(college) + key].config(
            command=lambda: self.change_color(student, college, key, char))
        self.widgets["colleges"][college][str(college) + key].place(
            in_=self.widgets["colleges"][college][str(college) + "accept"],
            relx=self.count * .5 + .5, rely=1, anchor=SW,
            bordermode="outside")
        self.count += 1

    # changes function of object
    def change_function(self, value, widget, index, type):
        if type == "college":
            widget.config(command=lambda: self.delete_widget(value, "2", index, "college"))
        elif type == "rec":
            widget.config(command=lambda: self.delete_widget(value, "2", index, "rec"))
        elif type == "mentee":
            widget.config(command=lambda: self.delete_widget(value, "2", index, "mentee"))
        elif type == "orig":
            widget.config(command=lambda: None)

    # changes function of buttons so they can be deleted by calling change_function
    def delete_widget(self, value, step, widget, type):
        if step == "1":
            self.widgets["main"]["deleteButton"].config(bg="red",
                                                        command=lambda: self.delete_widget(value, "2", "na", "reverse"))
            for i in student_dict[value].colleges:
                self.change_function(value, self.widgets["colleges"][i][str(i) + "accept"], i, "college")

            for i in student_dict[value].recs:
                self.change_function(value, self.widgets["recs"][i], i, "rec")

            for i in student_dict[value].mentees:
                self.change_function(value, self.widgets["mentees"][i], i, "mentee")

        elif step == "2":
            if type == "college":
                del student_dict[value].colleges[widget]
                self.erase_colleges()
                for i in student_dict[value].colleges:
                    self.draw_college(value, i)
            elif type == "rec":
                del student_dict[value].recs[widget]
                self.erase_recs()
                for i in student_dict[value].recs:
                    self.draw_rec(student_dict[self.value].recs[i].name, i)
            elif type == "mentee":
                del student_dict[value].mentees[widget]
                self.erase_mentees()
                count = 1
                for i in student_dict[self.value].mentees:
                    self.draw_mentee(student_dict[self.value].mentees[i].name, i)
                    count += 1
            for i in student_dict[value].colleges:
                self.change_function(value, self.widgets["colleges"][i][str(i) + "accept"], i, "orig")
            for i in student_dict[value].recs:
                self.change_function(value, self.widgets["recs"][i], i, "orig")
            self.widgets["main"]["deleteButton"].config(command=lambda: self.delete_widget(value, "1", "na", "na"),
                                                        bg="SystemButtonFace")
            self.widgets["main"]["deleteButton"].config(bg="SystemButtonFace")

    #erase all mentees
    def erase_mentees(self):
        for i in self.widgets["mentees"]:
            self.widgets["mentees"][i].destroy()
        self.widgets["mentees"].clear()

    #erase all recs
    def erase_recs(self):
        for i in self.widgets["recs"]:
            self.widgets["recs"][i].destroy()
        self.widgets["recs"].clear()

    # draw mentee dropdown
    def draw_mentee_listbox(self, value):
        if student_dict[value].Class == "Senior":
            menteevalue = "Freshman"
        elif student_dict[value].Class == "Freshman":
            menteevalue = "Senior"
        else:
            return
        self.widgets["frame"] = Frame(root)
        self.widgets["yscroll"] = Scrollbar(self.widgets["frame"])
        self.widgets["listbox"] = Listbox(self.widgets["frame"], yscrollcommand=self.widgets["yscroll"].set)
        self.widgets["frame"].place(in_=self.widgets["addMenteeButton"], relx=-1, anchor=NW, bordermode="outside")
        for i in student_dict:
            if student_dict[i].Class == menteevalue:
                self.widgets["listbox"].insert(END, student_dict[i].name)
        self.widgets["listbox"].size()
        self.widgets["yscroll"].config(command=self.widgets["listbox"].yview)
        self.widgets["listbox"].grid(row=0, column=0, sticky='nswe')
        self.widgets["yscroll"].grid(row=0, column=1, sticky='ns')
        if self.widgets["listbox"].size() > 0:
            self.widgets["listbox"].bind("<Double-Button-1>", self.add_mentee)
        else:
            self.widgets["listbox"].insert(END, "NO MENTEES/MENTORS TO ADD")
        self.widgets["addMenteeButton"].config(command=lambda: self.mentee_dropdown_destroy())

    #add single mentee to student object and draw said mentee
    def add_mentee(self, event):
        if student_dict[self.value].Class == "Senior":
            menteevalue = "Freshman"
        else:
            menteevalue = "Senior"
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        newmentee = value + str(len(student_dict[self.value].mentees) + 1)
        student_dict[self.value].change_attr("mentees", value, newmentee)
        for i in student_dict:
            if student_dict[i].Class == menteevalue:
                if student_dict[i].name == value:
                    student_dict[i].change_attr("mentees", student_dict[self.value].name, self.value + str(len(student_dict[self.value].mentees) + 1))
        self.draw_mentee(value, newmentee)
        self.mentee_dropdown_destroy()

    #erase mentee listbox/dropdown
    def mentee_dropdown_destroy(self):
        self.widgets["listbox"].destroy()
        self.widgets["yscroll"].destroy()
        self.widgets["frame"].destroy()
        self.widgets["addMenteeButton"].config(command=lambda: self.draw_mentee_listbox(self.value))

    #draw single mentee
    def draw_mentee(self, value, iden):
        self.widgets["mentees"][iden] = Button(text=value + ", ", width=10)
        self.widgets["mentees"][iden].place \
            (in_=self.widgets["addMenteeButton"],
             rely=len(self.widgets["mentees"]) * .5 + 1.5, anchor=SW, bordermode="outside")
        self.widgets["mentees"][iden + "entry"] = Entry(width=10)
        self.widgets["mentees"][iden + "entry"].insert(0, student_dict[self.value].mentees[iden].hours)
        self.widgets["mentees"][iden + "entry"].place(
            in_=self.widgets["mentees"][iden], relx=1, rely=1, anchor=SW,
            bordermode="outside")

    #only allow for y or n values - entry validation
    def callback_y(self, P):
        if (P == "y" or P == "Y" or P == "" or P == "N" or P == "n") and len(P) < 2:
            return True
        else:
            return False

    # draws main page
    def draw_main(self, value):
        #root.bind_class("Text", "<Control-a>", event.widget.tag_add("sel","1.0",END))
        vcmd = (root.register(self.callback))
        vcmd_y = (root.register(self.callback_y))
        totalaid = 0
        for i in student_dict[value].colleges:
            totalaid += float(student_dict[value].colleges[i].aid)

        self.widgets["main"]["name"] = Label(root, text=student_dict[self.value].name)
        self.widgets["main"]["name"].place(relx=.5, rely=0, anchor=N)

        self.widgets["main"]["totalaid"] = Label(root, text="Total Aid: " + '${:,.2f}'.format(totalaid), bg="lightgrey", height=2)
        self.widgets["main"]["totalaid"].place(anchor=SW, relx=0, rely=1)

        self.widgets["main"]["backButton"] = Button(root, text="Back", command=lambda: self.back())
        self.widgets["main"]["backButton"].place(relx=0, rely=0, anchor=NW)

        self.widgets["main"]["deleteButton"] = Button(root, text="Delete",
                                                      command=lambda: self.delete_widget(value, "1", "na", "na"))
        self.widgets["main"]["deleteButton"].place(in_=self.widgets["main"]["backButton"], relx=1, rely=1, anchor=SW,
                                                   bordermode="outside")
        self.widgets["main"]["laststudent"] = Button(root, text="Last Student", command=lambda: self.next_student(-1))
        self.widgets["main"]["laststudent"].place(in_=self.widgets["main"]["deleteButton"], relx=1, rely=1, anchor=SW,
                                                  bordermode="outside")

        self.widgets["main"]["nextstudent"] = Button(root, text="Next Student", command=lambda: self.next_student(1))
        self.widgets["main"]["nextstudent"].place(in_=self.widgets["main"]["laststudent"], relx=1, rely=1, anchor=SW,
                                                  bordermode="outside")

        self.widgets["main"]["addCollegeEntry"] = Entry(root)
        self.widgets["main"]["addCollegeEntry"].place(relx=.5, rely=.97, anchor=CENTER)

        self.widgets["main"]["addCollegeButton"] = Button(root, text="Add College",
                                                          command=lambda: self.add_college(value))
        self.widgets["main"]["addCollegeButton"].place(relx=.6, rely=.97, anchor=CENTER)

        for i, char in sorted(student_dict[value].__dict__.items()):
            if i != "colleges" and i != "collegeAmount" and i != "Class" and i != "mentees" and i != "recs":
                if len(self.widgetList) > 1:
                    self.widgets["main"][i.lower() + "Entry"] = Entry(root)
                    self.widgetList.append(self.widgets["main"][i.lower() + "Entry"])
                    self.widgets["main"][i.lower() + "Entry"].place(
                        in_=self.widgetList[self.widgetList.index(self.widgets["main"][i.lower() + "Entry"]) - 2],
                        anchor=SW,
                        rely=2, bordermode="outside")
                    self.widgets["main"][i.lower() + "Entry"].insert(0, char)
                else:
                    self.widgets["main"][i.lower() + "Entry"] = Entry(root)
                    self.widgetList.append(self.widgets["main"][i.lower() + "Entry"])
                    self.widgets["main"][i.lower() + "Entry"].place(relx=1, rely=0, anchor=NE)
                    self.widgets["main"][i.lower() + "Entry"].insert(0, char)

                self.widgets["main"][i.lower() + "Label"] = Label(root, text=i.upper() + ":")
                self.widgetList.append(self.widgets["main"][i.lower() + "Label"])
                self.widgets["main"][i.lower() + "Label"].place(
                    in_=self.widgetList[self.widgetList.index(self.widgets["main"][i.lower() + "Label"]) - 1], rely=.5,
                    anchor=E, bordermode="outside")
                if i == "gpa" or i == "act" or i == "meetamount" or i == "menteehours" or i == "classrank" or i == "cogat":
                    self.widgets["main"][i.lower() + "Entry"].config(validate="key")
                    self.widgets["main"][i.lower() + "Entry"].config(validatecommand=(vcmd, '%P'))
                elif i == "minority" or i == "firstgen" or i == "lowincome":
                    self.widgets["main"][i.lower() + "Entry"].config(validate="key")
                    self.widgets["main"][i.lower() + "Entry"].config(validatecommand=(vcmd_y, "%P"))



        for i in student_dict[value].colleges:
            self.draw_college(value, i)

        var = "Mentee"
        if self.currentgrade == "Freshman":
            var = "Mentor"
        self.widgets["addMenteeButton"] = Button(text="Add" + var, width=21,
                                                 command=lambda: self.draw_mentee_listbox(value))
        self.widgets["addMenteeButton"].place(in_=self.widgets["main"]["raceEntry"], relx=1, rely=3, anchor=SE,
                                              bordermode="outside")
        self.widgets["addRecButton"] = Button(text="Add Rec", width=10, command=lambda: self.add_rec())
        self.widgets["addRecButton"].place(in_=self.widgets["addMenteeButton"], relx=-1, rely=1, anchor=SW,
                                           bordermode="outside")

        self.widgets["addRecEntry"] = Entry(text="Add Rec", width=11)
        self.widgets["addRecEntry"].place(in_=self.widgets["addRecButton"], relx=1, rely=1, anchor=SW,
                                          bordermode="outside")
        for i in student_dict[self.value].mentees:
            self.draw_mentee(student_dict[self.value].mentees[i].name, i)
        for i in student_dict[self.value].recs:
            self.draw_rec(student_dict[self.value].recs[i].name, i)

    #add rec to student object, call draw rec function
    def add_rec(self):
        newrec = str(len(student_dict[self.value].recs) + 1) + self.widgets["addRecEntry"].get()
        student_dict[self.value].change_attr("recs", self.widgets["addRecEntry"].get(),
                                             newrec)
        self.draw_rec(self.widgets["addRecEntry"].get(), newrec)
        self.widgets["addRecEntry"].delete(0, END)

    #draw single rec
    def draw_rec(self, value, iden):
        if student_dict[self.value].recs[iden].status == "":
            color = "tomato"
        else:
            color = "springgreen"
        self.widgets["recs"][iden] = Button(root, text=value, width=13, command=lambda: self.change_rec_color(iden),
                                            bg=color)
        self.widgets["recs"][iden].place(in_=self.widgets["addRecButton"], relx=0, rely=len(self.widgets["recs"]) + 1,
                                         anchor=SW, bordermode="outside")

    #change color of rec and rec status within student object
    def change_rec_color(self, rec):
        if student_dict[self.value].recs[rec].status == "":
            student_dict[self.value].recs[rec].status = "Yes"
            self.widgets["recs"][rec].config(bg="springgreen")
        else:
            student_dict[self.value].recs[rec].status = ""
            self.widgets["recs"][rec].config(bg="tomato")

    # goes back to student page, destroys all currently displayed widgets
    def back(self):
        self.save_and_erase()
        StudentPageWindow(self.currentgrade)

    #save data to student object and erase page
    def save_and_erase(self):
        self.save_aid()
        self.erase_colleges()
        for i in self.widgets["main"]:
            if "Entry" in i:
                o = i.split("Entry")
                student_dict[self.value].change_attr(o[0], (self.widgets["main"][i].get()).replace(" ", ""), "na")
            self.widgets["main"][i].destroy()
        self.widgets.clear()
        self.widgetList[:] = []

    # adds college to selected student
    def add_college(self, value):
        student_dict[value].collegeAmount += 1
        student_dict[value].change_attr("college", key=student_dict[value].collegeAmount,
                                        new=College(self.widgets["main"]["addCollegeEntry"].get(), "No", "0", "No",
                                                    "No", "No", "No", "No", "No", "No", "No", ""))
        self.widgets["main"]["addCollegeEntry"].delete(0, END)
        self.draw_college(value, student_dict[value].collegeAmount)
