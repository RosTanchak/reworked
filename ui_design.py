# -*- coding: utf-8 -*-



# Form implementation generated from reading ui file 'pratyka.ui'

#

# Created by: PyQt4 UI code generator 4.11.4

#

# WARNING! All changes made in this file will be lost!



from PyQt4 import QtCore, QtGui



try:

    _fromUtf8 = QtCore.QString.fromUtf8

except AttributeError:

    def _fromUtf8(s):

        return s



try:

    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):

        return QtGui.QApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):

        return QtGui.QApplication.translate(context, text, disambig)



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName(_fromUtf8("MainWindow"))

        MainWindow.resize(800, 600)

        self.centralwidget = QtGui.QWidget(MainWindow)

        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.tabWidget = QtGui.QTabWidget(self.centralwidget)

        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 571))

        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))

        self.tab_2 = QtGui.QWidget()

        self.tab_2.setObjectName(_fromUtf8("tab_2"))

        self.frame = QtGui.QFrame(self.tab_2)

        self.frame.setGeometry(QtCore.QRect(30, 20, 561, 161))

        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)

        self.frame.setFrameShadow(QtGui.QFrame.Raised)

        self.frame.setObjectName(_fromUtf8("frame"))

        self.pushButton_5 = QtGui.QPushButton(self.frame)

        self.pushButton_5.setGeometry(QtCore.QRect(40, 40, 121, 41))

        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        self.pushButton_6 = QtGui.QPushButton(self.frame)

        self.pushButton_6.setGeometry(QtCore.QRect(40, 100, 121, 41))

        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

        self.label_2 = QtGui.QLabel(self.frame)

        self.label_2.setGeometry(QtCore.QRect(220, 30, 101, 31))

        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_3 = QtGui.QLabel(self.frame)

        self.label_3.setGeometry(QtCore.QRect(290, 70, 151, 51))

        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.frame_2 = QtGui.QFrame(self.tab_2)

        self.frame_2.setGeometry(QtCore.QRect(470, 310, 281, 221))

        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)

        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)

        self.frame_2.setObjectName(_fromUtf8("frame_2"))

        self.spinBox_2 = QtGui.QSpinBox(self.frame_2)

        self.spinBox_2.setGeometry(QtCore.QRect(110, 60, 151, 33))

        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))

        self.spinBox_4 = QtGui.QSpinBox(self.frame_2)

        self.spinBox_4.setGeometry(QtCore.QRect(110, 160, 151, 33))

        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))

        self.spinBox_3 = QtGui.QSpinBox(self.frame_2)

        self.spinBox_3.setGeometry(QtCore.QRect(110, 110, 151, 33))

        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))

        self.label_5 = QtGui.QLabel(self.frame_2)

        self.label_5.setGeometry(QtCore.QRect(0, 20, 271, 31))

        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.label_6 = QtGui.QLabel(self.frame_2)

        self.label_6.setGeometry(QtCore.QRect(70, 60, 41, 41))

        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.label_7 = QtGui.QLabel(self.frame_2)

        self.label_7.setGeometry(QtCore.QRect(60, 120, 56, 17))

        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.label_8 = QtGui.QLabel(self.frame_2)

        self.label_8.setGeometry(QtCore.QRect(0, 160, 121, 31))

        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.frame_3 = QtGui.QFrame(self.tab_2)

        self.frame_3.setGeometry(QtCore.QRect(30, 330, 321, 161))

        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)

        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)

        self.frame_3.setObjectName(_fromUtf8("frame_3"))

        self.label_4 = QtGui.QLabel(self.frame_3)

        self.label_4.setGeometry(QtCore.QRect(10, 20, 91, 31))

        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.spinBox = QtGui.QSpinBox(self.frame_3)

        self.spinBox.setGeometry(QtCore.QRect(100, 20, 161, 33))

        self.spinBox.setObjectName(_fromUtf8("spinBox"))

        self.spinBox.setMinimum(1)

        self.spinBox.setMaximum(10)

        self.radioButton_7 = QtGui.QRadioButton(self.frame_3)

        self.radioButton_7.setGeometry(QtCore.QRect(50, 110, 113, 29))

        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))

        self.radioButton_6 = QtGui.QRadioButton(self.frame_3)

        self.radioButton_6.setGeometry(QtCore.QRect(50, 70, 113, 29))

        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))

        self.radioButton_6.setChecked(True)

        self.pushButton_7 = QtGui.QPushButton(self.frame_3)

        self.pushButton_7.setGeometry(QtCore.QRect(220, 70, 91, 71))

        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))

        self.progressBar = QtGui.QProgressBar(self.tab_2)

        self.progressBar.setGeometry(QtCore.QRect(30, 200, 621, 91))

        self.progressBar.setProperty("value", 0)

        self.progressBar.setObjectName(_fromUtf8("progressBar"))

        self.label_9 = QtGui.QLabel(self.tab_2)

        self.label_9.setGeometry(QtCore.QRect(120, 0, 261, 17))

        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.label_10 = QtGui.QLabel(self.tab_2)

        self.label_10.setGeometry(QtCore.QRect(80, 310, 161, 17))

        self.label_10.setObjectName(_fromUtf8("label_10"))

        self.pushButton_8 = QtGui.QPushButton(self.tab_2)

        self.pushButton_8.setGeometry(QtCore.QRect(670, 200, 90, 91))

        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))

        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.tab = QtGui.QWidget()

        self.tab.setObjectName(_fromUtf8("tab"))

        self.tabWidget_2 = QtGui.QTabWidget(self.tab)

        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 791, 521))

        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))

        self.tab_3 = QtGui.QWidget()

        self.tab_3.setObjectName(_fromUtf8("tab_3"))

        self.pushButton = QtGui.QPushButton(self.tab_3)

        self.pushButton.setGeometry(QtCore.QRect(560, 200, 151, 71))

        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.tableWidget = QtGui.QTableWidget(self.tab_3)

        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 411, 491))

        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))

        self.tableWidget.setColumnCount(4)

        self.tableWidget.setRowCount(0)

        self.tableWidget.verticalHeader().setVisible(False)

        item = QtGui.QTableWidgetItem()

        self.tableWidget.setHorizontalHeaderItem(0, item)

        item = QtGui.QTableWidgetItem()

        self.tableWidget.setHorizontalHeaderItem(1, item)

        item = QtGui.QTableWidgetItem()

        self.tableWidget.setHorizontalHeaderItem(2, item)

        item = QtGui.QTableWidgetItem()

        self.tableWidget.setHorizontalHeaderItem(3, item)

        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))

        self.tab_4 = QtGui.QWidget()

        self.tab_4.setObjectName(_fromUtf8("tab_4"))

        self.tableWidget_2 = QtGui.QTableWidget(self.tab_4)

        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 501, 491))

        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))

        self.tableWidget_2.setColumnCount(4)

        self.tableWidget_2.setRowCount(0)

        self.tableWidget_2.verticalHeader().setVisible(False)

        item = QtGui.QTableWidgetItem()

        self.tableWidget_2.setHorizontalHeaderItem(0, item)

        item = QtGui.QTableWidgetItem()

        self.tableWidget_2.setHorizontalHeaderItem(1, item)

        item = QtGui.QTableWidgetItem()

        self.tableWidget_2.setHorizontalHeaderItem(2, item)

        item = QtGui.QTableWidgetItem()

        self.tableWidget_2.setHorizontalHeaderItem(3, item)

        self.pushButton_2 = QtGui.QPushButton(self.tab_4)

        self.pushButton_2.setGeometry(QtCore.QRect(590, 200, 121, 71))

        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.radioButton = QtGui.QRadioButton(self.tab_4)

        self.radioButton.setEnabled(True)

        self.radioButton.setGeometry(QtCore.QRect(560, 150, 71, 22))

        self.radioButton.setChecked(True)

        self.radioButton.setObjectName(_fromUtf8("radioButton"))

        self.radioButton_2 = QtGui.QRadioButton(self.tab_4)

        self.radioButton_2.setGeometry(QtCore.QRect(670, 150, 91, 22))

        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))

        self.tabWidget_2.addTab(self.tab_4, _fromUtf8(""))

        self.tab_5 = QtGui.QWidget()

        self.tab_5.setObjectName(_fromUtf8("tab_5"))

        self.label = QtGui.QLabel(self.tab_5)

        self.label.setGeometry(QtCore.QRect(20, 20, 131, 17))

        self.label.setObjectName(_fromUtf8("label"))

        self.lineEdit = QtGui.QLineEdit(self.tab_2)

        self.lineEdit.setGeometry(QtCore.QRect(160, 300, 161, 27))

        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.tableWidget_4 = QtGui.QTableWidget(self.tab_5)

        self.tableWidget_4.setGeometry(QtCore.QRect(0, 90, 791, 401))

        self.tableWidget_4.setObjectName(_fromUtf8("tableWidget_4"))

        self.tableWidget_4.setColumnCount(4)

        self.tableWidget_4.setRowCount(0)

        self.tableWidget_4.verticalHeader().setVisible(False)

        item = QtGui.QTableWidgetItem()

        self.tableWidget_4.setHorizontalHeaderItem(0, item)

        item = QtGui.QTableWidgetItem()

        self.tableWidget_4.setHorizontalHeaderItem(1, item)

        item = QtGui.QTableWidgetItem()

        self.tableWidget_4.setHorizontalHeaderItem(2, item)

        item = QtGui.QTableWidgetItem()

        self.tableWidget_4.setHorizontalHeaderItem(3, item)

        self.pushButton_4 = QtGui.QPushButton(self.tab_5)

        self.pushButton_4.setGeometry(QtCore.QRect(648, 16, 111, 61))

        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.radioButton_3 = QtGui.QRadioButton(self.tab_5)

        self.radioButton_3.setGeometry(QtCore.QRect(480, 0, 117, 22))

        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))

        self.radioButton_4 = QtGui.QRadioButton(self.tab_5)

        self.radioButton_4.setGeometry(QtCore.QRect(480, 30, 117, 22))

        self.radioButton_4.setChecked(True)

        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))

        self.tabWidget_2.addTab(self.tab_5, _fromUtf8(""))

        self.tab_6 = QtGui.QWidget()

        self.tab_6.setObjectName(_fromUtf8("tab_6"))

        self.tableWidget_3 = QtGui.QTableWidget(self.tab_6)

        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 431, 491))

        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))

        self.tableWidget_3.setColumnCount(4)

        self.tableWidget_3.setRowCount(0)

        self.tableWidget_3.verticalHeader().setVisible(False)

        item = QtGui.QTableWidgetItem()

        self.tableWidget_3.setHorizontalHeaderItem(0, item)

        item = QtGui.QTableWidgetItem()

        self.tableWidget_3.setHorizontalHeaderItem(1, item)

        item = QtGui.QTableWidgetItem()

        self.tableWidget_3.setHorizontalHeaderItem(2, item)

        item = QtGui.QTableWidgetItem()

        self.tableWidget_3.setHorizontalHeaderItem(3, item)

        self.pushButton_3 = QtGui.QPushButton(self.tab_6)

        self.pushButton_3.setGeometry(QtCore.QRect(610, 200, 111, 71))

        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.tabWidget_2.addTab(self.tab_6, _fromUtf8(""))

        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtGui.QStatusBar(MainWindow)

        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen = QtGui.QAction(MainWindow)

        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))

        self.actionChange = QtGui.QAction(MainWindow)

        self.actionChange.setObjectName(_fromUtf8("actionChange"))



        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        self.tabWidget_2.setCurrentIndex(3)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

        self.pushButton_5.setText(_translate("MainWindow", "Open File", None))

        self.pushButton_6.setText(_translate("MainWindow", "Save As", None))

        self.label_2.setText(_translate("MainWindow", "Selected File :", None))

        self.label_3.setText(_translate("MainWindow", " \"File name\"", None))

        self.label_5.setText(_translate("MainWindow", "You can choose an area  () to discover, below:", None))

        self.label_6.setText(_translate("MainWindow", "Lo:", None))

        self.label_7.setText(_translate("MainWindow", "deltaL:", None))

        self.label_8.setText(_translate("MainWindow", "Window step k:", None))

        self.label_4.setText(_translate("MainWindow", "Choose n:", None))

        self.radioButton_7.setText(_translate("MainWindow", "Slice", None))

        self.radioButton_6.setText(_translate("MainWindow", "Whole", None))

        self.pushButton_7.setText(_translate("MainWindow", "Calculate", None))

        self.label_9.setText(_translate("MainWindow", "                         FILE  OPERATIONS", None))

        self.label_10.setText(_translate("MainWindow", "Ti bins:", None))

        self.pushButton_8.setText(_translate("MainWindow", "Stop", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Preparation", None))

        self.pushButton.setText(_translate("MainWindow", "Build", None))

        item = self.tableWidget.horizontalHeaderItem(0)

        item.setText(_translate("MainWindow", "Rang", None))

        item = self.tableWidget.horizontalHeaderItem(1)

        item.setText(_translate("MainWindow", "Symbols", None))

        item = self.tableWidget.horizontalHeaderItem(2)

        item.setText(_translate("MainWindow", "f", None))

        item = self.tableWidget.horizontalHeaderItem(3)

        item.setText(_translate("MainWindow", "F", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Analysis", None))

        item = self.tableWidget_2.horizontalHeaderItem(0)

        item.setText(_translate("MainWindow", "dt", None))

        item = self.tableWidget_2.horizontalHeaderItem(1)

        item.setText(_translate("MainWindow", "N", None))

        item = self.tableWidget_2.horizontalHeaderItem(2)

        item.setText(_translate("MainWindow", "p(x)", None))

        item = self.tableWidget_2.horizontalHeaderItem(3)

        item.setText(_translate("MainWindow", "P(x)", None))

        self.pushButton_2.setText(_translate("MainWindow", "Build", None))

        self.radioButton.setText(_translate("MainWindow", "p(x)", None))

        self.radioButton_2.setText(_translate("MainWindow", "P(x)", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "dTi", None))

        self.label.setText(_translate("MainWindow", "Count of interval:", None))

        self.lineEdit.setPlaceholderText(_translate("MainWindow", "", None))

        self.lineEdit.setText("8")

        item = self.tableWidget_4.horizontalHeaderItem(0)

        item.setText(_translate("MainWindow", "Ti bin", None))

        item = self.tableWidget_4.horizontalHeaderItem(1)

        item.setText(_translate("MainWindow", "p(i)", None))

        item = self.tableWidget_4.horizontalHeaderItem(2)

        item.setText(_translate("MainWindow", "p(i')", None))

        item = self.tableWidget_4.horizontalHeaderItem(3)

        item.setText(_translate("MainWindow", "P(x)", None))

        self.pushButton_4.setText(_translate("MainWindow", "Build", None))

        self.radioButton_3.setText(_translate("MainWindow", "p(x)", None))

        self.radioButton_4.setText(_translate("MainWindow", "P(x)", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Ti", None))

        item = self.tableWidget_3.horizontalHeaderItem(0)

        item.setText(_translate("MainWindow", "Position", None))

        item = self.tableWidget_3.horizontalHeaderItem(1)

        item.setText(_translate("MainWindow", "Value", None))

        item = self.tableWidget_3.horizontalHeaderItem(2)

        item.setText(_translate("MainWindow", "p\'(x)", None))

        item = self.tableWidget_3.horizontalHeaderItem(3)

        item.setText(_translate("MainWindow", "P\'(x)", None))

        self.pushButton_3.setText(_translate("MainWindow", "Build", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "New Symbols", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "New Symbols", None))

        self.actionOpen.setText(_translate("MainWindow", "Open", None))

        self.actionChange.setText(_translate("MainWindow", "Save as", None))

        self.spinBox_2.setEnabled(False)

        self.spinBox_3.setEnabled(False)

        self.spinBox_4.setEnabled(False)





if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)

    MainWindow = QtGui.QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())