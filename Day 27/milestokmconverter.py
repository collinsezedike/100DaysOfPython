from tkinter import *


def convert_miles_to_km():
    miles = float(miles_input.get())
    miles_in_km = round(miles * 1.6, 2)   
    converted_miles.config(text=miles_in_km)


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=120)
window.config(padx=70, pady=30)


miles_in_km = 0

# Entry for miles input
miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)
miles_input.insert(END, 0)
miles_input.focus()

# label for "miles"
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

# label for "is equal to"
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

# label for calculated km
converted_miles = Label(text=miles_in_km)
converted_miles.grid(row=1, column=1)

# label for "km"
km_label = Label(text="Km")
km_label.grid(row=1, column=2)

# button for convert
convert_button = Button(text="Convert", command=convert_miles_to_km)
convert_button.grid(row=2, column=1)

window.mainloop()
