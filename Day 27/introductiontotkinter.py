from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# creating a label
my_label = Label(text="I am a label", font=("consolas", 16))
my_label.pack()

# to configure/change an argument/property of an object
my_label["text"] = "New label"
# or more appropriately
my_label.config(text="New label")


# a listening function of the button
def button_clicked():
    # when the button gets clicked, the label changes 
    my_label.config(text=input.get())


# create a button
button = Button(text="Click  me!", command=button_clicked)
button.pack()

# input - Entry
input = Entry(width=30)
# add some text to begin with
input.insert(END, string="Some text to begin with.")
input.pack()

# to retrieve the inputted text
print(input.get())


# text
text = Text(height=5, width=30)
# put cursor in textbox
text.focus()
# add some text to begin with
text.insert(END, "Example of a multiline text entry.")
# get current calue in line 1, xharacter 0
text.get("1.0", END)
text.pack()


# spinbox
def spinbox_used():
    # gets the current value in spinbox
    print(spinbox.get())


spinbox= Spinbox(from_=0, to=100, width=5, command=spinbox_used)
spinbox.pack()


# scale
# called with current value
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, width=50, command=scale_used)
scale.pack()


# checkbox
def checkbox_used():
    # prints 1 if button is checked, otherwise 0
    print(checked_state.get())


checked_state = IntVar()
checkbox = Checkbutton(text="Is On?", variable=checked_state, command=checkbox_used)
checkbox.pack()


# radio button
def radio_used():
    print(radio_state.get())


# variable to hold which radio button is checked
radio_state = IntVar()

radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radiobutton3 = Radiobutton(text="Option 3", value=3, variable=radio_state, command=radio_used)

radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()


# list box
def listbox_used(event):
    # gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
