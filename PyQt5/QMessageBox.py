import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QMessageBox")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def closeEvent(self, event): #QWidget을 종료할 때 자동생성되는 QCloseEvent를 수정한 함수
        reply = QMessageBox.question(self, "확인", "프로그램을 종료하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # 타이틀 텍스트, 메인 텍스트, 버튼종류, 기본 버튼
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())