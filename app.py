import pyttsx3
import os
import webbrowser 
import PyPDF2

# driver code

# create object and assign voice
engine = pyttsx3.init()

voices = engine.getProperty('voices')
x = ""
print("please enter 0 for male and 1 for female voice:")

while x != "0" or x != "1" :
    x=input()
    print("please enter 0 for male and 1 for female voice:")
    if x=="0" or x=="1":
        break
# changing index changes voices but ony
# 0 and 1 are working here
engine.setProperty('voice', voices[int(x)].id)   #changing index, changes voices. 1 for female

engine.runAndWait()
print("")
print("")

# introduction
username = input("Enter username:")
print(username)
print(
    "  =============================================== Hello World!! ================================================")
engine.say('Hello '+username ,)

print("    My name is suraj ,I make this tool With this help of tool you can open below things.......")

print(
    "\n\t0.E-book Reader\n\t 1.MICROSOFT WORD \t 2.MICROSOFT POWERPOINT \n\t 3.MICROSOFT EXCEL \t 4.GOOGLE CHROME \n\t 5.VLC PLAYER     \t 6.ADOBE ILLUSTRATOR \n\t 7.ADOBE PHOTOSHOP \t 8.MICROSOFT EDGE \n\t 9.NOTEPAD        \t 10.TELEGRAM \n\t 11.PAINT \n\n\t\t   0. FOR EXIT")

print("\n        (YOU CAN USE NUMBER OR YOU CAN DO CHAT LIKE 'OPEN NOTEBOOK' etc....)")

print(
    "\n  ============================================ Welcome To My Tools ============================================")
pyttsx3.speak("Welcome to my tools")
print("")
print("")

pyttsx3.speak("chat with me with your requirements")

while True:
    # take input
    print("    CHAT WITH ME WITH YOUR REQUIREMENTS : ", end='')
    p = input()
    p = p.upper()
    print(p)

    if ("DONT" == p) or ("DON'T" == p) or ("NOT" == p):
        pyttsx3.speak("Type Again")
        print(".")
        print(".")
        continue

    elif ("READ"==p )or ("0"==p):
        book = open('dd.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        print(pages)
        pyttsx3.speak("reading the book.")

        for num in range(0, pages):
            page = pdfReader.getPage(num)
            text = page.extractText()

            engine.say(text)
            engine.runAndWait()
    # assignements for diffenet applications == the menu
    elif ("GOOGLE" == p) or ("SEARCH" == p) or ("WEB BROWSER" == p) or ("CHROME" == p) or ("BROWSER" == p) or (
            "4" == p):
        print("please enter your search query:\n")
        search = input() 
        pyttsx3.speak("Opening")
        pyttsx3.speak("Browser")
        print(".")
        print(".")
        url="https://www.google.com"
        if search:
            url = "https://www.google.com/search?q="+ search 
        webbrowser.open(url, new=1, autoraise=True)
    elif  ("IE" == p) or ("MSEDGE" == p) or ("EDGE" == p) or ("8" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("MICROSOFT EDGE")
        print(".")
        print(".")
        os.system("msedge")

    elif ("NOTE" == p) or ("NOTES" == p) or ("NOTEPAD" == p) or ("EDITOR" == p) or ("9" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("NOTEPAD")
        print(".")
        print(".")
        os.system("Notepad")

    elif ("VLCPLAYER" == p) or ("PLAYER" == p) or ("VIDEO PLAYER" == p) or ("5" == p) or ("VLC" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("VLC PLAYER")
        print(".")
        print(".")
        os.system("VLC")

    elif ("MSpaint" == p) or ("paint" == p) or ("paintcolor" == p) or ("11" == p) or ("mspaint" == p):
        pyttsx3.speak("opening mspaint")    
        os.system("mspaint")
    elif ("ILLUSTRATOR" == p) or ("AI" == p) or ("6" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("ADOBE ILLUSTRATOR")
        print(".")
        print(".")
        os.system("illustrator")

    elif ("PHOTOSHOP" == p) or ("PS" == p) or ("PHOTOSHOP CC" == p) or ("7" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("ADOBE PHOTOSHOP")
        print(".")
        print(".")
        os.system("photoshop")

    elif ("TELEGRAM" == p) or ("TG" == p) or ("10" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("TELEGRAM")
        print(".")
        print(".")
        os.system("telegram")

    elif ("EXCEL" == p) or ("MSEXCEL" == p) or ("SHEET" == p) or ("WINEXCEL" == p) or ("3" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("MICROSOFT EXCEL")
        print(".")
        print(".")
        os.system("excel")

    elif ("SLIDE" == p) or ("MSPOWERPOINT" == p) or ("PPT" == p) or ("POWERPNT" == p) or ("2" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("MICROSOFT POWERPOINT")
        print(".")
        print(".")
        os.system("powerpnt")

    elif ("WORD" == p) or ("MSWORD" == p) or ("1" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("MICROSOFT WORD")
        print(".")
        print(".")
        os.system("winword")

    # close the program
    elif ("EXIT" == p) or ("QUIT" == p) or ("CLOSE" == p) or ("0" == p):
        pyttsx3.speak("Exiting")
        break

    # for ivalid input
    else:
        pyttsx3.speak(p)
        print("Is Invalid,Please Try Again")
        pyttsx3.speak("is Invalid,Please try again")
        print(".")
        print(".")
