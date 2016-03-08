# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radians/views/document_template.ui'
#
# Created: Mon Feb 29 09:25:31 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 631)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 915, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuDocumento = QtGui.QMenu(self.menubar)
        self.menuDocumento.setObjectName("menuDocumento")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_salva_documento = QtGui.QAction(MainWindow)
        self.action_salva_documento.setObjectName("action_salva_documento")
        self.action_elimina_documento = QtGui.QAction(MainWindow)
        self.action_elimina_documento.setObjectName("action_elimina_documento")
        self.menuDocumento.addAction(self.action_salva_documento)
        self.menuDocumento.addAction(self.action_elimina_documento)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDocumento.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "file", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDocumento.setTitle(QtGui.QApplication.translate("MainWindow", "documento", None, QtGui.QApplication.UnicodeUTF8))
        self.action_salva_documento.setText(QtGui.QApplication.translate("MainWindow", "salva", None, QtGui.QApplication.UnicodeUTF8))
        self.action_elimina_documento.setText(QtGui.QApplication.translate("MainWindow", "elimina", None, QtGui.QApplication.UnicodeUTF8))

