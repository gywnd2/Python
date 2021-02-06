import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDoubleSpinBox, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1=QLabel("QDoubleSpinBox")
        self.dspinbox=QDoubleSpinBox() # Double Spinbox는 실수 단위로 증감 가능
        self.dspinbox.setRange(0, 100)
        self.dspinbox.setSingleStep(0.5) # Spinbox와의 차이점으로, 소수점 단위 설정 가능
        self.dspinbox.setPrefix("$ ") # 단위 설정
        self.dspinbox.setDecimals(1) # 소수점 이하 자릿수 설정
        self.lbl2=QLabel("$ 0.0")

        self.dspinbox.valueChanged.connect(self.value_changed)

        vbox=QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.dspinbox)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle("QDoubleSpinBox")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def value_changed(self):
        self.lbl2.setText("$ "+str(self.dspinbox.value()))

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())