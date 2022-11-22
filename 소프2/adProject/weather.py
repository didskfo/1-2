import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Weather(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
    
    def selectDates(self):
        self.dateWindow = QWidget()
        self.cal = QCalendarWidget(self)
        self.cal.clicked[QtCore.QDate].connect(self.showDate)
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.cal)
        self.dateWindow.setLayout(self.hbox)
        self.dateWindow.setGeometry(300, 300, 350, 300)
        self.dateWindow.setWindowTitle('Calendar')
    
        self.dateWindow.show()
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())