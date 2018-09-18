from tkinter import *
from studentpagewindow import StudentPageWindow
from data import root
from data import student_dict


class StudentStatsWindow:
    def __init__(self, currentgrade):
        self.currentgrade=currentgrade
        self.widgets = {}
        self.draw_main()

    def draw_main(self):
        self.widgets["backButton"] = Button(root, text="Back", command=lambda: self.back())
        self.widgets["backButton"].place(relx=0, rely=0, anchor=NW, bordermode="outside")
        totalaid = 0
        accepted = 0
        totalcolleges = 0
        studentamt = 0
        gpa = 0
        meetamount = 0
        act = 0
        menteehours = 0
        minor = 0

        for i in student_dict:
            if student_dict[i].grade == self.currentgrade:
                for o in student_dict[i].colleges:
                    if student_dict[i].colleges[o].accept == "Yes" or student_dict[i].colleges[o].accept == "No":
                        totalcolleges += 1
                        if student_dict[i].colleges[o].accept == "Yes":
                            accepted += 1
                    totalaid += float(student_dict[i].colleges[o].aid)
                if student_dict[i].meetamount != "":
                    meetamount += float(student_dict[i].meetamount)
                if student_dict[i].act != "":
                    act += float(student_dict[i].act)
                if student_dict[i].menteehours != "":
                    menteehours += float(student_dict[i].menteehours)
                if student_dict[i].gpa != "":
                    gpa += float(student_dict[i].gpa)
                if student_dict[i].minority == "Y" or student_dict[i].minority == "y":
                    minor += 1
                studentamt += 1

        try:
            avgaccept = float(accepted) / float(totalcolleges) * 100
        except ZeroDivisionError:
            avgaccept = 0

        avggpa = float(gpa) / float(studentamt)
        avgaid = float(totalaid) / float(studentamt)
        avgmeetamount = meetamount / studentamt
        avgact = act / studentamt
        avgmenteehours = menteehours / studentamt
        minor = minor / studentamt * 100

        self.widgets["totalaid"] = Label(root, text="Total Aid: " + '${:,.2f}'.format(totalaid), bg="lightgrey", bd=2,
                                         height=2, width=30)
        self.widgets["totalaid"].place(anchor=CENTER, rely=.1, relx=.5)
        self.widgets["totalaccept"] = Label(root, text="Avg Acceptance Rate: " + '%.2f' % avgaccept + "%",
                                            bg="grey62", height=2, width=30)
        self.widgets["totalaccept"].place(in_=self.widgets["totalaid"], anchor=SW, rely=2, relx=0,
                                          bordermode="outside")
        self.widgets["avggpa"] = Label(root, text="Average GPA: " + '%.2f' % avggpa, width=30,
                                       height=2)
        self.widgets["avggpa"].place(in_=self.widgets["totalaccept"], anchor=SW, relx=0, rely=2, bordermode="outside")

        self.widgets["avgaid"] = Label(root, text="Average Aid: " + '${:,.2f}'.format(avgaid), height=2, width=30,
                                       bg="lightgrey")
        self.widgets["avgaid"].place(in_=self.widgets["avggpa"], anchor=SW, relx=0, rely=2, bordermode="outside")

        self.widgets["totalstudents"] = Label(root, text="Class Size: " + str(studentamt), height=2, width=30,
                                              bg="grey62")
        self.widgets["totalstudents"].place(in_=self.widgets["avgaid"], anchor=SW, relx=0, rely=2, bordermode="outside")

        self.widgets["avgmeetamount"] = Label(root, text="Average Meet Amount: " + str(avgmeetamount), height=2,
                                              width=30,
                                              )
        self.widgets["avgmeetamount"].place(in_=self.widgets["totalstudents"], anchor=SW, relx=0, rely=2,
                                            bordermode="outside")

        self.widgets["avgact"] = Label(root, text="Average ACT: " + str(avgact), height=2,
                                       width=30, bg="lightgrey"
                                       )
        self.widgets["avgact"].place(in_=self.widgets["avgmeetamount"], anchor=SW, relx=0, rely=2,
                                     bordermode="outside")

        self.widgets["avgmenteehours"] = Label(root, text="Average Mentee Hours: " + '%.2f' % avgmenteehours, height=2,
                                               width=30, bg="grey62"
                                               )
        self.widgets["avgmenteehours"].place(in_=self.widgets["avgact"], anchor=SW, relx=0, rely=2,
                                             bordermode="outside")
        self.widgets["%minor"] = Label(root, text="Minority Percentage: " + '%.2f' % minor + "%", height=2, width=30,
                                       )
        self.widgets["%minor"].place(in_=self.widgets["avgmenteehours"], anchor=SW, relx=0, rely=2,
                                     bordermode="outside")



    def back(self):
        for i in self.widgets:
            self.widgets[i].destroy()
        StudentPageWindow(self.currentgrade)