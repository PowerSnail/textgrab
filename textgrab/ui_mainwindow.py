# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_grab_from_clipboard = QAction(MainWindow)
        self.action_grab_from_clipboard.setObjectName(u"action_grab_from_clipboard")
        self.action_screenshot = QAction(MainWindow)
        self.action_screenshot.setObjectName(u"action_screenshot")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        MainWindow.setCentralWidget(self.central_widget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.action_grab_from_clipboard)
        self.toolBar.addAction(self.action_screenshot)

        self.retranslateUi(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_grab_from_clipboard.setText(QCoreApplication.translate("MainWindow", u"Grab From Clipboard", None))
        self.action_screenshot.setText(QCoreApplication.translate("MainWindow", u"Screenshot", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

