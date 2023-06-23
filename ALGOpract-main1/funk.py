from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QGroupBox, QMessageBox, QHBoxLayout, QRadioButton, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QListWidget

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
        window2.setStyleSheet("background-color: darkgray;") #функция для смены цвета
        setting_button2.setStyleSheet('QPushButton {color: white;}')  
        button_1.setStyleSheet('QPushButton {color: white;}')  
        button_2.setStyleSheet('QPushButton {color: white;}')  
        button_3.setStyleSheet('QPushButton {color: white;}')  
        button_4.setStyleSheet('QPushButton {color: white;}')  
        button_5.setStyleSheet('QPushButton {color: white;}')  
        button_6.setStyleSheet('QPushButton {color: white;}')  
        button_7.setStyleSheet('QPushButton {color: white;}')  
        button_8.setStyleSheet('QPushButton {color: white;}')  
        button_9.setStyleSheet('QPushButton {color: white;}')  
        button_0.setStyleSheet('QPushButton {color: white;}')  
        button_plus.setStyleSheet('QPushButton {color: white;}')  
        button_minus.setStyleSheet('QPushButton {color: white;}')  
        button_multiply.setStyleSheet('QPushButton {color: white;}')  
        button_divide.setStyleSheet('QPushButton {color: white;}')  
        button_smooth.setStyleSheet('QPushButton {color: white;}')  
        button_c.setStyleSheet('QPushButton {color: white;}')  
        button_bracket_right.setStyleSheet('QPushButton {color: white;}')  
        button_bracket_left.setStyleSheet('QPushButton {color: white;}')  
        button_point.setStyleSheet('QPushButton {color: white;}')  
        button_negative_positive.setStyleSheet('QPushButton {color: white;}')  
    elif setting_button1.text() == "🌑":
        setting_button1.setText("💡")
        window2.setStyleSheet("background-color: white;") #функция для смены цвета
        setting_button2.setStyleSheet('QPushButton {color: dark;}')  
        button_1.setStyleSheet('QPushButton {color: dark;}')  
        button_2.setStyleSheet('QPushButton {color: dark;}')  
        button_3.setStyleSheet('QPushButton {color: dark;}')  
        button_4.setStyleSheet('QPushButton {color: dark;}')  
        button_5.setStyleSheet('QPushButton {color: dark;}')  
        button_6.setStyleSheet('QPushButton {color: dark;}')  
        button_7.setStyleSheet('QPushButton {color: dark;}')  
        button_8.setStyleSheet('QPushButton {color: dark;}')  
        button_9.setStyleSheet('QPushButton {color: dark;}')  
        button_0.setStyleSheet('QPushButton {color: dark;}')  
        button_plus.setStyleSheet('QPushButton {color: dark;}')  
        button_minus.setStyleSheet('QPushButton {color: dark;}')  
        button_multiply.setStyleSheet('QPushButton {color: dark;}')  
        button_divide.setStyleSheet('QPushButton {color: dark;}')  
        button_smooth.setStyleSheet('QPushButton {color: dark;}')  
        button_c.setStyleSheet('QPushButton {color: dark;}')  
        button_bracket_right.setStyleSheet('QPushButton {color: dark;}')  
        button_bracket_left.setStyleSheet('QPushButton {color: dark;}')  
        button_point.setStyleSheet('QPushButton {color: dark;}')  
        button_negative_positive.setStyleSheet('QPushButton {color: dark;}')  
    
def svet_tma2():
    if setting_button3.text() == "💡":
        setting_button3.setText("🌑")
        window1.setStyleSheet("background-color: darkgray;") #функция для смены цвета
        setting_button4.setStyleSheet('QPushButton {color: white;}')  
        button4.setStyleSheet('QPushButton {color: white;}')  
        button5.setStyleSheet('QPushButton {color: white;}')  
    elif setting_button3.text() == "🌑":
        setting_button3.setText("💡")
        window1.setStyleSheet("background-color: white;") #функция для смены цвета
        setting_button4.setStyleSheet('QPushButton {color: dark;}')  
        button4.setStyleSheet('QPushButton {color: dark;}')  
        button5.setStyleSheet('QPushButton {color: dark;}')  
        
 

