## Ex 3-2. 어플리케이션 아이콘 넣기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      self.setWindowTitle('행운의 핑크돌고래')
      self.setWindowIcon(QIcon('C:/Users/2/Desktop/qt5/basic/img/pink.jpg'))
      self.setGeometry(300, 300, 300, 200)
      self.show()


if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())
