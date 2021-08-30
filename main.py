import pyttsx3
import pyPDF2
book = open('story.pdf', 'rb')
pdfReader = pyPDF2.pdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getaPage(4)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()