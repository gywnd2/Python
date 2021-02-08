import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("이벤트 핸들러를 재정의합니다.")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def keyPressEvent(self, e):
        if e.key()==Qt.Key_Escape:
            self.close()
        elif e.key()==Qt.Key_F:
            self.showFullScreen()
        elif e.key()==Qt.Key_N:
            self.showNormal()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())