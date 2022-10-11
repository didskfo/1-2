import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        name = QLabel('Name:', self)
        age = QLabel('Age:', self)
        score = QLabel('Score:', self)
        amount = QLabel('Amount:', self)
        key = QLabel('Key:', self)
        result = QLabel('Result:', self)

        self.nameEdit = QLineEdit(self)
        self.ageEdit = QLineEdit(self)
        self.scoreEdit = QLineEdit(self)
        self.amountEdit = QLineEdit(self)
        self.sortkey = QComboBox(self)
        self.monitor = QTextEdit(self)

        self.sortkey.addItems(['Name', 'Score', 'Age'])

        addButton = QPushButton("Add")
        delButton = QPushButton("Del")
        findButton = QPushButton("Find")
        incButton = QPushButton("Inc")
        showButton = QPushButton("show")

        hbox1 = QHBoxLayout()
        hbox1.addWidget(name)
        hbox1.addWidget(self.nameEdit)
        hbox1.addWidget(age)
        hbox1.addWidget(self.ageEdit)
        hbox1.addWidget(score)
        hbox1.addWidget(self.scoreEdit)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(amount)
        hbox2.addWidget(self.amountEdit)
        hbox2.addWidget(key)
        hbox2.addWidget(self.sortkey)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(addButton)
        hbox3.addWidget(delButton)
        hbox3.addWidget(findButton)
        hbox3.addWidget(incButton)
        hbox3.addWidget(showButton)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(result)
        vbox.addWidget(self.monitor)

        self.setLayout(hbox1)
        self.setLayout(hbox2)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()


        addButton.clicked.connect(self.addClicked)
        delButton.clicked.connect(self.delClicked)
        findButton.clicked.connect(self.findClicked)
        incButton.clicked.connect(self.incClicked)
        showButton.clicked.connect(self.showClicked)

    def addClicked(self):
        self.scoredb.append(
            {'Name': self.nameEdit.text(), 'Age': int(self.ageEdit.text()), 'Score': int(self.scoreEdit.text())})
        self.showScoreDB()

    def delClicked(self):
        delperson = self.nameEdit.text()
        scdb_ = self.scoredb[:]
        for p in scdb_:
            if p['Name'] == delperson:
                self.scoredb.remove(p)
        self.showScoreDB()

    def findClicked(self):
        findperson = self.nameEdit.text()
        self.monitor.clear()
        for p in sorted(self.scoredb, key=lambda person: person['Name']):
            findinfo = ""
            if p['Name'] == findperson:
                for attr in sorted(p):
                    findinfo += attr + "=" + str(p[attr]) + "    "
                self.monitor.append(findinfo)



    def incClicked(self):
        incperson = self.nameEdit.text()
        scoreamount = self.amountEdit.text()
        for p in self.scoredb:
            if p['Name'] == incperson:
                p['Score'] = int(p['Score']) + int(scoreamount)
        self.showScoreDB()

    def showClicked(self):
        self.showScoreDB()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        keyname = self.sortkey.currentText()
        self.monitor.clear()
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            info = ""
            for attr in sorted(p):
                info += attr + "=" + str(p[attr]) + "    "
            self.monitor.append(info)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())