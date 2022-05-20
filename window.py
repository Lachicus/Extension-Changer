# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerxxWSiH.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtCore import QSize

import res.bg_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(551, 261)
        MainWindow.setFixedSize(551, 261)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-2, -5, 591, 331))
        self.label.setStyleSheet(u"background-image: url(:/bgimg1/bgimg.png);")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 140, 491, 101))
        self.progressBar = QProgressBar(self.groupBox)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 60, 471, 23))
        self.progressBar.setValue(1)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 221, 21))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 20, 491, 111))
        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 30, 371, 31))
        self.lineEdit_2.setStyleSheet(u"border-color: rgb(170, 0, 255);")
        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 30, 91, 31))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(221, 221, 221);")
        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(250, 70, 91, 31))
        self.pushButton_3.setStyleSheet(u"")
        self.base = QLineEdit(self.groupBox_2)
        self.base.setObjectName(u"base")
        self.base.setGeometry(QRect(110, 70, 61, 31))
        self.base.setStyleSheet(u"border-color: rgb(170, 0, 255);")
        self.finish = QLineEdit(self.groupBox_2)
        self.finish.setObjectName(u"finish")
        self.finish.setGeometry(QRect(420, 70, 61, 31))
        self.finish.setStyleSheet(u"border-color: rgb(170, 0, 255);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Recursing Extention Changer", None))
        self.label.setText("")
        self.groupBox.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Progress</span></p></body></html>", None))
        self.groupBox_2.setTitle("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Locate Folder", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.base.setText(QCoreApplication.translate("MainWindow", u".mp3", None))
        self.finish.setText(QCoreApplication.translate("MainWindow", u".mp4", None))
    # retranslateUI

