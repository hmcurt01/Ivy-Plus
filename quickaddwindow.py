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

    #draw main window
    def draw_main(self):
        xcor = 0
        vcmd = (root.register(self.callback))
        vcmd_y = (root.register(self.callback_y))
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
                    self.widgets[i + "addcollege"] = Button(root, text="Add")
                    self.widgets[i + "addcollege"].place(in_=self.widgets["entry"][i], anchor=SW, relx=1, rely=1,
                                                     bordermode="outside")
                    self.set_function("college", i)
                elif self.which == "rec":
                    self.widgets[i + "addrec"] = Button(root, text="Add", command=lambda: self.add_rec(i))
                    self.widgets[i + "addrec"].place(in_=self.widgets["entry"][i], anchor=SW, relx=1, rely=1,
                                                     bordermode="outside")
                    self.set_function("rec", i)

                for o, char in sorted(student_dict[i].__dict__.items()):
                    if o == self.which:
                        self.widgets["entry"][i].insert(0, char)
                    if self.which == "gpa" or self.which == "act" or self.which == "meetamount" or self.which\
                            == "menteehours" or self.which == "cogat" or self.which == "classrank":
                        self.widgets["entry"][i].config(validate="key")
                        self.widgets["entry"][i].config(validatecommand=(vcmd, '%P'))
                    if self.which == "minority" or self.which == "firstgen" or self.which == "lowincome":
                        self.widgets["entry"][i].config(validate="key")
                        self.widgets["entry"][i].config(validatecommand=(vcmd_y, "%P"))

    #add college to student
    def add_college(self, value):
        student_dict[value].collegeAmount += 1
        student_dict[value].change_attr("college", key=student_dict[value].collegeAmount,
                                        new=College(self.widgets["entry"][value].get(), "No", "0", "No",
                                                    "No", "No", "No", "No", "No", "No", "No", ""))
        self.widgets["entry"][value].delete(0, END)

    #sets function of rec and college buttons
    def set_function(self, what, value):
        if what == "college":
            self.widgets[value + "addcollege"].config(command=lambda: self.add_college(value))
        else:
            self.widgets[value + "addrec"].config(command=lambda: self.add_rec(value))

    #add rec to student
    def add_rec(self, value):
        newrec = str(len(student_dict[value].recs) + 1) + self.widgets["entry"][value].get()
        student_dict[value].change_attr("recs", self.widgets["entry"][value].get(),
                                             newrec)
        self.widgets["entry"][value].delete(0, END)

    #makes sure entrys only allow numbers
    def callback(self, P):
        try:
            if P == "":
                return True
            float(P)
            return True
        except ValueError:
            return False

    def callback_y(self, P):
        if (P == "y" or P == "Y" or P == "" or P == "N" or P == "n") and len(P) < 2:
            return True
        else:
            return False

    #go back to student page window
    def back(self):
        self.save_and_erase()
        StudentPageWindow(self.currentgrade)

    #saves and erases page
    def save_and_erase(self):
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

from studentpagewindow import StudentPageWindow
from college import College