import time

from PyQt5 import QtCore


class TestThread(QtCore.QThread):
    update = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(TestThread, self).__init__(parent)

    def __del__(self):
        self.wait()

    def run(self):
        for index in range(1, 10):
            self.update.emit(index)
            time.sleep(0.5)
