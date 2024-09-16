#!/usr/bin/python
# -*- coding: cp1251 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
import sys


class Ui_GeneratPorol(object):
    generat_porol = ""
    poroli = ""
    
    
    def setupUi(self, GeneratPorol):
        GeneratPorol.setObjectName("GeneratPorol")
        GeneratPorol.resize(481, 471)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        GeneratPorol.setFont(font)
        GeneratPorol.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(GeneratPorol)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -1, 531, 33))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(157, 60, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(192, 108, 113, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 40, 45, 13))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(126, 340, 281, 91))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(209, 300, 111, 24))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 150, 141, 17))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 180, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 210, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 240, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(20, 291, 49, 26))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 270, 130, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        GeneratPorol.setCentralWidget(self.centralwidget)

        self.retranslateUi(GeneratPorol)
        QtCore.QMetaObject.connectSlotsByName(GeneratPorol)
        
        self.correct_button()

    def retranslateUi(self, GeneratPorol):
        _translate = QtCore.QCoreApplication.translate
        GeneratPorol.setWindowTitle(_translate("GeneratPorol", "GeneratPorol"))
        self.label.setText(_translate("GeneratPorol", "Разработчик: Veby, TG: @vebytop"))
        self.pushButton.setText(_translate("GeneratPorol", "Генерировать"))
        self.label_2.setText(_translate("GeneratPorol", "Длина"))
        self.label_3.setText(_translate("GeneratPorol", "Результат"))
        self.checkBox.setText(_translate("GeneratPorol", "Сохронить в файл"))
        self.checkBox_2.setText(_translate("GeneratPorol", "(A-Z)"))
        self.checkBox_3.setText(_translate("GeneratPorol", "(1-9)"))
        self.checkBox_4.setText(_translate("GeneratPorol", "(@!#$%&*)"))
        self.label_4.setText(_translate("GeneratPorol", "Количество поролей"))

    
    def correct_button(self) -> None:
        self.pushButton.clicked.connect(self.main)
    
    
    def save_file(self, porol: str) -> None:
        with open("Resyltat.txt", "w") as file:
            file.write(porol)
                
    
    def generat_vse_clychui(self, dlina: int, colvo: int) -> str:
        slovar_ang_chisla_cpes_simvol = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*"
        
        for i in range(1, int(colvo)+1):
            for g in range(1, int(dlina)+1):
                indx = randint(0, len(slovar_ang_chisla_cpes_simvol)-1)
                self.generat_porol += slovar_ang_chisla_cpes_simvol[indx]
            
            yield self.generat_porol
            self.generat_porol = ""    
    
    def generat_porol_spes_ang(self, dlina: int, colvo: int) -> str:
        slovar_ang_spec_simvoli =  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%&*"
        
        for i in range(1, int(colvo)+1):
            for g in range(1, int(dlina)+1):
                indx = randint(0, len(slovar_ang_spec_simvoli)-1)
                self.generat_porol += slovar_ang_spec_simvoli[indx]
            
            yield self.generat_porol
            self.generat_porol = ""  
    
    def generat_porol_ang(self, dlina: int, colvo: int) -> str:
        slovar_ang =  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        
        for i in range(1, int(colvo)+1):
            for g in range(1, int(dlina)+1):
                indx = randint(0, len(slovar_ang)-1)
                self.generat_porol += slovar_ang[indx]
            
            yield self.generat_porol
            self.generat_porol = ""  
    
    def generat_porol_ang_chisla(self, dlina: int, colvo: int) -> str:
        slovar_ang =  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        
        for i in range(1, int(colvo)+1):
            for g in range(1, int(dlina)+1):
                indx = randint(0, len(slovar_ang)-1)
                self.generat_porol += slovar_ang[indx]
            
            yield self.generat_porol
            self.generat_porol = ""  
    
    def generat_porol_chisla(self, dlina: int, colvo: int) -> str:
        slovar_ang =  "0123456789"
        
        for i in range(1, int(colvo)+1):
            for g in range(1, int(dlina)+1):
                indx = randint(0, len(slovar_ang)-1)
                self.generat_porol += slovar_ang[indx]
            
            yield self.generat_porol
            self.generat_porol = "" 
        
    def generat_porol_cpec(self, dlina: int, colvo: int) -> str:
        slovar_ang =  "!@#$%&*"
        
        for i in range(1, int(colvo)+1):
            for g in range(1, int(dlina)+1):
                indx = randint(0, len(slovar_ang)-1)
                self.generat_porol += slovar_ang[indx]
            
            yield self.generat_porol
            self.generat_porol = "" 
    
    def generat_porol_cpec_chisla(self, dlina: int, colvo: int) -> str:
        slovar_ang =  "0123456789!@#$%&*"
        
        for i in range(1, int(colvo)+1):
            for g in range(1, int(dlina)+1):
                indx = randint(0, len(slovar_ang)-1)
                self.generat_porol += slovar_ang[indx]
            
            yield self.generat_porol
            self.generat_porol = "" 
    
    
    
    def main(self):
        dlina_porola = self.textEdit.toPlainText()
        colvo = self.spinBox.value()
        
        if self.checkBox_2.isChecked() == True:
            if self.checkBox_3.isChecked() == True:
                if self.checkBox_4.isChecked() == True:
                    for i in self.generat_vse_clychui(dlina=dlina_porola, colvo=colvo):
                        self.poroli += i + "\n"
                    
                    self.textEdit_2.setText(self.poroli)
                    self.poroli = ""
                else:
                    if self.checkBox_4.isChecked() == False:
                        for i in self.generat_porol_ang_chisla(dlina=dlina_porola, colvo=colvo):
                            self.poroli += i + "\n"
                    
                        self.textEdit_2.setText(self.poroli)
                        self.poroli = ""
                
            else:
                if self.checkBox_3.isChecked() == False:
                    if self.checkBox_4.isChecked() == True:
                        for i in self.generat_porol_spes_ang(dlina=dlina_porola, colvo=colvo):
                            self.poroli += i + "\n"
                    
                        self.textEdit_2.setText(self.poroli)
                        self.poroli = ""
                
                    else:
                        for i in self.generat_porol_ang(dlina=dlina_porola, colvo=colvo):
                            self.poroli += i + "\n"
                    
                        self.textEdit_2.setText(self.poroli)
                        self.poroli = ""
        else:
            if self.checkBox_3.isChecked() == True:
                if self.checkBox_4.isChecked() == False:
                    for i in self.generat_porol_chisla(dlina=dlina_porola, colvo=colvo):
                        self.poroli += i + "\n"
                    
                    self.textEdit_2.setText(self.poroli)
                    self.poroli = ""
                
                else:
                    for i in self.generat_porol_cpec_chisla(dlina=dlina_porola, colvo=colvo):
                        self.poroli += i + "\n"
                    
                    self.textEdit_2.setText(self.poroli)
                    self.poroli = ""
                    

            
            else:
                if self.checkBox_4.isChecked() == True:
                    for i in self.generat_porol_cpec(dlina=dlina_porola, colvo=colvo):
                        self.poroli += i + "\n"
                    
                    self.textEdit_2.setText(self.poroli)
                    self.poroli = ""
                    
        
        if self.checkBox.isChecked() == True:
            self.save_file(self.textEdit_2.toPlainText())
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_GeneratPorol()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())     