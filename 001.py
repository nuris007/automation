import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QCoreApplication
import random

class 대표선출프로그램(QWidget):
    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        self.이미지()
        self.버튼()
        self.툴팁()
        self.대리인번호()

        self.setWindowTitle('대표를 선출하라')
        self.setWindowIcon(QIcon('img/weniv-licat.png'))
        self.setGeometry(500, 500, 400, 400)
        self.show()

    def 이미지(self):
        pass
    def 버튼(self):
        pass
    def 툴팁(self):
        pass
    def 대리인번호(self):
        pass

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 대표선출프로그램()
프로그램무한반복.exec_()