def russ_engl():
    if setting_button2.text() == "РУССКИЙ":
        setting_button2.setText("ENGLISH")
        window2.setWindowTitle("Kiparh calculator")
    elif setting_button2.text() == "ENGLISH":
        setting_button2.setText("РУССКИЙ")
        window2.setWindowTitle("Kiparh калькулятор")         


def russ_engl2():
    if setting_button4.text() == "РУССКИЙ":
        setting_button4.setText("ENGLISH")
        button4.setText('Calculator')
        button5.setText('Smart Notes')
        window1.setWindowTitle("Main page")
    elif setting_button4.text() == "ENGLISH":
        setting_button4.setText("РУССКИЙ")
        button4.setText('Калькулятор')
        button5.setText('Умные заметки')
        window1.setWindowTitle("Главная страница")         

app = QApplication([])
window1 = QWidget()
window1.setWindowTitle('Главная страница')
window2 = QWidget()
window2.setWindowTitle('Kiparh калькулятор')
line1 = QHBoxLayout()
line2 = QVBoxLayout()
line3 = QVBoxLayout()
line4 = QVBoxLayout()
line5 = QVBoxLayout()
line6 = QHBoxLayout()
line7 = QVBoxLayout()
line8 = QVBoxLayout()
text1 = QLabel()
text2 = QLabel()
setting_button1 = QPushButton('💡')
setting_button2 = QPushButton('РУССКИЙ')
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
button4 = QPushButton('Калькулятор')
button5 = QPushButton('Умные заметки')
setting_button3 = QPushButton('💡')
setting_button4 = QPushButton('РУССКИЙ')
window1.setLayout(line6)
line6.addLayout(line7)
line6.addLayout(line8)
line7.addWidget(button4)
line7.addWidget(setting_button3)
line8.addWidget(button5)
line8.addWidget(setting_button4)
window2.setLayout(line1)
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
line4.addWidget(setting_button1)
line4.addWidget(button_bracket_right)
line4.addWidget(button_9)
line4.addWidget(button_6)
line4.addWidget(button_3)
line4.addWidget(button_point)
line5.addWidget(setting_button2)
line5.addWidget(button_divide)
line5.addWidget(button_multiply)
line5.addWidget(button_minus)
line5.addWidget(button_plus)
line5.addWidget(button_smooth)
window1.show()


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
setting_button1.clicked.connect(svet_tma)   
setting_button2.clicked.connect(russ_engl)
setting_button3.clicked.connect(svet_tma2)
setting_button4.clicked.connect(russ_engl2)
button4.clicked.connect(window2.show)



   

window3 = QWidget()
window3.setWindowTitle('Умные заметки')
window4 = QWidget()
window4.setWindowTitle('Руководство')
list_tags = QListWidget()
text3 = QLabel('Для создания заметки нажмите на кнопку "Создать" и в окне напишите заметку')
text4 = QLabel('Для удаления заметки нажмите на неё в панеле "Сохраненные заметки" и используйте кнопку "Удалить"')
text5 = QLabel('Сохраненные заметки')
button1 = QPushButton('Создать')
button2 = QPushButton('Удалить')
button3 = QPushButton('Руководство')
setting_button5 = QPushButton('💡')
setting_button6 = QPushButton('РУССКИЙ')
setting_button7 = QPushButton('💡')
setting_button8 = QPushButton('РУССКИЙ')
line9 = QVBoxLayout()
line10 = QVBoxLayout()
line11 = QHBoxLayout()
line12 = QHBoxLayout()
line13 = QVBoxLayout()
line14 = QVBoxLayout()
window3.setLayout(line11)
window4.setLayout(line12)
line12.addLayout(line13)
line12.addLayout(line14)
line13.addWidget(text3)
line13.addWidget(text4)
line14.addWidget(setting_button7)
line14.addWidget(setting_button8)
line11.addLayout(line9)
line11.addLayout(line10)
line9.addWidget(text5)
line10.addWidget(setting_button5)
line10.addWidget(setting_button6)
line10.addWidget(button3)
line10.addWidget(button2)
line10.addWidget(button1)
line9.addWidget(list_tags)
notes = []

