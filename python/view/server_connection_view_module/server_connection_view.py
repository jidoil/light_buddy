from PySide2.QtCore import Slot, Qt, Signal
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView, QDialog, QMessageBox

from view.server_connection_view_module.ui_login_modal import UILogInModal
from view.server_connection_view_module.ui_server_connection import *


class ServerConnectionView(QMainWindow, UIServerConnection, UILogInModal):
    id_and_passwordRecieved = Signal(dict)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        icon = QIcon("/home/rapa/projects/kiya/images/fox_icon.png")
        self.setWindowIcon(icon)
        self.server_list_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.server_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.connection_button.clicked.connect(self.on_connection_button_clicked)
        self.log_in_modal = QDialog()
        self.log_in_modal_ui = UILogInModal()
        self.log_in_modal_ui.setupUi(self.log_in_modal)
        self.log_in_modal.setWindowModality(Qt.WindowModal)
        self.log_in_modal_ui.log_in_button.clicked.connect(self.on_login_button_clicked)

    def add_row(self, projects):
        for project_index, project in enumerate(projects):
            self.server_list_view.insertRow(project_index)
            for element_index_in_project, (_, element_value) in enumerate(project.items()):
                item = QTableWidgetItem(str(element_value))
                self.server_list_view.setItem(project_index, element_index_in_project, item)


    @Slot()
    def on_connection_button_clicked(self):
        self.log_in_modal.show()


    def on_login_button_clicked(self):
        log_in_data = {}
        log_in_data["id"] = str(self.log_in_modal_ui.id_line_edit.text())
        log_in_data["password"] = str(self.log_in_modal_ui.password_line_edit.text())
        self.id_and_passwordRecieved.emit(log_in_data)


    def log_in_succeed(self):
        while self.log_in_modal.layout().count():
            item = self.log_in_modal.layout().takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        message_box = QMessageBox(self.log_in_modal)
        message_box.setWindowTitle("로그인 성공")
        message_box.setText("로그인 성공")
        message_box.finished.connect(self.log_in_modal.close)
        message_box.exec_()