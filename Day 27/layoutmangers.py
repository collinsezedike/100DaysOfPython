# The three layout managers are:
# Pack
# Place and
# Grid

from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# add padding to window
window.config(padx=100, pady=200)


def button_clicked():
    my_label.config(text=input.get())


# Label
my_label = Label(text="I am a label", font=("consolas", 16))
my_label.config(text="New label")
# using pack
# my_label.pack(side="bottom")
# using place
# my_label.place(x=100, y=200)
# using grid
my_label.grid(row=1, column=1)
# add padding to a widget
my_label.config(padx=20, pady=100)

# Button
button = Button(text="New Button", command=button_clicked)
button.grid(row=1, column=3)

# Button
button = Button(text="Click  me!", command=button_clicked)
button.grid(row=2, column=2)

# Entry
input = Entry(width=30)
print(input.get())
input.grid(row=3, column=4)



window.mainloop()
