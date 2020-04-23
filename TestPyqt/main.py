import os
import platform
import sys
from pathlib import Path

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut, QWidget, QColorDialog, QLabel, QLineEdit, QPushButton

print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__, __name__, str(__package__)))

from res.ui import Ui_MainWindow
from res.ui import Ui_MainWindow2
from res.ui import Ui_MainWindow3
from res.ui import Ui_MainWindow4
from util import printHello


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setFont(QtGui.QFont('Arial', 10))
        rect = self.ui.label.geometry()  # get position of label
        self.ui.label.setGeometry(QtCore.QRect(rect.left(), rect.top() + 50, 600, 200))
        self.ui.label.setText('Nothing')
        self.ui.lineEdit.setText('Welcome!')

        self.ui.pushButton.setText('Display')

        self.ui.pushButton.clicked.connect(self.button_clicked)

        # MainWindow Title
        self.setWindowTitle('QIcon Test!!')

        # StatusBar
        self.statusBar().showMessage('TEST Again!!!')
        self.statusBar().setStyleSheet("color: red")
        # self.ui.statusbar.showMessage('TEST Again!!!') # also work

        # Set Window Icon
        self.setWindowIcon(QtGui.QIcon(':/image/Python_PyQt5.png'))

        # Pixmap
        image = QtGui.QPixmap()
        image.load(':/image/Python_PyQt5.png')
        image = image.scaled(self.width(), self.height())

        # Palette
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(image))
        self.setPalette(palette)

        # Hide Window Title
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # Menu
        # self.ui.retranslateUi(self) # this line will cause window title to overwrite setWindowTitle above
        self.ui.actionClose.setShortcut('Ctrl+Q')
        self.ui.actionClose.triggered.connect(self.exit)
        self.ui.actionClose.setIcon(QtGui.QIcon(':/image/Cancel.png'))

        # ToolBar
        self.ui.toolButton.setShortcut('Ctrl+E')
        self.ui.toolButton.setIcon(QtGui.QIcon(':/image/Cancel.png'))
        self.ui.toolButton.clicked.connect(self.exit)

        # ToolBar2
        self.ui.toolButton_2.clicked.connect(self.onMenuAbout)

        # translator
        self.ui.trans = QTranslator()
        self.ui.btnChinese.clicked.connect(self.trigger_zh_tw)
        self.ui.btnEnglish.clicked.connect(self.trigger_english)

    def button_clicked(self):
        text = self.ui.lineEdit.text()
        self.ui.label.setText(text)
        self.ui.lineEdit.clear()

        # Call python script
        # os.system("printHello.py")
        # os.subprocess.Popen("printHello.py", shell=True)

        printHello.runscript()

    def exit(self):
        app.exit()

    def onMenuAbout(self):
        QCoreApplication.setApplicationName('TestPyqt')
        QCoreApplication.setApplicationVersion('1.0.0')
        app_name = QCoreApplication.applicationName()
        app_version = QCoreApplication.applicationVersion()
        title = self.tr('About %s') % (app_name)
        text = self.tr("%s %s\n\nThe test app\n\n"
                       ) % (app_name, app_version)
        text += self.tr('Platform: %s\n') % (platform.platform())
        text += self.tr('Home data path: %s\n') % (Path.home())
        text += self.tr('Application data path: %s\n') % (os.path.dirname(os.path.abspath(__file__)))
        text += self.tr('\n')
        text += self.tr('Python: %s\n') % platform.python_version()
        text += self.tr('PyQt5: %s\n') % QtCore.PYQT_VERSION_STR
        QtWidgets.QMessageBox.about(self, title, text)

    def trigger_english(self):
        print("[MainWindow] Change to English")
        self.ui.trans.load("res/ui/lang_en")
        _app = QCoreApplication.instance()
        _app.installTranslator(self.ui.trans)
        try:
            self.ui.retranslateUi(self)
        except Exception as e:
            print(e)

    def trigger_zh_tw(self):
        print("[MainWindow] Change to zh_tw")
        self.ui.trans.load("res/ui/lang_zh_tw")
        _app = QCoreApplication.instance()
        _app.installTranslator(self.ui.trans)
        try:
            self.ui.retranslateUi(self)
        except Exception as e:
            print(e)

