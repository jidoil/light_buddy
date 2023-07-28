from PySide2.QtCore import Qt, QAbstractTableModel


class SelectedAssetModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(SelectedAssetModel, self).__init__(parent)
        self._data = []
        self._header_data = ["선택한 에셋"]

    def rowCount(self, parent=None):
        if not self._data:
            return 0
        return len(self._data)

    def columnCount(self, parent=None):
        if not self._data:
            return 0
        return len(self._data[0]) if self.rowCount() > 0 else 0

    def data(self, index, role):
        if not index.isValid():
            return 0

        row = index.row()
        col = index.column()

        if role == Qt.DisplayRole:
            return str(self._data[row][col])

        return None

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return str(self._header_data[section])
        return None

    def updateData(self, data, header_data):
        self.beginResetModel()
        self._data = data
        self._header_data = header_data
        self.endResetModel()