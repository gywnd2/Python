import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSpinBox, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1=QLabel("QSpinBox") # 레이블 생성
        self.spinbox=QSpinBox() # 스핀박스 생성
        self.spinbox.setRange(-10, 30) # 스핀박스 범위 생성
        self.spinbox.setSingleStep(2) # 변화값 단위 설정
        self.lbl2=QLabel('0') # 값 표시 레이블 생성

        self.spinbox.valueChanged.connect(self.value_changed) # 값 변화시 실행할 문장

        vbox=QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.spinbox)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle("QSpinBox")
        self.setGeometry(300, 300, 300, 200)
        self. show()

    def value_changed(self):
        self.lbl2.setText(str(self.spinbox.value())) # 값 변화시 레이블2의 문구를 spinbox.value()를 String으로 출력

if __name__ == "__main__":
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())