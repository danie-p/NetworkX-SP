from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSlider
import Kruskal
import LabelSet

class Ui_NetworkX(object):
    def setupUi(self, NetworkX):
        NetworkX.setObjectName("NetworkX")
        NetworkX.resize(1311, 810)
        NetworkX.setStyleSheet("QMainWindow {background: '#a7e8d1';}")

        self.centralwidget = QtWidgets.QWidget(NetworkX)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_dataset = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_dataset.setFont(font)
        self.label_dataset.setObjectName("label_dataset")
        self.horizontalLayout.addWidget(self.label_dataset)

    # COMBO BOX: DATASET
        self.comboBox_dataset = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_dataset.setAutoFillBackground(True)
        self.comboBox_dataset.setEditable(False)
        self.comboBox_dataset.addItem("")
        self.comboBox_dataset.addItem("")
        self.comboBox_dataset.setObjectName("comboBox_dataset")
        self.horizontalLayout.addWidget(self.comboBox_dataset)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 641, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_rozmedzie = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_rozmedzie.setFont(font)
        self.label_rozmedzie.setObjectName("label_rozmedzie")
        self.horizontalLayout_2.addWidget(self.label_rozmedzie)

    # SLIDER: VRCHOL 1
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.slider1 = QtWidgets.QSlider(self.horizontalLayoutWidget_2)
        self.slider1.setOrientation(QtCore.Qt.Horizontal)
        self.slider1.setObjectName("slider1")
        self.slider1.setMinimum(1)
        self.slider1.setMaximum(13)
        self.slider1.setTickPosition(QSlider.TicksBelow)
        self.slider1.setTickInterval(5)
        self.horizontalLayout_2.addWidget(self.slider1)

    # SLIDER: VRCHOL 2
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.slider2 = QtWidgets.QSlider(self.horizontalLayoutWidget_2)
        self.slider2.setOrientation(QtCore.Qt.Horizontal)
        self.slider2.setObjectName("slider2")
        self.slider2.setMinimum(1)
        self.slider2.setMaximum(13)
        self.slider2.setTickPosition(QSlider.TicksBelow)
        self.slider2.setTickInterval(5)
        self.horizontalLayout_2.addWidget(self.slider2)

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 210, 641, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

    # BUTTON NAJKRATSIA CESTA
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.button_najkratsia_cesta = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_najkratsia_cesta.sizePolicy().hasHeightForWidth())
        self.button_najkratsia_cesta.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_najkratsia_cesta.setFont(font)
        self.button_najkratsia_cesta.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.button_najkratsia_cesta.setAutoFillBackground(False)
        self.button_najkratsia_cesta.setObjectName("button_najkratsia_cesta")
        self.horizontalLayout_3.addWidget(self.button_najkratsia_cesta)
        self.button_najkratsia_cesta.setStyleSheet("""
                            QPushButton {
                                background-color:#5ddeb0;
                                border-style:outset;
                                border-radius:10px
                            }
                            QPushButton:hover {
                                background-color:#48cf9f
                            }
                            """)

    # LABEL CESTA
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_cesta = QtWidgets.QLabel(self.centralwidget)
        self.label_cesta.setEnabled(False)
        self.label_cesta.setGeometry(QtCore.QRect(10, 300, 641, 71))
        self.label_cesta.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cesta.setObjectName("label_cesta")
        self.label_cesta.setWordWrap(True)

    # LABEL DLZKA CESTY
        self.label_dlzka_cesty = QtWidgets.QLabel(self.centralwidget)
        self.label_dlzka_cesty.setEnabled(False)
        self.label_dlzka_cesty.setGeometry(QtCore.QRect(10, 260, 641, 41))
        self.label_dlzka_cesty.setAutoFillBackground(False)
        self.label_dlzka_cesty.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dlzka_cesty.setObjectName("label_dlzka_cesty")

        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(660, 60, 641, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

    # BUTTON KRUSKAL 1
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.button_kruskal1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_kruskal1.sizePolicy().hasHeightForWidth())
        self.button_kruskal1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_kruskal1.setFont(font)
        self.button_kruskal1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.button_kruskal1.setAutoFillBackground(False)
        self.button_kruskal1.setObjectName("button_kruskal1")
        self.horizontalLayout_4.addWidget(self.button_kruskal1)
        self.button_kruskal1.setStyleSheet("""
                            QPushButton {
                                background-color:#5ddeb0;
                                border-style:outset;
                                border-radius:10px
                            }
                            QPushButton:hover {
                                background-color:#48cf9f
                            }
                            """)

        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(660, 610, 641, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

    # BUTTON KRUSKAL 2
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.button_kruskal2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_kruskal2.sizePolicy().hasHeightForWidth())
        self.button_kruskal2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_kruskal2.setFont(font)
        self.button_kruskal2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.button_kruskal2.setAutoFillBackground(False)
        self.button_kruskal2.setObjectName("button_kruskal2")
        self.horizontalLayout_5.addWidget(self.button_kruskal2)
        self.button_kruskal2.setStyleSheet("""
                            QPushButton {
                                background-color:#5ddeb0;
                                border-style:outset;
                                border-radius:10px
                            }
                            QPushButton:hover {
                                background-color:#48cf9f
                            }
                            """)

        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(730, 10, 561, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.label_typkostry = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_typkostry.setFont(font)
        self.label_typkostry.setObjectName("label_typkostry")
        self.horizontalLayout_6.addWidget(self.label_typkostry)

    # COMBO BOX: TYP KOSTRY
        self.comboBox_typkostry = QtWidgets.QComboBox(self.horizontalLayoutWidget_6)
        self.comboBox_typkostry.setAutoFillBackground(True)
        self.comboBox_typkostry.setEditable(False)
        self.comboBox_typkostry.addItem("")
        self.comboBox_typkostry.addItem("")
        self.comboBox_typkostry.setObjectName("comboBox_typkostry")
        self.horizontalLayout_6.addWidget(self.comboBox_typkostry)

    # LABEL CENA KOSTRY 1
        self.label_cenakostry1 = QtWidgets.QLabel(self.centralwidget)
        self.label_cenakostry1.setEnabled(False)
        self.label_cenakostry1.setGeometry(QtCore.QRect(660, 120, 641, 31))
        self.label_cenakostry1.setAutoFillBackground(False)
        self.label_cenakostry1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cenakostry1.setObjectName("label_cenakostry1")

    # LABEL CENA KOSTRY 2
        self.label_cenakostry2 = QtWidgets.QLabel(self.centralwidget)
        self.label_cenakostry2.setEnabled(False)
        self.label_cenakostry2.setGeometry(QtCore.QRect(660, 661, 641, 31))
        self.label_cenakostry2.setAutoFillBackground(False)
        self.label_cenakostry2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cenakostry2.setObjectName("label_cenakostry2")

    # OBRAZOK KRUSKAL 2
        self.obrazok_kruskal2 = QtWidgets.QLabel(self.centralwidget)
        self.obrazok_kruskal2.setGeometry(QtCore.QRect(10, 370, 641, 440))
        self.obrazok_kruskal2.setText("")
        self.obrazok_kruskal2.setPixmap(QtGui.QPixmap("kruskal1.png"))
        self.obrazok_kruskal2.setScaledContents(True)
        self.obrazok_kruskal2.setObjectName("obrazok_kruskal2")

    # OBRAZOK KRUSKAL 1
        self.obrazok_kruskal1 = QtWidgets.QLabel(self.centralwidget)
        self.obrazok_kruskal1.setGeometry(QtCore.QRect(660, 161, 641, 440))
        self.obrazok_kruskal1.setText("")
        self.obrazok_kruskal1.setPixmap(QtGui.QPixmap("kruskal1.png"))
        self.obrazok_kruskal1.setScaledContents(True)
        self.obrazok_kruskal1.setObjectName("obrazok_kruskal1")

    # LABEL CISELNIKY
        self.label_ciselnik1 = QtWidgets.QLabel(self.centralwidget)
        self.label_ciselnik1.setGeometry(QtCore.QRect(250, 150, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setFamily("Bahnschrift Light")
        self.label_ciselnik1.setFont(font)
        self.label_ciselnik1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ciselnik1.setObjectName("label_ciselnik1")
        self.label_ciselnik2 = QtWidgets.QLabel(self.centralwidget)
        self.label_ciselnik2.setGeometry(QtCore.QRect(510, 150, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setFamily("Bahnschrift Light")
        self.label_ciselnik2.setFont(font)
        self.label_ciselnik2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ciselnik2.setObjectName("label_ciselnik2")

    # BUTTON POTVRD
        self.button_potvrd = QtWidgets.QPushButton(self.centralwidget)
        self.button_potvrd.setGeometry(QtCore.QRect(350, 10, 91, 41))
        self.button_potvrd.setObjectName("button_potvrd")
        self.button_potvrd.setStyleSheet("""
                            QPushButton {
                                background-color:#5ddeb0;
                                border-style:outset;
                                border-radius:10px
                            }
                            QPushButton:hover {
                                background-color:#48cf9f
                            }
                            """)

        NetworkX.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NetworkX)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1311, 21))
        self.menubar.setObjectName("menubar")
        NetworkX.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(NetworkX)
        self.statusbar.setObjectName("statusbar")
        NetworkX.setStatusBar(self.statusbar)


        self.button_najkratsia_cesta.clicked.connect(self.clicked_najkratsia_cesta)
        self.button_kruskal1.clicked.connect(self.clicked_kruskal1)
        self.button_kruskal2.clicked.connect(self.clicked_kruskal2)
        self.slider1.valueChanged.connect(self.slide_slider1)
        self.slider2.valueChanged.connect(self.slide_slider2)
        self.button_potvrd.clicked.connect(self.clicked_potvrd)

        self.retranslateUi(NetworkX)
        QtCore.QMetaObject.connectSlotsByName(NetworkX)

    def retranslateUi(self, NetworkX):
        _translate = QtCore.QCoreApplication.translate
        NetworkX.setWindowTitle(_translate("NetworkX", "NetworkX"))
        self.comboBox_dataset.setItemText(0, _translate("NetworkX", "TEST_mini.hrn"))
        self.comboBox_dataset.setItemText(1, _translate("NetworkX", "Strakonice.hrn"))
        self.comboBox_typkostry.setItemText(0, _translate("NetworkX", "Najlacnejsia"))
        self.comboBox_typkostry.setItemText(1, _translate("NetworkX", "Najdrahsia"))
        self.label_dataset.setText(_translate("NetworkX", "Vyberte dataset"))
        self.label_rozmedzie.setText(_translate("NetworkX", "Vyberte 2 vrcholy"))
        self.button_najkratsia_cesta.setText(_translate("NetworkX", "Najkratsia cesta medzi zvolenymi vrcholmi"))
        self.label_cesta.setText(_translate("NetworkX", ""))
        self.label_dlzka_cesty.setText(_translate("NetworkX", ""))
        self.button_kruskal1.setText(_translate("NetworkX", "Kruskal I"))
        self.button_kruskal2.setText(_translate("NetworkX", "Kruskal II"))
        self.label_typkostry.setText(_translate("NetworkX", "Vyberte typ hladanej kostry"))
        self.label_cenakostry1.setText(_translate("NetworkX", ""))
        self.label_cenakostry2.setText(_translate("NetworkX", ""))
        self.label_ciselnik1.setText(_translate("NetworkX", "1"))
        self.label_ciselnik2.setText(_translate("NetworkX", "1"))
        self.button_potvrd.setText(_translate("NetworkX", "Potvrdte"))

    # AKCIE

    def clicked_potvrd(self):
        if self.comboBox_dataset.currentText() == "TEST_mini.hrn":
            self.slider1.setMaximum(13)
            self.slider2.setMaximum(13)
        else:
            self.slider1.setMaximum(627)
            self.slider1.setTickInterval(50)
            self.slider2.setMaximum(627)
            self.slider2.setTickInterval(50)

    def slide_slider1(self, value):
        self.label_ciselnik1.setText(str(value))

    def slide_slider2(self, value):
        self.label_ciselnik2.setText(str(value))

    def clicked_najkratsia_cesta(self):
        graf = LabelSet.NajdiCestu(self.slider1.value(), self.slider2.value(), self.comboBox_dataset.currentText())
        self.label_dlzka_cesty.setText('Dlzka cesty z vrchola ' + str(self.slider1.value()) + ' do vrchola ' + str(self.slider2.value()) + ' je ' + LabelSet.Vypis(self.slider2.value(), graf))
        self.label_cesta.setText('Cesta vedie cez vrcholy ' + LabelSet.Vypis2(self.slider2.value(), graf))

    def clicked_kruskal1(self):
        if self.comboBox_typkostry.currentText() == "Najlacnejsia":
            kostra = Kruskal.KruskalI(False, self.comboBox_dataset.currentText())
            self.label_cenakostry1.setText('Cena kostry je ' + Kruskal.Vypis(kostra))
        else:
            kostra = Kruskal.KruskalI(True, self.comboBox_dataset.currentText())
            self.label_cenakostry1.setText('Cena kostry je ' + Kruskal.Vypis(kostra))
        self.obrazok_kruskal1.setPixmap(QtGui.QPixmap("obrazok.png"))

    def clicked_kruskal2(self):
        if self.comboBox_typkostry.currentText() == "Najlacnejsia":
            kostra = Kruskal.KruskalII(False, self.comboBox_dataset.currentText())
            self.label_cenakostry2.setText('Cena kostry je ' + Kruskal.Vypis(kostra))
        else:
            kostra = Kruskal.KruskalII(True, self.comboBox_dataset.currentText())
            self.label_cenakostry2.setText('Cena kostry je ' + Kruskal.Vypis(kostra))
        self.obrazok_kruskal2.setPixmap(QtGui.QPixmap("obrazok.png"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NetworkX = QtWidgets.QMainWindow()
    ui = Ui_NetworkX()
    ui.setupUi(NetworkX)
    NetworkX.show()
    sys.exit(app.exec_())
