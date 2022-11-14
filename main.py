import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyPrettyCalc(QMainWindow):
    def __init__(self):
        super(MyPrettyCalc, self).__init__()
        uic.loadUi('second.ui', self)
        self.qp = QPainter(self)
        self.qwer.clicked.connect(self.k)

    def k(self):
        self.update()

    def paintEvent(self, event) -> None:
        self.coords = random.randint(0, self.width()), random.randint(0,self.height() )
        self.qp.begin(self)
        self.pen = QBrush(QColor('yellow'))
        self.qp.setBrush(self.pen)
        self.qp.drawEllipse(self.coords[0], self.coords[1], 50, 50)
        self.qp.end()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPrettyCalc()
    ex.show()
    sys.exit(app.exec())