## Ex 5-8. QSlider & QDial.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDial, QPushButton,QAction,qApp

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        

        self.dial = QDial(self)
        self.dial.move(30, 50)
        self.dial.setRange(0, 50)
        self.setWindowTitle('joi')
        self.setGeometry(300, 300, 400, 200)
        
        
        #버튼1
        btn = QPushButton('A', self)
        btn.setToolTip('This is a <b>공격</b> 버튼')
        btn.move(200, 50)
        btn.resize(btn.sizeHint())
        # btn.clicked.connect(QCoreApplication.instance().quit)

        exitAction = QAction(QIcon("bro.jpg"), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('던진다')
        exitAction.triggered.connect(qApp.quit)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.setStyleSheet("color: black;"#폰트색 
                               "background-color: red")#배경색


#버튼2
        btn = QPushButton('B', self)
        btn.setToolTip('This is a <b>점프</b> 버튼')
        btn.move(300, 50)
        btn.resize(btn.sizeHint())
        # btn.clicked.connect(QCoreApplication.instance().quit)

        exitAction = QAction(QIcon("bro.jpg"), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('던진다')
        exitAction.triggered.connect(qApp.quit)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.setStyleSheet("color: Black;"
                               "background-color: green")


#버튼3
        btn = QPushButton('X', self)
        btn.setToolTip('This is a <b>점프</b> 버튼')
        btn.move(300, 100)
        btn.resize(btn.sizeHint())
        # btn.clicked.connect(QCoreApplication.instance().quit)

        exitAction = QAction(QIcon("bro.jpg"), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('던진다')
        exitAction.triggered.connect(qApp.quit)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.setStyleSheet("color: black;"
                               "background-color: blue")

#버튼4
        btn = QPushButton('Y', self)
        btn.setToolTip('This is a <b>점프</b> 버튼')
        btn.move(200, 100)
        btn.resize(btn.sizeHint())
        # btn.clicked.connect(QCoreApplication.instance().quit)

        exitAction = QAction(QIcon("bro.jpg"), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('던진다')
        exitAction.triggered.connect(qApp.quit)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.setStyleSheet("color: black;"
                               "background-color: yellow")




        
        
        
        
        self.show()

    def button_clicked(self):
        
        self.dial.setValue(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())