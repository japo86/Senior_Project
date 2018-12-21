# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtQuick
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtWidgets import QDialog, QMessageBox

import Attacks_script
import icmpflood
import nmap_port_scanner
import sys

# target = ""
#
# attack_port = 80
AttackType = ""


class Ui_DoSr(object):

    target = ""
    port_bot = "0"
    port_top = "65535"
    scanSignal = QtCore.Signal()

    def setupUi(self, DoSr):
        DoSr.setObjectName("DoSr")
        DoSr.resize(611, 604)
        self.centralwidget = QtWidgets.QWidget(DoSr)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 250, 591, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.output_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.output_layout.setContentsMargins(0, 0, 0, 0)
        self.output_layout.setObjectName("output_layout")

        self.Start_Attack_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Start_Attack_button.setObjectName("Start_Attack_button")
        ##########################################################################################
        # self.Start_Attack_button.clicked.connect()
        ##########################################################################################
        self.output_layout.addWidget(self.Start_Attack_button, 0, 0, 1, 1)
        self.Output_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Output_label.setObjectName("Output_label")
        self.output_layout.addWidget(self.Output_label, 2, 0, 1, 1)

        self.Stop_attack_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Stop_attack_button.setObjectName("Stop_attack_button")

        self.output_layout.addWidget(self.Stop_attack_button, 1, 0, 1, 1)

        # self.output_ScrollBar = QtWidgets.QScrollBar(self.gridLayoutWidget)
        # self.output_ScrollBar.setOrientation(QtCore.Qt.Vertical)
        # self.output_ScrollBar.setObjectName("output_ScrollBar")
        #
        # self.output_layout.addWidget(self.output_ScrollBar, 6, 1, 1, 1)

        self.Output_display_box = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.Output_display_box.setObjectName("Output_display_box")



        self.output_layout.addWidget(self.Output_display_box, 6, 0, 1, 1)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(439, 70, 151, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.attackType_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.attackType_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.attackType_verticalLayout.setObjectName("attackType_verticalLayout")
        ######################RADIO BUTTONS START ################################

        self.SYN_floodButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.SYN_floodButton.setObjectName("SYN_floodButton")
        self.SYN_floodButton.toggled.connect(lambda: self.btnstate(self.SYN_floodButton))
        self.attackType_verticalLayout.addWidget(self.SYN_floodButton)

        self.POST_FloodButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.POST_FloodButton.setObjectName("POST_FloodButton")
        self.POST_FloodButton.toggled.connect(lambda: self.btnstate(self.POST_FloodButton))

        self.attackType_verticalLayout.addWidget(self.POST_FloodButton)

        self.ICMP_floodButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.ICMP_floodButton.setObjectName("ICMP_floodButton")
        self.ICMP_floodButton.toggled.connect(lambda: self.btnstate(self.ICMP_floodButton))

        self.attackType_verticalLayout.addWidget(self.ICMP_floodButton)

        self.PODbutton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.PODbutton.setObjectName("PODbutton")
        self.PODbutton.toggled.connect(lambda: self.btnstate(self.PODbutton))

        self.attackType_verticalLayout.addWidget(self.PODbutton)

        self.TeardropButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.TeardropButton.setObjectName("TeardropButton")
        self.TeardropButton.toggled.connect(lambda: self.btnstate(self.TeardropButton))

        self.attackType_verticalLayout.addWidget(self.TeardropButton)

        self.MalformButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.MalformButton.setObjectName("MalformButton")
        self.MalformButton.toggled.connect(lambda: self.btnstate(self.MalformButton))

        self.attackType_verticalLayout.addWidget(self.MalformButton)
        ######################RADIO BUTTONS END################################

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 40, 371, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.input_entry_layer = QtWidgets.QGridLayout(self.horizontalLayoutWidget)
        self.input_entry_layer.setContentsMargins(0, 0, 0, 0)
        self.input_entry_layer.setObjectName("input_entry_layer")

        self.Top_port_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Top_port_label.setObjectName("Top_port_label")

        self.input_entry_layer.addWidget(self.Top_port_label, 1, 4, 1, 1)

        self.target_port_bot_entry = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.target_port_bot_entry.setObjectName("target_port_bot_entry")

        self.input_entry_layer.addWidget(self.target_port_bot_entry, 3, 2, 1, 1)

        self.bottom_port_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.bottom_port_label.setObjectName("bottom_port_label")

        self.input_entry_layer.addWidget(self.bottom_port_label, 1, 2, 1, 1)

        self.Target_IP_entry = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.Target_IP_entry.setObjectName("Target_IP_entry")

        self.input_entry_layer.addWidget(self.Target_IP_entry, 0, 2, 1, 1)

        self.Target_IP_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Target_IP_label.setObjectName("Target_IP_label")

        self.input_entry_layer.addWidget(self.Target_IP_label, 0, 1, 1, 1)

        self.Scan_port_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Scan_port_label.setObjectName("Scan_port_label")

        self.input_entry_layer.addWidget(self.Scan_port_label, 3, 1, 1, 1)
# ********************** port entry top ************************
        self.Target_port_top_entry = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.Target_port_top_entry.setObjectName("Target_port_top_entry")

# ****************
        self.input_entry_layer.addWidget(self.Target_port_top_entry, 3, 4, 1, 1)

        self.dash_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.dash_label.setObjectName("dash_label")

        self.input_entry_layer.addWidget(self.dash_label, 3, 3, 1, 1)

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 0, 541, 36))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")

        self.ProgramName_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.ProgramName_Layout.setContentsMargins(0, 0, 0, 0)
        self.ProgramName_Layout.setObjectName("ProgramName_Layout")
        self.Program_name = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.Program_name.setObjectName("Program_name")
        self.ProgramName_Layout.addWidget(self.Program_name)

        self.Attack_type_frame = QtWidgets.QFrame(self.centralwidget)
        self.Attack_type_frame.setGeometry(QtCore.QRect(430, 38, 161, 211))
        self.Attack_type_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Attack_type_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Attack_type_frame.setObjectName("Attack_type_frame")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Attack_type_frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 160, 31))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.attackType_verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.attackType_verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.attackType_verticalLayout_2.setObjectName("attackType_verticalLayout_2")

        self.attackType_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.attackType_label.setObjectName("attackType_label")

        self.attackType_verticalLayout_2.addWidget(self.attackType_label)

        self.attackType_line = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.attackType_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.attackType_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.attackType_line.setObjectName("attackType_line")

        self.attackType_verticalLayout_2.addWidget(self.attackType_line)

        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(250, 120, 168, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")

        self.Scan_buttons_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.Scan_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.Scan_buttons_layout.setObjectName("Scan_buttons_layout")

# ********* START SCAN BUTTON**********************
        self.Start_scan_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.Start_scan_button.setObjectName("Start_scan_button")
        self.Start_scan_button.clicked.connect(self.scan_btn_pressed)
        self.Scan_buttons_layout.addWidget(self.Start_scan_button)

        # self.Cancel_scan_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        # self.Cancel_scan_button.setObjectName("Cancel_scan_button")
        # self.Cancel_scan_button.clicked.connect(self.scannerThread.stop())

# ********* CANCEL SCAN BUTTON *********************

        # self.Scan_buttons_layout.addWidget(self.Cancel_scan_button)

        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(9, 210, 251, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")

        self.Attack_port_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.Attack_port_Layout.setContentsMargins(0, 0, 0, 0)
        self.Attack_port_Layout.setObjectName("Attack_port_Layout")

        self.Attack_port_label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.Attack_port_label.setObjectName("Attack_port_label")

        self.Attack_port_Layout.addWidget(self.Attack_port_label)

        self.Attack_port_entry = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.Attack_port_entry.setObjectName("Attack_port_entry")

        self.Attack_port_Layout.addWidget(self.Attack_port_entry)

        self.Attack_type_frame.raise_()

        self.gridLayoutWidget.raise_()

        self.verticalLayoutWidget.raise_()

        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.horizontalLayoutWidget_4.raise_()
        self.horizontalLayoutWidget_5.raise_()

        DoSr.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(DoSr)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 611, 22))
        self.menubar.setObjectName("menubar")

        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        DoSr.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(DoSr)
        self.statusbar.setObjectName("statusbar")

        DoSr.setStatusBar(self.statusbar)

        self.actionQuit = QtWidgets.QAction(DoSr)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.setShortcut('Ctrl+q')
        self.actionQuit.triggered.connect(self.quit_triggered)

        self.actionAbout = QtWidgets.QAction(DoSr)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.setShortcut('Ctrl+h')
        self.actionAbout.triggered.connect(self.showaboutdialog)

        self.menufile.addAction(self.actionQuit)

        self.menuHelp.addAction(self.actionAbout)

        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(DoSr)
        QtCore.QMetaObject.connectSlotsByName(DoSr)
        # *********** SCAN THREADING STUFF************
        self.scannerThread = ScannerThread()
        #self.Connect(self.scannerThread, QtCore.SIGNAL("scanComplete()"),self.scanComplete, Qt.DirectConnection)
        # ***************************************

    def scanComplete(self):
        sc = QMessageBox()
        sc.setText("Scan Complete!")
        sc.setWindowTitle("Port Scan")
        sc.setWindowModality(Qt.ApplicationModal)
        sc.exec_()

    def scan_btn_pressed(self):
        target = self.Target_IP_entry.text()

        if target == '':
                ui.Output_display_box.append('Please enter a target IP address...')
                return None
        if self.target_port_bot_entry.text == "":
            port_bot = '0'
        else:
            port_bot = self.target_port_bot_entry.text()
        if self.Target_port_top_entry.text() == "":
            port_top = "65535"
        else:
            port_top = self.Target_port_top_entry.text()

        #print(target, port_bot, port_top)
        self.scannerThread.start()
        self.scannerThread.wait()

    @staticmethod
    def btnstate(b):

        if b.objectName() == "SYN_floodButton":
            if b.isChecked():
                print(b.text() + " is selected")
            else:
                print(b.text() + " is deselected")

        if b.objectName() == "POST_FloodButton":
            if b.isChecked():
                print(b.text() + " is selected")
            else:
                print(b.text() + " is deselected")

        if b.objectName() == "ICMP_floodButton":
            if b.isChecked():
                print(b.text() + " is selected")
            else:
                print(b.text() + " is deselected")

        if b.objectName() == "PODbutton":
            if b.isChecked():
                print(b.text() + " is selected")
            else:
                print(b.text() + " is deselected")

        if b.objectName() == "TeardropButton":
            if b.isChecked():
                print(b.text() + " is selected")
            else:
                print(b.text() + " is deselected")

        if b.objectName() == "MalformButton":
            if b.isChecked():
                print(b.text() + " is selected")
            else:
                print(b.text() + " is deselected")

    @staticmethod
    def quit_triggered():
        app.quit()

    @staticmethod
    def showaboutdialog():
        d = QMessageBox()
        d.setText(
            "DoSr is a tool for administrator to test their systems. \nDeveloped by Jacob Pogue CSU Chico. \nDeveloped in Python"
            " and Scapy with a PyQt interface. \nThis Software is for educational and testing purposes only. ")

        d.setWindowTitle("About")
        d.setWindowModality(Qt.ApplicationModal)
        d.exec_()

    def retranslateUi(self, DoSr):
        _translate = QtCore.QCoreApplication.translate
        DoSr.setWindowTitle(_translate("DoSr", "MainWindow"))
        self.Start_Attack_button.setText(_translate("DoSr", "Perform Attack"))
        self.Output_label.setText(_translate("DoSr",
                                             "<html><head/><body><p><span style=\" font-size:18pt;\">Output:</span></p></body></html>"))
        self.Stop_attack_button.setText(_translate("DoSr", "Stop Attack"))
        self.SYN_floodButton.setText(_translate("DoSr", "SYN Flood Attack"))
        self.POST_FloodButton.setText(_translate("DoSr", "POST Flood Attack"))
        self.ICMP_floodButton.setText(_translate("DoSr", "PING Flood Attack"))
        self.PODbutton.setText(_translate("DoSr", "Ping-of-Death Attack"))
        self.TeardropButton.setText(_translate("DoSr", "Tear Drop Attack"))
        self.MalformButton.setText(_translate("DoSr", "Malformed Packet"))
        self.Top_port_label.setText(_translate("DoSr", "Top"))
        self.bottom_port_label.setText(_translate("DoSr", "Bottom"))
        self.Target_IP_label.setText(_translate("DoSr", "Target IP Address:"))
        self.Scan_port_label.setText(_translate("DoSr", "Scan Port:"))
        self.dash_label.setText(_translate("DoSr", "-"))
        self.Program_name.setText(_translate("DoSr",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">DoSr </span><span style=\" font-size:12pt;\">(Denial-of-Service Resiliance Tester)</span></p></body></html>"))
        self.attackType_label.setText(
            _translate("DoSr", "<html><head/><body><p align=\"center\">Attack Type:</p></body></html>"))
        self.Start_scan_button.setText(_translate("DoSr", "Scan"))
        # self.Cancel_scan_button.setText(_translate("DoSr", "Cancel"))
        self.Attack_port_label.setText(_translate("DoSr", "Attack Port:"))
        self.menufile.setTitle(_translate("DoSr", "File"))
        self.menuHelp.setTitle(_translate("DoSr", "Help"))
        self.actionQuit.setText(_translate("DoSr", "Quit"))
        self.actionAbout.setText(_translate("DoSr", "About"))


