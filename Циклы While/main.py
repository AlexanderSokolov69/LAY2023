import sys
import random

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication


class Circles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.setWindowTitle('Круги')
        self.circles = []
        self.pushButton.clicked.connect(self.paint_circle)
    
    def paint_circle(self):
        self.circles.append((random.randint(0, self.width()),
                             random.randint(0, self.height()),
                             random.randint(10, 300),
                             random.choice(['red',
                                            'yellow',
                                            'blue',
                                            'brown',
                                            'black'])))
        self.update()
    
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        
        self.draw_c(qp)
        qp.end()
    
    def draw_c(self, qp):
        for fig in self.circles:
            qp.setPen(QPen(QColor(fig[3]), 4, Qt.SolidLine))
            qp.drawArc(fig[0] - fig[2] // 2, fig[1] - fig[2] // 2,
                       fig[2], fig[2],
                       0, 360 * 16)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Circles()
    form.show()
    sys.exit(app.exec())
