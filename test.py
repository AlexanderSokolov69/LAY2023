#!/usr/bin/env python3
# coding:utf-8

import sys
from math import sin, cos, pi
from random import randint

from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPainter, QColor, QMouseEvent
from PyQt6.QtWidgets import QWidget, QApplication


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)
        self.coords_ = []
        self.qp = QPainter()
        self.status = None

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.draw()
        self.qp.end()

    def draw(self):
        R = randint(20, 100)
        self.qp.setBrush(QColor(*[randint(0, 255) for _ in range(3)]))
        if self.status == 1:
            self.qp.drawEllipse(int(self.coords_[0] - R / 2),
                                int(self.coords_[1] - R / 2), R, R)
        elif self.status == 2:
            self.qp.drawRect(int(self.coords_[0] - R / 2),
                             int(self.coords_[1] - R / 2), R, R)
        elif self.status == 3:
            x, y = self.coords_
            # pnt = [QPoint(x, y - R),
            #        QPoint(int(x + cos(7 * pi / 6) * R), int(y - sin(7 * pi / 6) * R)),
            #        QPoint(int(x + cos(11 * pi / 6) * R), int(y - sin(11 * pi / 6) * R))]
            angle = 2 * pi / 3
            sin_ = sin(angle) * R
            cos_ = cos(angle) * R
            print(R, x, y)
            coords = [QPoint(int(x), int(y - R)),
                      QPoint(int(x - sin_), int(y - cos_)),
                      QPoint(int(x + sin_), int(y - cos_))]
            # if (R, x, y) == (30, 40, 4):
            #     coords = [QPoint(40, -26), QPoint(14, 18), QPoint(65, 19)]
            self.qp.drawPolygon(coords)

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('Рисование')

    def mousePressEvent(self, event: QMouseEvent):
        self.coords_ = [event.position().x(), event.position().y()]
        if (event.button() == Qt.MouseButton.LeftButton):
            self.status = 1
        elif (event.button() == Qt.MouseButton.RightButton):
            self.status = 2
        self.update()

    def mouseMoveEvent(self, event: QMouseEvent):
        self.coords_ = [event.position().x(), event.position().y()]

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.status = 3
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