class MainWindow2(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow2, self).__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)

        # ProgressBar
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(99)
        self.ui.progressBar.setValue(0)

        # HorizontalSlider
        self.ui.horizontalSlider.valueChanged.connect(self.sliderValue)

        # Dial
        self.ui.dial.setRange(0, 100)
        self.ui.dial.setNotchesVisible(True)
        self.ui.dial.valueChanged.connect(self.dialValue)

        # ComboBox
        choices = ['1', '2', '3', '4']
        self.ui.comboBox.addItems(choices)
        self.ui.comboBox.currentIndexChanged.connect(self.initComboBox)
        self.initComboBox()

    def sliderValue(self):
        self.ui.progressBar.setValue(self.ui.horizontalSlider.value())

    def dialValue(self):
        self.ui.progressBar.setValue(self.ui.dial.value())

    def initComboBox(self):
        self.ui.label_2.setText('你目前選擇的是：%s' % self.ui.comboBox.currentText())


class MainWindow3(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow3, self).__init__()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self)
        self.ui.label.setScaledContents(True)

        # Hide
        self.ui.pushButton_2.hide()

        # Event
        self.ui.pushButton.clicked.connect(self.showButtonEvent)

    def showButtonEvent(self):
        self.ui.pushButton_2.show()


monthConvert = {'一': '01', '二': '02', '三': '03', '四': '04', '五': '05', '六': '06', '七': '07', '八': '08',
                '九': '09', '十': '10', '十一': '11', '十二': '12'}


class MainWindow4(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow4, self).__init__()
        self.ui = Ui_MainWindow4()
        self.ui.setupUi(self)
        self.setWindowTitle('Calendar')

        # QTimer
        self.timer = QTimer()

        # QPushButton
        self.ui.pushButton.clicked.connect(self.timeGo)
        self.ui.pushButton_2.clicked.connect(self.timeStop)

        # Other
        self.timer.timeout.connect(self.LCDEvent)
        self.s = 0

        # Calender
        self.ui.calendarWidget.selectionChanged.connect(self.calendarEvent)

        # Shortcut
        self.ctrl_n = QShortcut(QKeySequence("Ctrl+n"), self)
        self.ctrl_n.activated.connect(self.displayEventCtrlN)
        self.space = QShortcut(QKeySequence("Space"), self)
        self.space.activated.connect(self.displayEventSpace)

        # Mouse Event

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.ui.label.setText('The number you selected: Left!')

        if event.button() == Qt.RightButton:
            self.ui.label.setText('The number you selected: Right!')

    def displayEventCtrlN(self):
        self.ui.label.setText('The number you selected: Ctrl+n')

    def displayEventSpace(self):
        self.ui.label.setText('The number you selected: Space')

    def timeGo(self):
        self.timer.start(100)

    def timeStop(self):
        self.timer.stop()

    def LCDEvent(self):
        self.s += 1
        self.ui.lcdNumber.display(self.s)

    def calendarEvent(self):
        date = self.ui.calendarWidget.selectedDate().toString().split(' ')
        weekday, month, day, year = date
        print(date)
        month = monthConvert[month[0]]
        self.ui.lcdNumber.display('%s %s %s' % (year, month, day))


class colorSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Color Selector')
        self.setGeometry(600, 500, 400, 200)

        # OpenColorDialog
        color = QColorDialog.getColor()
        if color.isValid():
            print(color.name())


class MainWindow5(QWidget):
    def __init__(self):
        super(MainWindow5, self).__init__()
        self.resize(200, 100)

        self.settings = QSettings("ppcrong", "hello_pyqt")

        self.label_display = QLabel(self)
        self.label_display.setGeometry(0, 0, 100, 10)

        try:
            self.label_display.setText(self.settings.value('context'))
        except:
            self.label_display.setText('TEST')

        self.editLine = QLineEdit(self)
        self.editLine.setGeometry(0, 20, 100, 20)

        self.button = QPushButton(self)
        self.button.clicked.connect(self.buttonEvent)
        self.button.setGeometry(0, 40, 100, 20)
        self.button.setText('Enter')

    def buttonEvent(self):
        self.settings.setValue('context', self.editLine.text())
        self.label_display.setText(self.settings.value('context'))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    # window = MainWindow2()
    # window = MainWindow3()
    # window = MainWindow4()
    # window = colorSelector();
    # window = MainWindow5()
    window.show()
    sys.exit(app.exec_())
