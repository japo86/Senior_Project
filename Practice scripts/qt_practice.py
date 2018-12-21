#!/use/bin/python3.6
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import time

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.counter = 0

        layout = QVBoxLayout()

        #self.l = QLabel("Start")
        #b = QPushButton("DANGER!")

        #b.pressed.connect(self.oh_no)

        c = QPushButton("Start Scan")
        c.pressed.connect(self.scan_btn_pressed)
        self.le = QLineEdit()
        #layout.addWidget(self.l)
        #layout.addWidget(b)
        layout.addWidget(self.le)
        layout.addWidget(c)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

    def scan_btn_pressed(self):
        target = self.le.text()
        print(target)

    # def change_message(self):
    #     self.message = "OH NO"
    #
    # def oh_no(self):
    #     self.message = "Pressed"
    #
    #     for n in range(100):
    #         time.sleep(0.1)
    #         self.l.setText(self.message)
    #         QApplication.processEvents()


app = QApplication([])
window = MainWindow()
app.exec_()
