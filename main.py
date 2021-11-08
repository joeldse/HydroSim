from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *
import numpy as np
import pandas as pd
import csv
import os, sys

from Interface.InterfaceSim import Ui_IntSim
from Interface.InterfaceRes import Ui_IntRes
from hydrocyclones import *
from parameters import *
from parameterization import *



class IntSim(QMainWindow):
    def __init__(self, parent=None):
        super(IntSim, self).__init__(parent=parent)
        self.ui = Ui_IntSim()
        self.ui.setupUi(self)
        self.ui.ButtonReset.clicked.connect(self.reset)
        self.ui.ButtonRun.clicked.connect(self.run)
        self.setWindowIcon(QIcon("Interface/icon/logo.png"))
        

    def GranParameter(self):
        if self.ui.radioButtonRRB.isChecked():
            granulometry = "RRB"
        elif self.ui.radioButtonGGS.isChecked():
            granulometry = "GGS"
        elif self.ui.radioButtonSig.isChecked():
            granulometry = "sigmoide"
        elif self.ui.radioButtonBest.isChecked():
            granulometry = "best"
        else:
            granulometry = "RRB"
        return granulometry

    def FamilyParameter(self):
        family = "Rietema"
        if self.ui.radioButtonRiet.isChecked():
            family = "Rietema"
        elif self.ui.radioButtonBrad.isChecked():
            family = "Bradley"
        elif self.ui.radioButtonDemc.isChecked():
            family = "Demco4H"
        else:
            family = "Rietema"
            #QMessageBox.information(QMessageBox(), "Warning", "The family has been established by default")
        return family
    
    def BasicParameter(self):
        dc = self.ui.lineEditDc.text()
        cv = self.ui.lineEditCv.text()
        dp = self.ui.lineEditdP.text()
        Du = self.ui.lineEditDu.text()
        mu = self.ui.lineEditMu.text()
        qt = self.ui.lineEditQ.text()
        rho = self.ui.lineEditRho.text()
        rhos = self.ui.lineEditRhos.text()
        dc, cv, dp, Du = 0.06, 0.01, 344750, 0.008
        mu, qt, rho, rhos = 0.001, 50/3600, 1000, 2700
        dc = float(dc)
        cv = float(cv)
        dp = float(dp)
        Du = float(Du)
        mu = float(mu)
        qt = float(qt)
        rho = float(rho)
        rhos = float(rhos)
        return dc, cv, dp, Du, mu, qt, rho, rhos

    def OptimizationParameter(self):
        if self.ui.radioButtonOptim.isChecked():
            optimization = "Y"
            variance = self.ui.lineEditVariance.text()
            variance = float(variance)
        else:
            optimization = "N"
            variance = 0
        return optimization, variance

    def GranulometricDataParameter(self):
        rowcount = self.ui.tableWidget.rowCount()
        columncount = 2
        for row in range(rowcount):
            for column in range(columncount):
                widgetitem = self.ui.tableWidget.item(row,column)
        return widgetitem
    
    def values(self):
        #Obtaining User Parameters
        granulometry = self.GranParameter()
        family = self.FamilyParameter()
        dc, cv, dp, Du, mu, qt, rho, rhos = self.BasicParameter()
        optimization, variance = self.OptimizationParameter()
        GranulometricData = self.GranulometricDataParameter()
        
        # Calculation of variables
        n, k, r2 = DistrGranul(x_exp, y_exp, granulometry)
        result = calc(cv, dc, dp, Du, granulometry, family, k, mu, n, phydro, qt, rho, rhos)
        
        #Saving as CSV
        f = open('results.csv', 'w', newline='', encoding='utf-8')  # 1. cria o arquivo
        w = csv.writer(f)                                           # 2. cria o objeto de gravação
        w.writerow(["name", "value"])
        w.writerow(["granulometry method", granulometry])
        w.writerow(["family", family])
        w.writerow(["n", float(n)])
        w.writerow(["k", float(k)])
        w.writerow(["R2", r2])
        w.writerow(["Q", result[0]])
        w.writerow(["Re", result[1]])
        w.writerow(["d50", result[5]])
        w.writerow(["E't", result[6]])
        w.writerow(["Et", result[8]])
        w.writerow(["Cvu", result[9]])
        w.writerow(["n° hydrocyclon", result[15]])
        return 

    def run(self):
        self.values()

        self.w = IntRes() 
        self.w.show()
        #QMessageBox.information(QMessageBox(), "Titulo", "texto")
    
    def reset(self):
        self.ui.radioButtonGGS.setChecked(False)
        print("clear")
        au, al = 3, 5
        print(au)
        






class IntRes(QMainWindow):
    def __init__(self):
        super(IntRes, self).__init__()
        self.ui = Ui_IntRes()
        self.ui.setupUi(self)
        self.results()
        self.setWindowIcon(QIcon("Interface/icon/logo.png"))
    
    

    def results(self):
        for i in range(10):
            self.ui.tableWidget.setItem(0,i,QtWidgets.QTableWidgetItem(f"{float(y_res[i+2]):.2f}".center(25," ")))




if (QtWidgets.QDialog.Accepted == True):
    app = QtWidgets.QApplication(sys.argv)
    w = IntSim()
    w.show()
sys.exit(app.exec_())


