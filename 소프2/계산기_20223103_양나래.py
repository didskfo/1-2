from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit('')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons
        self.digitButton = [Button(str(x), self.buttonClicked) for x in range(10)] # 숫자버튼 리스트 생성
        # for i in range(10):
        #     self.digitButton[i] = Button(str(i), self.buttonClicked)

        self.op = ['*', '/', '+', '-', '(', ')', 'C']
        self.opButton = [Button(self.op[x], self.buttonClicked) for x in range(7)] # 기호버튼 리스트 생성
        # for i in range(7):
        #     self.opButton[i] = Button(self.op[i], self.buttonClicked)

        # . and = Buttons
        self.decButton = Button('.', self.buttonClicked)
        self.eqButton = Button('=', self.buttonClicked)

        # Operator Buttons
        # self.mulButton = Button('*')
        # self.divButton = Button('/')
        # self.addButton = Button('+')
        # self.subButton = Button('-')

        # Parentheses Buttons
        # self.lparButton = Button('(')
        # self.rparButton = Button(')')

        # Clear Button
        # self.clearButton = Button('C')

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()

        numLayout.addWidget(self.digitButton[0], 3, 0)

        # for i in range(1, 10):
        #     row = int((9-i)/3)
        #     col = (i-1) % 3
        #     numLayout.addWidget(self.digitButton[i], row, col)

        for i in range(3):
            for j in range(3):
                numLayout.addWidget(self.digitButton[3*i + j + 1], 2-i, j) # 숫자버튼 레이아웃에 더하기

        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        opLayout = QGridLayout()

        for i in range(3):
            for j in range(2):
                opLayout.addWidget(self.opButton[2*i + j], i, j) # 기호버튼 레이아웃에 더학기

        # opLayout.addWidget(self.opButton[0], 0, 0)
        # opLayout.addWidget(self.opButton[1], 0, 1)
        # opLayout.addWidget(self.opButton[2], 1, 0)
        # opLayout.addWidget(self.opButton[3], 1, 1)
        #
        # opLayout.addWidget(self.opButton[4], 2, 0)
        # opLayout.addWidget(self.opButton[5], 2, 1)

        opLayout.addWidget(self.opButton[6], 3, 0)

        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")


    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        if key == '=':
            result = str(eval(self.display.text()))
            self.display.setText(result)
        elif key == 'C':
            self.display.setText('')
        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
