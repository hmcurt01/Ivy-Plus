from tkinter import *
from random import randint
from student import Student
from data import root
from data import student_dict
from data import save
from printdata import printdict

class StudentPageWindow:
    def __init__(self, currentgrade):
        self.currentgrade=currentgrade
        self.widgets = {}
        self.xCor = 0
        self.yCor = .1
        self.options = ["Senior", "Junior", "Sophomore", "Freshman", "Graduated", "Other"]
        self.optionvalue = StringVar()
        self.optionvalue.set("Designate Class")
        self.draw_main()
        #for i in range(120):
         #   self.widgets["addStudentEntry"].insert(0, i)
          #  self.add_student()

    # draws all students and add student button/entry
    def draw_main(self):
        self.xCor = 0
        self.yCor = .1
        totalaid = 0
        accepted = 0
        totalcolleges = 0
        for i in student_dict:
            if student_dict[i].grade == self.currentgrade:
                self.draw_student(student_dict[i], i)
                for o in student_dict[i].colleges:
                    if student_dict[i].colleges[o].accept == "Yes" or student_dict[i].colleges[o].accept == "No":
                        totalcolleges += 1
                        if student_dict[i].colleges[o].accept == "Yes":
                            accepted += 1
                    totalaid += float(student_dict[i].colleges[o].aid)

        self.widgets["addStudentEntry"] = Entry(root)
        self.widgets["addStudentEntry"].place(relx=.5, rely=.97, anchor=CENTER)

        self.widgets["addStudentButton"] = Button(root, text="Add Student", command=lambda: self.add_student())
        self.widgets["addStudentButton"].place(relx=.6, rely=.97, anchor=CENTER)

        self.widgets["backButton"] = Button(root, text="Back", command=lambda: self.back())
        self.widgets["backButton"].place(relx=0, rely=0, anchor=NW, bordermode="outside")
        self.create_designate_dropdown()
        self.widgets["designate"] = OptionMenu(root, self.optionvalue, *self.options,
                                               command=lambda _: self.designate(self.optionvalue.get()))
        self.widgets["designate"].place(in_=self.widgets["backButton"], relx=1, rely=1.09, anchor=SW,
                                        bordermode="outside")
        self.widgets["statsbutton"] = Button(root, text="Class Statistics", command=lambda: self.next("N/A", "lol"))
        self.widgets["statsbutton"].place(in_=self.widgets["designate"], relx=1, rely=.92, anchor=SW,
                                          bordermode="outside")
        self.widgets["removeStudentButton"] = Button(root, text="Delete Student",
                                                     command=lambda: self.remove_student(1, "na", "na"))
        self.widgets["removeStudentButton"].place(in_=self.widgets["statsbutton"], relx=1, rely=1, anchor=SW,
                                                  bordermode="outside")

        self.choosequick = StringVar()
        self.choosequick.set("Quick Add/View")
        self.chooselist = ["ACT", "GPA", "RACE", "NAME", "EMAIL", "PASSW", "EMAIL", "NEXTMEET", "LASTMEET",
                           "MEETAMOUNT", "MENTEEHOURS", "COGAT", "FIRSTGEN", "LOWINCOME", "HOUSE", "CLASSRANK",
                           "MINORITY", "PARENTONEEMAIL",
                           "PARENTONENUM", "PARENTTWOEMAIL", "PARENTTWONUM", "COLLEGE", "REC"]
        self.widgets["quickadd"] = OptionMenu(root, self.choosequick, *self.chooselist, command=lambda _:
        self.next(self.choosequick.get(), "quick"))
        self.widgets["quickadd"].place(in_=self.widgets["removeStudentButton"], relx=1, rely=1.09, anchor=SW,
                                       bordermode=
                                       "outside")

        self.widgets["copystats"] = Button(root, text="Copy Stats", command=lambda: printdict("stats",
                                                                                              self.currentgrade))
        self.widgets["copystats"].place(in_=self.widgets["quickadd"], relx=1, rely=.92, anchor=SW, bordermode="outside")

        self.widgets["copyinfo"] = Button(root, text="Copy Personal Info", command=lambda: printdict("info",
                                                                                              self.currentgrade))
        self.widgets["copyinfo"].place(in_=self.widgets["copystats"], relx=1, rely=1, anchor=SW, bordermode="outside")

        self.widgets["removeButton"] = Button(root, text="Delete Class", command=lambda: self.remove_class(1, "na"))
        self.widgets["removeButton"].place(in_=self.widgets["copyinfo"], relx=1, rely=1, anchor=SW,
                                           bordermode="outside")
    #create dropdown to designate class
    def create_designate_dropdown(self):
        for i in student_dict:
            if student_dict[i].grade == self.currentgrade:
                if student_dict[i].Class != "":
                    self.optionvalue.set(student_dict[i].Class)
        for i in student_dict:
            if student_dict[i].Class in self.options and student_dict[i].Class != ("Graduated" and "Other") and \
                            student_dict[i].grade != self.currentgrade:
                self.options.remove(student_dict[i].Class)

    #designate class as senior, junior, etc
    def designate(self, var):
        for i in student_dict:
            if student_dict[i].grade == self.currentgrade:
                student_dict[i].change_attr("Class", var, "na")

    #change function of widget
    def change_function(self, var, step, value, what):
        self.widgets[var].config(command=lambda: self.remove_student(step, value, what))

    def remove_student(self, step, value, type):
        if step == 1:
            self.widgets["removeStudentButton"].config(bg="red",
                                                       command=lambda: self.remove_student(2, "revert", "revert"))
            for i in student_dict:
                if student_dict[i].grade == self.currentgrade:
                    self.change_function(student_dict[i], 2, i, "delete")
            return
        elif step == 2:
            if type == "delete":
                del student_dict[value]
                for i in self.widgets:
                    self.widgets[i].destroy()
                self.draw_main()
            elif type == "revert":
                self.widgets["removeStudentButton"].config(command=lambda: self.remove_student(1, "na", "na"),
                                                           bg="SystemButtonFace")
                for i in student_dict:
                    if student_dict[i].grade == self.currentgrade:
                        self.widgets[student_dict[i]].config(command=lambda: self.next(i, "info"))

    # goes back to grade window and removes everything currently displayed
    def back(self):
        for i in self.widgets:
            self.widgets[i].destroy()
        GradeWindow()

    # removes current class
    def remove_class(self, step, type):
        if step == 1:
            self.widgets["removeButton"].config(bg="#ffb900", command=lambda: None)

            self.widgets["sure"] = Label(root, text="Are you sure?", width=10)
            self.widgets["sure"].place(in_=self.widgets["removeButton"], relx=1, rely=1, anchor=SW,
                                       bordermode="outside")

            self.widgets["yes"] = Button(root, text="Yes", width=10, command=lambda: self.remove_class(2, "del"))
            self.widgets["yes"].place(in_=self.widgets["sure"], relx=1, rely=1, anchor=SW, bordermode="outside")

            self.widgets["no"] = Button(root, text="No", width=10, command=lambda: self.remove_class(2, "revert"))
            self.widgets["no"].place(in_=self.widgets["yes"], relx=1, rely=1, anchor=SW, bordermode="outside")
        elif step == 2 and type == "del":
            deletionlist = []
            for i in student_dict:
                if student_dict[i].grade == self.currentgrade:
                    deletionlist.append(i)
            for i in deletionlist:
                del student_dict[i]
            self.back()
        else:
            self.widgets["yes"].destroy()
            self.widgets["no"].destroy()
            self.widgets["sure"].destroy()
            self.widgets["removeButton"].config(bg="SystemButtonFace", command=lambda: self.remove_class(1, "na"))

    # creates new student object
    def add_student(self):
        hash = ""
        choices = "abcdefghijklmnopqrstuvwxyz123456789"
        for i in range(6):
            hash += choices[randint(0, 34)]
        student_dict[hash] = Student("", "", "", self.widgets["addStudentEntry"].get(), "", "", "", "", "", "",
                                     self.currentgrade, self.optionvalue.get(), "", "", "", "", ""
                                     , "", "", "", "", "")
        self.widgets["addStudentEntry"].delete(0, END)
        self.draw_student(student_dict[hash], hash)

    # draws one student button
    def draw_student(self, value, iden):
        self.xCor += .125
        if self.xCor > .875:
            self.xCor = .125
            self.yCor += .05
        else:
            pass
        self.widgets[value] = Button(root, text=value.name, height=1, width=20, command=lambda: self.next(iden, "info"))
        self.widgets[value].place(relx=self.xCor, rely=self.yCor, anchor=CENTER)

    # calls StudentInfoWindow, deletes all currently displayed widgets
    def next(self, iden, which):
        for i in self.widgets:
            self.widgets[i].destroy()
        self.widgets.clear()
        if which == "info":
            StudentInfoWindow(iden, self.currentgrade)
        elif which == "quick":
            QuickAddWindow(iden, self.currentgrade)
        else:
            StudentStatsWindow(self.currentgrade)

from gradewindow import GradeWindow
from studentstatswindow import StudentStatsWindow
from studentinfowindow import StudentInfoWindow
from quickaddwindow import QuickAddWindow
