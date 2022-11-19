import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.f = False
        self.setWindowTitle('Желтые круги')
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.f = True
        self.update()

    def paintEvent(self, event):
        if self.f:
            qp = QPainter()
            qp.begin(self)
            a = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            qp.setPen(QColor(*a))
            qp.setBrush(QColor(*a))
            a = random.randint(10, 130)
            qp.drawEllipse(random.randint(100, 600), random.randint(100, 400), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())