import sys
from PyQt5.QtWidgets import *

def window():
    #__inisialisasi pyqt5
    app = QApplication(sys.argv)
    window = QWidget()


    #__menyiapkan label, menempelkan label ke window
    #__settext, dan posisi
    first = 1
    while first <= 10:
        lb = QLabel(window)
        lb.setText("Hello World - " + str(first))
        lb.move(200, first*20)
        first += 1

    #__menentukan ukuran window, + title dan menampilkan
    window.setGeometry(400,100,700,500)
    window.setWindowTitle("PyQt5 Looping")
    window.setStyleSheet("background-color:#e6e6fa")
    window.show()
    sys.exit(app.exec_())

if __name__== '__main__':
    window()

