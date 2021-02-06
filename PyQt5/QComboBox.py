import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl=QLabel("옵션 1", self)
        self.lbl.move(50, 150)

        cb=QComboBox(self)
        cb.addItem("옵션 1")
        cb.addItem("옵션 2")
        cb.addItem("옵션 3")
        cb.addItem("옵션 4")
        cb.move(50, 50)

        cb.activated[str].connect(self.onActivated) #Overloaded signal로서, int형의 index 대신 string을 전달함

        self.setWindowTitle("QComboBox")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onActivated(self, text): #20행에서 Overloaded signal로 전달받은 String을 Parameter로 받음
        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())