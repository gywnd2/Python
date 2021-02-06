import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        rbtn1=QRadioButton("첫번째 버튼", self)
        rbtn1.move(50, 50)
        rbtn1.setChecked(True)

        rbtn2=QRadioButton("두세번째 버튼", self)
        rbtn2.move(50, 70)
        #rbtn2.setText("두번째 버튼")

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("QRadioButton")
        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())