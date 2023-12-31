# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'server_connection.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UIServerConnection(object):
    def setupUi(self, server_connection_widget):
        if not server_connection_widget.objectName():
            server_connection_widget.setObjectName(u"server_connection_widget")
        server_connection_widget.resize(916, 573)
        icon = QIcon()
        iconThemeName = u"accessories-calculator"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        server_connection_widget.setWindowIcon(icon)
        server_connection_widget.setStyleSheet(u"background-color: rgb(77, 89, 69);")
        self.centralwidget = QWidget(server_connection_widget)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tab_widget = QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_widget.setTabletTracking(True)
        self.tab_widget.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(77, 89, 69);")
        self.tab_widget.setTabShape(QTabWidget.Rounded)
        self.tab_widget.setTabsClosable(False)
        self.server_tab = QWidget()
        self.server_tab.setObjectName(u"server_tab")
        self.server_tab.setStyleSheet(u"background-color: rgb(77, 89, 69);")
        self.server_list_view = QTableWidget(self.server_tab)
        if (self.server_list_view.columnCount() < 6):
            self.server_list_view.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.server_list_view.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.server_list_view.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.server_list_view.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.server_list_view.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.server_list_view.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.server_list_view.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.server_list_view.setObjectName(u"server_list_view")
        self.server_list_view.setGeometry(QRect(0, 20, 891, 401))
        font = QFont()
        font.setFamily(u"Arial")
        self.server_list_view.setFont(font)
        self.server_list_view.setTabletTracking(True)
        self.server_list_view.setStyleSheet(u"background-color: rgb(53, 63, 46);")
        self.server_list_view.setFrameShape(QFrame.NoFrame)
        self.server_list_view.setFrameShadow(QFrame.Plain)
        self.server_list_view.setLineWidth(0)
        self.server_list_view.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.server_list_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.server_list_view.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.server_list_view.setShowGrid(False)
        self.server_list_view.setGridStyle(Qt.NoPen)
        self.server_list_view.horizontalHeader().setVisible(True)
        self.server_list_view.horizontalHeader().setDefaultSectionSize(135)
        self.server_list_view.horizontalHeader().setHighlightSections(False)
        self.server_list_view.horizontalHeader().setProperty("showSortIndicator", False)
        self.server_list_view.verticalHeader().setVisible(False)
        self.log_in_button = QPushButton(self.server_tab)
        self.log_in_button.setObjectName(u"log_in_button")
        self.log_in_button.setGeometry(QRect(760, 430, 131, 71))
        self.log_in_info_label = QLabel(self.server_tab)
        self.log_in_info_label.setObjectName(u"log_in_info_label")
        self.log_in_info_label.setGeometry(QRect(0, 470, 341, 20))
        self.password_line_edit = QLineEdit(self.server_tab)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setGeometry(QRect(640, 470, 113, 28))
        self.password_line_edit.setAutoFillBackground(False)
        self.id_line_edit = QLineEdit(self.server_tab)
        self.id_line_edit.setObjectName(u"id_line_edit")
        self.id_line_edit.setGeometry(QRect(640, 430, 113, 28))
        self.id_line_edit.setAutoFillBackground(False)
        self.tab_widget.addTab(self.server_tab, "")
        self.tasks_tab = QWidget()
        self.tasks_tab.setObjectName(u"tasks_tab")
        self.import_assets_button = QPushButton(self.tasks_tab)
        self.import_assets_button.setObjectName(u"import_assets_button")
        self.import_assets_button.setGeometry(QRect(770, 440, 121, 61))
        self.sync_all_assets_button = QPushButton(self.tasks_tab)
        self.sync_all_assets_button.setObjectName(u"sync_all_assets_button")
        self.sync_all_assets_button.setGeometry(QRect(640, 440, 121, 61))
        self.add_select_asset_button = QPushButton(self.tasks_tab)
        self.add_select_asset_button.setObjectName(u"add_select_asset_button")
        self.add_select_asset_button.setGeometry(QRect(400, 70, 111, 51))
        self.add_all_assets_button = QPushButton(self.tasks_tab)
        self.add_all_assets_button.setObjectName(u"add_all_assets_button")
        self.add_all_assets_button.setGeometry(QRect(400, 130, 111, 51))
        self.remove_asset_from_import_list_button = QPushButton(self.tasks_tab)
        self.remove_asset_from_import_list_button.setObjectName(u"remove_asset_from_import_list_button")
        self.remove_asset_from_import_list_button.setGeometry(QRect(400, 210, 111, 51))
        self.remove_all_assets_from_import_list_button = QPushButton(self.tasks_tab)
        self.remove_all_assets_from_import_list_button.setObjectName(u"remove_all_assets_from_import_list_button")
        self.remove_all_assets_from_import_list_button.setGeometry(QRect(400, 270, 111, 51))
        self.scene_asset_list_view = QTableView(self.tasks_tab)
        self.scene_asset_list_view.setObjectName(u"scene_asset_list_view")
        self.scene_asset_list_view.setGeometry(QRect(0, 0, 371, 441))
        self.scene_asset_list_view.setStyleSheet(u"background-color: rgb(53, 63, 46);")
        self.assets_to_import_list_view = QTableView(self.tasks_tab)
        self.assets_to_import_list_view.setObjectName(u"assets_to_import_list_view")
        self.assets_to_import_list_view.setGeometry(QRect(540, 0, 351, 441))
        self.assets_to_import_list_view.setStyleSheet(u"background-color: rgb(53, 63, 46);")
        self.tab_widget.addTab(self.tasks_tab, "")
        self.upload_tab = QWidget()
        self.upload_tab.setObjectName(u"upload_tab")
        self.tableView = QTableView(self.upload_tab)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 0, 371, 441))
        self.tableView.setStyleSheet(u"background-color: rgb(53, 63, 46);")
        self.add_select_asset_button_2 = QPushButton(self.upload_tab)
        self.add_select_asset_button_2.setObjectName(u"add_select_asset_button_2")
        self.add_select_asset_button_2.setGeometry(QRect(400, 70, 111, 51))
        self.add_select_asset_button_3 = QPushButton(self.upload_tab)
        self.add_select_asset_button_3.setObjectName(u"add_select_asset_button_3")
        self.add_select_asset_button_3.setGeometry(QRect(400, 130, 111, 51))
        self.add_select_asset_button_4 = QPushButton(self.upload_tab)
        self.add_select_asset_button_4.setObjectName(u"add_select_asset_button_4")
        self.add_select_asset_button_4.setGeometry(QRect(400, 210, 111, 51))
        self.add_select_asset_button_5 = QPushButton(self.upload_tab)
        self.add_select_asset_button_5.setObjectName(u"add_select_asset_button_5")
        self.add_select_asset_button_5.setGeometry(QRect(400, 270, 111, 51))
        self.tableView_2 = QTableView(self.upload_tab)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setGeometry(QRect(540, 0, 371, 441))
        self.tableView_2.setStyleSheet(u"background-color: rgb(53, 63, 46);")
        self.add_select_asset_button_6 = QPushButton(self.upload_tab)
        self.add_select_asset_button_6.setObjectName(u"add_select_asset_button_6")
        self.add_select_asset_button_6.setGeometry(QRect(770, 440, 121, 61))
        self.tab_widget.addTab(self.upload_tab, "")
        self.sync_tab = QWidget()
        self.sync_tab.setObjectName(u"sync_tab")
        self.current_sync_status_list_view = QTableView(self.sync_tab)
        self.current_sync_status_list_view.setObjectName(u"current_sync_status_list_view")
        self.current_sync_status_list_view.setGeometry(QRect(0, 0, 371, 441))
        self.current_sync_status_list_view.setStyleSheet(u"background-color: rgb(53, 63, 46);")
        self.updated_sync_list_view = QTableView(self.sync_tab)
        self.updated_sync_list_view.setObjectName(u"updated_sync_list_view")
        self.updated_sync_list_view.setGeometry(QRect(540, 0, 351, 441))
        self.updated_sync_list_view.setStyleSheet(u"background-color: rgb(53, 63, 46);")
        self.add_select_asset_button_7 = QPushButton(self.sync_tab)
        self.add_select_asset_button_7.setObjectName(u"add_select_asset_button_7")
        self.add_select_asset_button_7.setGeometry(QRect(780, 440, 111, 61))
        self.tab_widget.addTab(self.sync_tab, "")

        self.verticalLayout.addWidget(self.tab_widget)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        server_connection_widget.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(server_connection_widget)
        self.statusbar.setObjectName(u"statusbar")
        server_connection_widget.setStatusBar(self.statusbar)

        self.retranslateUi(server_connection_widget)

        self.tab_widget.setCurrentIndex(0)
        self.password_line_edit.setEchoMode(QLineEdit.Password)


        QMetaObject.connectSlotsByName(server_connection_widget)
    # setupUi

    def retranslateUi(self, server_connection_widget):
        server_connection_widget.setWindowTitle(QCoreApplication.translate("server_connection_widget", u"Kiya", None))
