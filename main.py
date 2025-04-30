import pyttsx3
import PyPDF2
from tkinter import *
from tkinter.filedialog import *

engine = pyttsx3.init()

filelocation = askopenfilename() # Opens a file dialog to select the PDF file
with open(filelocation, "rb") as f:
    pdf = PyPDF2.PdfReader(f)



    string = ""
    for page in pdf.pages:
        string += page.extract_text()

engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
engine.say(string)  # Text to be spoken
engine.runAndWait()  # Wait until the speech is finished

 

