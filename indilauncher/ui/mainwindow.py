# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed May 27 22:51:13 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_IndilauncherMainWindow(object):
    def setupUi(self, IndilauncherMainWindow):
        IndilauncherMainWindow.setObjectName(_fromUtf8("IndilauncherMainWindow"))
        IndilauncherMainWindow.resize(748, 528)
        self.centralwidget = QtGui.QWidget(IndilauncherMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.txt_console = QtGui.QPlainTextEdit(self.centralwidget)
        self.txt_console.setMinimumSize(QtCore.QSize(450, 0))
        self.txt_console.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.txt_console.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255,255,255);\n"
"font-family: monospace;\n"
"font-size: 10pt;"))
        self.txt_console.setReadOnly(True)
        self.txt_console.setObjectName(_fromUtf8("txt_console"))
        self.gridLayout.addWidget(self.txt_console, 0, 0, 4, 1)
        self.lyt_finalactions = QtGui.QVBoxLayout()
        self.lyt_finalactions.setObjectName(_fromUtf8("lyt_finalactions"))
        self.btn_indiserver = QtGui.QPushButton(self.centralwidget)
        self.btn_indiserver.setObjectName(_fromUtf8("btn_indiserver"))
        self.lyt_finalactions.addWidget(self.btn_indiserver)
        self.gridLayout.addLayout(self.lyt_finalactions, 3, 1, 1, 1)
        self.lyt_USBactions = QtGui.QVBoxLayout()
        self.lyt_USBactions.setObjectName(_fromUtf8("lyt_USBactions"))
        self.btn_listUSB = QtGui.QPushButton(self.centralwidget)
        self.btn_listUSB.setObjectName(_fromUtf8("btn_listUSB"))
        self.lyt_USBactions.addWidget(self.btn_listUSB)
        self.btn_saveUSB = QtGui.QPushButton(self.centralwidget)
        self.btn_saveUSB.setObjectName(_fromUtf8("btn_saveUSB"))
        self.lyt_USBactions.addWidget(self.btn_saveUSB)
        self.gridLayout.addLayout(self.lyt_USBactions, 0, 1, 1, 1)
        self.lyt_driverform = QtGui.QFormLayout()
        self.lyt_driverform.setObjectName(_fromUtf8("lyt_driverform"))
        self.lbl_telescope = QtGui.QLabel(self.centralwidget)
        self.lbl_telescope.setObjectName(_fromUtf8("lbl_telescope"))
        self.lyt_driverform.setWidget(0, QtGui.QFormLayout.LabelRole, self.lbl_telescope)
        self.cb_telescope = QtGui.QComboBox(self.centralwidget)
        self.cb_telescope.setMinimumSize(QtCore.QSize(200, 0))
        self.cb_telescope.setObjectName(_fromUtf8("cb_telescope"))
        self.lyt_driverform.setWidget(0, QtGui.QFormLayout.FieldRole, self.cb_telescope)
        self.lbl_ccdapn = QtGui.QLabel(self.centralwidget)
        self.lbl_ccdapn.setObjectName(_fromUtf8("lbl_ccdapn"))
        self.lyt_driverform.setWidget(1, QtGui.QFormLayout.LabelRole, self.lbl_ccdapn)
        self.cb_ccdapn = QtGui.QComboBox(self.centralwidget)
        self.cb_ccdapn.setMinimumSize(QtCore.QSize(200, 0))
        self.cb_ccdapn.setObjectName(_fromUtf8("cb_ccdapn"))
        self.lyt_driverform.setWidget(1, QtGui.QFormLayout.FieldRole, self.cb_ccdapn)
        self.lbl_guide = QtGui.QLabel(self.centralwidget)
        self.lbl_guide.setObjectName(_fromUtf8("lbl_guide"))
        self.lyt_driverform.setWidget(2, QtGui.QFormLayout.LabelRole, self.lbl_guide)
        self.cb_guide = QtGui.QComboBox(self.centralwidget)
        self.cb_guide.setMinimumSize(QtCore.QSize(200, 0))
        self.cb_guide.setObjectName(_fromUtf8("cb_guide"))
        self.lyt_driverform.setWidget(2, QtGui.QFormLayout.FieldRole, self.cb_guide)
        self.lbl_focuser = QtGui.QLabel(self.centralwidget)
        self.lbl_focuser.setObjectName(_fromUtf8("lbl_focuser"))
        self.lyt_driverform.setWidget(3, QtGui.QFormLayout.LabelRole, self.lbl_focuser)
        self.cb_focuser = QtGui.QComboBox(self.centralwidget)
        self.cb_focuser.setMinimumSize(QtCore.QSize(200, 0))
        self.cb_focuser.setObjectName(_fromUtf8("cb_focuser"))
        self.lyt_driverform.setWidget(3, QtGui.QFormLayout.FieldRole, self.cb_focuser)
        self.lbl_joystick = QtGui.QLabel(self.centralwidget)
        self.lbl_joystick.setObjectName(_fromUtf8("lbl_joystick"))
        self.lyt_driverform.setWidget(4, QtGui.QFormLayout.LabelRole, self.lbl_joystick)
        self.cb_joystick = QtGui.QComboBox(self.centralwidget)
        self.cb_joystick.setMinimumSize(QtCore.QSize(200, 0))
        self.cb_joystick.setObjectName(_fromUtf8("cb_joystick"))
        self.lyt_driverform.setWidget(4, QtGui.QFormLayout.FieldRole, self.cb_joystick)
        self.lbl_aux1 = QtGui.QLabel(self.centralwidget)
        self.lbl_aux1.setObjectName(_fromUtf8("lbl_aux1"))
        self.lyt_driverform.setWidget(5, QtGui.QFormLayout.LabelRole, self.lbl_aux1)
        self.cb_aux1 = QtGui.QComboBox(self.centralwidget)
        self.cb_aux1.setMinimumSize(QtCore.QSize(200, 0))
        self.cb_aux1.setObjectName(_fromUtf8("cb_aux1"))
        self.lyt_driverform.setWidget(5, QtGui.QFormLayout.FieldRole, self.cb_aux1)
        self.lbl_aux2 = QtGui.QLabel(self.centralwidget)
        self.lbl_aux2.setObjectName(_fromUtf8("lbl_aux2"))
        self.lyt_driverform.setWidget(6, QtGui.QFormLayout.LabelRole, self.lbl_aux2)
        self.cb_aux2 = QtGui.QComboBox(self.centralwidget)
        self.cb_aux2.setMinimumSize(QtCore.QSize(200, 0))
        self.cb_aux2.setObjectName(_fromUtf8("cb_aux2"))
        self.lyt_driverform.setWidget(6, QtGui.QFormLayout.FieldRole, self.cb_aux2)
        self.lbl_aux3 = QtGui.QLabel(self.centralwidget)
        self.lbl_aux3.setObjectName(_fromUtf8("lbl_aux3"))
        self.lyt_driverform.setWidget(7, QtGui.QFormLayout.LabelRole, self.lbl_aux3)
        self.cb_aux3 = QtGui.QComboBox(self.centralwidget)
        self.cb_aux3.setMinimumSize(QtCore.QSize(200, 0))
        self.cb_aux3.setObjectName(_fromUtf8("cb_aux3"))
        self.lyt_driverform.setWidget(7, QtGui.QFormLayout.FieldRole, self.cb_aux3)
        self.gridLayout.addLayout(self.lyt_driverform, 1, 1, 1, 1)
        IndilauncherMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(IndilauncherMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 748, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_Fichier = QtGui.QMenu(self.menubar)
        self.menu_Fichier.setObjectName(_fromUtf8("menu_Fichier"))
        IndilauncherMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(IndilauncherMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        IndilauncherMainWindow.setStatusBar(self.statusbar)
        self.act_quitter = QtGui.QAction(IndilauncherMainWindow)
        self.act_quitter.setObjectName(_fromUtf8("act_quitter"))
        self.act_nightmode = QtGui.QAction(IndilauncherMainWindow)
        self.act_nightmode.setCheckable(True)
        self.act_nightmode.setObjectName(_fromUtf8("act_nightmode"))
        self.menu_Fichier.addAction(self.act_nightmode)
        self.menu_Fichier.addSeparator()
        self.menu_Fichier.addAction(self.act_quitter)
        self.menubar.addAction(self.menu_Fichier.menuAction())

        self.retranslateUi(IndilauncherMainWindow)
        QtCore.QObject.connect(self.act_quitter, QtCore.SIGNAL(_fromUtf8("triggered()")), IndilauncherMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(IndilauncherMainWindow)
        IndilauncherMainWindow.setTabOrder(self.btn_listUSB, self.btn_saveUSB)
        IndilauncherMainWindow.setTabOrder(self.btn_saveUSB, self.cb_telescope)
        IndilauncherMainWindow.setTabOrder(self.cb_telescope, self.cb_ccdapn)
        IndilauncherMainWindow.setTabOrder(self.cb_ccdapn, self.cb_guide)
        IndilauncherMainWindow.setTabOrder(self.cb_guide, self.cb_focuser)
        IndilauncherMainWindow.setTabOrder(self.cb_focuser, self.cb_joystick)
        IndilauncherMainWindow.setTabOrder(self.cb_joystick, self.cb_aux1)
        IndilauncherMainWindow.setTabOrder(self.cb_aux1, self.cb_aux2)
        IndilauncherMainWindow.setTabOrder(self.cb_aux2, self.cb_aux3)
        IndilauncherMainWindow.setTabOrder(self.cb_aux3, self.btn_indiserver)
        IndilauncherMainWindow.setTabOrder(self.btn_indiserver, self.txt_console)

    def retranslateUi(self, IndilauncherMainWindow):
        IndilauncherMainWindow.setWindowTitle(_translate("IndilauncherMainWindow", "Indilauncher", None))
        self.btn_indiserver.setStatusTip(_translate("IndilauncherMainWindow", "Lancer INDI Server avec les pilotes sélectionnés", None))
        self.btn_indiserver.setText(_translate("IndilauncherMainWindow", "&Lancer INDI Server", None))
        self.btn_indiserver.setShortcut(_translate("IndilauncherMainWindow", "Ctrl+S", None))
        self.btn_listUSB.setText(_translate("IndilauncherMainWindow", "Lister les périphériques &USB", None))
        self.btn_listUSB.setShortcut(_translate("IndilauncherMainWindow", "Alt+U", None))
        self.btn_saveUSB.setStatusTip(_translate("IndilauncherMainWindow", "Enregistre le résultat de la commence lsusb dans un fichier", None))
        self.btn_saveUSB.setText(_translate("IndilauncherMainWindow", "&Sauvegarder la liste...", None))
        self.lbl_telescope.setText(_translate("IndilauncherMainWindow", "Téléscope", None))
        self.lbl_ccdapn.setText(_translate("IndilauncherMainWindow", "CCD/APN", None))
        self.lbl_guide.setText(_translate("IndilauncherMainWindow", "Guidage", None))
        self.lbl_focuser.setText(_translate("IndilauncherMainWindow", "Focuser", None))
        self.lbl_joystick.setText(_translate("IndilauncherMainWindow", "Joystick", None))
        self.lbl_aux1.setText(_translate("IndilauncherMainWindow", "Aux 1", None))
        self.lbl_aux2.setText(_translate("IndilauncherMainWindow", "Aux 2", None))
        self.lbl_aux3.setText(_translate("IndilauncherMainWindow", "Aux 3", None))
        self.menu_Fichier.setTitle(_translate("IndilauncherMainWindow", "&Fichier", None))
        self.act_quitter.setText(_translate("IndilauncherMainWindow", "&Quitter", None))
        self.act_quitter.setStatusTip(_translate("IndilauncherMainWindow", "Quitter l\'application", None))
        self.act_quitter.setShortcut(_translate("IndilauncherMainWindow", "Ctrl+Q", None))
        self.act_nightmode.setText(_translate("IndilauncherMainWindow", "Mode &Nuit", None))
        self.act_nightmode.setStatusTip(_translate("IndilauncherMainWindow", "Change les couleurs de l\'interface", None))
        self.act_nightmode.setShortcut(_translate("IndilauncherMainWindow", "Alt+N", None))

