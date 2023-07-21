from PySide2.QtCore import Qt, Signal
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QTableWidgetItem, \
    QAbstractItemView
from view.server_connection_view_module.ui_server_connection import UIServerConnection


class ServerConnectionView(QMainWindow, UIServerConnection):
    id_and_passwordRecieved = Signal(dict)
    isLoggedIn = Signal(bool)
    _isLoggedIn = None
    assigned_assets = []
    selected_assets = []
    sync_button_pushed = Signal()
    add_selected_asset_button_pushed = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        icon = QIcon("/home/rapa/projects/kiya/images/fox_icon.png")
        self.setWindowIcon(icon)
        self.server_list_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.server_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.log_in_button.clicked.connect(self.on_login_button_clicked)
        self.sync_all_assets_button.clicked.connect(self.sync_button_clicked)
        self.import_assets_button.clicked.connect(self.import_assets_button_clicked)
        self.add_select_asset_button.clicked.connect(self.on_add_select_asset_button_clicked)
        self.assets_to_import_list_view.setSelectionBehavior(QAbstractItemView.SelectRows)


    def on_add_select_asset_button_clicked(self):
        print("add select clicked")
        self.add_selected_asset_button_pushed.emit()

    def add_row(self, projects) -> None:
        for project_index, project in enumerate(projects):
            self.server_list_view.insertRow(project_index)
            for element_index_in_project, (_, element_value) in enumerate(project.items()):
                item = QTableWidgetItem(str(element_value))
                item.setTextAlignment(Qt.AlignCenter)
                self.server_list_view.setItem(project_index, element_index_in_project, item)

    def on_login_button_clicked(self) -> None:
        if not self._isLoggedIn:
            self.isLoggedIn.emit(True)
            self.logIn()
        else:
            self.isLoggedIn.emit(False)

    def logIn(self) -> None:
        log_in_data = {}
        print("id: ", self.id_line_edit.text())
        print("pass: ", self.password_line_edit.text())
        log_in_data["id"] = str(self.id_line_edit.text())
        log_in_data["password"] = str(self.password_line_edit.text())
        print(log_in_data)
        self.id_and_passwordRecieved.emit(log_in_data)
        self.isLoggedIn.emit(True)
        self._isLoggedIn = True

    def regenerate_log_in_form(self) -> None:
        self.id_line_edit.show()
        self.password_line_edit.show()
        self.log_in_button.setText("Connect")
        self._isLoggedIn = False
    def log_in_succeed(self) -> None:
        self._isLoggedIn = True
        print("login succeeded!")
        self.log_in_button.setText("Log Out")
        self.id_line_edit.hide()
        self.password_line_edit.hide()

    def sync_button_clicked(self) -> None:
        self.sync_button_pushed.emit()

    def import_assets_button_clicked(self) -> None:
        self.add_selected_asset_button_pushed.emit()
# 핵심 코드를 찾는다. 이런 기능이 필요해 저런기능이 필요해
# 그함수들을 찾아서 테스트를 한뒤 구조화
# 객체로 쪼갠다든지
# 인자값, ui 로받을건지 씬에서추출해서 받을건지 그런걸 정리하면서 큰 구조를 찾는다.
# 처음부터 큰구조를 짜는것보다는 작은것부터 짜고 테스트하고 만든다.
# 문제해결할때 작은단위부터 추가추가 해서
# 반대로하면 힘들어져
# 마야는 문서보는게 좋다.
# chatgpt한테 물어보고...
