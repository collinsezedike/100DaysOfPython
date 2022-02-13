from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")

    global reps, marks
    reps = 0
    marks = ""

    checkmark.config(text=marks)


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            global marks
            marks += "✔"
            checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

BACKGROUND = YELLOW
marks = ""


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BACKGROUND)

# create a canvas widget
canvas = Canvas(width=200, height=230, bg=BACKGROUND, highlightthickness=0)

# convert the image to a Photo image
IMAGE = PhotoImage(file="tomato.png")
# because the type of file required
# for the image argument of the create_image method
# is a photo image and not jpg or png or otherwise

canvas.create_image(100, 115, image=IMAGE, )
timer_text = canvas.create_text(102, 135, text="00:00", fill="white", font=("Consolas", 35, "bold"))
canvas.grid(row=1, column=1)

# timer label
title_label = Label(text="Timer", bg=BACKGROUND, fg=GREEN, font=(FONT_NAME, 50))
title_label.grid(row=0, column=1)

# start button
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

# reset button
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

# check mark label
checkmark = Label(bg=BACKGROUND, fg=GREEN, font=(FONT_NAME, 20))
checkmark.grid(row=3, column=1)

window.mainloop()
