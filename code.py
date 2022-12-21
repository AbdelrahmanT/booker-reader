import PyPDF3
import pyttsx3
import pdfplumber

book_pdf = PyPDF3.PdfFileReader(open("the_devoted_friend.pdf", 'rb'))

pages = book_pdf.numPages

book_string = ''

with pdfplumber.open("the_devoted_friend.pdf") as pdf:
    
    for page in pdf.pages:
        text = page.extract_text()
        book_string += text


engine = pyttsx3.init()

engine.setProperty('rate', 100)
engine.setProperty('volume', 100)
book_string += text

for line in book_string.split("."):
    print(line)
    engine.say(line)
    engine.runAndWait()
    
engine.say(book_string)
engine.runAndWait()