class ScannerThread(QtCore.QThread):

    def __init__(self, parent: object = None) -> object:
        super(ScannerThread, self).__init__(parent)
        self.threadactive = True

    def run(self):

        ui.Output_display_box.append('Starting Scan.....')
        # self.tar = tar
        p = nmap_port_scanner.Port_Scan(ui.target, ui.port_bot, ui.port_top)
        p.scanner()
        for host in p.nm.all_hosts():
            ui.Output_display_box.append('----------------------------------------------------')
            ui.Output_display_box.append('Host : %s (%s)' % (host, p.nm[host].hostname()))
            ui.Output_display_box.append('State : %s' % p.nm[host].state())
            for proto in p.nm[host].all_protocols():
                ui.Output_display_box.append('----------')
                ui.Output_display_box.append('Protocol : %s' % proto)

                lport = p.nm[host][proto].keys()

                for port in lport:
                    ui.Output_display_box.append('port : %s\tState: %s\t Service: %s\t Version: %s %s'
                           % (port, p.nm[host][proto][port]['state'],
                              p.nm[host][proto][port]['product'],
                              p.nm[host][proto][port]['version'],
                              p.nm[host][proto][port]['name']))
        # self.emit(QtCore.SIGNAL("scanComplete()"))

    def stop(self):
            self.threadactive = False
            self.wait()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    DoSr = QtWidgets.QMainWindow()
    ui = Ui_DoSr()
    ui.setupUi(DoSr)
    DoSr.show()
    sys.exit(app.exec_())
