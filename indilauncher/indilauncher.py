#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import os
import glob

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from indilauncher.ui.mainwindow import Ui_IndilauncherMainWindow


class Indilauncher(QMainWindow):
    indiserver_executable = '/usr/bin/indiserver'
    logs_directory = 'devices_logs'
    drivers_directory = '/usr/share/indi'
    drivers_pattern = 'indi_*.xml'

    def __init__(self):
        super(Indilauncher, self).__init__()
        self.ui = Ui_IndilauncherMainWindow()
        self.ui.setupUi(self)
        # Ajout des combobox dans une liste pour faciliter la manipulation
        self.drivers_comboboxes = (
            self.ui.cb_telescope,
            self.ui.cb_ccdapn,
            self.ui.cb_focuser,
            self.ui.cb_guide,
            self.ui.cb_joystick,
            self.ui.cb_aux1,
            self.ui.cb_aux2,
            self.ui.cb_aux3
        )

        # Définition des processus enfants
        self.proc_lsusb = QProcess(self)
        self.proc_lsusb.setProcessChannelMode(QProcess.MergedChannels)
        self.proc_indiserver = QProcess(self)
        # En réactivant la ligne ci-dessous, on envoie stdout et stderr vers le même canal
        # et ça spam dans la console (la fameuse erreur "execlp: No such file or directory")
        # self.proc_indiserver.setProcessChannelMode(QProcess.MergedChannels)
        self.pid_indiserver = 0

        self.connect_signals()

        self.list_devices()
        self.populate_drivers_lists()

    def connect_signals(self):
        # Bouton Liste USB
        self.ui.btn_listUSB.clicked.connect(self.list_devices)
        # Processus Liste USB
        self.proc_lsusb.readyRead.connect(self.show_device_list)
        self.proc_lsusb.started.connect(lambda: self.ui.btn_listUSB.setEnabled(False))
        self.proc_lsusb.finished.connect(lambda: self.ui.btn_listUSB.setEnabled(True))

        # Bouton INDI Server
        self.ui.btn_indiserver.clicked.connect(self.launch_indi_server)
        # Processus Liste USB
        self.proc_indiserver.readyRead.connect(self.show_server_output)
        self.proc_indiserver.started.connect(self.on_indiserver_started)
        self.proc_indiserver.finished.connect(self.on_indiserver_stopped)

    @pyqtSlot()
    def list_devices(self):
        self.ui.txt_console.appendPlainText("\nBus & Périphériques USB détectés :\n")
        self.proc_lsusb.start('lsusb')

    @pyqtSlot()
    def show_device_list(self):
        # Motif d'expression régulière
        # Bus 004   Device 002:     ID 0a5c:2145 Broadcom Corp. BCM2045B (BDC-2.1) [Bluetooth Controller]
        # Bus <bus> Device <device> ID <id>      <tag>
        device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
        # récupérer le résultat du process lsusb
        output = self.proc_lsusb.readAll()
        # Traiter ligne par ligne
        for line in output.split('\n'):
            if line:
                line = bytes(line).decode()
                # Appliquer l'expression régulière device_re sur la ligne en cours
                dev_info = device_re.match(line)
                if dev_info:
                    # Récupérer les captures ( ?<nom>...) dans un "dictionnaire" Python
                    info_line = dev_info.groupdict()
                    # Extraire/dépiler la case "tag" du dictionnaire
                    device_name = info_line.pop('tag')
                    # Ajout à la fin de la zone de texte
                    self.ui.txt_console.appendPlainText(device_name)

    @pyqtSlot()
    def show_server_output(self):
        indi_output = bytes(self.proc_indiserver.readAll()).decode()
        self.ui.txt_console.appendPlainText(indi_output)

    @pyqtSlot()
    def populate_drivers_lists(self):
        # Initialise les combobox
        tuple(cb.clear() for cb in self.drivers_comboboxes)
        tuple(cb.addItem('') for cb in self.drivers_comboboxes)
        # Récupère la liste des fichiers drivers
        drivers = glob.glob(self.drivers_directory + '/' + self.drivers_pattern)
        # Tri par ordre alpha
        drivers.sort()
        # Pour chaque nom de fichier, on l'ajoute à chaque liste déroulante
        for fileName in drivers:
            tuple(cb.addItem(fileName.replace(self.drivers_directory + '/', '')) for cb in self.drivers_comboboxes)

    @pyqtSlot()
    def launch_indi_server(self):
        selected_drivers = ['-v']
        for combo in self.drivers_comboboxes:
            current_val = combo.currentText().replace('.xml', '')
            if current_val:
                selected_drivers.append(current_val)

        self.ui.txt_console.appendPlainText(('-' * 10) + '\n')
        self.ui.txt_console.appendPlainText(self.indiserver_executable + ' ' + ' '.join(selected_drivers))
        self.proc_indiserver.start(self.indiserver_executable, selected_drivers)

    @pyqtSlot()
    def on_indiserver_started(self):
        self.ui.btn_indiserver.setEnabled(False)
        self.ui.txt_console.appendPlainText('Process ID : ' + str(self.proc_indiserver.pid()))
        self.pid_indiserver = self.proc_indiserver.pid()

    @pyqtSlot()
    def on_indiserver_stopped(self):
        self.pid_indiserver = 0
        self.ui.txt_console.appendPlainText('Process ended')
        self.ui.btn_indiserver.setEnabled(True)

    def closeEvent(self, q_close_event):
        if self.pid_indiserver > 0:
            print('Close Event catched, killing subprocess #%d' % self.pid_indiserver)
            os.kill(self.pid_indiserver, 9)
        super().closeEvent(q_close_event)
