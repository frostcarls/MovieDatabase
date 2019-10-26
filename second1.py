from subprocess import Popen, PIPE
import csv

connectionString = 'SYSTEM/123'

def runSqlQuery(sqlCommand):
    sqlCommand = "set heading off;\nset serveroutput on;\n" + sqlCommand
    session = Popen(['sqlplus', '-S', connectionString], stdin = PIPE, stdout = PIPE, stderr = PIPE)
    session.stdin.write(sqlCommand.encode('utf-8'))
    result, error = session.communicate()
    return result.decode('utf-8').splitlines()

from PyQt5 import QtCore, QtGui, QtWidgets

MovienameR=""
UserR=""
RateR=""

class Ui_Form2(object):
        
    def click_on_MovieR(self):
        global MovienameR
        MovienameR=self.Movie_Name_2.text()
        print(MovienameR)
    
    def click_on_UserR(self):
        global UserR
        UserR=self.UserID.text()
        print(UserR)
        
    def click_on_RateR(self):
        RateR=self.IMDB_Rating.currentText()
        sqlcommand='execute ins_review('+UserR+',\''+MovienameR+'\','+RateR[1]+');'
        ans3=runSqlQuery(sqlcommand)
        print(ans3[0])
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(523, 519)
        Form.setAutoFillBackground(True)
        
        self.UserID = QtWidgets.QLineEdit(Form)
        self.UserID.setGeometry(QtCore.QRect(30, 150, 137, 22))
        self.UserID.setObjectName("UserID")
        self.OK_UserID = QtWidgets.QPushButton(Form)
        self.OK_UserID.setGeometry(QtCore.QRect(30, 180, 93, 28))
        self.OK_UserID.setObjectName("OK_UserID")
        self.OK_UserID.clicked.connect(self.click_on_UserR)
        
        self.Movie_Name_2 = QtWidgets.QLineEdit(Form)
        self.Movie_Name_2.setGeometry(QtCore.QRect(31, 67, 261, 22))
        self.Movie_Name_2.setObjectName("Movie_Name_2")
        self.OK_MovieName = QtWidgets.QPushButton(Form)
        self.OK_MovieName.setGeometry(QtCore.QRect(30, 100, 93, 28))
        self.OK_MovieName.setObjectName("OK_MovieName")
        self.OK_MovieName.clicked.connect(self.click_on_MovieR)
        
        self.IMDB_Rating = QtWidgets.QComboBox(Form)
        self.IMDB_Rating.setGeometry(QtCore.QRect(30, 240, 101, 22))
        self.IMDB_Rating.setObjectName("IMDB_Rating")
        self.IMDB_Rating.addItem("")
        self.IMDB_Rating.addItem("")
        self.IMDB_Rating.addItem("")
        self.IMDB_Rating.addItem("")
        self.IMDB_Rating.addItem("")
        self.IMDB_Rating.addItem("")
        self.IMDB_Rating.addItem("")
        self.OK_UserID_2 = QtWidgets.QPushButton(Form)
        self.OK_UserID_2.setGeometry(QtCore.QRect(30, 270, 71, 28))
        self.OK_UserID_2.setObjectName("OK_UserID_2")
        self.OK_UserID_2.clicked.connect(self.click_on_RateR)

        
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(0, -10, 931, 791))
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.raise_()
        self.OK_MovieName.raise_()
        self.UserID.raise_()
        self.OK_UserID.raise_()
        self.Movie_Name_2.raise_()
        self.OK_UserID_2.raise_()
        self.IMDB_Rating.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.OK_MovieName.setText(_translate("Form", "OK"))
        self.UserID.setWhatsThis(_translate("Form", "<html><head/><body><p>Relevant Keyword</p><p><br/></p></body></html>"))
        self.UserID.setText(_translate("Form", "User ID"))
        self.OK_UserID.setText(_translate("Form", "OK"))
        self.Movie_Name_2.setWhatsThis(_translate("Form", "<html><head/><body><p>Relevant Keyword</p><p><br/></p></body></html>"))
        self.Movie_Name_2.setText(_translate("Form", "Movie Name"))
        self.OK_UserID_2.setText(_translate("Form", "OK"))
        self.IMDB_Rating.setWhatsThis(_translate("Form", "<html><head/><body><p>IMDB Rating</p></body></html>"))
        self.IMDB_Rating.setItemText(0, _translate("Form", "Rating"))
        self.IMDB_Rating.setItemText(1, _translate("Form", "NULL"))
        self.IMDB_Rating.setItemText(2, _translate("Form", ">0"))
        self.IMDB_Rating.setItemText(3, _translate("Form", ">1"))
        self.IMDB_Rating.setItemText(4, _translate("Form", ">2"))
        self.IMDB_Rating.setItemText(5, _translate("Form", ">3"))
        self.IMDB_Rating.setItemText(6, _translate("Form", ">4"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form2()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

