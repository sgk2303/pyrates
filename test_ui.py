from PyQt5 import QtCore, QtGui, QtWidgets


client = pymongo.MongoClient("mongodb+srv://sgk2303:<password>@cluster0.dsp9o.mongodb.net/?retryWrites=true&w=majority")
db = client.test


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(469, 244)
        MainWindow.setStyleSheet("background-color: rgb(23, 23, 23);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 461, 31))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 47, 31))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Downloads/plasticpyrolysisplantindia-removebg-preview.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.team_name = QtWidgets.QLabel(self.frame)
        self.team_name.setGeometry(QtCore.QRect(170, 0, 131, 31))
        self.team_name.setStyleSheet("color: rgb(255, 137, 3);\n"
"font-family: \'Staatliches\', cursive;")
        self.team_name.setAlignment(QtCore.Qt.AlignCenter)
        self.team_name.setObjectName("team_name")
        self.main_value_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_value_frame.setGeometry(QtCore.QRect(10, 30, 111, 201))
        self.main_value_frame.setObjectName("main_value_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_value_frame)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.reactor_tem = QtWidgets.QLabel(self.main_value_frame)
        self.reactor_tem.setStyleSheet("background-color: rgb(18, 18, 18);\n"
"color:  rgb(255, 137, 3);\n"
"border-radius: 15px")
        self.reactor_tem.setAlignment(QtCore.Qt.AlignCenter)
        self.reactor_tem.setObjectName("reactor_tem")
        self.verticalLayout.addWidget(self.reactor_tem)
        self.catalyst_tem = QtWidgets.QLabel(self.main_value_frame)
        self.catalyst_tem.setStyleSheet("background-color: rgb(18, 18, 18);\n"
"color:  rgb(255, 137, 3);\n"
"border-radius: 15px")
        self.catalyst_tem.setAlignment(QtCore.Qt.AlignCenter)
        self.catalyst_tem.setObjectName("catalyst_tem")
        self.verticalLayout.addWidget(self.catalyst_tem)
        self.motor_1 = QtWidgets.QLabel(self.main_value_frame)
        self.motor_1.setStyleSheet("background-color: rgb(18, 18, 18);\n"
"color:  rgb(255, 137, 3);\n"
"border-radius: 15px")
        self.motor_1.setAlignment(QtCore.Qt.AlignCenter)
        self.motor_1.setObjectName("motor_1")
        self.verticalLayout.addWidget(self.motor_1)
        self.motor_2 = QtWidgets.QLabel(self.main_value_frame)
        self.motor_2.setStyleSheet("background-color: rgb(18, 18, 18);\n"
"color:  rgb(255, 137, 3);\n"
"border-radius: 15px")
        self.motor_2.setAlignment(QtCore.Qt.AlignCenter)
        self.motor_2.setObjectName("motor_2")
        self.verticalLayout.addWidget(self.motor_2)
        self.reactor_induction_2 = QtWidgets.QLabel(self.main_value_frame)
        self.reactor_induction_2.setStyleSheet("background-color: rgb(18, 18, 18);\n"
"color:  rgb(255, 137, 3);\n"
"border-radius: 15px")
        self.reactor_induction_2.setAlignment(QtCore.Qt.AlignCenter)
        self.reactor_induction_2.setObjectName("reactor_induction_2")
        self.verticalLayout.addWidget(self.reactor_induction_2)
        self.feed_pressure_frame = QtWidgets.QFrame(self.centralwidget)
        self.feed_pressure_frame.setGeometry(QtCore.QRect(150, 120, 81, 111))
        self.feed_pressure_frame.setObjectName("feed_pressure_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.feed_pressure_frame)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.motor_1_indi = QtWidgets.QLCDNumber(self.feed_pressure_frame)
        self.motor_1_indi.setStyleSheet("color:  rgb(255, 137, 3);\n"
"border-color:  rgb(255, 137, 3);")
        self.motor_1_indi.setObjectName("motor_1_indi")
        self.verticalLayout_2.addWidget(self.motor_1_indi)
        self.motor_2_indi = QtWidgets.QLCDNumber(self.feed_pressure_frame)
        self.motor_2_indi.setStyleSheet("color:  rgb(255, 137, 3);\n"
"border-color:  rgb(255, 137, 3);")
        self.motor_2_indi.setObjectName("motor_2_indi")
        self.verticalLayout_2.addWidget(self.motor_2_indi)
        self.reactor_induction = QtWidgets.QLCDNumber(self.feed_pressure_frame)
        self.reactor_induction.setObjectName("reactor_induction")
        self.verticalLayout_2.addWidget(self.reactor_induction)
        self.motors_frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.motors_frame_2.setGeometry(QtCore.QRect(250, 120, 91, 101))
        self.motors_frame_2.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.motors_frame_2.setObjectName("motors_frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.motors_frame_2)
        self.verticalLayout_3.setSpacing(13)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pressure_label = QtWidgets.QLabel(self.motors_frame_2)
        self.pressure_label.setStyleSheet("background-color: rgb(18, 18, 18);\n"
"color:  rgb(255, 137, 3);\n"
"border-radius: 15px")
        self.pressure_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pressure_label.setObjectName("pressure_label")
        self.verticalLayout_3.addWidget(self.pressure_label)
        self.Feed_label = QtWidgets.QLabel(self.motors_frame_2)
        self.Feed_label.setStyleSheet("background-color: rgb(18, 18, 18);\n"
"color:  rgb(255, 137, 3);\n"
"border-radius: 15px")
        self.Feed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Feed_label.setObjectName("Feed_label")
        self.verticalLayout_3.addWidget(self.Feed_label)
        self.motors_frame = QtWidgets.QFrame(self.centralwidget)
        self.motors_frame.setGeometry(QtCore.QRect(360, 120, 91, 101))
        self.motors_frame.setObjectName("motors_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.motors_frame)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pressure_value = QtWidgets.QLCDNumber(self.motors_frame)
        self.pressure_value.setObjectName("pressure_value")
        self.verticalLayout_4.addWidget(self.pressure_value)
        self.Feed_rate = QtWidgets.QLCDNumber(self.motors_frame)
        self.Feed_rate.setStyleSheet("color:  rgb(255, 137, 3);\n"
"border-color:  rgb(255, 137, 3);")
        self.Feed_rate.setObjectName("Feed_rate")
        self.verticalLayout_4.addWidget(self.Feed_rate)
        self.progress_bar_frame = QtWidgets.QFrame(self.centralwidget)
        self.progress_bar_frame.setGeometry(QtCore.QRect(140, 40, 111, 81))
        self.progress_bar_frame.setObjectName("progress_bar_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.progress_bar_frame)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tem_rt_bar = QtWidgets.QProgressBar(self.progress_bar_frame)
        self.tem_rt_bar.setStyleSheet("background-color: rgb(107, 107, 107);\n"
"border-color: rgb(99, 99, 99);\n"
"")
        self.tem_rt_bar.setMaximum(10)
        self.tem_rt_bar.setProperty("value", 1)
        self.tem_rt_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.tem_rt_bar.setTextVisible(True)
        self.tem_rt_bar.setObjectName("tem_rt_bar")
        self.verticalLayout_5.addWidget(self.tem_rt_bar)
        self.tem_rt_bar_2 = QtWidgets.QProgressBar(self.progress_bar_frame)
        self.tem_rt_bar_2.setStyleSheet("background-color: rgb(107, 107, 107);\n"
"border-color: rgb(99, 99, 99);\n"
"")
        self.tem_rt_bar_2.setMaximum(10)
        self.tem_rt_bar_2.setProperty("value", 1)
        self.tem_rt_bar_2.setAlignment(QtCore.Qt.AlignCenter)
        self.tem_rt_bar_2.setTextVisible(True)
        self.tem_rt_bar_2.setObjectName("tem_rt_bar_2")
        self.verticalLayout_5.addWidget(self.tem_rt_bar_2)
        self.hmi_feed_enter = QtWidgets.QSpinBox(self.centralwidget)
        self.hmi_feed_enter.setGeometry(QtCore.QRect(260, 50, 91, 22))
        self.hmi_feed_enter.setStyleSheet("background-color: rgb(107, 107, 107);\n"
"color:  rgb(255, 137, 3);\n"
"border-radius: 15px")
        self.hmi_feed_enter.setMaximum(200)
        self.hmi_feed_enter.setSingleStep(5)
        self.hmi_feed_enter.setObjectName("hmi_feed_enter")
        self.hmi_temperature_enter = QtWidgets.QSpinBox(self.centralwidget)
        self.hmi_temperature_enter.setGeometry(QtCore.QRect(260, 90, 91, 22))
        self.hmi_temperature_enter.setStyleSheet("background-color: rgb(107, 107, 107);\n"
"color:  rgb(255, 137, 3);\n"
"border-radius: 15px")
        self.hmi_temperature_enter.setMaximum(1600)
        self.hmi_temperature_enter.setSingleStep(5)
        self.hmi_temperature_enter.setObjectName("hmi_temperature_enter")
        self.set_feed_btn = QtWidgets.QPushButton(self.centralwidget)
        self.set_feed_btn.setGeometry(QtCore.QRect(370, 50, 81, 23))
        self.set_feed_btn.setStyleSheet("background-color: rgb(18, 18, 18);\n"
"color:  rgb(255, 137, 3);\n"
"border-radius: 15px\n"
"")
        self.set_feed_btn.setObjectName("set_feed_btn")
        self.set_tempbtn = QtWidgets.QPushButton(self.centralwidget)
        self.set_tempbtn.setGeometry(QtCore.QRect(374, 90, 81, 23))
        self.set_tempbtn.setStyleSheet("background-color: rgb(18, 18, 18);\n"
"color:  rgb(255, 137, 3);\n"
"border-radius: 15px")
        self.set_tempbtn.setObjectName("set_tempbtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.team_name.setText(_translate("MainWindow", "PyRox Monitor"))
        self.reactor_tem.setText(_translate("MainWindow", "Reactor Tem"))
        self.catalyst_tem.setText(_translate("MainWindow", "Catalyst Tem"))
        self.motor_1.setText(_translate("MainWindow", "Motor 1"))
        self.motor_2.setText(_translate("MainWindow", "Motor 1"))
        self.reactor_induction_2.setText(_translate("MainWindow", "Induction"))
        self.pressure_label.setText(_translate("MainWindow", "Pressure"))
        self.Feed_label.setText(_translate("MainWindow", "Feed"))
        self.set_feed_btn.setText(_translate("MainWindow", "Set Feed"))
        self.set_tempbtn.setText(_translate("MainWindow", "Set Temprature"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
