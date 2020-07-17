#!python3.8

# pyuic5 ./unic_ui.ui -o ./unic_ui.py
# qtDesigner

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from unic_ui import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

window = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(window)

def unique(list1): 
    # insert the list to the set 
    list_set = set(list1) 
    # convert the set to the list 
    unique_list = (list(list_set)) 
    return unique_list
      

def operatetext():
	text = ui.plainTextEdit.toPlainText()
	if (ui.checkBox_2.checkState()):
		text = text.lower()
	lines = text.splitlines()

	u_lines = unique(lines)
	if (ui.checkBox_1.checkState()):
		u_lines.sort()
	ui.plainTextEdit.setPlainText("\n".join(u_lines))
	ui.plainTextEdit.repaint()

#clicks
ui.pushButton.clicked.connect(operatetext)


window.show()
sys.exit(app.exec_())

# 123
# asd
# ASD
# qwe
# QWE