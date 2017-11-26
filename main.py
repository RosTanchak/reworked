#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import sys
import math

import ui_design #import form from '/reworked/ui_design.py'



class PraktykaApp(QtGui.QMainWindow, ui_design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(PraktykaApp, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_5.clicked.connect(self.open_file)

    def open_file(self):
        filename = QtGui.QFileDialog.getOpenFileName()
        if filename:
            filename = unicode(filename, "utf-8")
            text = open(filename).read()
            print("filename", text)
            # self.originalText = text.decode("utf-8")
            # global L
            # L = len(self.originalText)
            # self.splitText(self.originalText)

    def save_file(self):
        name = QtGui.QFileDialog.getSaveFileName()
        name = unicode(name, "utf-8")
        self.file1 = open(name + ":AnalysisSymbol.txt", 'w' )
        self.file2 = open(name + ":dti.txt", 'w' )
        self.file3 = open(name + ":Ti.txt", 'w' )
        self.file4 = open(name + ":NewSymbols.txt", 'w' )
        self.setTab1 = True
        self.setTab2 = True
        self.setTab3 = True
        self.setTab4 = True

        #SAVE IMplamentation
        # self.table1()
        # self.fillTableTab2()
        # self.fillTableTab3()
        # self.buildTable4()



def main():
    app = QtGui.QApplication(sys.argv)
    form = PraktykaApp()
    form.show()
    app.exec_()


#excute main app
if __name__ == '__main__':
    main()
