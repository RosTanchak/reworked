#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import sys
import math
import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *


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

        self.prepearedText = self.all_calculations.splitText(4)
        new_symbols_Text = self.all_calculations.calcNewSymbols(self.prepearedText)
        self.fill_table(4, new_symbols_Text)
        self.tabWidget.setTabEnabled(1, True)


    def fill_table(self, tableNumber, text):
        if tableNumber == 1:
            pass
        elif tableNumber == 2:
            pass
        elif tableNumber == 3:
            pass
        elif tableNumber == 4:
            big_P_x = self.all_calculations.calculate_P_tab4()
            self.tableWidget_3.setRowCount(len(text))
            for itemRow in range(0,len(text)):
                item0 = QTableWidgetItem(0)
                item0.setData(Qt.DisplayRole,itemRow)
                item1 = QTableWidgetItem(1)
                item1.setText(str(self.prepearedText[itemRow]))
                item2 = QTableWidgetItem(2)
                item2.setText(str(text[itemRow]))
                item3 = QTableWidgetItem(3)
                item3.setText(str(big_P_x[itemRow]))
                #self.setTab4.append(,self.readyText[itemRow], self.newWordsText[itemRow], self.big_P_x[itemRow])
                self.tableWidget_3.setItem(itemRow,0,item0)
                self.tableWidget_3.setItem(itemRow,1,item1)
                self.tableWidget_3.setItem(itemRow,2,item2)
                self.tableWidget_3.setItem(itemRow,3,item3)
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