#if QT_CONFIG(tooltip)
        self.centralwidget.setToolTip(QCoreApplication.translate("server_connection_widget", u"asdf", None))
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem = self.server_list_view.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("server_connection_widget", u"project", None));
        ___qtablewidgetitem1 = self.server_list_view.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("server_connection_widget", u"assets", None));
        ___qtablewidgetitem2 = self.server_list_view.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("server_connection_widget", u"shots", None));
        ___qtablewidgetitem3 = self.server_list_view.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("server_connection_widget", u"sequences", None));
        ___qtablewidgetitem4 = self.server_list_view.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("server_connection_widget", u"artists", None));
        ___qtablewidgetitem5 = self.server_list_view.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("server_connection_widget", u"deadlines", None));
        self.log_in_button.setText(QCoreApplication.translate("server_connection_widget", u"Connect", None))
        self.log_in_info_label.setText("")
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.server_tab), QCoreApplication.translate("server_connection_widget", u"Servers", None))
        self.import_assets_button.setText(QCoreApplication.translate("server_connection_widget", u"Import", None))
        self.sync_all_assets_button.setText(QCoreApplication.translate("server_connection_widget", u"Sync", None))
        self.add_select_asset_button.setText(QCoreApplication.translate("server_connection_widget", u">", None))
        self.add_all_assets_button.setText(QCoreApplication.translate("server_connection_widget", u">>", None))
        self.remove_asset_from_import_list_button.setText(QCoreApplication.translate("server_connection_widget", u"<", None))
        self.remove_all_assets_from_import_list_button.setText(QCoreApplication.translate("server_connection_widget", u"<<", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tasks_tab), QCoreApplication.translate("server_connection_widget", u"Tasks", None))
        self.add_select_asset_button_2.setText(QCoreApplication.translate("server_connection_widget", u">", None))
        self.add_select_asset_button_3.setText(QCoreApplication.translate("server_connection_widget", u">>", None))
        self.add_select_asset_button_4.setText(QCoreApplication.translate("server_connection_widget", u"<", None))
        self.add_select_asset_button_5.setText(QCoreApplication.translate("server_connection_widget", u"<<", None))
        self.add_select_asset_button_6.setText(QCoreApplication.translate("server_connection_widget", u"Update", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.upload_tab), QCoreApplication.translate("server_connection_widget", u"Update", None))
        self.add_select_asset_button_7.setText(QCoreApplication.translate("server_connection_widget", u"Sync", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.sync_tab), QCoreApplication.translate("server_connection_widget", u"Sync", None))
    # retranslateUi

