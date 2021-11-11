from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *
import numpy as np
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
        #dc, cv, Du, dp = 6, 0.01, 0.8, 3.4023
        #mu, qt, rho, rhos = 1, 50, 1000, 2800
        #dc, cv, Du, dp = 1, 0.0025, 0.15, 2
        #mu, qt, rho, rhos = 1, 50, 996.02, 997.27

        dc = float(dc)/100
        cv = float(cv)
        dp = float(dp)*101325
        Du = float(Du)/100
        mu = float(mu)/1000
        qt = float(qt)
        rho = float(rho)
        rhos = float(rhos)
        return dc, cv, dp, Du, mu, qt, rho, rhos

    def GranulometricDataParameter(self):
        list = []
        tam = 0
        for i in range(50):
            if self.ui.tableWidget.item(i, 0) != None:
                tam += 1
        for i in range(tam):  #linha
            for j in range(2):
                item = self.ui.tableWidget.item(i, j)
                value = float(item.text())
                list.append(value)
        
        #Saving as CSV
        f = open('Granulometric_Data.csv', 'w', newline='', encoding='utf-8')  # 1. cria o arquivo
        w = csv.writer(f)                                           # 2. cria o objeto de gravação
        w.writerow(["d", "y"])
        for i in range(tam):
            w.writerow([list[2*i], list[2*i+1]])
        return list
    
    def values(self):
        #Obtaining User Parameters
        self.GranulometricDataParameter()
        granulometry = self.GranParameter()

        family = self.FamilyParameter()
        dc, cv, dp, Du, mu, qt, rho, rhos = self.BasicParameter()
        
        #Saving as CSV
        f = open('results.csv', 'w', newline='', encoding='utf-8')  # 1. cria o arquivo
        w = csv.writer(f)                                           # 2. cria o objeto de gravação
        w.writerow(["granulometry", "family", "Dc", "Du", "Q\u209C", "\u03BC", 
        "\u0394P", "\u03C1", "\u03C1\u209B", "cv", "n", "k", "R²", "Q", "Re",
        "d50", "E'T", "Et", "cvu", "Hydrocyclones in parallel", "Total equipment cost","Bare Module Cost"])

        # Calculation of variables
        n, k, r2 = DistrGranul(granulometry)
        # for Sensitivity Analysis
        if self.ui.radioButtonSensAna.isChecked():
            result = parameterization(cv, dc, dp, Du, granulometry, family, k, mu, n, phydro, qt, rho, rhos, 4)
            # Save results
            for i in range(len(result)):
                w.writerow([granulometry, family, result["dc"][i], result["Du"][i], qt, mu, 
                result["dp"][i], rho, rhos, cv, float(n), float(k), r2, 3600*(result["Q"][i]), 
                result["Re"][i], result["d50"][i], result["Et_red"][i], result["Et"][i], 
                result["cvu"][i], result["n_hydro"][i], result["cp"][i], result["cbm"][i]])
        # for Optimization
        elif self.ui.radioButtonOptim.isChecked():
            result = calc(cv, dc, dp, Du, granulometry, family, k, mu, n, phydro, qt, rho, rhos)
            w.writerow([granulometry, family, dc, Du, qt, mu, dp, rho, rhos, cv,
            float(n), float(k), r2, 3600*result[0], result[1], result[5], result[6], 
            result[8], result[9], result[15], result[16], result[17]])
        # for a simple calculation
        else:
            result = calc(cv, dc, dp, Du, granulometry, family, k, mu, n, phydro, qt, rho, rhos)
            w.writerow([granulometry, family, dc, Du, qt, mu, dp, rho, rhos, cv,
            float(n), float(k), r2, 3600*result[0], result[1], result[5], result[6], 
            result[8], result[9], result[15], result[16], result[17]])
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
        data = pd.read_csv('results.csv', sep=',')
        self.ui.tableWidget.setRowCount(len(np.array(data.iloc[:,0])))
        for i in range(12):
            for j in range(len(np.array(data.iloc[:,0]))):
                self.ui.tableWidget.setItem(j,i,QtWidgets.QTableWidgetItem(f"{float(data.iloc[j,i+10]):.2f}".center(25," ")))




if (QtWidgets.QDialog.Accepted == True):
    app = QtWidgets.QApplication(sys.argv)
    w = IntSim()
    w.show()
sys.exit(app.exec_())


