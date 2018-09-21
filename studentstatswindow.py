from tkinter import *
from studentpagewindow import StudentPageWindow
from data import root
from data import student_dict


class StudentStatsWindow:
    def __init__(self, currentgrade):
        selectall
        self.currentgrade=currentgrade
        self.widgets = {}
        self.draw_main()

    def selectall(self, event):
        event.widget.tag_add("sel", "1.0", END)

    #draw main window
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
        li = 0
        firstgen = 0
        cogat = 0

        studentamts = {
            "totalaid":0,
            "accepted":0,
            "totalcolleges":0,
            "studentamt":0,
            "gpa":0,
            "meetamount":0,
            "act":0,
            "menteehours":0,
            "minor":0,
            "li":0,
            "firstgen":0,
            "cogat":0
        }

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
                    studentamts["meetamount"] += 1
                if student_dict[i].act != "":
                    act += float(student_dict[i].act)
                    studentamts["act"] += 1
                if student_dict[i].menteehours != "":
                    menteehours += float(student_dict[i].menteehours)
                    studentamts["menteehours"] += 1
                if student_dict[i].gpa != "":
                    gpa += float(student_dict[i].gpa)
                    studentamts["gpa"] += 1
                if student_dict[i].cogat != "":
                    cogat += float(student_dict[i].cogat)
                    studentamts["cogat"] += 1
                if student_dict[i].minority == "Y" or student_dict[i].minority == "y":
                    minor += 1
                    studentamts["minority"] += 1
                if student_dict[i].lowincome == "Y" or student_dict[i].minority == "n":
                    li += 1
                    studentamts["li"] += 1
                if student_dict[i].firstgen == "Y" or student_dict[i].firstgen == "n":
                    firstgen += 1
                    studentamts["firstgen"] += 1
                studentamt += 1

        try:
            avgaccept = float(accepted) / float(totalcolleges) * 100
        except ZeroDivisionError:
            avgaccept = 0
        for i in studentamts:
            if studentamts[i] == 0:
                studentamts[i] = 1
        avggpa = float(gpa) / studentamts["gpa"]
        avgaid = float(totalaid) / studentamts["totalaid"]
        avgmeetamount = meetamount / studentamts["meetamount"]
        avgact = act / studentamts["act"]
        avgmenteehours = menteehours / studentamts["menteehours"]
        minor = minor / studentamts["minor"] * 100
        li = li / studentamts["li"] * 100
        cogat = cogat / studentamts["cogat"] * 100
        firstgen = firstgen / studentamts["firstgen"] * 100

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

        self.widgets["avgmeetamount"] = Label(root, text="Average Meet Amount: " + '%.2f' % avgmeetamount, height=2,
                                              width=30,
                                              )
        self.widgets["avgmeetamount"].place(in_=self.widgets["totalstudents"], anchor=SW, relx=0, rely=2,
                                            bordermode="outside")

        self.widgets["avgact"] = Label(root, text="Average ACT: " + '%.2f' % avgact, height=2,
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

        self.widgets["%li"] = Label(root, text="Low Income Percentage: " + '%.2f' % li + "%", height=2, width=30, bg=
                                    "lightgrey")
        self.widgets["%li"].place(in_=self.widgets["%minor"], anchor=SW, relx=0, rely=2, bordermode="outside")

        self.widgets["avgcogat"] = Label(root, text="Average COGAT: " + '%.2f' % cogat, height=2, width=30, bg=
        "grey62")
        self.widgets["avgcogat"].place(in_=self.widgets["%li"], anchor=SW, relx=0, rely=2, bordermode="outside")

        self.widgets["firstgen"] = Label(root, text="First Gen Percentage: " + '%.2f' % firstgen + "%",
                                         height=2, width=30)
        self.widgets["firstgen"].place(in_=self.widgets["avgcogat"], anchor=SW, relx=0, rely=2, bordermode="outside")


    #back to student page
    def back(self):
        for i in self.widgets:
            self.widgets[i].destroy()
        StudentPageWindow(self.currentgrade)