from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QGroupBox, QMessageBox, QHBoxLayout, QRadioButton, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

text = "" #переменная в которой хранится текст, который мы выводим

#функции
def b_1(text): #функция для кнопки "1"
    text += "1"
def b_2(text): #функция для кнопки "2"
    text += "2"
def b_3(text): #функция для кнопки "3"
    text += "3"
def b_4(text): #функция для кнопки "4"
    text += "4"
def b_5(text): #функция для кнопки "5"
    text += "5"
def b_6(text): #функция для кнопки "6"
    text += "6"
def b_7(text): #функция для кнопки "7"
    text += "7"  
def b_8(text): #функция для кнопки "8"
    text += "8"
def b_9(text): #функция для кнопки "9"
    text += "9"
def b_pl(text): #функция для кнопки "+"
    text += "+"
def b_mi(text): #функция для кнопки "-"
    text += "-"
def b_mu(text): #функция для кнопки "*"
    text += "*" 
def b_d(text): #функция для кнопки ":"
    text += "/"

def b_s(text): #функция для кнопки "="
    text = evel(text)        

def b_even_odd(text): #функция для кнопки "чётность/нечётность" (=)
    text = int(text)

    if text % 2 == 0:
        text = "Число чётное"
    else:    
        text = "Число нечётное"

def b_c(text): #функция для кнопки "C"
    text = ""

def b_naturalness(text): #функция для кнопки "натуральное/не натуральное" (=)
    text = int(text)
    if text > 0:
        text = "число натуральное"
    elif text < 0:
        text = "число не натуральное"
    elif text == 0:
        text = "число не натуральное"

#спец-функции
def svet_tma():
    if setting_button1.text() == "💡":
        setting_button1.setText("🌑")
        main_win.setStyleSheet("background-color: darkgray;") #функция для смены цвета
        setting_button2.setStyleSheet('QPushButton {color: white;}')  
        setting_button3.setStyleSheet('QPushButton {color: white;}')
    elif setting_button1.text() == "🌑":
        setting_button1.setText("💡")
        main_win.setStyleSheet("background-color: white;") #функция для смены цвета
        setting_button2.setStyleSheet('QPushButton {color: dark;}')  
        setting_button3.setStyleSheet('QPushButton {color: dark;}')      

def russ_engl():
    if setting_button2.text() == "РУССКИЙ":
        setting_button2.setText("ENGLISH")
        setting_button3.setText("CONTACT DEVELOPERS")
        main_win.setWindowTitle("Kiparh calculator")
    elif setting_button2.text() == "ENGLISH":
        setting_button2.setText("РУССКИЙ")
        setting_button3.setText("СВЯЗАТЬСЯ С РАЗРАБОТЧИКАМИ")
        main_win.setWindowTitle("Kiparh калькулятор")         

def calculator(): #фунуция класического калькулятора
    while True:
        button_1.clicked.connect(b_1)
        button_2.clicked.connect(b_2)
        button_3.clicked.connect(b_3)
        button_4.clicked.connect(b_4)
        button_5.clicked.connect(b_5)
        button_6.clicked.connect(b_6)
        button_7.clicked.connect(b_7)
        button_8.clicked.connect(b_8)
        button_9.clicked.connect(b_9)
        button_plus.clicked.connect(b_pl)
        button_minus.clicked.connect(b_mi)
        button_multiply.clicked.connect(b_mu)
        button_divide.clicked.connect(b_d)
        button_smooth.clicked.connect(b_s)
        button_c.clicked.connect(b_c)
        if text[-1] == "=":
            text = eval(text)
            break

def even_odd(): #функция проверки чётности числа
    while True: 
        button_1.clicked.connect(b_1)
        button_2.clicked.connect(b_2)
        button_3.clicked.connect(b_3)
        button_4.clicked.connect(b_4)
        button_5.clicked.connect(b_5)
        button_6.clicked.connect(b_6)
        button_7.clicked.connect(b_7)
        button_8.clicked.connect(b_8)
        button_9.clicked.connect(b_9)
        button_smooth.clicked.connect(b_even_odd)
        if text[-1] == "=":
            b_even_odd()
            break

def naturalness(): #фунуция провереки натуральности
    while True:
        button_1.clicked.connect(b_1)
        button_2.clicked.connect(b_2)
        button_3.clicked.connect(b_3)
        button_4.clicked.connect(b_4)
        button_5.clicked.connect(b_5)
        button_6.clicked.connect(b_6)
        button_7.clicked.connect(b_7)
        button_8.clicked.connect(b_8)
        button_9.clicked.connect(b_9)
        button_minus.clicked.connect(b_mi)
        button_smooth.clicked.connect(b_s)
        if text[-1] == "=":
            b_naturalness()
            break