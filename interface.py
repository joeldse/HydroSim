#from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

def data():
    dc = interfaceGran.lineEdit_PDc.text()
    Du = interfaceGran.lineEdit_PDu.text()
    rho = interfaceGran.lineEdit_Prho.text()
    rhos = interfaceGran.lineEdit_Prhos.text()
    mu = interfaceGran.lineEdit_Pmu.text()
    dp = interfaceGran.lineEdit_PdP.text()
    qt = interfaceGran.lineEdit_PQt.text()
    cv = interfaceGran.lineEdit_Pcv.text()
    if interfaceGran.radioButton_RRB.isChecked():
        granulometry = "RRB"
    elif interfaceGran.radioButton_GGS.isChecked():
        granulometry = "GGS"
    elif interfaceGran.radioButton_Sigm.isChecked():
        granulometry = "sigmoide"
    elif interfaceGran.radioButton_best.isChecked():
        granulometry = "best"
    else:
        granulometry = "best"
    if interfaceGran.radioButton_Rietema.isChecked():
        family = "Rietema"
    elif interfaceGran.radioButton_Bradley.isChecked():
        family = "Bradley"
    elif interfaceGran.radioButton_Demco.isChecked():
        family = "Demco4H"
    else:
        family = "Rietema"
    if interfaceGran.radioButton_2D.isChecked():
        graphics = "2D"
    elif interfaceGran.radioButton_3D.isChecked():
        graphics = "3D"
    else:
        graphics = "2D"
    print(dc, Du, rho, rhos, mu, dp, qt, cv, granulometry, family, graphics)
    return

def reset():
    print("clear")


app = QtWidgets.QApplication([])
QtGui.QIcon(":/Interface/image/Hydrocyclone-fonctionnement.png")
interfaceGran = uic.loadUi("Interface/parameterization.ui")
interfaceGran.ButtonReset.clicked.connect(reset)
interfaceGran.ButtonRun.clicked.connect(data)

interfaceGran.show()
app.exec()
