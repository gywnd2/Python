import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate, Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal=QCalendarWidget(self)
        cal.setGridVisible(True) # 달력의 격자 표시
        cal.clicked[QDate].connect(self.showDate) # 클릭 시 레이블에 표시될 날짜를 바꿔 줌

        self.lbl=QLabel(self) # 선택한 날짜(초기 실행 시는 오늘 날짜가 선택됨)를 표시하는 레이블 생성
        date=cal.selectedDate()
        self.lbl.setText(date.toString(Qt.DefaultLocaleLongDate))

        vbox=QVBoxLayout() # 달력과 레이블로 위젯의 레이아웃 설정
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setWindowTitle("QCalendarWidget")
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString(Qt.DefaultLocaleLongDate))

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())