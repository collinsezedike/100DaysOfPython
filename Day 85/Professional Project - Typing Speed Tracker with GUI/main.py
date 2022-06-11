from tkinter import Tk, Label, Button, Text, END, CENTER
from paragraph import Paragraph
import timeit


# these variables will be globalized
starttime = None
typing_area = None
test_paragraph = None


def start_test():
    global starttime, typing_area, test_paragraph

    for widgets in window.winfo_children():
        widgets.destroy()

    paragraph = Paragraph()
    
    test_paragraph = paragraph.get_random_paragraph()
    window.title("Start typing")

    test_label = Label(text=test_paragraph, width=60, justify="left")
    # so that the test paragraph wraps the text and the width is automatically set
    test_label.bind('<Configure>', lambda e: test_label.config(wraplength=test_label.winfo_width()))
    test_label.config(padx=20, pady=10, bg="#3e3e3e", fg="white", font=("consolas", 16))
    test_label.place(relx=0.5, rely=0.2, anchor=CENTER)

    test_paragraph = test_paragraph.split(" ")

    typing_area = Text(padx=20, pady=10, width=60, font=("consolas", 16))
    typing_area.focus()
    typing_area.place(relx=0.5, rely=0.6, anchor=CENTER, height=180)

    stop_button = Button(text="Stop timer", command=end_test)
    stop_button.config(padx=50, pady=10, font=("consolas", 15), border=0)
    stop_button.place(relx=0.5, rely=0.9, anchor=CENTER)

    # start the timer
    starttime = timeit.default_timer()


def end_test():
    # end the timer
    endtime = timeit.default_timer()
    time_difference = (endtime - starttime) / 60
    typed_paragraph = typing_area.get("1.0", END).split(" ")
    correctly_typed_words = 0
    for typed_text, test_text in zip(typed_paragraph, test_paragraph):
        if typed_text == test_text:
            correctly_typed_words += 1
    
    typing_speed = round(correctly_typed_words / time_difference)

    window.title("Your score")
    for widgets in window.winfo_children():
        widgets.destroy()
    a_label = Label(text="Your typing speed is...")
    a_label.config(padx=5, bg="#98B4AA", fg="black", font=("open sans", 35, "bold"))
    a_label.place(relx=0.5, rely=0.3, anchor=CENTER)

    speed_label = Label(text=f"{typing_speed} wpm")
    speed_label.config(padx=5, bg="#98B4AA", fg="black", font=("consolas", 35, "bold"))
    speed_label.place(relx=0.5, rely=0.45, anchor=CENTER)
    
    restart_button = Button(text="Retake test", command=start_test)
    restart_button.config(padx=50, pady=10, font=("consolas", 15), border=0)
    restart_button.place(relx=0.3, rely=0.7, anchor=CENTER)

    quit_button = Button(text="Quit", command=end_program)
    quit_button.config(padx=50, pady=8, font=("consolas", 15), border=2, bg="#98B4AA", fg="white")
    quit_button.place(relx=0.7, rely=0.7, anchor=CENTER)


def end_program():
    window.destroy()


window = Tk()
window.geometry("800x600")
window.title("canitypefast.net")
window.config(bg="#98B4AA", padx=100, pady=50)
window.resizable(False, False)

heading = Label(text="How fast can you type?")
heading.config(padx=5, bg="#98B4AA", fg="black", font=("open sans", 35, "bold"))
heading.place(relx=0.5, rely=0.43, anchor=CENTER)

start_button = Button(text="Start test", command=start_test)
start_button.config(padx=50, pady=10, font=("consolas", 15), border=0)
start_button.place(relx=0.5, rely=0.6, anchor=CENTER)

window.mainloop()
