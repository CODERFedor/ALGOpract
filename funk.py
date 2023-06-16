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
    text = even(text)        

def b_even_odd(text): #функция для кнопки "чётность/нечётность"
    text = int(text)

    if text % 2 == 0:
        text = "Число чётное"
    else:    
        text = "Число нечётное"

def b_c(text): #функция для кнопки "C"
    text = "" 

def b_negative_positive(): #функция для кнопки "-/+"
    text = evan(text)
    if text = 0:
        text = "0"
    elif text > 0:
        text = text - (text * 2)
        text = str(text) 
    elif text < 0:
        text = text * (-1)
        text = str(text)

def calculator(): #фунуция класического калькулятора
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
    button_negative_positive.clicked.connect(b_negative_positive)

def even_odd(): #функция проверки чётности числа
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