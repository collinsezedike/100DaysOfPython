from tkinter import *
import pyperclip


FONT = ("consolas", 15)
BACKGROUND = "#1d3557"

idleness_indicator = list("|"*5)

count_time = 5*60  # in secsonds
mins, secs = divmod(count_time, 60)
countdown_timer = f"{mins:02d}:{secs:02d}"


def start_typing():
    def on_click(event):
        window.after(1001, regulator)
        text_area.configure(state=NORMAL)
        text_area.delete("1.0", END)
        text_area.unbind('<Button-1>', on_click_id)  # make the callback only work once

    def regulator():
        global idleness_indicator, count_time

        def detect_typing(key):
            global idleness_indicator
            idleness_indicator = list("|"*5)
            idleness_label.config(text=idleness_indicator)

        def count_down():
            global count_time
            count_time -= 1
            mins, secs = divmod(count_time, 60)
            countdown_timer = f"{mins:02d}:{secs:02d}"
            countdown_label.config(text=countdown_timer)

        try:
            idleness_indicator.pop()
        except IndexError:
            text_area.delete("1.0", END)
            idleness_indicator = list("|"*5)

            count_time = 60*5  # in secsonds
            mins, secs = divmod(count_time, 60)
            countdown_timer = f"{mins:02d}:{secs:02d}"
            countdown_label.config(text=countdown_timer)
        else:
            key_bind_id = text_area.bind('<Key>', detect_typing)
        finally:
            idleness_label.config(text=idleness_indicator)

        if count_time == 0:
            text_area.unbind('<Key>', key_bind_id)
            idleness_indicator = list("|"*5)
            count_time = 5  # in seconds
            text = text_area.get("1.0", END)
            time_up(text)
            return
        else:
            count_down()

        window.after(1000, regulator)

    for widget in window.winfo_children():
        widget.destroy()

    countdown_label = Label(text=countdown_timer, font=FONT)
    countdown_label.config(fg="white", bg=BACKGROUND)
    countdown_label.place(relx=-0.08, rely=-0.01, anchor=CENTER)

    idleness_label = Label(text=idleness_indicator, font=FONT)
    idleness_label.config(fg="white", bg=BACKGROUND)
    idleness_label.place(relx=1.02, rely=-0.01, anchor=CENTER)

    text_area = Text(padx=20, pady=10, font=FONT, border=0)
    text_area.config(bg="#111", fg="white", width=65, insertbackground="white")
    text_area.insert("1.0", "Start typing...")
    text_area.configure(state=DISABLED)
    text_area.place(relx=0.5, rely=0.55, anchor=CENTER, height=500)
    
    on_click_id = text_area.bind('<Button-1>', on_click)


def time_up(typed_text):
    for widget in window.winfo_children():
        widget.destroy()
    
    pyperclip.copy(typed_text)

    retype_button = Button(text="Type again", command=start_typing)
    retype_button.config(padx=50, pady=10, font=FONT, border=0)
    retype_button.place(relx=0.3, rely=0.6, anchor=CENTER)

    quit_button = Button(text="Quit", command=end_program)
    quit_button.config(padx=50, pady=8, font=FONT, border=2, bg=BACKGROUND, fg="white")
    quit_button.place(relx=0.7, rely=0.6, anchor=CENTER)

    info_label = Label(text="Your writing has been copied to your clipboard.")
    info_label.config(font=FONT, bg=BACKGROUND, fg="white")
    info_label.place(relx=0.5, rely=0.45, anchor=CENTER)


def end_program():
    window.destroy()


window = Tk()
window.title("cantstoptyping.org")
window.geometry("800x600")
window.config(bg=BACKGROUND, padx=100, pady=50)
window.resizable(False, False)

intro_label = Label(text="Write for 5 minutes without stopping else,\nyou lose everything you have typed.")
intro_label.config(font=("consolas", 20, "bold"), bg=BACKGROUND, fg="white")
intro_label.place(relx=0.5, rely=0.45, anchor=CENTER)

start_button = Button(text="Start Typing", command=start_typing)
start_button.config(padx=50, pady=10, font=FONT, border=0)
start_button.place(relx=0.5, rely=0.65, anchor=CENTER)

window.mainloop()
