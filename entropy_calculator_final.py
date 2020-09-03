# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\Makieta do prac mgr.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QSizePolicy, QAction, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon, QKeySequence
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from try_parse import try_parse_int
from try_parse import try_parse_float
import mpl_toolkits.mplot3d as p3
import pandas as pd
import numpy as np
import os.path

from ApEn_final import ApEn as ApEn
from SampEn_final import SampEn as SampEn


class Ui_MainWindow(object):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

        self.data_header = 0
        self.data_header_length = 0
        self.data_header_cells = list()
        self.data = []
        self.data_progenitor = []
        self.data_dictionary = {}
        self.data_header_dictionary = {}
        self.path = None
        self.chosen_data_header = ''
        self.x = []
        self.y = []
        self.z = []
        self.filterTypes = 'Text Document Csv (*.csv);; Python (*.py);; (*.txt)'
        self.comboBox_data_standardisation_text = ["normal", "standardise"]
        self.comboBox_data_standarization_first_fill_ticket = 0
        self.resultsPopup = QMessageBox()
        self.calculating_data_length = 5000

        self.ApEn_m_value = 2
        self.ApEn_r_value = 0.25
        self.ApEn_N_start_value = 0
        self.ApEn_N_stop_value = 0

        self.SampEn_m_value = 2
        self.SampEn_r_value = 0.25
        self.SampEn_N_start_value = 0
        self.SampEn_N_stop_value = 0



        # self.chosen_data_header_3d_x_axis = ''
        # self.chosen_data_header_3d_y_axis = ''
        # self.chosen_data_header_3d_z_axis = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Entropy_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.Entropy_tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Entropy_tabWidget.sizePolicy().hasHeightForWidth())
        self.Entropy_tabWidget.setSizePolicy(sizePolicy)
        self.Entropy_tabWidget.setObjectName("Entropy_tabWidget")

        self.ApEn_tab = QtWidgets.QWidget()
        self.ApEn_tab.setObjectName("ApEn_tab")
        self.verticalLayout_ApEn_inside_tap = QtWidgets.QVBoxLayout(self.ApEn_tab)
        self.verticalLayout_ApEn_inside_tap.setObjectName("verticalLayout_5")

        self.horizontalLayout_ApEn_precision = QtWidgets.QHBoxLayout()
        self.horizontalLayout_ApEn_precision.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_ApEn_precision.setObjectName("horizontalLayout_ApEn_precision")

        self.pushButton_ApEn_precision = QtWidgets.QLabel(self.ApEn_tab)
        self.pushButton_ApEn_precision.setObjectName("pushButton_ApEn_precision")
        #self.pushButton_ApEn_precision.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_ApEn_precision.addWidget(self.pushButton_ApEn_precision)

        self.checkBox_approx_ApEn_precision = QtWidgets.QCheckBox(self.ApEn_tab)
        self.checkBox_approx_ApEn_precision.setObjectName("checkBox_approx_ApEn_precision")
        self.checkBox_approx_ApEn_precision.setChecked(True)
        self.horizontalLayout_ApEn_precision.addWidget(self.checkBox_approx_ApEn_precision)

        self.checkBox_normal_ApEny_precision = QtWidgets.QCheckBox(self.ApEn_tab)
        self.checkBox_normal_ApEny_precision.setObjectName("checkBox_normal_ApEny_precision")
        self.horizontalLayout_ApEn_precision.addWidget(self.checkBox_normal_ApEny_precision)

        self.verticalLayout_ApEn_inside_tap.addLayout(self.horizontalLayout_ApEn_precision)

        self.horizontalLayout_ApEn_distance_measure = QtWidgets.QHBoxLayout()
        self.horizontalLayout_ApEn_distance_measure.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_ApEn_distance_measure.setObjectName("horizontalLayout_ApEn_distance_measure")

        self.pushButton_ApEn_measure = QtWidgets.QLabel(self.ApEn_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_ApEn_measure.sizePolicy().hasHeightForWidth())
        self.pushButton_ApEn_measure.setSizePolicy(sizePolicy)
        self.pushButton_ApEn_measure.setObjectName("pushButton_ApEn_measure")
        #self.pushButton_ApEn_measure.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_ApEn_distance_measure.addWidget(self.pushButton_ApEn_measure)

        self.radioButton_Euclidean = QtWidgets.QCheckBox(self.ApEn_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_Euclidean.sizePolicy().hasHeightForWidth())
        self.radioButton_Euclidean.setSizePolicy(sizePolicy)
        self.radioButton_Euclidean.setObjectName("radioButton_Euclidean")

        self.horizontalLayout_ApEn_distance_measure.addWidget(self.radioButton_Euclidean)

        self.radioButton_Chebyshev = QtWidgets.QCheckBox(self.ApEn_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_Chebyshev.sizePolicy().hasHeightForWidth())
        self.radioButton_Chebyshev.setSizePolicy(sizePolicy)
        self.radioButton_Chebyshev.setObjectName("radioButton_Chebyshev")
        self.radioButton_Chebyshev.setChecked(True)

        self.horizontalLayout_ApEn_distance_measure.addWidget(self.radioButton_Chebyshev)

        # self.radioButton_distance_measure_both = QtWidgets.QRadioButton(self.ApEn_tab)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(2)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.radioButton_distance_measure_both.sizePolicy().hasHeightForWidth())
        #
        # self.radioButton_distance_measure_both.setSizePolicy(sizePolicy)
        # self.radioButton_distance_measure_both.setObjectName("radioButton_distance_measure_both")
        # self.horizontalLayout_ApEn_distance_measure.addWidget(self.radioButton_distance_measure_both)

        self.verticalLayout_ApEn_inside_tap.addLayout(self.horizontalLayout_ApEn_distance_measure)

        self.horizontalLayout_ApEn_calculation_parameters_description = QtWidgets.QHBoxLayout()
        self.horizontalLayout_ApEn_calculation_parameters_description.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_ApEn_calculation_parameters_description.setObjectName("horizontalLayout_ApEn_calculation_parameters_description")

        self.pushButton_ApEn_calculation_standard_parameters = QtWidgets.QCheckBox(self.ApEn_tab)
        self.pushButton_ApEn_calculation_standard_parameters.setObjectName("pushButton_ApEn_calculation_parameters")
        self.pushButton_ApEn_calculation_standard_parameters.setChecked(True)

        self.horizontalLayout_ApEn_calculation_parameters_description.addWidget(self.pushButton_ApEn_calculation_standard_parameters)

        # poniżej wihajstry do wpisywania parametrów ApEn
        self.button_ApEn_m_description = QtWidgets.QLabel(self.ApEn_tab)
        self.button_ApEn_m_description.setObjectName("button_m_description")
        self.button_ApEn_m_description.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_ApEn_calculation_parameters_description.addWidget(self.button_ApEn_m_description)

        self.button_ApEn_r_description = QtWidgets.QLabel(self.ApEn_tab)
        self.button_ApEn_r_description.setObjectName("button_r_description")
        self.button_ApEn_r_description.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_ApEn_calculation_parameters_description.addWidget(self.button_ApEn_r_description)

        self.button_ApEn_N_start_description = QtWidgets.QLabel(self.ApEn_tab)
        self.button_ApEn_N_start_description.setObjectName("button_N_start_description")
        self.button_ApEn_N_start_description.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_ApEn_calculation_parameters_description.addWidget(self.button_ApEn_N_start_description)

        self.button_ApEn_N_stop_description = QtWidgets.QLabel(self.ApEn_tab)
        self.button_ApEn_N_stop_description.setObjectName("button_N_stop_description")
        self.button_ApEn_N_stop_description.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_ApEn_calculation_parameters_description.addWidget(self.button_ApEn_N_stop_description)

        self.verticalLayout_ApEn_inside_tap.addLayout(self.horizontalLayout_ApEn_calculation_parameters_description)

        self.horizontalLayout_ApEn_calculation_parameters = QtWidgets.QHBoxLayout()
        self.horizontalLayout_ApEn_calculation_parameters.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_ApEn_calculation_parameters.setObjectName("horizontalLayout_ApEn_calculation_parameters")

        #self.pushButton_ApEn_calculation_parameters = QtWidgets.QLineEdit(self.ApEn_tab)
        self.pushButton_ApEn_calculation_parameters = QtWidgets.QLabel(self.ApEn_tab)
        #self.pushButton_ApEn_calculation_parameters.setReadOnly(True)
        self.pushButton_ApEn_calculation_parameters.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton_ApEn_calculation_parameters.setObjectName("pushButton_ApEn_calculation_parameters")
        # żeby miejsca do wpisywania i opis się równo rozchodziły
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_ApEn_calculation_parameters.sizePolicy().hasHeightForWidth())
        self.pushButton_ApEn_calculation_parameters.setSizePolicy(sizePolicy)
        self.horizontalLayout_ApEn_calculation_parameters.addWidget(self.pushButton_ApEn_calculation_parameters)

        # poniżej wihajstry do wpisywania parametrów ApEn
        self.checkBox_ApEn_m = QtWidgets.QLineEdit(self.ApEn_tab)
        self.checkBox_ApEn_m.setObjectName("checkBox_m")
        # żeby miejsca do wpisywania i opis się równo rozchodziły
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ApEn_m.sizePolicy().hasHeightForWidth())
        self.checkBox_ApEn_m.setSizePolicy(sizePolicy)
        self.horizontalLayout_ApEn_calculation_parameters.addWidget(self.checkBox_ApEn_m)

        self.checkBox_ApEn_r = QtWidgets.QLineEdit(self.ApEn_tab)
        self.checkBox_ApEn_r.setObjectName("checkBox_r")
        # żeby miejsca do wpisywania i opis się równo rozchodziły
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ApEn_r.sizePolicy().hasHeightForWidth())
        self.checkBox_ApEn_r.setSizePolicy(sizePolicy)
        self.horizontalLayout_ApEn_calculation_parameters.addWidget(self.checkBox_ApEn_r)

        self.checkBox_ApEn_N_start = QtWidgets.QLineEdit(self.ApEn_tab)
        self.checkBox_ApEn_N_start.setObjectName("checkBox_7")
        # żeby miejsca do wpisywania i opis się równo rozchodziły
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ApEn_N_start.sizePolicy().hasHeightForWidth())
        self.checkBox_ApEn_N_start.setSizePolicy(sizePolicy)
        self.horizontalLayout_ApEn_calculation_parameters.addWidget(self.checkBox_ApEn_N_start)

        self.checkBox_ApEn_N_stop = QtWidgets.QLineEdit(self.ApEn_tab)
        self.checkBox_ApEn_N_stop.setObjectName("checkBox_8")
        # żeby miejsca do wpisywania i opis się równo rozchodziły
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ApEn_N_stop.sizePolicy().hasHeightForWidth())
        self.checkBox_ApEn_N_stop.setSizePolicy(sizePolicy)
        self.horizontalLayout_ApEn_calculation_parameters.addWidget(self.checkBox_ApEn_N_stop)

        self.verticalLayout_ApEn_inside_tap.addLayout(self.horizontalLayout_ApEn_calculation_parameters)
        self.Entropy_tabWidget.addTab(self.ApEn_tab, "")

        self.horizontalLayout_SampEn_precision = QtWidgets.QHBoxLayout()

        self.SampEn_tab = QtWidgets.QWidget()
        self.SampEn_tab.setObjectName("SampEn_tab")
        self.verticalLayout_SampEn_inside_tap = QtWidgets.QVBoxLayout(self.SampEn_tab)
        self.verticalLayout_SampEn_inside_tap.setObjectName("verticalLayout_4")

        self.horizontalLayout_SampEn_precision = QtWidgets.QHBoxLayout()
        self.horizontalLayout_SampEn_precision.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_SampEn_precision.setObjectName("horizontalLayout_SampEn_precision")

        self.pushButton_SampEn_precision = QtWidgets.QLabel(self.SampEn_tab)
        self.pushButton_SampEn_precision.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SampEn_precision.sizePolicy().hasHeightForWidth())
        self.pushButton_SampEn_precision.setSizePolicy(sizePolicy)
        self.pushButton_SampEn_precision.setObjectName("pushButton_ApEn_precision_2")
        #self.pushButton_SampEn_precision.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_SampEn_precision.addWidget(self.pushButton_SampEn_precision)

        self.checkBox_approx_SampEn_precision = QtWidgets.QCheckBox(self.SampEn_tab)
        self.checkBox_approx_SampEn_precision.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_approx_SampEn_precision.sizePolicy().hasHeightForWidth())
        self.checkBox_approx_SampEn_precision.setSizePolicy(sizePolicy)
        self.checkBox_approx_SampEn_precision.setObjectName("checkBox_approx_SampEn_precision")
        self.horizontalLayout_SampEn_precision.addWidget(self.checkBox_approx_SampEn_precision)

        self.checkBox_normal_SampEny_precision = QtWidgets.QCheckBox(self.SampEn_tab)
        self.checkBox_normal_SampEny_precision.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_normal_SampEny_precision.sizePolicy().hasHeightForWidth())
        self.checkBox_normal_SampEny_precision.setSizePolicy(sizePolicy)
        self.checkBox_normal_SampEny_precision.setAcceptDrops(False)
        self.checkBox_normal_SampEny_precision.setAutoFillBackground(False)
        self.checkBox_normal_SampEny_precision.setChecked(True)
        self.checkBox_normal_SampEny_precision.setObjectName("checkBox_normal_SampEny_precision")
        self.horizontalLayout_SampEn_precision.addWidget(self.checkBox_normal_SampEny_precision)

        self.verticalLayout_SampEn_inside_tap.addLayout(self.horizontalLayout_SampEn_precision)

        self.horizontalLayout_SampEn_distance_measure = QtWidgets.QHBoxLayout()
        self.horizontalLayout_SampEn_distance_measure.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_SampEn_distance_measure.setObjectName("horizontalLayout_SampEn_distance_measure")

        self.pushButton_SampEn_measure = QtWidgets.QLabel(self.SampEn_tab)
        self.pushButton_SampEn_measure.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SampEn_measure.sizePolicy().hasHeightForWidth())
        self.pushButton_SampEn_measure.setSizePolicy(sizePolicy)
        self.pushButton_SampEn_measure.setObjectName("pushButton_SampEn_measure")
        #self.pushButton_SampEn_measure.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_SampEn_distance_measure.addWidget(self.pushButton_SampEn_measure)

        self.radioButton_Euclidean_2 = QtWidgets.QRadioButton(self.SampEn_tab)
        self.radioButton_Euclidean_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_Euclidean_2.sizePolicy().hasHeightForWidth())
        self.radioButton_Euclidean_2.setSizePolicy(sizePolicy)
        self.radioButton_Euclidean_2.setChecked(False)
        self.radioButton_Euclidean_2.setObjectName("radioButton_Euclidean_2")
        self.horizontalLayout_SampEn_distance_measure.addWidget(self.radioButton_Euclidean_2)

        self.radioButton_Chebyshev_2 = QtWidgets.QRadioButton(self.SampEn_tab)
        self.radioButton_Chebyshev_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_Chebyshev_2.sizePolicy().hasHeightForWidth())
        self.radioButton_Chebyshev_2.setSizePolicy(sizePolicy)
        self.radioButton_Chebyshev_2.setChecked(True)
        self.radioButton_Chebyshev_2.setObjectName("radioButton_Chebyshev_2")
        self.horizontalLayout_SampEn_distance_measure.addWidget(self.radioButton_Chebyshev_2)

        self.radioButton_Sampen_distance_measure_both = QtWidgets.QRadioButton(self.SampEn_tab)
        self.radioButton_Sampen_distance_measure_both.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_Sampen_distance_measure_both.sizePolicy().hasHeightForWidth())
        self.radioButton_Sampen_distance_measure_both.setSizePolicy(sizePolicy)
        self.radioButton_Sampen_distance_measure_both.setChecked(False)
        self.radioButton_Sampen_distance_measure_both.setObjectName("radioButton_Sampen_distance_measure_both")
        self.horizontalLayout_SampEn_distance_measure.addWidget(self.radioButton_Sampen_distance_measure_both)

        self.verticalLayout_SampEn_inside_tap.addLayout(self.horizontalLayout_SampEn_distance_measure)

        self.horizontalLayout_SampEn_calculation_parameters = QtWidgets.QHBoxLayout()
        self.horizontalLayout_SampEn_calculation_parameters.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_SampEn_calculation_parameters.setObjectName("horizontalLayout_SampEn_calculation_parameters")

        # self.pushButton_SampEn_Calculation_parameters = QtWidgets.QPushButton(self.SampEn_tab)
        # self.pushButton_SampEn_Calculation_parameters.setEnabled(True)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.pushButton_SampEn_Calculation_parameters.sizePolicy().hasHeightForWidth())
        # self.pushButton_SampEn_Calculation_parameters.setSizePolicy(sizePolicy)
        # self.pushButton_SampEn_Calculation_parameters.setObjectName("pushButton_SampEn_calculation_parameters")
        # self.horizontalLayout_SampEn_calculation_parameters.addWidget(self.pushButton_SampEn_Calculation_parameters)
        #
        # self.checkBox_3 = QtWidgets.QCheckBox(self.SampEn_tab)
        # self.checkBox_3.setEnabled(True)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        # self.checkBox_3.setSizePolicy(sizePolicy)
        # self.checkBox_3.setObjectName("checkBox_3")
        # self.horizontalLayout_SampEn_calculation_parameters.addWidget(self.checkBox_3)
        #
        # self.checkBox_4 = QtWidgets.QCheckBox(self.SampEn_tab)
        # self.checkBox_4.setEnabled(True)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        # self.checkBox_4.setSizePolicy(sizePolicy)
        # self.checkBox_4.setObjectName("checkBox_4")
        # self.horizontalLayout_SampEn_calculation_parameters.addWidget(self.checkBox_4)
        #
        # self.verticalLayout_4.addLayout(self.horizontalLayout_SampEn_calculation_parameters)

        # self.Entropy_tabWidget.addTab(self.SampEn_tab, "")

        self.horizontalLayout_SampEn_calculation_parameters_description = QtWidgets.QHBoxLayout()
        self.horizontalLayout_SampEn_calculation_parameters_description.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_SampEn_calculation_parameters_description.setObjectName(
            "horizontalLayout_SampEn_calculation_parameters_description")

        self.pushButton_SampEn_calculation_standard_parameters = QtWidgets.QCheckBox(self.SampEn_tab)
        self.pushButton_SampEn_calculation_standard_parameters.setObjectName("pushButton_SampEn_calculation_parameters")
        self.pushButton_SampEn_calculation_standard_parameters.setChecked(True)

        self.horizontalLayout_SampEn_calculation_parameters_description.addWidget(
            self.pushButton_SampEn_calculation_standard_parameters)

        # poniżej wihajstry do wpisywania parametrów ApEn
        self.button_SampEn_m_description = QtWidgets.QLabel(self.SampEn_tab)
        self.button_SampEn_m_description.setObjectName("button_m_description")
        self.button_SampEn_m_description.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_SampEn_calculation_parameters_description.addWidget(self.button_SampEn_m_description)

        self.button_SampEn_r_description = QtWidgets.QLabel(self.SampEn_tab)
        self.button_SampEn_r_description.setObjectName("button_r_description")
        self.button_SampEn_r_description.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_SampEn_calculation_parameters_description.addWidget(self.button_SampEn_r_description)

        self.button_SampEn_N_start_description = QtWidgets.QLabel(self.SampEn_tab)
        self.button_SampEn_N_start_description.setObjectName("button_N_start_description")
        self.button_SampEn_N_start_description.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_SampEn_calculation_parameters_description.addWidget(
            self.button_SampEn_N_start_description)

        self.button_SampEn_N_stop_description = QtWidgets.QLabel(self.SampEn_tab)
        self.button_SampEn_N_stop_description.setObjectName("button_N_stop_description")
        self.button_SampEn_N_stop_description.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_SampEn_calculation_parameters_description.addWidget(self.button_SampEn_N_stop_description)

        self.verticalLayout_SampEn_inside_tap.addLayout(self.horizontalLayout_SampEn_calculation_parameters_description)

        self.horizontalLayout_SampEn_calculation_parameters = QtWidgets.QHBoxLayout()
        self.horizontalLayout_SampEn_calculation_parameters.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_SampEn_calculation_parameters.setObjectName(
            "horizontalLayout_SampEn_calculation_parameters")

        #self.pushButton_SampEn_calculation_parameters = QtWidgets.QLineEdit(self.SampEn_tab)
        self.pushButton_SampEn_calculation_parameters = QtWidgets.QLabel(self.SampEn_tab)
        #self.pushButton_SampEn_calculation_parameters.setReadOnly(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SampEn_calculation_parameters.sizePolicy().hasHeightForWidth())
        self.pushButton_SampEn_calculation_parameters.setSizePolicy(sizePolicy)
        self.pushButton_SampEn_calculation_parameters.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton_SampEn_calculation_parameters.setObjectName("pushButton_SampEn_calculation_parameters")
        self.horizontalLayout_SampEn_calculation_parameters.addWidget(self.pushButton_SampEn_calculation_parameters)

        # poniżej wihajstry do wpisywania parametrów SampEn
        self.checkBox_SampEn_m = QtWidgets.QLineEdit(self.SampEn_tab)
        self.checkBox_SampEn_m.setObjectName("checkBox_SampEn_m")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_SampEn_m.sizePolicy().hasHeightForWidth())
        self.checkBox_SampEn_m.setSizePolicy(sizePolicy)
        self.horizontalLayout_SampEn_calculation_parameters.addWidget(self.checkBox_SampEn_m)

        self.checkBox_SampEn_r = QtWidgets.QLineEdit(self.SampEn_tab)
        self.checkBox_SampEn_r.setObjectName("checkBox_SampEn_r")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_SampEn_r.sizePolicy().hasHeightForWidth())
        self.checkBox_SampEn_r.setSizePolicy(sizePolicy)
        self.horizontalLayout_SampEn_calculation_parameters.addWidget(self.checkBox_SampEn_r)

        self.checkBox_SampEn_N_start = QtWidgets.QLineEdit(self.SampEn_tab)
        self.checkBox_SampEn_N_start.setObjectName("checkBox_SampEn_N_start")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_SampEn_N_start.sizePolicy().hasHeightForWidth())
        self.checkBox_SampEn_N_start.setSizePolicy(sizePolicy)
        self.horizontalLayout_SampEn_calculation_parameters.addWidget(self.checkBox_SampEn_N_start)

        self.checkBox_SampEn_N_stop = QtWidgets.QLineEdit(self.SampEn_tab)
        self.checkBox_SampEn_N_stop.setObjectName("checkBox_SampEn_N_stop")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_SampEn_N_stop.sizePolicy().hasHeightForWidth())
        self.checkBox_SampEn_N_stop.setSizePolicy(sizePolicy)
        self.horizontalLayout_SampEn_calculation_parameters.addWidget(self.checkBox_SampEn_N_stop)

        self.verticalLayout_SampEn_inside_tap.addLayout(self.horizontalLayout_SampEn_calculation_parameters)

        self.Entropy_tabWidget.addTab(self.SampEn_tab, "")

        # wyniki obliczeń

        self.Results_tab = QtWidgets.QWidget()
        self.Results_tab.setObjectName("Results")
        self.verticalLayout_Results_inside_tap = QtWidgets.QVBoxLayout(self.Results_tab)
        self.verticalLayout_Results_inside_tap.setObjectName("verticalLayout_Results")

        self.results_text = QtWidgets.QTextEdit(self.Results_tab)
        #self.results_text.setDisabled(True)

        self.results_text.setObjectName("pushButton_Results_precision_")

        self.verticalLayout_Results_inside_tap.addWidget(self.results_text)

        self.Entropy_tabWidget.addTab(self.Results_tab, "Results")

        self.verticalLayout.addWidget(self.Entropy_tabWidget)

        self.pushButton_standardization_description = QtWidgets.QLabel(self.centralwidget)
        self.pushButton_standardization_description.setObjectName("pushButton_opis_knefla_ponizej")
        self.pushButton_standardization_description.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.pushButton_standardization_description)

        self.comboBox_data_standarization = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_data_standarization.setObjectName("comboBox_data_standardization")

        self.comboBox_data_standarization.addItems(self.comboBox_data_standardisation_text)
        self.verticalLayout.addWidget(self.comboBox_data_standarization)
        self.comboBox_data_standarization.currentIndexChanged.connect(self.normalize_data)

        self.charts_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.charts_tabWidget.sizePolicy().hasHeightForWidth())
        self.charts_tabWidget.setSizePolicy(sizePolicy)
        self.charts_tabWidget.setObjectName("charts_tabWidget")

        self.chart_2d_tab = QtWidgets.QWidget()
        self.chart_2d_tab.setObjectName("chart_2d_tab")

        self.verticalLayout_2d_chart = QtWidgets.QVBoxLayout(self.chart_2d_tab)
        self.verticalLayout_2d_chart.setObjectName("verticalLayout_2")

        self.button_2d_chart_description = QtWidgets.QLabel(self.chart_2d_tab)
        self.button_2d_chart_description.setObjectName("button_3d")
        self.button_2d_chart_description.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2d_chart.addWidget(self.button_2d_chart_description)

        self.comboBox_2d_chart_axis = QtWidgets.QComboBox(self.chart_2d_tab)
        self.comboBox_2d_chart_axis.setObjectName("comboBox_2d_chart_axis")
        self.verticalLayout_2d_chart.addWidget(self.comboBox_2d_chart_axis)

        # załadowanie wykresu po pojawienu się wartości w okienku "dropbox"
        self.comboBox_2d_chart_axis.currentIndexChanged.connect(self.update_2d_chart)

        #wykres 2d

        self.fig = Figure()
        self.ax1 = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setSizePolicy(QSizePolicy.Expanding,
                                  QSizePolicy.Expanding)
        self.canvas.updateGeometry()
        self.verticalLayout_2d_chart.addWidget(self.canvas)

        # opcjonalnie dodatkowy button
        # self.Wykres2d = QtWidgets.QPushButton(self.chart_2d_tab)
        # self.Wykres2d.setObjectName("Wykres2d")
        # self.verticalLayout_2.addWidget(self.Wykres2d)

        self.charts_tabWidget.addTab(self.chart_2d_tab, "")

        self.chart_3d_tab = QtWidgets.QWidget()
        self.chart_3d_tab.setObjectName("chart_3d_tab")

        self.verticalLayout_3d_chart = QtWidgets.QVBoxLayout(self.chart_3d_tab)
        self.verticalLayout_3d_chart.setObjectName("verticalLayout_3")

        self.button_3d_chart_description = QtWidgets.QLabel(self.chart_3d_tab)
        self.button_3d_chart_description.setObjectName("button_3d")
        self.button_3d_chart_description.setAlignment(Qt.AlignCenter)
        self.verticalLayout_3d_chart.addWidget(self.button_3d_chart_description)

        self.comboBox_3d_chart_x = QtWidgets.QComboBox(self.chart_3d_tab)
        self.comboBox_3d_chart_x.setObjectName("comboBox_3d_chart_x")
        self.verticalLayout_3d_chart.addWidget(self.comboBox_3d_chart_x)
        # rysuje plot 3d
        self.comboBox_3d_chart_x.currentIndexChanged.connect(self.draw_plot_3d)

        self.comboBox_3d_chart_y = QtWidgets.QComboBox(self.chart_3d_tab)
        self.comboBox_3d_chart_y.setObjectName("comboBox_3d_chart_y")
        self.verticalLayout_3d_chart.addWidget(self.comboBox_3d_chart_y)
        # rysuje plot 3d
        self.comboBox_3d_chart_y.currentIndexChanged.connect(self.draw_plot_3d)

        self.comboBox_3d_chart_z = QtWidgets.QComboBox(self.chart_3d_tab)
        self.comboBox_3d_chart_z.setObjectName("comboBox_3d_chart_z")
        self.verticalLayout_3d_chart.addWidget(self.comboBox_3d_chart_z)
        #rysuje plot 3d
        self.comboBox_3d_chart_z.currentIndexChanged.connect(self.draw_plot_3d)

        #wykres 3d

        self.fig2 = Figure()
        self.ax2 = p3.Axes3D(self.fig2)
        self.canvas2 = FigureCanvas(self.fig2)
        #self.canvas2.setParent(self)
        self.canvas2.setSizePolicy(QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        self.canvas2.updateGeometry()
        self.verticalLayout_3d_chart.addWidget(self.canvas2)

        # opcjonalnie dodatkowy button




        self.charts_tabWidget.addTab(self.chart_3d_tab, "")
        self.verticalLayout.addWidget(self.charts_tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setIconSize(QSize(60, 60))

        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.Entropy_tabWidget.setCurrentIndex(0)
        self.charts_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # wyłączenie niestandardowych przycisków do ustawienia parametrów ApEn z podpięciem funkcji pod checkBox
        # musi być na końcu, bo musi być wykonana po utworzeniu GUI
        # (bo się do niego odnosi, a nie może się odnosić do czegoś, czego jeszcze nie ma)

        self.pushButton_ApEn_calculation_standard_parameters.stateChanged.connect(
            self.enable_ApEn_uncustomary_parameters)
        self.enable_ApEn_uncustomary_parameters()

        self.pushButton_SampEn_calculation_standard_parameters.stateChanged.connect(
            self.enable_SampEn_uncustomary_parameters)
        self.enable_SampEn_uncustomary_parameters()

        # dodanie do toolbaru

        open_file_action = QAction(QIcon(), 'Open File...', self.toolBar)
        open_file_action.setStatusTip('Open file')
        open_file_action.setShortcut(QKeySequence.Open)
        open_file_action.triggered.connect(self.file_open)  # TODO

        calc_ApEn_action = QAction(QIcon(), 'ApEn...', self.toolBar)
        calc_ApEn_action.setStatusTip('ApEn')
        calc_ApEn_action.setShortcut(QKeySequence.Open)
        calc_ApEn_action.triggered.connect(self.calculate_ApEn_only)

        calc_SampEn_action = QAction(QIcon(), 'SampEn...', self.toolBar)
        calc_SampEn_action.setStatusTip('SampEn')
        calc_SampEn_action.setShortcut(QKeySequence.Open)
        calc_SampEn_action.triggered.connect(self.calculate_SampEn_only)

        calc_SampEn_and_ApEn_action = QAction(QIcon(), 'Both...', self.toolBar)
        calc_SampEn_and_ApEn_action.setStatusTip('ApEn and SampEn')
        calc_SampEn_and_ApEn_action.setShortcut(QKeySequence.Open)
        calc_SampEn_and_ApEn_action.triggered.connect(self.calculate_Apen_and_Sampen_only)

        calc_XLSX_action = QAction(QIcon(), 'Calc. to XLSX...', self.toolBar)
        calc_XLSX_action.setStatusTip('XLSX')
        calc_XLSX_action.setShortcut(QKeySequence.Open)
        calc_XLSX_action.triggered.connect(self.results_to_excel)

        calc_SQL_action = QAction(QIcon(), 'Calc. to SQL...', self.toolBar)
        calc_SQL_action.setStatusTip('SQL')
        calc_SQL_action.setShortcut(QKeySequence.Open)
        # calc_CSV_action.triggered.connect()

        self.toolBar.addActions([open_file_action, calc_ApEn_action, calc_SampEn_action, calc_SampEn_and_ApEn_action,
                                 calc_SQL_action, calc_XLSX_action])

    def ApEn_parameters(self, enable_or_disable):
        if enable_or_disable == False:
            self.ApEn_m_value = 2
            self.ApEn_r_value = 0.25
            self.ApEn_N_start_value = 0
            self.ApEn_N_stop_value = self.calculating_data_length
        else:
            ApEn_m_value = str(self.checkBox_ApEn_m.text())
            ApEn_m_value = try_parse_int(ApEn_m_value)
            if ApEn_m_value == None or ApEn_m_value == 0:
                self.ApEn_m_value = 2
            else:
                self.ApEn_m_value = ApEn_m_value

            ApEn_r_value = str(self.checkBox_ApEn_r.text())
            ApEn_r_value = try_parse_float(ApEn_r_value)
            if ApEn_r_value == None or ApEn_r_value == 0.0:
                self.ApEn_r_value = 0.25
            else:
                self.ApEn_r_value = ApEn_r_value

            ApEn_N_start_value = str(self.checkBox_ApEn_N_start.text())
            ApEn_N_start_value = try_parse_int(ApEn_N_start_value)
            if ApEn_N_start_value == None or ApEn_N_start_value == 0:
                self.ApEn_N_start_value = 0
            else:
                self.ApEn_N_start_value = ApEn_N_start_value

            ApEn_N_stop_value = str(self.checkBox_ApEn_N_stop.text())
            ApEn_N_stop_value = try_parse_int(ApEn_N_stop_value)
            if ApEn_N_stop_value == None or ApEn_N_stop_value == 0:
                self.ApEn_N_stop_value = self.calculating_data_length
            else:
                self.ApEn_N_stop_value = ApEn_N_stop_value

    def SampEn_parameters(self, enable_or_disable):
        if enable_or_disable == False:
            self.SampEn_m_value = 2
            self.SampEn_r_value = 0.25
            self.SampEn_N_start_value = 0
            self.SampEn_N_stop_value = self.calculating_data_length
        else:
            SampEn_m_value = str(self.checkBox_SampEn_m.text())
            SampEn_m_value = try_parse_int(SampEn_m_value)
            if SampEn_m_value == None or SampEn_m_value == 0:
                self.SampEn_m_value = 2
            else:
                self.SampEn_m_value = SampEn_m_value

            SampEn_r_value = str(self.checkBox_SampEn_r.text())
            SampEn_r_value = try_parse_float(SampEn_r_value)
            if SampEn_r_value == None or SampEn_r_value == 0.0:
                self.SampEn_r_value = 0.25
            else:
                self.SampEn_r_value = SampEn_r_value

            SampEn_N_start_value = str(self.checkBox_SampEn_N_start.text())
            SampEn_N_start_value = try_parse_int(SampEn_N_start_value)
            if SampEn_N_start_value == None or SampEn_N_start_value == 0:
                self.SampEn_N_start_value = 0
            else:
                self.SampEn_N_start_value = SampEn_N_start_value

            SampEn_N_stop_value = str(self.checkBox_SampEn_N_stop.text())
            SampEn_N_stop_value = try_parse_int(SampEn_N_stop_value)
            if SampEn_N_stop_value == None or SampEn_N_stop_value == 0:
                self.SampEn_N_stop_value = self.calculating_data_length
            else:
                self.SampEn_N_stop_value = SampEn_N_stop_value


    def enable_ApEn_uncustomary_parameters(self):
        # Karol2
        if self.pushButton_ApEn_calculation_standard_parameters.isChecked():
            self.checkBox_ApEn_m.setEnabled(False)
            self.checkBox_ApEn_r.setEnabled(False)
            self.checkBox_ApEn_N_start.setEnabled(False)
            self.checkBox_ApEn_N_stop.setEnabled(False)
            self.button_ApEn_m_description.setEnabled(False)
            self.button_ApEn_r_description.setEnabled(False)
            self.button_ApEn_N_start_description.setEnabled(False)
            self.button_ApEn_N_stop_description.setEnabled(False)
            self.pushButton_ApEn_calculation_parameters.setEnabled(False)

        else:
            self.checkBox_ApEn_m.setEnabled(True)
            self.checkBox_ApEn_r.setEnabled(True)
            self.checkBox_ApEn_N_start.setEnabled(True)
            self.checkBox_ApEn_N_stop.setEnabled(True)
            self.button_ApEn_m_description.setEnabled(True)
            self.button_ApEn_r_description.setEnabled(True)
            self.button_ApEn_N_start_description.setEnabled(True)
            self.button_ApEn_N_stop_description.setEnabled(True)
            self.pushButton_ApEn_calculation_parameters.setEnabled(True)

    def enable_SampEn_uncustomary_parameters(self):
        # Karol2
        if self.pushButton_SampEn_calculation_standard_parameters.isChecked():
            self.checkBox_SampEn_m.setEnabled(False)
            self.checkBox_SampEn_r.setEnabled(False)
            self.checkBox_SampEn_N_start.setEnabled(False)
            self.checkBox_SampEn_N_stop.setEnabled(False)
            self.button_SampEn_m_description.setEnabled(False)
            self.button_SampEn_r_description.setEnabled(False)
            self.button_SampEn_N_start_description.setEnabled(False)
            self.button_SampEn_N_stop_description.setEnabled(False)
            self.pushButton_SampEn_calculation_parameters.setEnabled(False)
        else:
            self.checkBox_SampEn_m.setEnabled(True)
            self.checkBox_SampEn_r.setEnabled(True)
            self.checkBox_SampEn_N_start.setEnabled(True)
            self.checkBox_SampEn_N_stop.setEnabled(True)
            self.button_SampEn_m_description.setEnabled(True)
            self.button_SampEn_r_description.setEnabled(True)
            self.button_SampEn_N_start_description.setEnabled(True)
            self.button_SampEn_N_stop_description.setEnabled(True)
            self.pushButton_SampEn_calculation_parameters.setEnabled(True)

    def normalize_data(self):
        if self.comboBox_data_standarization.currentText() == '' or self.data_header_length == 0:
            return
        else:
            if self.comboBox_data_standarization.currentText() == "standardise":
                x = self.data
                # linijka poniżej traci referencje, żeby nie zostawała można też użyć Lib/copy.py
                x = (x+x)/2
                if self.data_header_length == 0:
                    return
                else:
                    for i in range(0,  self.data_header_length):
                        # print(self.data_dictionary[i])
                        data = self.data[[self.data_header_dictionary[i]]]
                        self.data[[self.data_header_dictionary[i]]] = (data - np.mean(data)) / np.std(data)
                    self.data_progenitor = x
            else:
                self.data = self.data_progenitor

            self.draw_plot_3d()
            self.update_2d_chart()

    def draw_plot_3d(self):

        data = self.data
        self.x = []
        self.y = []
        self.z = []
        if self.data_header == 0:
            if (self.comboBox_3d_chart_x.currentText() is int or self.comboBox_3d_chart_y.currentText() is int
                    or self.comboBox_3d_chart_z.currentText() is int
                    or self.comboBox_3d_chart_x.currentText() == ''
                    or self.comboBox_3d_chart_y.currentText() == ''
                    or self.comboBox_3d_chart_z.currentText() == ''):
                return
            else:
                x = str(self.comboBox_3d_chart_x.currentText())
                if self.comboBox_3d_chart_y.currentText() == '':
                    z = x
                    y = x
                    pass
                else:
                    y = str(self.comboBox_3d_chart_y.currentText())
                    if self.comboBox_3d_chart_z.currentText() == '':
                        z = x
                        pass
                    else:
                        z = str(self.comboBox_3d_chart_z.currentText())
        else:
            if (self.comboBox_3d_chart_x.currentText() is str or self.comboBox_3d_chart_y.currentText() is str
                    or self.comboBox_3d_chart_z.currentText() is str
                    or self.comboBox_3d_chart_x.currentText() == ''
                    or self.comboBox_3d_chart_y.currentText() == ''
                    or self.comboBox_3d_chart_z.currentText() == ''):
                return
            else:
                x = int(self.comboBox_3d_chart_x.currentText())
                if self.comboBox_3d_chart_y.currentText() == '':
                    z = x
                    y = x
                    pass
                else:
                    y = int(self.comboBox_3d_chart_y.currentText())
                    if self.comboBox_3d_chart_z.currentText() == '':
                        z = x
                        pass
                    else:
                        z = int(self.comboBox_3d_chart_z.currentText())
            # x = int(self.comboBox_3d_chart_x.currentText())
            # y = int(self.comboBox_3d_chart_y.currentText())
            # z = int(self.comboBox_3d_chart_z.currentText())

        # self.x = self.data_dictionary[self.data_header_dictionary[x]][:, 0]
        # self.y = self.data_dictionary[self.data_header_dictionary[y]][:, 0]
        # self.z = self.data_dictionary[self.data_header_dictionary[z]][:, 0]


        self.x = data[[x]].values[:, 0]
        self.y = data[[y]].values[:, 0]
        self.z = data[[z]].values[:, 0]

        self.ax2 = p3.Axes3D(self.fig2)
        self.ax2.plot3D(self.x, self.y, self.z)
        self.canvas2.draw()

    def file_open(self):
        path, _ = QFileDialog.getOpenFileName(
            parent=MainWindow,
            caption='Open file',
            directory='',
            filter=self.filterTypes
        )

        if path:
            try:
                with open(path, 'r') as f:
                    text = f.read()
                    f.close()
            except Exception as e:
                self.dialog_message(str(e))
            else:
                self.path = path
                self.data_header = self.identify_header(path)

                self.data = pd.read_csv(path, header=self.data_header)
                self.data_progenitor = self.data
                # napisać słownik z gdzie będą dane i w oznaczeniu tytuły kolumn (przy odczycie wystarczy odczyt z
                # header cells użyć do odczytu (można header cells też zrobić jako słownik gdzie zwracana będize
                # długość)

                self.load_dropdown()



    def fill_drop_downs(self):
        self.comboBox_2d_chart_axis.clear()

        self.comboBox_2d_chart_axis.addItems(self.data_header_cells)

        self.comboBox_3d_chart_x.clear()
        self.comboBox_3d_chart_y.clear()
        self.comboBox_3d_chart_z.clear()

        self.comboBox_3d_chart_x.addItems(self.data_header_cells)
        self.comboBox_3d_chart_y.addItems(self.data_header_cells)
        self.comboBox_3d_chart_z.addItems(self.data_header_cells)

    def load_dictionaries(self):
        self.data_dictionary = {}
        self.data_header_dictionary = {}
        if (self.data_header == None):
            for i in range(0, self.data_header_length):
                self.data_dictionary[i] = self.data[[int(self.data_header_cells[i])]].values
                self.data_header_dictionary[i] = int(self.data_header_cells[i])
        else:
            for i in range(0, self.data_header_length):
                self.data_dictionary[i] = self.data[[str(self.data_header_cells[i])]].values
                self.data_header_dictionary[i] = str(self.data_header_cells[i])

    def load_dropdown(self):

        data = self.data
        data_header = self.data_header

        if (len(data) != 0):
            if (data_header == None):

                self.data_header_length = len(pd.read_csv(self.path, header=0).columns.values.tolist())
                self.data_header_cells = self.header_length_to_list_of_digit_string(self.data_header_length)
                self.load_dictionaries()

                self.fill_drop_downs()

            else:
                if (data_header == 0):
                    # print(pd.read_csv(self.path, header=0).columns.values.tolist())
                    self.data_header_length = len(pd.read_csv(self.path, header=0).columns.values.tolist())
                    self.data_header_cells = pd.read_csv(self.path, header=0).columns.values.tolist()
                    self.load_dictionaries()
                    self.fill_drop_downs()

                else:
                    # print(len(pd.read_csv(self.path, header=0).columns.values.tolist()))
                    print("data_header error")

    def identify_header(self, path, n=5, th=0.9):
        df1 = pd.read_csv(path, header='infer', nrows=n)
        df2 = pd.read_csv(path, header=None, nrows=n)
        sim = (df1.dtypes.values == df2.dtypes.values).mean()
        return 0 if sim < th else None

    #     0 - header jest
    #     1 - headera nie ma

    def header_length_to_list_of_digit_string(self, header_length):
        list_of_digits = list()
        for i in range(0, header_length):
            list_of_digits.append(str(i))
        return list_of_digits

    def update_2d_chart(self):
        # self.dropdown3.clear()
        colors=["b", "r", "g", "y", "k", "c"]
        self.ax1.clear()
        self.chosen_data_header = self.comboBox_2d_chart_axis.currentText()
        cat = self.comboBox_2d_chart_axis.currentText()
        data = self.data
        data_header = self.data_header


        if (len(data) != 0):
            if(cat== ''):
                pass
                # print('empty dropdown3')

            else:
                if(data_header==0):
                    #print(data[['x']].values[0:5])
                    #self.data_dictionary.plot(kind="line", x=None, y=str(cat), ax=self.ax1,
                    #                                                   c=colors[0], label=str(self.chosen_data_header))
                    data.plot(kind="line", x=None, y=str(cat), ax=self.ax1, c=colors[0], label=str(self.chosen_data_header))
                else:
                    # print(data[[0]].values[0:4])
                    #self.data_dictionary.plot(kind="line", x=None, y=int(cat), ax=self.ax1,
                    #                                                   c=colors[0], label=str(self.chosen_data_header))
                    data.plot(kind="line", x=None, y=int(cat), ax=self.ax1, c=colors[0], label=str(self.chosen_data_header))

        # np.arange(0, len(data[0].values), 1), data[0].vales,

        self.fig.canvas.draw_idle()

    # def update_3d_chart(self):
    ## funkcja tylko temporalna, w przyszłości do zmiany
    #     data = self.data
    #     data_header_cells = self.data_header_cells
    #
    #     if self.data_header == 0:
    #         x = str(data_header_cells[0])
    #         y = str(data_header_cells[1])
    #         z = str(data_header_cells[2])
    #     else:
    #         x = int(data_header_cells[0])
    #         y = int(data_header_cells[1])
    #         z = int(data_header_cells[2])
    #
    #     self.x = data[[x]].values[:, 0]
    #     self.y = data[[y]].values[:, 0]
    #     self.z = data[[z]].values[:, 0]
    #
    #     self.ax2 = p3.Axes3D(self.fig2)
    #     self.ax2.plot3D(self.x, self.y, self.z)
    #     self.canvas2.draw()

    def calculate_ApEn_only(self):
        ApEn = self.approximate_entropy_calculation()
        self.popup(ApEn, None, "ApEn")

    def calculate_SampEn_only(self):
        SampEn = self.sample_entropy_calculation()
        self.popup(None, SampEn, "SampEn")

    def calculate_Apen_and_Sampen_only(self):
        ApEn = self.approximate_entropy_calculation()
        SampEn = self.sample_entropy_calculation()
        self.popup(ApEn, SampEn, "Entropy results")

    def approximate_entropy_calculation(self):


        #wpisać wszędzie self.ApEn_r i ApEn_m value zamiast z palca

        data = self.data
        cat = self.comboBox_2d_chart_axis.currentText()
        if (cat == '') or (not self.radioButton_Chebyshev.isChecked() and
                            not self.radioButton_Euclidean.isChecked()) or (
                            not self.checkBox_normal_ApEny_precision.isChecked() and
                            not self.checkBox_approx_ApEn_precision.isChecked()):
            pass
        else:
            try:
                chosen_data_header = int(self.chosen_data_header)
            except ValueError as verr:
                chosen_data_header = self.chosen_data_header
                pass
            except Exception as ex:
                print("chosen_data_header error, chosen_data_header = "+chosen_data_header)
                pass  # do job to handle: Exception occurred while converting to int
            self.calculating_data_length = len(data[[chosen_data_header]].values)
            if self.pushButton_ApEn_calculation_standard_parameters.isChecked():
                self.ApEn_parameters(False)
            else:
                self.ApEn_parameters(True)

            approximate_entropy = ApEn(data[[chosen_data_header]].values[self.ApEn_N_start_value:
                                                                         self.ApEn_N_stop_value],
                                       self.ApEn_m_value, self.ApEn_r_value,
                                       self.radioButton_Chebyshev.isChecked(),
                                       self.radioButton_Euclidean.isChecked(),
                                       self.checkBox_normal_ApEny_precision.isChecked(),
                                       self.checkBox_approx_ApEn_precision.isChecked())

            return approximate_entropy

    def sample_entropy_calculation(self):
        data = self.data
        cat = self.comboBox_2d_chart_axis.currentText()
        if(cat== ''):
            pass
        else:
            try:
                chosen_data_header = int(self.chosen_data_header)
            except ValueError as verr:
                chosen_data_header = self.chosen_data_header
                pass
            except Exception as ex:
                print("chosen_data_header error, chosen_data_header = "+chosen_data_header)
                pass  # do job to handle: Exception occurred while converting to int

            self.calculating_data_length = len(data[[chosen_data_header]].values)
            if self.pushButton_SampEn_calculation_standard_parameters.isChecked():
                self.SampEn_parameters(False)
            else:
                self.SampEn_parameters(True)

            sample_entropy = SampEn(data[[chosen_data_header]].values[self.SampEn_N_start_value:self.SampEn_N_stop_value],
                                    self.SampEn_m_value, self.SampEn_r_value)
            #self.comboBox_2d_chart_axis.setText('SampEn = '+str(sample_entropy))
            #print(sample_entropy)
            return sample_entropy

    def popup(self, ApEn, SampEn, entropy_type):
        ApEn_results = ApEn
        SampEn_results = SampEn
        self.resultsPopup.setWindowTitle(entropy_type)
        # approx_Chebyshev, approx_Euclidean, Chebyshev_full_method, Euclidean_full_method

        if ApEn_results:
            if ApEn_results[0]==None:
                approx_Chebyshev = ''
            else:
                approx_Chebyshev = 'Approximate Chebyshev: ' + str(ApEn_results[0]) + '\n'
            if ApEn_results[1] == None:
                approx_Euclidean = ''
            else:
                approx_Euclidean = 'Approximate Euclidean: ' + str(ApEn_results[1]) + '\n'
            if ApEn_results[2] == None:
                Chebyshev_full_method = ''
            else:
                Chebyshev_full_method = 'Chebyshev: ' + str(ApEn_results[2]) + '\n'
            if ApEn_results[3] == None:
                Euclidean_full_method = ''
            else:
                Euclidean_full_method = 'Euclidean: ' + str(ApEn_results[3]) + '\n'

            ApEn_results_text = approx_Chebyshev + approx_Euclidean + Chebyshev_full_method + Euclidean_full_method

        else:
            ApEn_results_text = ''

        if SampEn_results:
            SampEn_results_text = 'SampEn: ' + str(SampEn_results)

        else:
            SampEn_results_text = ''

        if not ApEn_results_text + SampEn_results_text == '':
            self.results_text.setText(ApEn_results_text + SampEn_results_text)
            self.resultsPopup.setText(ApEn_results_text + SampEn_results_text)

            self.resultsPopup.setGeometry(700, 300, 100, 100)
            self.resultsPopup.exec_()

    def results_to_excel(self):
        cat = self.comboBox_2d_chart_axis.currentText()
        if (cat == ''):
            pass
        else:
            data_column = []

            # poprawić, żeby nie zapisywał path tylko nazwę pliku
            data_column.append(str(self.path))
            #approx_Chebyshev, approx_Euclidean, Chebyshev_full_method, Euclidean_full_method
            ApEn_results = self.approximate_entropy_calculation()
            SampEn_results = self.sample_entropy_calculation()
            data_column.append(str(ApEn_results[0]))
            data_column.append(str(ApEn_results[1]))
            data_column.append(str(ApEn_results[2]))
            data_column.append(str(ApEn_results[3]))
            data_column.append(str(SampEn_results))


            if os.path.isfile('calculation results.xlsx'):


                df2 = pd.read_excel('calculation results.xlsx', sheet_name='Sheet1')
                df2.drop('Unnamed: 0', axis=1, inplace=True)
                df1 = pd.DataFrame([data_column[:]],

                                   index=[str(len(df2[['file_name']].values)+1)],

                                   columns=['file_name', 'approx_Chebyshev', 'approx_Euclidean', 'Chebyshev_full_method',
                                            'Euclidean_full_method', 'Sampen'])

                df3 = pd.concat([df2, df1])
                df3.to_excel('calculation results.xlsx')
            else:
                df1 = pd.DataFrame([data_column[:]],

                                   index=['0'],

                                   columns=['file_name', 'approx_Chebyshev', 'approx_Euclidean', 'Chebyshev_full_method',
                                            'Euclidean_full_method', 'Sampen'])
                df1.to_excel('calculation results.xlsx')





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_ApEn_precision.setText(_translate("MainWindow", "ApEn precision:"))
        self.checkBox_approx_ApEn_precision.setText(_translate("MainWindow", "approx"))
        self.checkBox_normal_ApEny_precision.setText(_translate("MainWindow", "normal"))
        self.pushButton_ApEn_measure.setText(_translate("MainWindow", "ApEn distance measure:"))
        self.radioButton_Euclidean.setText(_translate("MainWindow", "Euclidean"))
        self.radioButton_Chebyshev.setText(_translate("MainWindow", "Chebyshev"))
        # self.radioButton_distance_measure_both.setText(_translate("MainWindow", "Both"))
        self.pushButton_ApEn_calculation_parameters.setText(_translate("MainWindow", "Calculation parameters:"))
        self.checkBox_ApEn_m.setText(_translate("MainWindow", ""))
        self.checkBox_ApEn_r.setText(_translate("MainWindow", ""))
        self.checkBox_ApEn_N_start.setText(_translate("MainWindow", ""))
        self.pushButton_ApEn_calculation_standard_parameters.setText(_translate("MainWindow", "m=2, r=0.25"))
        self.button_ApEn_m_description.setText(_translate("MainWindow", "m:"))
        self.button_ApEn_r_description.setText(_translate("MainWindow", "r:"))
        self.button_ApEn_N_start_description.setText(_translate("MainWindow", "N start:"))
        self.button_ApEn_N_stop_description.setText(_translate("MainWindow", "N stop:"))
        self.checkBox_ApEn_N_stop.setText(_translate("MainWindow", ""))
        self.Entropy_tabWidget.setTabText(self.Entropy_tabWidget.indexOf(self.ApEn_tab), _translate("MainWindow", "ApEn"))
        self.pushButton_SampEn_precision.setText(_translate("MainWindow", "SampEn precision:"))
        self.checkBox_approx_SampEn_precision.setText(_translate("MainWindow", "approx"))
        self.checkBox_normal_SampEny_precision.setText(_translate("MainWindow", "normal"))
        self.pushButton_SampEn_measure.setText(_translate("MainWindow", "SampEn distance measure:"))
        self.radioButton_Euclidean_2.setText(_translate("MainWindow", "Euclidean"))
        self.radioButton_Chebyshev_2.setText(_translate("MainWindow", "Chebyshev"))
        self.radioButton_Sampen_distance_measure_both.setText(_translate("MainWindow", "Both"))
        self.pushButton_SampEn_calculation_parameters.setText(_translate("MainWindow", "Calculation parameters:"))
        self.checkBox_SampEn_m.setText(_translate("MainWindow", ""))
        self.checkBox_SampEn_r.setText(_translate("MainWindow", ""))
        self.checkBox_SampEn_N_start.setText(_translate("MainWindow", ""))
        self.pushButton_SampEn_calculation_standard_parameters.setText(_translate("MainWindow", "m=2, r=0.25"))
        self.button_SampEn_m_description.setText(_translate("MainWindow", "m:"))
        self.button_SampEn_r_description.setText(_translate("MainWindow", "r:"))
        self.button_SampEn_N_start_description.setText(_translate("MainWindow", "N start:"))
        self.button_SampEn_N_stop_description.setText(_translate("MainWindow", "N stop:"))
        self.Entropy_tabWidget.setTabText(self.Entropy_tabWidget.indexOf(self.SampEn_tab), _translate("MainWindow", "SampEn"))
        self.pushButton_standardization_description.setText(_translate("MainWindow", "Data standardisation:"))
        #self.Wykres2d.setText(_translate("MainWindow", "wykres 2d"))
        self.button_2d_chart_description.setText(_translate("MainWindow", "Chose axis to display:"))
        self.charts_tabWidget.setTabText(self.charts_tabWidget.indexOf(self.chart_2d_tab), _translate("MainWindow", "2d chart"))
        #self.comboBox_3d_chart_z.setText(_translate("MainWindow", "3d chart"))
        self.button_3d_chart_description.setText(_translate("MainWindow", "Chose axes to display:"))
        self.charts_tabWidget.setTabText(self.charts_tabWidget.indexOf(self.chart_3d_tab), _translate("MainWindow", "3d chart"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.move(600, 50)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
