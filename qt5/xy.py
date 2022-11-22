## Ex 10-2. (x, y) 위치 반복 클릭 프로그램2.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import pyautogui


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.x_le = QLineEdit(self)
        self.y_le = QLineEdit(self)
        self.x_le2 = QLineEdit(self)
        self.y_le2 = QLineEdit(self)
        self.x_le3 = QLineEdit(self)
        self.y_le3 = QLineEdit(self)
        self.delay_le = QLineEdit(self)
        self.num_le = QLineEdit(self)
        self.start_btn = QPushButton('Start', self)

        self.x, self.y = 0, 0
        self.x2, self.y2 = 0, 0
        self.x3, self.y3 = 0, 0
        self.delay, self.num_click = 0, 0
        self.initUI()

    def initUI(self):
        self.x_le.move(20, 20)
        self.x_le.setPlaceholderText('x 위치')
        self.x_le2.move(20, 50)
        self.x_le2.setPlaceholderText('x 위치2')
        self.x_le3.move(20, 80)
        self.x_le3.setPlaceholderText('x 위치3')

        self.y_le.move(160, 20)
        self.y_le.setPlaceholderText('y 위치')
        self.y_le2.move(160, 50)
        self.y_le2.setPlaceholderText('y 위치2')
        self.y_le3.move(160, 80)
        self.y_le3.setPlaceholderText('y 위치3')

        self.delay_le.move(20, 110)
        self.delay_le.setPlaceholderText('클릭 사이 간격 (초)')

        self.num_le.move(160, 110)
        self.num_le.setPlaceholderText('클릭 횟수')

        self.start_btn.move(110, 150)
        self.start_btn.clicked.connect(self.start_btn_click)

        self.setWindowTitle('Click')
        self.setGeometry(400, 400, 300, 200)
        self.show()

    def start_btn_click(self):
        self.timer = QTimer()
        self.x, self.y = int(self.x_le.text()), int(self.y_le.text())
        self.x2, self.y2 = int(self.x_le2.text()), int(self.y_le2.text())
        self.x3, self.y3 = int(self.x_le3.text()), int(self.y_le3.text())
        self.delay = int(self.delay_le.text())
        self.num_click = 0

        self.timer.start(self.delay * 1000)
        self.timer.timeout.connect(self.mouse_click)

 
    def mouse_click(self):
        pyautogui.click(self.x, self.y)
        pyautogui.click(self.x2, self.y2)
        pyautogui.click(self.x3, self.y3)
        self.num_click += 1

        if self.num_click == int(self.num_le.text()):
            self.timer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())