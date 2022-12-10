#Modules
from PyPDF2 import PdfReader
import pyttsx3

#Text to Speech
engine = pyttsx3.init ('sapi5')
voices = engine.getProperty('voices')
VoiceGender = engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)
def speak(texttospeech):
    engine.say(texttospeech)
    engine.runAndWait()

#PDF file path
reader =PdfReader(r"C:\Users\Elijah\Downloads\The Handmaids Tale [full text].pdf") 

#PDF page input up to 5 pages
page1 = reader.pages[int(input("Page: "))]
page2 = reader.pages[int(input("Page: "))]
page3 = reader.pages[int(input("Page: "))]
page4 = reader.pages[int(input("Page: "))]
page5 = reader.pages[int(input("Page: "))]

#Text extraction
text1 = page1.extract_text()
text2 = page2.extract_text()
text3 = page3.extract_text()
text4 = page4.extract_text()
text5 = page5.extract_text()

#Execute
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
