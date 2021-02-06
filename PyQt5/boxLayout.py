import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        acceptButton=QPushButton("확인")
        cancelButton=QPushButton("닫기")

        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(acceptButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        vbox=QVBoxLayout()
        vbox.addStretch(6)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle("박스 레이아웃")
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex =MyApp()
    sys.exit(app.exec_())