import os
import json
from PyQt5.QtCore import QTimer
from random_username.generate import generate_username
import minecraft_launcher_lib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QSize, Qt
from minecraft_launcher import launch_minecraft


class LauncherThread(QtCore.QThread):
    
    launch_setup_signal = pyqtSignal(str, str)
    progress_update_signal = pyqtSignal(int, int, str)
    process_finished_signal = pyqtSignal()
    state_update_signal = pyqtSignal(bool)

    progress = 0
    progress_max = 0
    progress_label = ''

    def __init__(self, username):
        super().__init__()
        self.launch_setup_signal.connect(self.launch_setup)
        self.username = username

    def launch_setup(self, version_id, username):
        self.version_id = version_id
        self.username = username
    
    def update_progress_label(self, value):
        self.progress_label = value
        self.progress_update_signal.emit(self.progress, self.progress_max, self.progress_label)
    def update_progress(self, value):
        self.progress = value
        self.progress_update_signal.emit(self.progress, self.progress_max, self.progress_label)
    def update_progress_max(self, value):
        self.progress_max = value
        self.progress_update_signal.emit(self.progress, self.progress_max, self.progress_label)

    def run(self):
        self.state_update_signal.emit(True)



        self.process = launch_minecraft(callback={
            'setStatus': self.update_progress_label,
            'setProgress': self.update_progress,
            'setMax': self.update_progress_max
        })
        
        self.process.finished.connect(self.on_process_finished)
        self.state_update_signal.emit(False)


class Ui_MainWindow(object):

    def start_minecraft(self):
        new_username = self.Username.text()
        if new_username == '':
            new_username = generate_username()[0]
        with open('options.json', 'r+') as f:
            options = json.load(f)
            options['username'] = new_username
            f.seek(0)
            json.dump(options, f, indent=4)
            f.truncate()
        
        self.Username.hide()
        self.start_button.hide()
        self.launcher_thread = LauncherThread(new_username)
        self.launcher_thread.state_update_signal.connect(self.state_update)
        self.launcher_thread.progress_update_signal.connect(self.update_progress)
        self.launcher_thread.start()

        self.progressBar.setValue(0)
        self.progressBar.show()
        
        
    def state_update(self, value):
        self.start_button.setDisabled(value)
        self.start_progress_label.setVisible(value)
        self.progressBar.setVisible(value)
        
    def update_progress(self, progress, max_progress, label):
        self.progressBar.setValue(progress)
        self.progressBar.setMaximum(max_progress)
        self.start_progress_label.setText(label)
        if "Installation complete" in label:
            print("Closing launcher...")
            QtCore.QTimer.singleShot(10000, MainWindow.hide)
        
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
        with open('options.json', 'r') as f:
            person_option = json.load(f)
            self.Username.setText(person_option.get('username', ''))
        self.verticalLayout_2.addWidget(self.Username)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.start_progress_label = QtWidgets.QLabel(self.centralwidget)
        self.start_progress_label.setText('')
        self.start_progress_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.start_progress_label.setStyleSheet("""
            QLabel {
                color: white;  /* Колір тексту */
                background: none;  /* Вимкнути фон */
                padding: 0;  /* Без внутрішніх відступів */
            }
        """)
        self.start_progress_label.setVisible(False)
        self.verticalLayout_2.addWidget(self.start_progress_label, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)  # Центруємо по горизонталі
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setStyleSheet("""
                                        QLabel {
                                            font-size: 8px;
                                            color: white;  /* Колір тексту */
                                        }
                                    """)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setVisible(False)
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
        self.start_button.clicked.connect(self.start_minecraft)


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