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
        server_connection_widget.resize(908, 567)
        icon = QIcon(QIcon.fromTheme(u"accessories-calculator"))
        server_connection_widget.setWindowIcon(icon)
        server_connection_widget.setStyleSheet(u"background-color: rgb(77, 89, 69);")
        self.centralwidget = QWidget(server_connection_widget)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 40, 851, 481))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tab_widget = QTabWidget(self.widget)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_widget.setTabletTracking(True)
        self.tab_widget.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(77, 89, 69);")
        self.tab_widget.setTabShape(QTabWidget.Rounded)
        self.tab_widget.setTabsClosable(False)
        self.first_tab = QWidget()
        self.first_tab.setObjectName(u"first_tab")
        self.first_tab.setStyleSheet(u"background-color: rgb(77, 89, 69);")
        self.server_list_view = QTableWidget(self.first_tab)
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
        if (self.server_list_view.rowCount() < 2):
            self.server_list_view.setRowCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.server_list_view.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.server_list_view.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.server_list_view.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.server_list_view.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.server_list_view.setItem(0, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.server_list_view.setItem(0, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.server_list_view.setItem(0, 4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.server_list_view.setItem(0, 5, __qtablewidgetitem13)
        self.server_list_view.setObjectName(u"server_list_view")
        self.server_list_view.setGeometry(QRect(0, 40, 881, 381))
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
        self.server_list_view.horizontalHeader().setVisible(False)
        self.server_list_view.horizontalHeader().setDefaultSectionSize(135)
        self.server_list_view.horizontalHeader().setHighlightSections(False)
        self.server_list_view.horizontalHeader().setProperty("showSortIndicator", False)
        self.server_list_view.verticalHeader().setVisible(False)
        self.frame = QFrame(self.first_tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 851, 41))
        self.frame.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.widget1 = QWidget(self.frame)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 0, 851, 41))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.server_label = QLabel(self.widget1)
        self.server_label.setObjectName(u"server_label")
        self.server_label.setStyleSheet(u"background-color: rgb(77, 89, 69);\n"
"color: rgb(255, 255, 255);")
        self.server_label.setFrameShape(QFrame.StyledPanel)
        self.server_label.setFrameShadow(QFrame.Plain)
        self.server_label.setLineWidth(1)
        self.server_label.setMidLineWidth(0)
        self.server_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.server_label)

        self.project_label = QLabel(self.widget1)
        self.project_label.setObjectName(u"project_label")
        self.project_label.setStyleSheet(u"background-color: rgb(77, 89, 69);\n"
"color: rgb(255, 255, 255);")
        self.project_label.setFrameShape(QFrame.StyledPanel)
        self.project_label.setFrameShadow(QFrame.Plain)
        self.project_label.setLineWidth(1)
        self.project_label.setMidLineWidth(0)
        self.project_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.project_label)

        self.asset_label = QLabel(self.widget1)
        self.asset_label.setObjectName(u"asset_label")
        self.asset_label.setStyleSheet(u"background-color: rgb(77, 89, 69);\n"
"color: rgb(255, 255, 255);")
        self.asset_label.setFrameShape(QFrame.StyledPanel)
        self.asset_label.setFrameShadow(QFrame.Plain)
        self.asset_label.setLineWidth(1)
        self.asset_label.setMidLineWidth(0)
        self.asset_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.asset_label)

        self.shots_label = QLabel(self.widget1)
        self.shots_label.setObjectName(u"shots_label")
        self.shots_label.setStyleSheet(u"background-color: rgb(77, 89, 69);\n"
"color: rgb(255, 255, 255);")
        self.shots_label.setFrameShape(QFrame.StyledPanel)
        self.shots_label.setFrameShadow(QFrame.Plain)
        self.shots_label.setLineWidth(1)
        self.shots_label.setMidLineWidth(0)
        self.shots_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.shots_label)

        self.sequences_label = QLabel(self.widget1)
        self.sequences_label.setObjectName(u"sequences_label")
        self.sequences_label.setStyleSheet(u"background-color: rgb(77, 89, 69);\n"
"color: rgb(255, 255, 255);")
        self.sequences_label.setFrameShape(QFrame.StyledPanel)
        self.sequences_label.setFrameShadow(QFrame.Plain)
        self.sequences_label.setLineWidth(1)
        self.sequences_label.setMidLineWidth(0)
        self.sequences_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.sequences_label)

        self.artists_label = QLabel(self.widget1)
        self.artists_label.setObjectName(u"artists_label")
        self.artists_label.setStyleSheet(u"background-color: rgb(77, 89, 69);\n"
"color: rgb(255, 255, 255);")
        self.artists_label.setFrameShape(QFrame.StyledPanel)
        self.artists_label.setFrameShadow(QFrame.Plain)
        self.artists_label.setLineWidth(1)
        self.artists_label.setMidLineWidth(0)
        self.artists_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.artists_label)

        self.tab_widget.addTab(self.first_tab, "")
        self.second_tab = QWidget()
        self.second_tab.setObjectName(u"second_tab")
        self.tab_widget.addTab(self.second_tab, "")

        self.verticalLayout.addWidget(self.tab_widget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(418, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.signup_button = QPushButton(self.widget)
        self.signup_button.setObjectName(u"signup_button")
        self.signup_button.setAutoFillBackground(False)
        self.signup_button.setStyleSheet(u"background-color: rgb(77, 89, 69);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.signup_button)

        self.connection_button = QPushButton(self.widget)
        self.connection_button.setObjectName(u"connection_button")
        self.connection_button.setStyleSheet(u"background-color: rgb(77, 89, 69);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.connection_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        server_connection_widget.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(server_connection_widget)
        self.statusbar.setObjectName(u"statusbar")
        server_connection_widget.setStatusBar(self.statusbar)

        self.retranslateUi(server_connection_widget)

        self.tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(server_connection_widget)
    # setupUi

    def retranslateUi(self, server_connection_widget):
        server_connection_widget.setWindowTitle(QCoreApplication.translate("server_connection_widget", u"Kiya", None))
        ___qtablewidgetitem = self.server_list_view.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("server_connection_widget", u"server", None));
        ___qtablewidgetitem1 = self.server_list_view.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("server_connection_widget", u"project", None));
        ___qtablewidgetitem2 = self.server_list_view.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("server_connection_widget", u"assets", None));
        ___qtablewidgetitem3 = self.server_list_view.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("server_connection_widget", u"shots", None));
        ___qtablewidgetitem4 = self.server_list_view.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("server_connection_widget", u"sequences", None));
        ___qtablewidgetitem5 = self.server_list_view.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("server_connection_widget", u"artists", None));
        ___qtablewidgetitem6 = self.server_list_view.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("server_connection_widget", u"headers", None));
        ___qtablewidgetitem7 = self.server_list_view.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("server_connection_widget", u"test", None));

        __sortingEnabled = self.server_list_view.isSortingEnabled()
        self.server_list_view.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.server_list_view.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("server_connection_widget", u"server status", None));
        ___qtablewidgetitem9 = self.server_list_view.item(0, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("server_connection_widget", u"project name", None));
        ___qtablewidgetitem10 = self.server_list_view.item(0, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("server_connection_widget", u"asset count", None));
        ___qtablewidgetitem11 = self.server_list_view.item(0, 3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("server_connection_widget", u"shot count", None));
        ___qtablewidgetitem12 = self.server_list_view.item(0, 4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("server_connection_widget", u"seq count", None));
        ___qtablewidgetitem13 = self.server_list_view.item(0, 5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("server_connection_widget", u"artists", None));
        self.server_list_view.setSortingEnabled(__sortingEnabled)

        self.server_label.setText(QCoreApplication.translate("server_connection_widget", u"Server", None))
        self.project_label.setText(QCoreApplication.translate("server_connection_widget", u"Project", None))
        self.asset_label.setText(QCoreApplication.translate("server_connection_widget", u"Assets", None))
        self.shots_label.setText(QCoreApplication.translate("server_connection_widget", u"Shots", None))
        self.sequences_label.setText(QCoreApplication.translate("server_connection_widget", u"Sequences", None))
        self.artists_label.setText(QCoreApplication.translate("server_connection_widget", u"Artists", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.first_tab), QCoreApplication.translate("server_connection_widget", u"Servers", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.second_tab), "")
        self.signup_button.setText(QCoreApplication.translate("server_connection_widget", u"Signup", None))
        self.connection_button.setText(QCoreApplication.translate("server_connection_widget", u"Connection", None))
    # retranslateUi

