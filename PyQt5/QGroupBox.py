import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, QRadioButton, QCheckBox, QPushButton, QMenu, QGridLayout, QVBoxLayout)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid=QGridLayout() # 네 개의 위젯으로 이루어진 그리드 생성
        grid.addWidget(self.createFirstExclusiveGroup(), 0, 0)
        grid.addWidget(self.createSecondExclusiveGroup(), 1, 0)
        grid.addWidget(self.createNonExclusiveGroup(), 0, 1)
        grid.addWidget(self.createPushButtonGroup(), 1, 1)

        self.setLayout(grid) #그리드를 개체의 레이아웃으로 설정

        self.setWindowTitle("박스 레이아웃") # 개체의 타이틀과 크기 설정 그리고 실행
        self.setGeometry(300, 300, 400, 320)
        self.show()

    def createFirstExclusiveGroup(self):
        groupbox=QGroupBox("Exclusive Radio Buttons") # 그룹박스 타이틀 설정

        radio1=QRadioButton("Radio 1") # 네개의 라디오 버튼 추가
        radio2=QRadioButton("Radio 2")
        radio3=QRadioButton("Radio 3")
        radio1.setChecked(True) # 그 중 첫번째는 체크 되어 있도록 설정

        vbox=QVBoxLayout() # 네 개의 라디오 버튼을 세로로(탑을 쌓는다 생각) 추가한 박스 생성
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        groupbox.setLayout(vbox) # 생성한 박스를 그룹박스의 레이아웃으로 설정

        return groupbox # 완성된 그룹박스 반환 => initUI 클래스의 addWidget 메서드의 인수로 사용

    def createSecondExclusiveGroup(self):
        groupbox = QGroupBox('Exclusive Radio Buttons')
        groupbox.setCheckable(True) # 위의 그룹박스와 같으나 그룹박스 레이블에 라디오 버튼이 추가됨
        groupbox.setChecked(False)

        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3')
        radio1.setChecked(True) # 첫째 라디오 버튼만 체크된 상태로 생성
        checkbox = QCheckBox('Independent Checkbox') # 세 개의 라디오 버튼에 이어 체크박스 하나 생성
        checkbox.setChecked(True)

        vbox = QVBoxLayout() # 위의 그룹박스와 마찬가지로 Vertical 박스 생성
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addWidget(checkbox)
        vbox.addStretch(1) # 빈 공간 생성. 위 아래로 두번 사용된 경우 두 메서드의 비율에 맞춰 자동 조정
        groupbox.setLayout(vbox)

        return groupbox

    def createNonExclusiveGroup(self):
        groupbox = QGroupBox('Non-Exclusive Checkboxes')
        groupbox.setFlat(True) #평평하게 보이도록 설정 (테두리 X)

        checkbox1 = QCheckBox('Checkbox1')
        checkbox2 = QCheckBox('Checkbox2')
        checkbox2.setChecked(True)
        tristatebox = QCheckBox('Tri-state Button')
        tristatebox.setTristate(True)

        vbox = QVBoxLayout()
        vbox.addWidget(checkbox1)
        vbox.addWidget(checkbox2)
        vbox.addWidget(tristatebox)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def createPushButtonGroup(self):
        groupbox = QGroupBox('Push Buttons')
        groupbox.setCheckable(True)
        groupbox.setChecked(True)

        pushbutton = QPushButton('Normal Button')
        togglebutton = QPushButton('Toggle Button')
        togglebutton.setCheckable(True) # 토글방식으로 설정
        togglebutton.setChecked(True)
        flatbutton = QPushButton('Flat Button')
        flatbutton.setFlat(True) # 클릭해야 눌린 윤곽이 드러나는 버튼
        popupbutton = QPushButton('Popup Button')
        menu = QMenu(self) # 드롭다운 메뉴 생성
        menu.addAction('First Item')
        menu.addAction('Second Item')
        menu.addAction('Third Item')
        menu.addAction('Fourth Item')
        popupbutton.setMenu(menu) #팝업 버튼을 메뉴로 설정하고 드롭다운 메뉴 할당

        vbox = QVBoxLayout()
        vbox.addWidget(pushbutton)
        vbox.addWidget(togglebutton)
        vbox.addWidget(flatbutton)
        vbox.addWidget(popupbutton)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())