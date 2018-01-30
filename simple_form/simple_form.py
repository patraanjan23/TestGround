import sys

from PyQt5 import QtWidgets, QtGui, QtCore

from form import Ui_Form


class SimpleForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)
        self.setGeometry(64, 64, 640, 480)

        self.click_pt = QtCore.QPoint()
        self.drag_pt = QtCore.QPoint()

        self.stylesheet = "stylesheet.css"
        try:
            with open(self.stylesheet) as stylesheet:
                self.setStyleSheet(stylesheet.read())
        except FileNotFoundError:
            print("{} not found, switching to default look".format(self.stylesheet))
        
        self.btnExit.clicked.connect(self.exit_app)
        self.btnMax.clicked.connect(self.restore_app)
        self.btnMin.clicked.connect(self.minimize_app)
        self.btnSubmit.clicked.connect(self.print_text)

    def print_text(self):
        text = self.inputInfo.text()
        print(text)

    def minimize_app(self):
        self.showMinimized()

    def restore_app(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def exit_app(self):
        self.close()

    def mousePressEvent(self, event):
        self.click_pt = QtCore.QPoint(event.x(), event.y())

    def mouseMoveEvent(self, event):
        children = self.findChildren((QtWidgets.QPushButton, QtWidgets.QLineEdit))
        if True in map(lambda x: x.underMouse(), children):
            pass
        else:
            self.drag_pt = QtCore.QPoint(- self.click_pt.x() + self.x() + event.x(),
                                         - self.click_pt.y() + self.y() + event.y())
            self.move(self.drag_pt)

    def paintEvent(self, event):
        path = QtGui.QPainterPath()
        radius = 7
        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = SimpleForm()
    form.show()
    sys.exit(app.exec_())
