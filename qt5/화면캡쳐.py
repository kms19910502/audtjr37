## Ex 10-4. 화면 캡처 프로그램.

import sys
from PyQt5.QtWidgets import QLineEdit,QPushButton,QWidget,QHBoxLayout
from PyQt5.QtCore import QTimer
import pyautogui
import datetime


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.delay_le = QLineEdit(self)
        self.num_le = QLineEdit(self)
        self.start_btn = QPushButton('Capture', self)

        self.delay, self.num_cap = 0, 0
        self.initUI()

    def initUI(self):
        self.delay_le.setPlaceholderText('캡처 간격 (초)')
        self.num_le.setPlaceholderText('캡처 횟수')
        self.start_btn.clicked.connect(self.start_btn_click)

        hbox = QHBoxLayout()
        hbox.addWidget(self.delay_le)
        hbox.addWidget(self.num_le)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.start_btn)

        self.setLayout(vbox)

        self.setWindowTitle('Capture')
        self.setGeometry(200, 200, 300, 150)
        self.show()

    def start_btn_click(self):
        self.delay = int(self.delay_le.text())
        self.num_cap = 0
        self.timer = QTimer()
        self.timer.start(self.delay * 1000)
        self.timer.timeout.connect(self.capture)

    def capture(self):
        today = str(datetime.datetime.today())
        pyautogui.screenshot(today + '.png')
        self.num_cap += 1

        if self.num_cap == int(self.num_le.text()):
            self.timer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())