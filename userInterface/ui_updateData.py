# Form implementation generated from reading ui file 'e:\Semester 5\Artificial Intelligence\Bulldozer_Price_Prediction_with_PyQt6_Interface\userInterface\updateData.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(280, 100, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background: transparent;\n"
"font-weight:bold;\n"
"color:black;\n"
"font-size: 37px;")
        self.label.setObjectName("label")
        self.updateButton = QtWidgets.QPushButton(parent=Dialog)
        self.updateButton.setGeometry(QtCore.QRect(350, 410, 93, 28))
        self.updateButton.setObjectName("updateButton")
        self.error = QtWidgets.QLabel(parent=Dialog)
        self.error.setGeometry(QtCore.QRect(350, 370, 101, 16))
        self.error.setText("")
        self.error.setObjectName("error")
        self.condition = QtWidgets.QSpinBox(parent=Dialog)
        self.condition.setGeometry(QtCore.QRect(330, 180, 141, 31))
        self.condition.setMinimum(500)
        self.condition.setMaximum(30000)
        self.condition.setObjectName("condition")
        self.modelID = QtWidgets.QSpinBox(parent=Dialog)
        self.modelID.setGeometry(QtCore.QRect(330, 230, 141, 31))
        self.modelID.setMinimum(500)
        self.modelID.setMaximum(30000)
        self.modelID.setObjectName("modelID")
        self.yearMade = QtWidgets.QSpinBox(parent=Dialog)
        self.yearMade.setGeometry(QtCore.QRect(330, 290, 141, 31))
        self.yearMade.setMinimum(1990)
        self.yearMade.setMaximum(2021)
        self.yearMade.setObjectName("yearMade")
        self.meterReading = QtWidgets.QSpinBox(parent=Dialog)
        self.meterReading.setGeometry(QtCore.QRect(330, 350, 141, 31))
        self.meterReading.setMinimum(0)
        self.meterReading.setMaximum(9999999)
        self.meterReading.setSingleStep(100)
        self.meterReading.setProperty("value", 0)
        self.meterReading.setObjectName("meterReading")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(350, 160, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(350, 260, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(350, 210, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(310, 320, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 801, 601))
        self.widget.setStyleSheet("background-image: url(./static_data/images/bulldozerBack.jfif);")
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.label.raise_()
        self.updateButton.raise_()
        self.error.raise_()
        self.condition.raise_()
        self.modelID.raise_()
        self.yearMade.raise_()
        self.meterReading.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Update Data"))
        self.updateButton.setText(_translate("Dialog", "Update"))
        self.label_2.setText(_translate("Dialog", "Enter P.ModelID"))
        self.label_3.setText(_translate("Dialog", "Enter Year Made"))
        self.label_4.setText(_translate("Dialog", "Enter ModelID"))
        self.label_5.setText(_translate("Dialog", "Enter Expected Meter Reading"))
