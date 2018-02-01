import sys
from PyQt5 import QtCore, QtWidgets, QtGui


class TableWidgetModel(QtCore.QAbstractTableModel):
    def __init__(self, list_of_tuples=[], parent=None):
        super(TableWidgetModel, self).__init__(parent)
        self.__tuples = list_of_tuples

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.__tuples)

    def columnCount(self, parent=None, *args, **kwargs):
        if len(self.__tuples) > 0:
            return len(self.__tuples[0])

    def data(self, q_model_index, role=None):
        if role == QtCore.Qt.DisplayRole:
            row = q_model_index.row()
            col = q_model_index.column()
            return self.__tuples[row][col]

    def headerData(self, p_int, qt__orientation, role=None):
        if role == QtCore.Qt.DisplayRole:
            if qt__orientation == QtCore.Qt.Horizontal:
                return "column {}".format(p_int)


class NumberSortModel(QtCore.QSortFilterProxyModel):
    def lessThan(self, left, right):
        l_value = left.data()  # .toDouble()[0]
        r_value = right.data()  # .toDouble()[0]
        return l_value < r_value


class ListWidget(QtWidgets.QTableView):
    def __init__(self):
        super(ListWidget, self).__init__()

        self.setMinimumSize(320, 240)

        tuples = [[1 / x ** y for y in range(1, 5)] for x in range(1, 5)]
        # tuples = [[x ** y for y in range(1, 5)] for x in range(1, 5)]
        model = TableWidgetModel(tuples)
        proxy = NumberSortModel()
        proxy.setSourceModel(model)
        self.setModel(proxy)
        self.setSortingEnabled(True)
        self.verticalHeader().hide()
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = ListWidget()
    form.show()
    sys.exit(app.exec_())
