from tkinter import *
from data import root
from data import student_dict

class QuickAddWindow:
    def __init__(self, which, currentgrade):
        self.currentgrade=currentgrade
        self.widgets = {"entry":{}}
        self.which = which.lower()
        self.studentamt = 0
        self.draw_main()

    def draw_main(self):
        xcor = 0
        vcmd = (root.register(self.callback))
        self.widgets["backButton"] = Button(root, text="Back", command=lambda: self.back())
        self.widgets["backButton"].place(relx=0, rely=0, anchor=NW, bordermode="outside")
        self.widgets["iden"] = Label(root, text=self.which.upper())
        self.widgets["iden"].place(in_=self.widgets["backButton"], relx=1, rely=1, anchor=SW, bordermode="outside")
        for i in student_dict:
            if student_dict[i].grade == self.currentgrade:
                self.studentamt += 1
                if self.studentamt > 24:
                    self.studentamt = 1
                    xcor += 4
                self.widgets[i+"label"] = Label(root, text=student_dict[i].name + ":", width=10)
                self.widgets[i+"label"].place(in_=self.widgets["backButton"], anchor=SW, relx=xcor,
                                              rely=1+self.studentamt, bordermode="outside")

                self.widgets["entry"][i] = Entry(root, width=8)
                self.widgets["entry"][i].place(in_=self.widgets[i+"label"], anchor=SW, relx=1, rely=1,
                                               bordermode="outside")

                if self.which == "college":
                    self.widgets["addcollege"] = Button(root, text="Add", command=lambda: self.add_college(i))
                    self.widgets["addcollege"].place(in_=self.widgets["entry"][i], anchor=SW, relx=1, rely=1,
                                                     bordermode="outside")
                elif self.which == "rec":
                    self.widgets["addrec"] = Button(root, text="Add", command=lambda: self.add_rec(i))
                    self.widgets["addrec"].place(in_=self.widgets["entry"][i], anchor=SW, relx=1, rely=1,
                                                     bordermode="outside")


                for o, char in sorted(student_dict[i].__dict__.items()):
                    if o == self.which:
                        self.widgets["entry"][i].insert(0, char)
                    if self.which == "gpa" or self.which == "act" or self.which == "meetamount" or self.which\
                            == "menteehours" or self.which == "cogat" or self.which == "classrank":
                        self.widgets["entry"][i].config(validate="key")
                        self.widgets["entry"][i].config(validatecommand=(vcmd, '%P'))

    def add_college(self, value):
        student_dict[value].collegeAmount += 1
        student_dict[value].change_attr("college", key=student_dict[value].collegeAmount,
                                        new=College(self.widgets["entry"][value].get(), "No", "0", "No",
                                                    "No", "No", "No", "No", "No", "No", "No", ""))
        self.widgets["entry"][value].delete(0, END)

    def set_function(self, what):
        

    def add_rec(self, value):
        newrec = str(len(student_dict[value].recs) + 1) + self.widgets["entry"][value].get()
        student_dict[value].change_attr("recs", self.widgets["entry"][value].get(),
                                             newrec)
        self.widgets["entry"][value].delete(0, END)

    def callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False


    def back(self):
        for i in self.widgets:
            if i == "entry":
                for o in self.widgets["entry"]:
                    for u in student_dict:
                        if u == o and self.which != "college":
                            student_dict[u].change_attr(self.which, self.widgets["entry"][o].get(), "na")
                    self.widgets["entry"][o].destroy()
            else:
                self.widgets[i].destroy()
        self.widgets.clear()
        StudentPageWindow(self.currentgrade)

from studentpagewindow import StudentPageWindow
from college import College