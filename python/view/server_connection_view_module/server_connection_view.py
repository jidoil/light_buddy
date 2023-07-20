from PySide2.QtCore import Slot, Qt, Signal
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView, QDialog, QMessageBox

from view.server_connection_view_module.ui_server_connection import UIServerConnection


class ServerConnectionView(QMainWindow, UIServerConnection):
    id_and_passwordRecieved = Signal(dict)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        icon = QIcon("/home/rapa/projects/kiya/images/fox_icon.png")
        self.setWindowIcon(icon)
        self.server_list_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.server_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.log_in_button.clicked.connect(self.on_login_button_clicked)


    def add_row(self, projects):
        for project_index, project in enumerate(projects):
            self.server_list_view.insertRow(project_index)
            for element_index_in_project, (_, element_value) in enumerate(project.items()):
                item = QTableWidgetItem(str(element_value))
                self.server_list_view.setItem(project_index, element_index_in_project, item)



    def on_login_button_clicked(self):
        log_in_data = {}
        print("id: ", self.id_line_edit.text())
        print("pass: ", self.password_line_edit.text())
        log_in_data["id"] = str(self.id_line_edit.text())
        log_in_data["password"] = str(self.password_line_edit.text())
        print(log_in_data)
        self.id_and_passwordRecieved.emit(log_in_data)


    def log_in_succeed(self):
        print("login succeeded!")