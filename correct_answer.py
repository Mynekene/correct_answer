from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QRadioButton, QMessageBox
app = QApplication([])
window = QWidget()
window.resize(500, 400)
window.move(450, 150)

question = QLabel("Скільки буде 2+2*2")
button1 = QRadioButton("4")
button2 = QRadioButton("10")
button3 = QRadioButton("8")
button4 = QRadioButton("6")
Message = QMessageBox()

layout1 = QHBoxLayout()
layout1.addWidget(button1, alignment = Qt.AlignCenter)
layout1.addWidget(button2, alignment = Qt.AlignCenter)

layout2 = QHBoxLayout()
layout2.addWidget(button3, alignment = Qt.AlignCenter)
layout2.addWidget(button4, alignment = Qt.AlignCenter)

main_layout = QVBoxLayout()
main_layout.addWidget(question, alignment = Qt.AlignCenter)
main_layout.addLayout(layout1)
main_layout.addLayout(layout2)

window.setLayout(main_layout)

def win():
    qm = QMessageBox()
    qm.setText("You win")
    qm.exec_()

def lose():
    qm = QMessageBox()
    qm.setText("You lose")
    qm.exec_()

button1.clicked.connect(lose)
button2.clicked.connect(lose)
button3.clicked.connect(lose)
button4.clicked.connect(win)

window.show()
app.exec_()
