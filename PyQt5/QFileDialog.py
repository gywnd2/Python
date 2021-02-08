import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit=QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile=QAction(QIcon("/res/open.ico"), '열기', self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("새로 파일을 엽니다.")
        openFile.triggered.connect(self.showDialog)

        menuBar=self.menuBar()
        menuBar.setNativeMenuBar(False)
        fileMenu=menuBar.addMenu("&File")
        fileMenu.addAction(openFile)

        self.setWindowTitle("File Dialog")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showDialog(self):
        fname=QFileDialog.getOpenFileName(self, "파일 열기", "./") # 열기 창 타이틀, 기본 경로

        if fname[0]:
            f=open(fname[0], 'r')
            #self.textEdit.setText(f) 하지 말고 read()한 후 textEdit.setText()를 따로 해줘야 함

            with f:
                data=f.read()
                self.textEdit.setText(data)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())
