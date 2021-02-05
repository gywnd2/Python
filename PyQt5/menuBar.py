import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction=QAction(QIcon('240.ico'),'나가기', self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("프로그램을 닫습니다.")
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar=self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu=menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        self.setWindowTitle("메뉴 바")
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())