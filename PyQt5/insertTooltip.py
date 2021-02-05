import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('AppleSDGothicNeoB00', 10))
        self.setToolTip('이 것은 <b>QWidget</b> 입니다.')

        btn= QPushButton('단추', self)
        btn.setToolTip('이 것은 <b>QPushButton</b> 입니다.')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        self.setWindowTitle('Tooltips')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())