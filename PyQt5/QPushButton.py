import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1=QPushButton("&버튼 1", self)
        btn1.setCheckable(True) #클릭 후 다시 튀어 나오는지? / True => 클릭 후 계속 들어가 있음
        btn1.toggle()

        btn2=QPushButton(self)
        btn2.setText("버튼 &2")

        btn3=QPushButton("버튼 3", self)
        btn3.setEnabled(False)

        vbox=QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle("QPushButton")
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())