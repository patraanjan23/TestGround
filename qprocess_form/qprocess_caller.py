import re
import sys
from PyQt5 import QtCore, QtWidgets
import qprocess_form


class ProcessCaller(QtWidgets.QWidget, qprocess_form.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.process = QtCore.QProcess(self)

        self.btnStart.clicked.connect(self.start_process)
        self.btnStop.clicked.connect(self.stop_process)
        self.process.readyReadStandardOutput.connect(self.read_stdout)

    def start_process(self):
        self.process.start("python", ["test.py"])

    def stop_process(self):
        print("process {} killed".format(self.process.pid()))
        self.process.kill()

    def read_stdout(self):
        txt = str(self.process.readAllStandardOutput())
        regex = re.compile(r"\d* seconds")
        match = regex.search(txt)
        self.label.setText(match.group(0))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = ProcessCaller()
    form.show()
    sys.exit(app.exec_())
