##Ex9-1. QTextBrowser (advanced).

import sys
from PyQt5.QtWidgets import QWidget,QLineEdit,QPushButton
import requests
from bs4 import BeautifulSoup

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.le = QLineEdit()
        self.le.setPlaceholderText('Enter you search word')
        self.le.returnPressed.connect(self.crawl_news)

        self.btn = QPushButton('Search')
        self.btn.clicked.connect(self.crawl_news)



