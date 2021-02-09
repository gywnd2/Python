import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow

class Communicate(QObject):
    closeApp=pyqtSignal()

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c=Communicate()
        self.c.closeApp.connect(self.close) # 방출 받아 close() 슬롯에 연결

        self.setWindowTitle('시그널 발생')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mousePressEvent(self, e):
        self.c.closeApp.emit() # closeApp 시그널 방출

if __name__ == "__main__":
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())