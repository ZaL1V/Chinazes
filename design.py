

import minecraft_launcher_lib
from PyQt5 import QtCore, QtGui, QtWidgets

from .main import minecraft_directory

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(600, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget.setStyleSheet("background-image: url(\"D:/PROJECTS/Project/App/Chinazes/images/OIG2.jpg\");\n"
"background-size: 600px 600px;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setStyleSheet("QWidget {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #f7f7f7,  /* Світліший світло-сірий колір */\n"
"        stop:1 #dcdcdc   /* Світло-сірий колір */\n"
"    );\n"
"}\n"
"\n"
"/* Стиль для прогрес-бару */\n"
"QProgressBar {\n"
"    border: 2px solid #888888;  /* Темніша рамка */\n"
"    border-radius: 10px;        /* Згладжені кути */\n"
"    background-color: #e0e0e0;  /* Світло-сірий фон прогрес-бару */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #888888, \n"
"        stop:1 #555555\n"
"    );\n"
"    border-radius: 10px;        /* Згладжені кути для частини */\n"
"}\n"
"\n"
"/* Стиль для кнопки */\n"
"QPushButton {\n"
"    background-color: #7a7a7a;  /* Темно-сірий фон кнопки */\n"
"    color: white;                /* Колір тексту */\n"
"    border: 2px solid #5a5a5a;  /* Темніша рамка */\n"
"    border-radius: 10px;        /* Згладжені кути */\n"
"    padding: 10px;              /* Внутрішні відступи */\n"
"    font-size: 16px;            /* Розмір шрифту */\n"
"    font-weight: bold;          /* Жирний шрифт */\n"
"    transition: background-color 0.3s, color 0.3s;  /* Анімація переходу */\n"
"    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);  /* Тінь для глибини */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #646464;  /* Колір при наведенні */\n"
"    color: #ffffff;              /* Колір тексту при наведенні */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #505050;   /* Темніший колір при натисканні */\n"
"}\n"
"\n"
"/* Стиль для поля вводу юзернейма */\n"
"QLineEdit {\n"
"    background-color: #ffffff;   /* Білий фон для поля вводу */\n"
"    color: #333333;              /* Темний колір тексту */\n"
"    border: 2px solid #888888;   /* Темніша рамка */\n"
"    border-radius: 10px;        /* Згладжені кути */\n"
"    padding: 10px;              /* Внутрішні відступи */\n"
"    font-size: 16px;            /* Розмір шрифту */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #555555;   /* Темніша рамка при фокусі */\n"
"    background-color: #f0f0f0;   /* Світло-сірий фон при фокусі */\n"
"}")
        self.Username.setReadOnly(False)
        self.Username.setObjectName("lineEdit")
        self.Username.setPlaceholderText('Username')
        self.verticalLayout_2.addWidget(self.Username)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    border: 2px solid #0056b3;\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #e0e0e0, stop:1 #d0d0d0);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0078d7, stop:1 #0056b3);\n"
"    border-radius: 10px;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setStyleSheet("QWidget {\n"
"    background: qlineargradient(  /* Градієнт для фону вікна */\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #f0f0f0,  /* Світло-сірий колір */\n"
"        stop:1 #b0b0b0   /* Темніший сірий колір */\n"
"    );\n"
"}\n"
"\n"
"/* Стиль для прогрес-бару */\n"
"QProgressBar {\n"
"    border: 2px solid #888888;  /* Темніша рамка */\n"
"    border-radius: 10px;        /* Згладжені кути */\n"
"    background-color: #dcdcdc;  /* Світло-сірий фон прогрес-бару */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(  /* Градієнт для частини прогрес-бару */\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #888888, \n"
"        stop:1 #555555\n"
"    );\n"
"    border-radius: 10px;        /* Згладжені кути для частини */\n"
"}\n"
"\n"
"/* Стиль для кнопки */\n"
"QPushButton {\n"
"    background-color: #7a7a7a;  /* Темно-сірий фон кнопки */\n"
"    color: white;                /* Колір тексту */\n"
"    border: 2px solid #5a5a5a;  /* Темніша рамка */\n"
"    border-radius: 10px;        /* Згладжені кути */\n"
"    padding: 10px;              /* Внутрішні відступи */\n"
"    font-size: 16px;            /* Розмір шрифту */\n"
"    font-weight: bold;          /* Жирний шрифт */\n"
"    transition: background-color 0.3s, color 0.3s;  /* Анімація переходу */\n"
"    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);  /* Тінь для глибини */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #646464;  /* Колір при наведенні */\n"
"    color: #ffffff;              /* Колір тексту при наведенні */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #505050;   /* Темніший колір при натисканні */\n"
"}")
        self.start_button.setObjectName("pushButton")
        self.start_button.setText('Start')
        self.verticalLayout_2.addWidget(self.start_button)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
