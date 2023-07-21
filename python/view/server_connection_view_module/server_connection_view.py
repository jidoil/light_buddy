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
    sync_button_pushed = Signal()
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


    def add_row(self, projects):
        for project_index, project in enumerate(projects):
            self.server_list_view.insertRow(project_index)
            for element_index_in_project, (_, element_value) in enumerate(project.items()):
                item = QTableWidgetItem(str(element_value))
                item.setTextAlignment(Qt.AlignCenter)
                self.server_list_view.setItem(project_index, element_index_in_project, item)



    def on_login_button_clicked(self):
        if not self._isLoggedIn:
            self.isLoggedIn.emit(True)
            self.logIn()
        else:
            self.isLoggedIn.emit(False)
    def logIn(self):
        log_in_data = {}
        print("id: ", self.id_line_edit.text())
        print("pass: ", self.password_line_edit.text())
        log_in_data["id"] = str(self.id_line_edit.text())
        log_in_data["password"] = str(self.password_line_edit.text())
        print(log_in_data)
        self.id_and_passwordRecieved.emit(log_in_data)
        self.isLoggedIn.emit(True)
        self._isLoggedIn = True

    def regenerate_log_in_form(self):
        self.id_line_edit.show()
        self.password_line_edit.show()
        self.log_in_button.setText("Connect")
        self._isLoggedIn = False
    def log_in_succeed(self):
        self._isLoggedIn = True
        print("login succeeded!")
        self.log_in_button.setText("Log Out")
        self.id_line_edit.hide()
        self.password_line_edit.hide()

    def sync_button_clicked(self):
        self.sync_button_pushed.emit()

    def import_assets_button_clicked(self):
        print("import clicked")
