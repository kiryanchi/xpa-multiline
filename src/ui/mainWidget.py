# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_text = QFrame(self.centralwidget)
        self.frame_text.setObjectName(u"frame_text")
        self.frame_text.setMaximumSize(QSize(16777215, 100))
        self.frame_text.setFrameShape(QFrame.StyledPanel)
        self.frame_text.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_text)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame_text)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_customer = QLineEdit(self.frame_text)
        self.lineEdit_customer.setObjectName(u"lineEdit_customer")

        self.gridLayout_2.addWidget(self.lineEdit_customer, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame_text)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_address = QLineEdit(self.frame_text)
        self.lineEdit_address.setObjectName(u"lineEdit_address")

        self.gridLayout_2.addWidget(self.lineEdit_address, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_text, 0, 0, 1, 1)

        self.frame_image = QFrame(self.centralwidget)
        self.frame_image.setObjectName(u"frame_image")
        self.frame_image.setFrameShape(QFrame.StyledPanel)
        self.frame_image.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_image)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout.addWidget(self.frame_image, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 43))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_open)
        self.menu.addAction(self.action_save)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"open", None))
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uace0\uac1d\uc815\ubcf4", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\uc18c\uc9c0", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c", None))
    # retranslateUi

