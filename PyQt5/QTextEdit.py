import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1=QLabel("텍스트를 입력하세요 : ")
        self.te=QTextEdit()
        self.te.setAcceptRichText(False) # 모두 Plain text로 인식
        self.lbl2=QLabel("단어의 개수는 0 입니다.")

        self.te.textChanged.connect(self.text_changed)

        vbox=QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.te)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle("QTextEdit")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def text_changed(self):
        text=self.te.toPlainText()
        self.lbl2.setText("단어의 개수는 : "+str(len(text.split())))

if __name__ == "__main__":
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())