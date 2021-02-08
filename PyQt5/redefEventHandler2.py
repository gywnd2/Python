import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        x=0
        y=0

        self.text="x:{0}, y:{1}".format(x, y)
        self.label=QLabel(self.text, self)
        self.label.move(20, 20)

        self.setMouseTracking(True)

        self.setWindowTitle("이벤트 핸들러 재정의")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mouseMoveEvent(self, e): # e=> 이벤트에 대한 정보를 갖고 있는 객체. 이벤트 유형에 따라 바뀜
        x=e.x() #e.globalX(), e.globalY()는 화면 전체에서의 좌표 반환
        y=e.y()

        text="x:{0}, y:{1}".format(x, y)
        self.label.setText(text)
        self.label.adjustSize()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())