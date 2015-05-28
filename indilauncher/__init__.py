#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'scollado'

import os

from indilauncher.indilauncher import Indilauncher

# Si le répertoire de sauvegarde des fichiers lsusb n'existe pas, on le crée
if not os.path.exists(Indilauncher.logs_directory):
    os.makedirs(Indilauncher.logs_directory)

# Si le répertoire des pilotes INDIlib n'existe pas, on chouine
if not os.path.exists(Indilauncher.drivers_directory):
    raise FileNotFoundError("INDIlib drivers directory not found (/usr/share/indi).")
