from PyQt5 import QtCore, QtGui, QtWidgets
from model import text2voice

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SavepathWidget = QtWidgets.QWidget(self.centralwidget)
        self.SavepathWidget.setGeometry(QtCore.QRect(60, 20, 681, 51))
        self.SavepathWidget.setObjectName("SavepathWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.SavepathWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.savepath = QtWidgets.QTextEdit(self.SavepathWidget)
        self.savepath.setObjectName("savepath")
        self.horizontalLayout.addWidget(self.savepath)
        self.confirmsave = QtWidgets.QPushButton(self.SavepathWidget)
        self.confirmsave.setObjectName("confirmsave")
        self.horizontalLayout.addWidget(self.confirmsave)
        self.Translator = QtWidgets.QWidget(self.centralwidget)
        self.Translator.setGeometry(QtCore.QRect(420, 90, 321, 421))
        self.Translator.setObjectName("Translator")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Translator)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.translateText = QtWidgets.QTextEdit(self.Translator)
        self.translateText.setObjectName("translateText")
        self.verticalLayout_2.addWidget(self.translateText)
        self.saveaudio = QtWidgets.QPushButton(self.Translator)
        self.saveaudio.setObjectName("saveaudio")
        self.verticalLayout_2.addWidget(self.saveaudio)
        self.Input = QtWidgets.QWidget(self.centralwidget)
        self.Input.setGeometry(QtCore.QRect(60, 90, 311, 421))
        self.Input.setObjectName("Input")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Input)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputText = QtWidgets.QTextEdit(self.Input)
        self.inputText.setObjectName("inputText")
        self.verticalLayout.addWidget(self.inputText)
        self.translateButton = QtWidgets.QPushButton(self.Input)
        self.translateButton.setObjectName("translateButton")
        self.verticalLayout.addWidget(self.translateButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuStart = QtWidgets.QMenu(self.menubar)
        self.menuStart.setObjectName("menuStart")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLog_In = QtWidgets.QAction(MainWindow)
        self.actionLog_In.setObjectName("actionLog_In")
        self.menuStart.addAction(self.actionLog_In)
        self.menubar.addAction(self.menuStart.menuAction())

        #change ui
        self.savepath.setText("Please input save path")      # 设置输入文本
        self.inputText.setText("Please input text wanted to be translated")
        self.translateText.setText("Please input text wanted to be transfer to audio")
        self.saveaudio.clicked.connect(self.saveAudioHelper)
        #until there

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text to Speech"))
        self.confirmsave.setText(_translate("MainWindow", "Confirm"))
        self.saveaudio.setText(_translate("MainWindow", "SaveAudio"))
        self.translateButton.setText(_translate("MainWindow", "Translate"))
        self.menuStart.setTitle(_translate("MainWindow", "Start"))
        self.actionLog_In.setText(_translate("MainWindow", "Log In"))

    #add function there
    def saveAudioHelper(self):
        #set subscription key
        subscription_key = "YOUR_KEY_HERE"
        #get token
        accessToken = text2voice.getToken(subscription_key)

        savepath = self.savepath.toPlainText()
        text = self.translateText.toPlainText()
        text2voice.saveAudio(savepath, text, accessToken)

    #end