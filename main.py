#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, unicode_literals

from PyQt4 import QtGui
import sys
import math
import os
import ntpath

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
from collections import Counter


import ui_design #import form from '/reworked/ui_design.py'
from  all_calculations import All_calculations #import all math functions



class PraktykaApp(QtGui.QMainWindow, ui_design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(PraktykaApp, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buildTabHist1)
        self.pushButton_2.clicked.connect(self.buildGrahTab2)
        self.pushButton_3.clicked.connect(self.buildGrahTab4)
        self.pushButton_5.clicked.connect(self.open_file)
        self.pushButton_6.clicked.connect(self.save_file)
        self.pushButton_7.clicked.connect(self.build)
        self.radioButton_6.clicked.connect(self.enableOrDisable)
        self.radioButton_7.clicked.connect(self.enableOrDisable)
        self.file1_info = []
        self.file2_info = []
        self.file3_info = []
        self.file4_info = []

    def open_file(self):
        filename = QtGui.QFileDialog.getOpenFileName()
        if filename:
            filename = unicode(filename, "utf-8")
            text = open(filename).read()
            self.originalText = text
            self.all_calculations = All_calculations(text)
            self.label_3.setText(ntpath.basename(filename))
            self.label_5.setText("You can choose an area  ( 1-"+  str(len(self.originalText )) + " ) to discover, below:")

    def save_file(self):
        name = QtGui.QFileDialog.getSaveFileName()
        if name and len(name)>0:
            name = unicode(name, "utf-8")
            file1 = open(name + ":AnalysisSymbol.txt", 'w' )
            self.write_loop(file1, 1)
            file2 = open(name + ":dti.txt", 'w' )
            self.write_loop(file2, 2)
            file3 = open(name + ":Ti.txt", 'w' )
            file4 = open(name + ":NewSymbols.txt", 'w' )
            self.write_loop(file4, 4)

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            stringer= str("please set name")
            msg.setText(stringer)
            msg.setWindowTitle("Save error")
            msg.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            msg.setStandardButtons(QMessageBox.Ok )
            msg.exec_()
            return

    def write_loop(self, file, file_number):
        if file_number == 1:
            for item in self.file1_info:
                file.write(str(str(item[0]) + '\t' + str(item[1])+ '\t' + str(item[2])+'\t' + str(item[3]))+'\n')
        if file_number == 2:
            for item in self.file2_info:
                file.write(item)
        if file_number == 3:
            for item in self.file1_info:
                file.write(item)
        if file_number == 4:
            for item in self.file4_info:
                file.write(item)


    def enableOrDisable(self):
        if self.radioButton_6.isChecked():
            self.spinBox_2.setEnabled(False)
            self.spinBox_3.setEnabled(False)
            self.spinBox_4.setEnabled(False)
        elif self.radioButton_7.isChecked():
            self.spinBox_2.setEnabled(True)
            self.spinBox_3.setEnabled(True)
            self.spinBox_4.setEnabled(True)

    def build(self):
        # self.completed = 0
        # while self.completed < 100:
        #     self.completed += 0.00001
        #     self.progressBar.setValue(self.completed)
        #     self.tabWidget.setTabEnabled(1, False)
        self.prepearedText = self.all_calculations.splitText(self.spinBox.value())
        self.new_symbols_Text = self.all_calculations.calcNewSymbols(self.prepearedText)
        self.fill_table(1, self.prepearedText)
        self.fill_table(2, self.new_symbols_Text)
        self.fill_table(4, self.new_symbols_Text)
        self.tabWidget.setTabEnabled(1, True)


    def fill_table(self, tableNumber, text):
        if tableNumber == 1:
            counts = Counter(text)
            labels, valuesF = zip(*counts.items())
            indexes = np.arange(len(labels))
            values_f = self.all_calculations.calcf( valuesF)
            self.tableWidget.setRowCount(len(valuesF))
            output = [0] * len(valuesF)
            for i, x in enumerate(sorted(range(len(valuesF)), key=lambda y: valuesF[y], reverse = True)):
                output[x] = i+1
            for itemRow in range(0,len(valuesF)):
                item0 = QTableWidgetItem(0)
                item0.setData(Qt.DisplayRole, output[itemRow])
                item1 = QTableWidgetItem(1)
                item1.setText(labels[itemRow])
                item2 = QTableWidgetItem(2)
                item2.setData(Qt.DisplayRole, valuesF[itemRow])
                item3 = QTableWidgetItem(3)
                item3.setText(str(values_f[itemRow]))
                self.tableWidget.setItem(itemRow, 0, item0)
                self.tableWidget.setItem(itemRow, 1, item1)
                self.tableWidget.setItem(itemRow, 2, item2)
                self.tableWidget.setItem(itemRow, 3, item3)
                self.file1_info.append([output[itemRow],labels[itemRow],valuesF[itemRow],values_f[itemRow]])
            self.file1_info = sorted(self.file1_info, key=itemgetter(0))
        elif tableNumber == 2:
                self.result_tap_2 = self.all_calculations.calcSecTab(self.new_symbols_Text)
                self.result_P_tap_2 = self.all_calculations.calc_Big_P_tab2()
                self.tableWidget_2.setRowCount(len(self.result_tap_2)-1)
                summary = sum(self.result_tap_2)
                for itemRow in range(0,len(self.result_tap_2)):
                    item0 = QTableWidgetItem()
                    item0.setData(Qt.DisplayRole, itemRow)
                    item1 = QTableWidgetItem()
                    #item1.setText(str(self.result_tap_2[itemRow]))
                    item1.setData(Qt.DisplayRole, self.result_tap_2[itemRow])
                    item2 = QTableWidgetItem()
                    item2.setText(str(self.result_tap_2[itemRow]/summary))
                    self.result_tap_2[itemRow] = self.result_tap_2[itemRow]/summary
                    item3 = QTableWidgetItem()
                    item3.setText(str(self.result_P_tap_2[itemRow]))
                    #self.setTab2.append(str(str(itemRow + 1) + '\t' + str(self.result_tap_2[itemRow]) + '\t' + str(self.result_tap_2[itemRow]/summary)+ '\t' + str(self.result_P_tap_2[itemRow])+ '\n'))
                    self.tableWidget_2.setItem(itemRow,0,item0)
                    self.tableWidget_2.setItem(itemRow,1,item1)
                    self.tableWidget_2.setItem(itemRow,2,item2)
                    self.tableWidget_2.setItem(itemRow,3,item3)
                    self.file2_info.append(str(str(itemRow + 1) + '\t' + str(self.result_tap_2[itemRow]) + '\t' + str(self.result_tap_2[itemRow]/summary)+ '\t' + str(self.result_P_tap_2[itemRow]))+'\n')

        elif tableNumber == 3:
            pass
        elif tableNumber == 4:
            self.big_P_x = self.all_calculations.calculate_P_tab4(self.new_symbols_Text)
            self.tableWidget_3.setRowCount(len(text))
            for itemRow in range(0,len(text)):
                item0 = QTableWidgetItem(0)
                item0.setData(Qt.DisplayRole,itemRow)
                item1 = QTableWidgetItem(1)
                item1.setText(str(self.prepearedText[itemRow]))
                item2 = QTableWidgetItem(2)
                item2.setText(str(text[itemRow]))
                item3 = QTableWidgetItem(3)
                item3.setText(str(self.big_P_x[itemRow]))
                #self.setTab4.append(,self.readyText[itemRow], self.newWordsText[itemRow], self.big_P_x[itemRow])
                self.tableWidget_3.setItem(itemRow,0,item0)
                self.tableWidget_3.setItem(itemRow,1,item1)
                self.tableWidget_3.setItem(itemRow,2,item2)
                self.tableWidget_3.setItem(itemRow,3,item3)
                self.file4_info.append(str(str(itemRow) + '\t' + str(self.prepearedText[itemRow])+ '\t' + str(text[itemRow])+'\t' + str( self.big_P_x[itemRow]))+'\n')
        else:
            return

    def buildTabHist1(self):
        prepeare_counts = self.prepearedText
        result = None
        counts = Counter(prepeare_counts)
        labels, values = zip(*counts.items())
        indSort = np.argsort(values)[::-1]
        labels = np.array(labels)[indSort]
        values = np.array(values)[indSort]
        seen = set()
        seen_add = seen.add
        result= [x for x in values if not (x in seen or seen_add(x))]

        indexes = np.arange(len(result))
        bar_width = 0.35
        for i in range(1,len(result)):
            result[i] = math.log10(result[i])
        plt.bar(indexes[1::], result[1::])
        plt.xlim(min(indexes), max(indexes))
        plt.show()

    def buildGrahTab2(self):
        if self.radioButton.isChecked():
            iteration_x = []
            iteration_y = self.result_tap_2
            newArrayX = []
            newArrayY = []
            for i in range(1, len(self.result_tap_2)):
                #    x = [math.log10(item) for item in iteration_x]
                newArrayX.append(math.log10(i))
                newArrayY.append(math.log10(iteration_y[i]))
                y = newArrayY
                x = newArrayX

            plt.plot(x, y, 'k', marker='o')
            plt.grid(color='b', linestyle='-', linewidth=0.5)
            plt.show()
        elif self.radioButton_2.isChecked():
            iteration_x = []
            iteration_y = self.result_P_tap_2
            newArrayY = []
            newArrayX = []
            for i in range(1,len(self.result_P_tap_2)):
                newArrayX.append(math.log10(i))
                newArrayY.append(math.log10(iteration_y[i]))
                x = newArrayX
                y = newArrayY

            plt.plot(x, y, 'k', marker='o')
            plt.grid(color='b', linestyle='-', linewidth=0.5)
            plt.show()

    def buildGrahTab4(self):
        iteration_x = []
        iteration_y = self.big_P_x
        newArrayY = []
        for i in range(1,len(self.big_P_x)):
            if iteration_y[i] != 0:
                iteration_x.append(math.log10(i))
                newArrayY.append(math.log10(iteration_y[i]))
        x = iteration_x
        y = newArrayY

        plt.plot(x, y, 'k', marker = 'o')
        plt.grid(color='b', linestyle='-', linewidth=0.5)
        plt.show()


def main():
    app = QtGui.QApplication(sys.argv)
    form = PraktykaApp()
    form.show()
    app.exec_()


#excute main app
if __name__ == '__main__':
    main()
