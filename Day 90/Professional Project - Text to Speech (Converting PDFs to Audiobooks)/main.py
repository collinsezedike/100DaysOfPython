import pyttsx3
import pdfplumber

with pdfplumber.open("file.pdf") as pdf:
    all_content = ""
    for page in pdf.pages:
        all_content+=page.extract_text()

engine = pyttsx3.init()
engine.save_to_file(all_content, 'audio.mp3')
engine.runAndWait()
