#Imports
from PyPDF2 import PdfReader
import pyttsx3

#Initialize the text to speech engine and set the voice to the first voice in the list of voices.
engine = pyttsx3.init ('sapi5')
voices = engine.getProperty('voices')
VoiceGender = engine.setProperty('voice', voices[0].id)
#Set the rate of the voice to 175.
engine.setProperty('rate', 175)

#Define a function that takes in a string of text and converts it to speech using the engine.
def speak(texttospeech):
    engine.say(texttospeech)
    engine.runAndWait()

#PDF file path
reader =PdfReader(r"C:\Users\Elijah\Downloads\The Handmaids Tale [full text].pdf")
#Read in the PDF file and store the pages in variables.
page1 = reader.pages[int(input("Page: "))]
page2 = reader.pages[int(input("Page: "))]
page3 = reader.pages[int(input("Page: "))]
page4 = reader.pages[int(input("Page: "))]
page5 = reader.pages[int(input("Page: "))]

#Extract the text from each page and store it in a separate variable.
text1 = page1.extract_text()
text2 = page2.extract_text()
text3 = page3.extract_text()
text4 = page4.extract_text()
text5 = page5.extract_text()

#Infinite loop that prints the text from each page and converts it to speech.
while True:
 print(text1)
 speak (text1)
 print(text2)
 speak (text2)
 print(text3)
 speak (text3)
 print(text4)
 speak (text4)
 print(text5)
 speak (text5)
