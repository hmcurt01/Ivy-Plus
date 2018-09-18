from tkinter import *
from data import root
from data import student_dict


# grade choosing page
class GradeWindow:
    def __init__(self):
        self.widgets = {}
        self.dropVar = StringVar()
        self.dropVar.set("Choose Class")
        self.classes = []
        self.draw_main()

    def draw_main(self):

        for i in student_dict:
            if student_dict[i].grade not in self.classes:
                self.classes.append(student_dict[i].grade)
        if not self.classes:
            self.classes = ["Please Add a Class"]

        self.widgets["addClassEntry"] = Entry(root)
        self.widgets["addClassEntry"].place(relx=.5, rely=.5, anchor=CENTER)

        self.widgets["addClassButton"] = Button(root, text="Add Class", command=lambda: self.add_class())
        self.widgets["addClassButton"].place(in_=self.widgets["addClassEntry"], relx=1, rely=1, anchor=SW,
                                             bordermode="outside")

        self.widgets["chooseOption"] = OptionMenu(root, self.dropVar, *self.classes,
                                                  command=lambda _: self.choose_class(self.dropVar.get()))
        self.widgets["chooseOption"].place(relx=.5, rely=.6, anchor=CENTER)

    # choose class to display students
    def choose_class(self, var):
        if var == "Please Add a Class":
            return
        self.erase_main()
        currentgrade = var
        StudentPageWindow(currentgrade)

    # add class to class list
    def add_class(self):
        self.classes.append(self.widgets["addClassEntry"].get())
        self.widgets["addClassEntry"].delete(0, END)
        self.widgets["chooseOption"].destroy()
        self.widgets["chooseOption"] = OptionMenu(root, self.dropVar, *self.classes,
                                                  command=lambda _: self.choose_class(self.dropVar.get()))
        self.widgets["chooseOption"].place(relx=.5, rely=.6, anchor=CENTER)

    # erase all
    def erase_main(self):
        for i in self.widgets:
            self.widgets[i].destroy()

from studentpagewindow import StudentPageWindow
