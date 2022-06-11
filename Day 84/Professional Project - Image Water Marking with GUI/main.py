import time
import os

from datetime import datetime
from tkinter import Tk, Entry, Button, END, CENTER
from tkinter import filedialog
from tkinter import messagebox

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def watermark(image_path):
    img = Image.open(image_path)
    img_w, img_h = img.size

    drawer = ImageDraw.Draw(img)
    font = ImageFont.truetype("Courier", 50)

    text = watermark_test.get()
    txt_w, txt_h = drawer.textsize(text, font)
    pos = img_w - txt_w - 50, img_h - txt_h - 200

    c_text = Image.new("RGB", (txt_w + 50, txt_h + 50), color="#000000")
    drawing = ImageDraw.Draw(c_text)
    drawing.text((20, 20), text, fill="#ffffff", font=font)
    c_text.putalpha(200)

    img.paste(c_text, pos, c_text)
    time_of_save = datetime.now()
    img.save(f"images/watermarked_{time_of_save.strftime('%Y%m%d_%H%M%S')}.jpg")


def get_image():
    if len(watermark_test.get()) > 30:
        messagebox.showinfo(title="Oops", message="Watermark text is too long. Shouldn't be more than 30")
    if len(watermark_test.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave the watermark text field empty")
    else:
        file_types = [("Images", ".jpg")]
        images_to_watermark = filedialog.askopenfilenames(parent=window, initialdir=os.getcwd(),
                                                          filetypes=file_types)
        for image in images_to_watermark:
            watermark(image)
            time.sleep(1)
        messagebox.showinfo(title="Completed", message="Watermarked all images Successfully")


window = Tk()
window.title("mywatermark.io")
window.config(padx=100, pady=200, bg="#bbeebb")
window.resizable(False, False)
window.geometry("500x350")

watermark_test = Entry(width=30)
watermark_test.focus()
watermark_test.insert(END, "@mywatermark.io")
watermark_test.place(relx=0.5, rely=0.9, anchor=CENTER)

sel_img_btn = Button(text="Select Image", command=get_image)
sel_img_btn.place(relx=0.5, rely=0.2, anchor=CENTER)

window.mainloop()
