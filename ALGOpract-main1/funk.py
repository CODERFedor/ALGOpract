from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QGroupBox, QMessageBox, QHBoxLayout, QRadioButton, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

text = "" #переменная в которой хранится текст, который мы выводим

#функции
def b_1(text): #функция для кнопки "1"
    text += 1
def b_2(text): #функция для кнопки "2"
    text += 2
def b_3(text): #функция для кнопки "3"
    text += 3
def b_4(text): #функция для кнопки "4"
    text += 4
def b_5(text): #функция для кнопки "5"
    text += 5
def b_6(text): #функция для кнопки "6"
    text += 6
def b_7(text): #функция для кнопки "7"
    text += 7 
def b_8(text): #функция для кнопки "8"
    text += 8
def b_9(text): #функция для кнопки "9"
    text += 9
def b_0(text): #функция для кнопки "0"
    text += 0
def b_pl(text): #функция для кнопки "+"
    text += "+"
def b_mi(text): #функция для кнопки "-"
    text += "-"
def b_mu(text): #функция для кнопки "*"
    text += "*" 
def b_d(text): #функция для кнопки ":"
    text += ":"
def b_b_r(text):
    text += "("
def b_b_l(text):
    text += ")"
def b_p(text):
    text += '.'

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
    if text == 0:
        text = "0"
    elif text > 0:
        text = text * (-1)
        text = str(text) 
    elif text < 0:
        text = text * (-1)
        text = str(text)

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


app = QApplication([])
window = QWidget()
window.setWindowTitle('Калькулятор Kiparh')
line1 = QHBoxLayout()
line2 = QVBoxLayout()
line3 = QVBoxLayout()
line4 = QVBoxLayout()
line5 = QVBoxLayout()
text1 = QLabel()
text2 = QLabel()
text3 = QLabel()
text4 = QLabel()
button_1 = QPushButton('1')
button_2 = QPushButton('2')
button_3 = QPushButton('3')
button_4 = QPushButton('4')
button_5 = QPushButton('5')
button_6 = QPushButton('6')
button_7 = QPushButton('7')
button_8 = QPushButton('8')
button_9 = QPushButton('9')
button_0 = QPushButton('0')
button_plus = QPushButton('+')
button_minus = QPushButton('-')
button_multiply = QPushButton('*')
button_divide = QPushButton(':')
button_smooth = QPushButton('=')
button_c = QPushButton('c')
button_bracket_right = QPushButton('(')
button_bracket_left = QPushButton(')')
button_point = QPushButton('.')
button_negative_positive = QPushButton('-/+')
window.setLayout(line1)
line1.addLayout(line2)
line1.addLayout(line3)
line1.addLayout(line4)
line1.addLayout(line5)
line2.addWidget(text1)
line2.addWidget(button_c)
line2.addWidget(button_7)
line2.addWidget(button_4)
line2.addWidget(button_1)
line2.addWidget(button_negative_positive)
line3.addWidget(text2)
line3.addWidget(button_bracket_left)
line3.addWidget(button_8)
line3.addWidget(button_5)
line3.addWidget(button_2)
line3.addWidget(button_0)
line4.addWidget(text3)
line4.addWidget(button_bracket_right)
line4.addWidget(button_9)
line4.addWidget(button_6)
line4.addWidget(button_3)
line4.addWidget(button_point)
line5.addWidget(text4)
line5.addWidget(button_divide)
line5.addWidget(button_multiply)
line5.addWidget(button_minus)
line5.addWidget(button_plus)
line5.addWidget(button_smooth)
window.show()


button_1.clicked.connect(b_1)
button_2.clicked.connect(b_2)
button_3.clicked.connect(b_3)
button_4.clicked.connect(b_4)
button_5.clicked.connect(b_5)
button_6.clicked.connect(b_6)
button_7.clicked.connect(b_7)
button_8.clicked.connect(b_8)
button_9.clicked.connect(b_9)
button_0.clicked.connect(b_0)
button_plus.clicked.connect(b_pl)
button_minus.clicked.connect(b_mi)
button_multiply.clicked.connect(b_mu)
button_divide.clicked.connect(b_d)
button_smooth.clicked.connect(b_s)
button_c.clicked.connect(b_c)
button_bracket_right.clicked.connect(b_b_r)
button_bracket_left.clicked.connect(b_b_l)
button_point.clicked.connect(b_p)
button_negative_positive.clicked.connect(b_negative_positive)
button_smooth.clicked.connect(b_even_odd)        


   

    

app.exec_()