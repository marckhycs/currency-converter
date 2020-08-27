from tkinter import DoubleVar
from tkinter import Label
from tkinter import Entry
from tkinter import Tk
from tkinter import Button
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
import requests


def done():
    processingLabel.config(text = "Done!")


def conversion():
    usDollar()
    brPound()
    cadDollar()
    euro()
    done()

    


def usDollar():
    url = 'https://transferwise.com/gb/currency-converter/usd-to-php-rate?amount=1000'
    site = requests.get(url)
    soup = BeautifulSoup(site.content, 'html.parser')
    us = soup.find('span', class_='text-success').text

    pesoItem = float(peso.get())
    
    us = round(float(us), 2)

    pesoConverted = pesoItem/us
    pesoConverted = round(pesoConverted, 2)
    pesoUs = str(pesoConverted)
    usLabel.config(text ="$" + pesoUs)
  
    
    

def euro():
    url = 'https://transferwise.com/gb/currency-converter/eur-to-php-rate?amount=1000'
    site = requests.get(url)
    soup = BeautifulSoup(site.content, 'html.parser')
    eu = soup.find('span', class_='text-success').text
    
    pesoItem = float(peso.get())
    
    eu = round(float(eu), 2)

    pesoConverted = pesoItem/eu
    pesoConverted = round(pesoConverted, 2)
    pesoPound = str(pesoConverted)
    euLabel.config(text = "€" + pesoPound)
    
    
       
def brPound():
    url = 'https://transferwise.com/gb/currency-converter/gbp-to-php-rate?amount=1000'
    site = requests.get(url)
    soup = BeautifulSoup(site.content, 'html.parser')

    pound = soup.find('span', class_='text-success').text
    
    pesoItem = float(peso.get())
    
    pound = round(float(pound), 2)

    pesoConverted = pesoItem/pound
    pesoConverted = round(pesoConverted, 2)
    pesoPound = str(pesoConverted)
    poundLabel.config(text = "£" + pesoPound)
    
    

def cadDollar():
    url = 'https://transferwise.com/gb/currency-converter/cad-to-php-rate?amount=1000'
    site = requests.get(url)
    soup = BeautifulSoup(site.content, 'html.parser')

    cadollar = soup.find('span', class_='text-success').text
    pesoItem = float(peso.get())
    
    cadollar = round(float(cadollar), 2)

    pesoConverted = pesoItem/cadollar
    pesoConverted = round(pesoConverted, 2)
    pesoCad = str(pesoConverted)
    cadLabel.config(text = "$" + pesoCad)
    

def mainScreen():
    screen = Tk()
    screen.config(bg = 'white')
    screen.iconbitmap('images/65714.ico')
    screen.title("Online Currency Converter")
    
    converter = Image.open('images/converter.png')
    converter = converter.resize((200,70), Image.ANTIALIAS)
    converter = ImageTk.PhotoImage(converter)

    img_peso = Image.open('images/peso.jpg')
    img_peso = img_peso.resize((33,20), Image.ANTIALIAS)
    img_peso = ImageTk.PhotoImage(img_peso)

    img_can = Image.open('images/canada.png')
    img_can = img_can.resize((33,20), Image.ANTIALIAS)
    img_can = ImageTk.PhotoImage(img_can)

    img_euro = Image.open('images/euro.png')
    img_euro = img_euro.resize((33,20), Image.ANTIALIAS)
    img_euro = ImageTk.PhotoImage(img_euro)
     
    img_usa = Image.open('images/us.png')
    img_usa = img_usa.resize((33,20), Image.ANTIALIAS)
    img_usa = ImageTk.PhotoImage(img_usa)

    img_uk = Image.open('images/uk.jpg')
    img_uk = img_uk.resize((33,20), Image.ANTIALIAS)
    img_uk = ImageTk.PhotoImage(img_uk)
    
    Label(screen, image = converter, bg = 'white').grid(row = 0, column = 1, sticky = "W", columnspan =2, pady = 10, padx= 20)
    Label(screen, image = img_peso, bg = 'white').grid(row = 1 , sticky = "E", padx = 5)
    
    global peso
    global usLabel
    global poundLabel
    global cadLabel
    global euLabel
    global processingLabel

    peso = DoubleVar()
    Entry(screen, textvariable = peso, width = 25).grid(row = 1, column = 1, sticky = "W")
    Button(screen, text = 'Convert', width = 20, command = conversion).grid(row = 1, column = 2, sticky = "W")

    Label(screen, image = img_usa, bg = 'white').grid(row = 2, column = 0 , sticky = "E", padx = 5)
    Label(screen, text = "United States", font = ('Calibri', 12), bg = 'white').grid(row = 2, column = 1, sticky = "W", pady = 2)
    usLabel = Label(screen, font = ("Calibri", 12), fg = 'green', bg = 'white')
    usLabel.grid(row = 2, column = 2, sticky = "W", pady = 2)

    Label(screen, image = img_uk, bg = 'white').grid(row = 3, column = 0 , sticky = "E", padx = 5)
    Label(screen, text = "Great Britain", font = ('Calibri', 12), bg = 'white').grid(row = 3, column = 1, sticky = "W", pady = 2)
    poundLabel = Label(screen, font = ("Calibri", 12), fg = 'green', bg = 'white')
    poundLabel.grid(row = 3, column = 2, sticky = "W", pady = 2)

    Label(screen, image = img_can, bg = 'white').grid(row = 4, column = 0 , sticky = "E", padx = 5)
    Label(screen, text = "Canada", font = ('Calibri', 12), bg = 'white').grid(row = 4, column = 1, sticky = "W", pady = 2)
    cadLabel = Label(screen, font = ("Calibri", 12), fg = 'green', bg = 'white')
    cadLabel.grid(row = 4, column = 2, sticky = "W", pady = 2)

    Label(screen, image = img_euro, bg = 'white').grid(row = 5, column = 0 , sticky = "E", padx = 5)
    Label(screen, text = "Euro", font = ('Calibri', 12), bg = 'white').grid(row = 5, column = 1, sticky = "W", pady = 2)
    euLabel = Label(screen, font = ("Calibri", 12), fg = 'green', bg = 'white')
    euLabel.grid(row = 5, column = 2, sticky = "W", pady = 2)


    processingLabel = Label(screen, font = ("Calibri", 12), fg = 'green', bg = 'white')
    processingLabel.grid(row = 6, column = 1, sticky = "N", pady = 2)



    usDollar()
    brPound()
    cadDollar()
    euro()
    


    screen.mainloop()

mainScreen()