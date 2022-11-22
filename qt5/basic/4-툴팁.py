## Ex 3-4. 툴팁 나타내기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon('../widget/img/pink.jpg'))
        QToolTip.setFont(QFont('SansSerif', 20))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('알빠노', self)
        btn.setToolTip('This is a <b>겜던진다고!!!</b> widget')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        btn = QPushButton('닷지', self)
        btn.setToolTip('This is a <b>오늘은 페이커가 미드 리신한날!!!</b> widget')
        btn.move(50, 100)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)


        self.setWindowTitle('행운의핑크돌고래')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())