## Ex 3-3. 창 닫기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon



class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      btn = QPushButton('닷지', self)
      btn.move(50, 50)
      btn.resize(btn.sizeHint())
      btn.clicked.connect(QCoreApplication.instance().quit)

      self.setWindowTitle('알빠노')
      self.setWindowIcon(QIcon('../widget/img/보라돌이.jpg'))
      self.setGeometry(300, 300, 300, 200)
      self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
