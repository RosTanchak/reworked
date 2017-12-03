#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, unicode_literals

from PyQt4 import QtGui
from PyQt4.QtCore import QThread
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
#from thread import CalculateThread #import calculatin thread

#calculate3pad(1,2,4)
class CalculateThread(QThread):
    def __init__(self, text, prepearedText, isSliced, steps, step, wholeText, N, all_calculations):
        QThread.__init__(self)
        self.originalText = text
        self.prepearedText = prepearedText
        self.prepearedTextLength = len(prepearedText)
        self.steps = steps
        self.step = step
        self.N = N
        self.isSliced = isSliced
        self.wholeText = wholeText
        self.all_calculations = all_calculations


    def __del__(self):
        self.wait()

    #calculate new symbols in background
    def run(self):
        text = self.prepearedText
        if self.isSliced == True and self.step > 0:
            text = self.wholeText
        readyItems = []
        binaryItems = []
        self.new_symbols_Text = []
        for item in text:
            try:
                result = readyItems.index(item)
                self.emit(SIGNAL('add_binary(QString)'), str(0))
                readyItems.append(item)
                self.new_symbols_Text.append(0)
                # self.emit(SIGNAL('add_ready(QString)'), str(item))
            except ValueError:
                self.emit(SIGNAL('add_binary(QString)'), str(1))
                self.new_symbols_Text.append(1)
                readyItems.append(item)
                # self.emit(SIGNAL('add_ready(QString)'), str(item))
        self.emit(SIGNAL('fill_table(QString)'), str(1))
        self.emit(SIGNAL('fill_table(QString)'), str(2))
        self.emit(SIGNAL('fill_table(QString)'), str(4))
        #special for 3rd tab
        if self.isSliced == True and self.step > 0:
            k_text_len = self.prepearedTextLength
            index = 0
            p_arrays = []
            while k_text_len == self.prepearedTextLength:
                k_text = self.new_symbols_Text[index : index + self.prepearedTextLength]
                index += self.step
                k_text_len = len(k_text)
                p_arrays.append(self.all_calculations.chunksIntervals(k_text))
                # p_arrays.append(sum(k_text))
            self.emit(SIGNAL('fill_table(QString)'), str(3))

# while self.breakAll == False:
#     #loop1
#     print("00",self.loop1Idex)
#     if  self.loop1Idex < len(text) and self.breakOne == False and self.breakSecond == False:
#         try:
#             print("1")
#             result = readyItems.index(text[self.loop1Idex])
#             self.emit(SIGNAL('add_binary(QString)'), str(0))
#             readyItems.append(loop1Idex)
#             self.new_symbols_Text.append(0)
#             loop1Idex+=1
#             # self.emit(SIGNAL('add_ready(QString)'), str(item))
#         except ValueError:
#             print("2")
#             self.emit(SIGNAL('add_binary(QString)'), str(1))
#             self.new_symbols_Text.append(1)
#             readyItems.append(self.loop1Idex)
#             self.loop1Idex +=1
#     elif self.loop1Idex >= len(text):
#         self.breakOne = True
#             # self.emit(SIGNAL('add_ready(QString)'), str(item))
#     #special for 3rd tab
#     # elif self.isSliced == True and self.k_text_len == self.prepearedTextLength  and  self.breakOne == True and self.breakSecond == False:
#     #         print("3")
#     #         k_text = self.new_symbols_Text[self.loop2Idex  : self.loop2Idex  + self.prepearedTextLength]
#     #         self.loop2Idex  += self.step
#     #         self.k_text_len = len(k_text)
#     #         p_arrays.append(self.all_calculations.chunksIntervals(k_text))
#     #         # p_arrays.append(sum(k_text))
#     # elif self.k_text_len != self.prepearedTextLength:
#     #     print("4")
#     #     self.breakSecond = True
#     elif self.breakSecond and self.breakOne:
#         print("5")
#         self.breadAll= True

