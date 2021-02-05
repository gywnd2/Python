import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction=QAction(QIcon("res/240.ico"),"나가기", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("프로그램을 닫습니다.")
        exitAction.setToolTip("나가기")
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        self.toolbar = self.addToolBar("나가기")
        self.toolbar.addAction(exitAction)

        self.setWindowTitle("툴바")
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())