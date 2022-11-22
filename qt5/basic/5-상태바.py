## Ex 3-5. 상태바 만들기.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QPushButton
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon('../widget/img/pink.jpg'))
        QToolTip.setFont(QFont('SansSerif', 10))
        self.statusBar().showMessage('던지기3초전')
        self.setWindowTitle('행운의핑크돌고래')
        self.setGeometry(300, 300, 300, 200)
        btn = QPushButton('말파1인궁', self)
        btn.setToolTip('This is a <b>겜던진다고!!!</b> widget')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    