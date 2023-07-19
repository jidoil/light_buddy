# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_modal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UILogInModal(object):
    def setupUi(self, logInModal):
        if not logInModal.objectName():
            logInModal.setObjectName(u"logInModal")
        logInModal.setWindowModality(Qt.WindowModal)
        logInModal.resize(286, 214)
        self.gridLayout = QGridLayout(logInModal)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.id_label = QLabel(logInModal)
        self.id_label.setObjectName(u"id_label")

        self.horizontalLayout.addWidget(self.id_label)

        self.id_line_edit = QLineEdit(logInModal)
        self.id_line_edit.setObjectName(u"id_line_edit")

        self.horizontalLayout.addWidget(self.id_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.password_label = QLabel(logInModal)
        self.password_label.setObjectName(u"password_label")

        self.horizontalLayout_2.addWidget(self.password_label)

        self.password_line_edit = QLineEdit(logInModal)
        self.password_line_edit.setObjectName(u"password_line_edit")

        self.horizontalLayout_2.addWidget(self.password_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.sign_up_button = QPushButton(logInModal)
        self.sign_up_button.setObjectName(u"sign_up_button")

        self.horizontalLayout_3.addWidget(self.sign_up_button)

        self.log_in_button = QPushButton(logInModal)
        self.log_in_button.setObjectName(u"log_in_button")

        self.horizontalLayout_3.addWidget(self.log_in_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(logInModal)


        QMetaObject.connectSlotsByName(logInModal)
    # setupUi

    def retranslateUi(self, logInModal):
        logInModal.setWindowTitle(QCoreApplication.translate("logInModal", u"Form", None))
        self.id_label.setText(QCoreApplication.translate("logInModal", u"id/email", None))
        self.password_label.setText(QCoreApplication.translate("logInModal", u"password", None))
        self.sign_up_button.setText(QCoreApplication.translate("logInModal", u"Signup", None))
        self.log_in_button.setText(QCoreApplication.translate("logInModal", u"Login", None))
    # retranslateUi