class PraktykaApp(QtGui.QMainWindow, ui_design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(PraktykaApp, self).__init__(parent)
        self.setupUi(self)
        self.disaleAll(True)
        self.pushButton.clicked.connect(self.buildTabHist1)
        self.pushButton_2.clicked.connect(self.buildGrahTab2)
        self.pushButton_3.clicked.connect(self.buildGrahTab4)
        self.pushButton_5.clicked.connect(self.open_file)
        self.pushButton_6.clicked.connect(self.save_file)
        self.pushButton_7.clicked.connect(self.build)
        self.radioButton_6.clicked.connect(self.enableOrDisable)
        self.radioButton_7.clicked.connect(self.enableOrDisable)
        self.tabWidget.setTabEnabled(1, False)
        self.spinBox_3.setMinimum(100)
        self.spinBox_4.setMinimum(0)
        self.flagStep = True
        self.N = self.getFromLineEdit()


        self.file1_info = []
        self.file2_info = []
        self.file3_info = []
        self.file4_info = []

        self.isSliced = False;

    def disaleAll(self, getValue):
        if getValue:
            self.pushButton_6.setEnabled(False)
            self.pushButton_7.setEnabled(False)
            self.pushButton_8.setEnabled(False)
            self.radioButton_6.setEnabled(False)
            self.radioButton_7.setEnabled(False)
            self.spinBox.setEnabled(False)
            self.spinBox_2.setEnabled(False)
            self.spinBox_3.setEnabled(False)
            self.spinBox_4.setEnabled(False)
            self.lineEdit.setEnabled(False)
            return
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.radioButton_6.setEnabled(True)
        self.radioButton_7.setEnabled(True)
        self.spinBox.setEnabled(True)
        self.lineEdit.setEnabled(True)
        if self.radioButton_7.isChecked():
            self.isSliced = True;
            self.spinBox_2.setEnabled(True)
            self.spinBox_3.setEnabled(True)
            self.spinBox_4.setEnabled(True)

    def open_file(self):
        filename = QtGui.QFileDialog.getOpenFileName()
        if filename:
            filename = unicode(filename, "utf-8")
            text = open(filename).read()
            self.disaleAll(False)
            self.originalText = text
            self.spinBox_2.setMaximum(len(self.originalText) - self.spinBox_3.value())
            self.spinBox_3.setMaximum(len(self.originalText))
            self.spinBox_4.setMaximum(len(self.originalText))
            self.all_calculations = All_calculations(text, self.N)
            print("2")
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
            self.write_loop(file3, 3)
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
            for item in self.file3_info:
                file.write(item)
        if file_number == 4:
            for item in self.file4_info:
                file.write(item)


    def enableOrDisable(self):
        if self.radioButton_6.isChecked():
            self.isSliced = False;
            self.spinBox_2.setEnabled(False)
            self.spinBox_3.setEnabled(False)
            self.spinBox_4.setEnabled(False)
        elif self.radioButton_7.isChecked():
            self.isSliced = True;
            self.spinBox_2.setEnabled(True)
            self.spinBox_3.setEnabled(True)
            self.spinBox_4.setEnabled(True)



    #build function
    def build(self):
        self.new_symbols_Text = []
        self.readyText = []
        self.steps = 0
        self.step = 0
        self.wholeText = []
        self.all_calculations.clearAll()
        self.prepearedText = self.all_calculations.splitText(self.spinBox.value(), self.isSliced, self.spinBox_2.value(), self.spinBox_3.value())
        if self.spinBox_4.value() > 1:
            self.steps = int(len(self.originalText[self.spinBox_2.value(): len(self.originalText)])/self.spinBox_4.value())
            self.step  = self.spinBox_4.value()
            self.wholeText = self.all_calculations.splitText(self.spinBox.value(), False, self.spinBox_2.value(), self.spinBox_3.value())
        if(len(self.wholeText)>0):
            self.progressBar.setMaximum(len(self.wholeText) + 12)
        else:
            self.progressBar.setMaximum(len(self.prepearedText) + 12)
        self.progressBar.setValue(0)
        self.disaleAll(True)

        #initialise second thread
        self.calcTread = CalculateThread(self.originalText, self.prepearedText, self.isSliced, self.steps, self.step, self.wholeText, self.N, self.all_calculations)
        self.connect(self.calcTread, SIGNAL("add_binary(QString)"), self.add_binary)
        self.connect(self.calcTread, SIGNAL("fill_table(QString)"), self.fill_table)
        self.connect(self.calcTread, SIGNAL("updateProgress(QString)"), self.updateProgress)
        self.connect(self.calcTread, SIGNAL("finished()"), self.done)
        self.pushButton_8.clicked.connect(self.calcTread.terminate)

        self.calcTread.start()
        self.pushButton_8.setEnabled(True)



    def add_binary(self, value):
        self.new_symbols_Text.append(int(value))
        self.progressBar.setValue(self.progressBar.value()+1)

    def updateProgress(self, value):
        self.progressBar.setValue(self.progressBar.value()+1)

    def done(self):
        self.disaleAll(False)
        self.pushButton_8.setEnabled(False)
        QtGui.QMessageBox.information(self, "Done!", "Done Calculating!")
        self.progressBar.setValue(0)
        self.tabWidget.setTabEnabled(1, True)

    def getFromLineEdit(self):
        new_value = ""
        value = [str(item) for item in self.lineEdit.text()]
        for item in value:
            new_value = new_value + item
        return int(new_value)

    def fill_table(self, getTableNumber):
        if self.steps > 0 and self.isSliced and self.flagStep :
            self.wholeText = self.new_symbols_Text
            self.new_symbols_Text = self.new_symbols_Text[:self.spinBox_3.value()]
            self.flagStep = False
        tableNumber = int(getTableNumber)
        if tableNumber == 1:
            counts = Counter(self.prepearedText)
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
            self.progressBar.setValue(self.progressBar.value()+3)

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
            self.progressBar.setValue(self.progressBar.value()+3)

        elif tableNumber == 3:
            p = self.all_calculations.calculate_p_3(self.steps)
            self.small_p_3 = self.all_calculations.small_p_3
            self.p_i_schtrich = self.all_calculations.p_i_schtrich
            self.P_pad3 = self.all_calculations.P_pad3
            self.tableWidget_4.setRowCount(self.N)
            for itemRow in range(0,len(self.all_calculations.pad3_p)):
                print(self.P_pad3[itemRow])
                item0 = QTableWidgetItem()
                item0.setData(Qt.DisplayRole, itemRow + 1)
                item1 = QTableWidgetItem()
                item1.setData(Qt.DisplayRole, self.small_p_3[itemRow])
                item2 = QTableWidgetItem()
                item2.setText(str(self.p_i_schtrich[itemRow]))
                item3 = QTableWidgetItem()
                item3.setText(str(self.P_pad3[itemRow]))
                self.tableWidget_4.setItem(itemRow,0,item0)
                self.tableWidget_4.setItem(itemRow,1,item1)
                self.tableWidget_4.setItem(itemRow,2,item2)
                self.tableWidget_4.setItem(itemRow,3,item3)
                self.file3_info.append(str(str(itemRow + 1) + '\t' + str( self.small_p_3[itemRow])+ '\t' + str(self.p_i_schtrich[itemRow])+'\t' + str( self.P_pad3[itemRow]))+'\n')


        elif tableNumber == 4:
            self.big_P_x = self.all_calculations.calculate_P_tab4(self.new_symbols_Text)
            self.tableWidget_3.setRowCount(len(self.new_symbols_Text))
            for itemRow in range(0,len(self.new_symbols_Text)):
                item0 = QTableWidgetItem(0)
                item0.setData(Qt.DisplayRole,itemRow)
                item1 = QTableWidgetItem(1)
                item1.setText(self.prepearedText[itemRow])
                item2 = QTableWidgetItem(2)
                item2.setText(str(self.new_symbols_Text[itemRow]))
                item3 = QTableWidgetItem(3)
                item3.setText(str(self.big_P_x[itemRow]))
                #self.setTab4.append(,self.readyText[itemRow], self.newWordsText[itemRow], self.big_P_x[itemRow])
                self.tableWidget_3.setItem(itemRow,0,item0)
                self.tableWidget_3.setItem(itemRow,1,item1)
                self.tableWidget_3.setItem(itemRow,2,item2)
                self.tableWidget_3.setItem(itemRow,3,item3)
                self.file4_info.append(str(str(itemRow) + '\t' + str(self.prepearedText[itemRow])+ '\t' + str(self.new_symbols_Text[itemRow])+'\t' + str( self.big_P_x[itemRow]))+'\n')
            self.progressBar.setValue(self.progressBar.value()+3)
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
