from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QListWidget, QListWidgetItem,
        QLineEdit, QTextEdit,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox, QMessageBox, QFileDialog)


app = QApplication([])

#вікно
win = QWidget()
win.resize(700,500)
win.setWindowTitle("Easy Editor")
# win.setStyleSheet("background-color: #666666; color: #ffffff;")

#віджети вікна

img_list = QListWidget() #список картинок
open_folder_btn  = QPushButton("Відкрити папку")
open_folder_btn.setStyleSheet("width: 100px; height:30px;")
open_folder_btn.setStyleSheet("color: #ffffff")

image_lb = QLabel("Картинка")

left_btn = QPushButton("Вліво")
right_btn = QPushButton("Вправо")
mirror_btn = QPushButton("Дзеркало")
sharpen_btn = QPushButton("Різкість")
black_btn = QPushButton("Чорно-біле")

#напрямні лінії
main_line = QHBoxLayout()

col_1 = QVBoxLayout()
col_2 = QVBoxLayout()

row_1 = QHBoxLayout()

row_1.addWidget(left_btn)
row_1.addWidget(right_btn)
row_1.addWidget(mirror_btn)
row_1.addWidget(sharpen_btn)
row_1.addWidget(black_btn)

col_1.addWidget(open_folder_btn)
col_1.addWidget(img_list)

col_2.addWidget(image_lb)
col_2.addLayout(row_1)

main_line.addLayout(col_1, stretch=1)
main_line.addLayout(col_2, stretch=2)

win.setLayout(main_line)

workdir = ''

def chooseWorkDir():
        global workdir
        workdir = QFileDialog.getExistingDirectory() #запускаємо вікно вибору папки
        print(workdir)

def filter(filenames,extensions):
        for filename in filenames:
            for ext in extensions:
                if filename.endwith(ext):
                    result.append(filename)



def openFolder():
    try:
        chooseWorkDir()
        filenames = os.listdir(worddir)
        extensions = [".jpg",".png",".jpeg", ".gif", ".bmp"]
        imga = filter(filenames,extensions)
        filter(filenames,extensions)
        print(images)
        img_list.clear
        img_list.addItems(images)
    except:
        print("Папку не вибрано")


open_folder_btn.clicked.connect(openFolder)

win.show()
app.exec_()
