import sys
from PyQt5 import QtCore, QtWidgets


class ListWidgetModel(QtCore.QAbstractListModel):
    def __init__(self, strings=[], parent=None):
        super(ListWidgetModel, self).__init__(parent)
        self.__strings = strings

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.__strings)

    def data(self, q_model_index, role=None):
        if role == QtCore.Qt.DisplayRole:
            row = q_model_index.row()
            return self.__strings[row]


class ListWidget(QtWidgets.QListView):
    def __init__(self):
        super(ListWidget, self).__init__()
        model = ListWidgetModel("hello this is a strong model".split())
        self.setModel(model)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = ListWidget()
    form.show()
    sys.exit(app.exec_())
