#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import sys
import math
import os


import ui_design #import form from '/reworked/ui_design.py'
from  all_calculations import All_calculations #import all math functions



class PraktykaApp(QtGui.QMainWindow, ui_design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(PraktykaApp, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_5.clicked.connect(self.open_file)
        self.pushButton_6.clicked.connect(self.save_file)
        self.pushButton_7.clicked.connect(self.build)

    def open_file(self):
        filename = QtGui.QFileDialog.getOpenFileName()
        if filename:
            filename = unicode(filename, "utf-8")
            text = open(filename).read()
            self.all_calculations = All_calculations(text)

    def save_file(self):
        name = QtGui.QFileDialog.getSaveFileName()
        name = unicode(name, "utf-8")
        self.file1 = open(name + ":AnalysisSymbol.txt", 'w' )
        self.file2 = open(name + ":dti.txt", 'w' )
        self.file3 = open(name + ":Ti.txt", 'w' )
        self.file4 = open(name + ":NewSymbols.txt", 'w' )

    def build(self):
        # self.completed = 0
        # while self.completed < 100:
        #     self.completed += 0.00001
        #     self.progressBar.setValue(self.completed)
        #     self.tabWidget.setTabEnabled(1, False)

        prepearedText = self.all_calculations.splitText(4)
        new_symbols_Text = self.all_calculations.calcNewSymbols(prepearedText)
        print("hui", new_symbols_Text)
        self.tabWidget.setTabEnabled(1, True)


    def fill_table(self, tableNumber):
        if tableNumber == 1:
            print("1")
        elif tableNumber == 2:
            pass
        elif tableNumber == 3:
            pass
        elif tableNumber == 4:
            pass
        else:
            return




def main():
    app = QtGui.QApplication(sys.argv)
    form = PraktykaApp()
    form.show()
    app.exec_()


#excute main app
if __name__ == '__main__':
    main()
