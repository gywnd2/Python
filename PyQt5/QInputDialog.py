import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn=QPushButton("Dialog", self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.le=QLineEdit(self)
        self.le.move(130, 32)

        self. setWindowTitle("Input Dialog")
        self.setGeometry(300,300, 400, 200)
        self.show()

    def showDialog(self):
        text, ok=QInputDialog.getText(self, "InputDialog", "Enter your name: ")
        # 타이틀, 대화창 안의 메시지. 입력받은 메시지와 boolean 값을 반환함(ok변수가 있는 이유)
        if ok:
            self.le.setText(str(text))

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())