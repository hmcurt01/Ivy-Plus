import pickle
from tkinter import *
# save file
def save():
    with open('save.p', 'wb') as handle:
        pickle.dump(student_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


# load file
def load():
    with open('save.p', 'rb') as handle:
        b = pickle.load(handle)
    return b

def init():
    root.bind_class("Text","<Control-a>", selectall)

def selectall(event):
    event.widget.tag_add("sel","1.0",END)

# stores student objects
global student_dict
student_dict = {}
# token number used to determine student ids
# grade var used to determine what students are displayed

# loads saved students into student dictionary
student_dict = load()

global root
root = Tk()


