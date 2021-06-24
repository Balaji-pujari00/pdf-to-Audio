import pyttsx3
import PyPDF2
book=open('python3.pdf','rb')
reader=PyPDF2.PdfFileReader(book)
audio=pyttsx3.init()
page=reader.getPage(1)
text=page.extractText()
audio.say(text)
audio.runAndWait()