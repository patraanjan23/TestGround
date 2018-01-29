import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QPoint

from form import Ui_Form


class SimpleForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.click_pt = QPoint()
        self.drag_pt = QPoint()

    def mousePressEvent(self, event):
        self.click_pt = QPoint(event.x(), event.y())

    def mouseMoveEvent(self, event):
        self.drag_pt = QPoint(- self.click_pt.x() + self.x() + event.x(),
                              - self.click_pt.y() + self.y() + event.y())
        self.move(self.drag_pt)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = SimpleForm()
    form.show()
    sys.exit(app.exec_())
