from PySide2.QtCore import Qt, QAbstractTableModel

class SelectedAssetModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(SelectedAssetModel, self).__init__(parent)
        self._data = []
        self._header_data = ["선택한 에셋"]

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data[0]) if self.rowCount() > 0 else 0

    def data(self, index, role):
        if not index.isValid():
            return None

        row = index.row()
        col = index.column()

        if role == Qt.DisplayRole:
            return str(self._data[row][col])

        return None

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return str(self._header_data[section])
        return None

    def updateData(self, data: list, header_data: list) -> None:  # TODO: data가 캐릭터로 쪼개져서 테이블로 등록되는 현생
        self.beginResetModel()
        for d in data:
            self._data.append(d)
            print(self._data)
        self._data = data
        self._header_data = header_data
        self.endResetModel()