def show_note():
    key = list_tags.selectedItems()[0].text()
    for note in notes:
        if note[0] == key:
            list_tags.addItems(note[2])

def add_note():
    note_name, ok = QInputDialog.getText(window3, "Добавить заметку", "Название заметки: ")
    if ok and note_name != "":
        note = list()
        note = [note_name, '', []]
        notes.append(note)
        list_tags.addItem(note[0])
        print(notes)
        with open(str(len(notes)-1)+".txt", "w") as file:
            file.write(note[0]+'\n')

def del_note():
    if list_tags.selectedItems():
        key = list_tags.selectedItems()[0].text()
        del notes[key]
        list_tags.clear()
        list_tags.addItems(notes)
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Заметка для удаления не выбрана!")



def svet_tma3():
    if setting_button5.text() == "💡":
        setting_button5.setText("🌑")
        window3.setStyleSheet("background-color: darkgray;") #функция для смены цвета
        setting_button6.setStyleSheet('QPushButton {color: white;}')  
        button1.setStyleSheet('QPushButton {color: white;}')  
        button2.setStyleSheet('QPushButton {color: white;}')  
        button3.setStyleSheet('QPushButton {color: white;}')  
        text5.setStyleSheet('QLabel {color: white;}') 
    elif setting_button5.text() == "🌑":
        setting_button5.setText("💡")
        window3.setStyleSheet("background-color: white;") #функция для смены цвета
        setting_button6.setStyleSheet('QPushButton {color: dark;}')  
        button1.setStyleSheet('QPushButton {color: dark;}')  
        button2.setStyleSheet('QPushButton {color: dark;}')  
        button3.setStyleSheet('QPushButton {color: dark;}')  
        text5.setStyleSheet('QLabel {color: dark;}') 


def svet_tma4():
    if setting_button7.text() == "💡":
        setting_button7.setText("🌑")
        window4.setStyleSheet("background-color: darkgray;") #функция для смены цвета
        setting_button8.setStyleSheet('QPushButton {color: white;}')  
        text3.setStyleSheet('QLabel {color: white;}') 
        text4.setStyleSheet('QLabel {color: white;}') 
    elif setting_button7.text() == "🌑":
        setting_button7.setText("💡")
        window4.setStyleSheet("background-color: white;") #функция для смены цвета
        setting_button8.setStyleSheet('QPushButton {color: dark;}')  
        text3.setStyleSheet('QLabel {color: dark;}') 
        text4.setStyleSheet('QLabel {color: dark;}') 


def russ_engl3():
    if setting_button6.text() == "РУССКИЙ":
        setting_button6.setText("ENGLISH")
        button1.setText('Create')
        button2.setText('Delete')
        button3.setText('Guide')
        text5.setText('Saved notes')
        window3.setWindowTitle("Smart Notes")
    elif setting_button6.text() == "ENGLISH":
        setting_button6.setText("РУССКИЙ")
        button1.setText('Создать')
        button2.setText('Удалить')
        button3.setText('Руководство')
        text5.setText('Сохраненные заметки')
        window3.setWindowTitle("Умные заметки")     

def russ_engl4():
    if setting_button8.text() == "РУССКИЙ":
        setting_button8.setText("ENGLISH")
        text3.setText('To create a note, click on the "Create" button and write a note in the window')
        text4.setText('To delete a note, click on it in the "Saved Notes" panel and use the "Delete" button')
        window4.setWindowTitle("Guide")
    elif setting_button8.text() == "ENGLISH":
        setting_button8.setText("РУССКИЙ")
        text3.setText('Для создания заметки нажмите на кнопку "Создать" и в окне напишите заметку')
        text4.setText('Для удаления заметки нажмите на неё в панеле "Сохраненные заметки" и используйте кнопку "Удалить"')
        window4.setWindowTitle("Руководство")     


list_tags.itemClicked.connect(show_note)
button1.clicked.connect(add_note)
button2.clicked.connect(del_note)
button3.clicked.connect(window4.show)
button5.clicked.connect(window3.show)
setting_button5.clicked.connect(svet_tma3)
setting_button6.clicked.connect(russ_engl3)
setting_button7.clicked.connect(svet_tma4)
setting_button8.clicked.connect(russ_engl4)




    

app.exec_()