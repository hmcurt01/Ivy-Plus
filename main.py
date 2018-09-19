from tkinter import *
from gradewindow import GradeWindow
from data import root
from data import save
from data import student_dict
from printdata import printdict
printdict("stas", "2019")

root.minsize(1368, 720)
GradeWindow()
root.mainloop()
save()

