from PySide2 import QtCore
from PySide2.QtCore import QAbstractTableModel


class TasksModel(QAbstractTableModel):
    def __init__(self, data, header_data, parent=None):
        super(TasksModel, self).__init__(parent)
        self._data = data
        self._header_data = header_data

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data[0]) if self.rowCount() > 0 else 0

    def data(self, index, role):
        if not index.isValid():
            return None

        row = index.row()
        col = index.column()

        if role == QtCore.Qt.DisplayRole:
            return str(self._data[row][col])

        return None

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return str(self._header_data[section])

        return None
