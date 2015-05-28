#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'scollado'

import sys

from PyQt4.QtGui import QApplication

from indilauncher.indilauncher import Indilauncher



# pour rendre le fichier *.py exécutable
if __name__ == "__main__":  # pour rendre le code exécutable
    app = QApplication(sys.argv)
    window = Indilauncher()
    window.show()
    sys.exit(app.exec_())
