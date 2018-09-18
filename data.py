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


# stores student objects
global student_dict
student_dict = {}
# token number used to determine student ids
# grade var used to determine what students are displayed

# loads saved students into student dictionary
student_dict = load()

global root
root = Tk()
