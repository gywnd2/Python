import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar=QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn=QPushButton("시작", self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer=QBasicTimer()
        self.step=0

        self.setWindowTitle("QProgressBar")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def timerEvent(self, e): #self.timer.start로 시작
        if self.step>=100:
            self.timer.stop()
            self.btn.setText("완료")
            return

        self.step=self.step+1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText("시작")

        else:
            self.timer.start(100, self) #(종료시간, 이벤트 수행 객체)
            self.btn.setText("정지")

if __name__ == "__main__":
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())