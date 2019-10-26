# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'third1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from subprocess import Popen, PIPE
import csv

connectionString = 'SYSTEM/123'

def runSqlQuery(sqlCommand):
    sqlCommand = "set heading off;\nset serveroutput on;\n" + sqlCommand
    session = Popen(['sqlplus', '-S', connectionString], stdin = PIPE, stdout = PIPE, stderr = PIPE)
    session.stdin.write(sqlCommand.encode('utf-8'))
    result, error = session.communicate()
    return result.decode('utf-8').splitlines()

#sql file o create tables
sqlcommand = '@insert_movie.sql'
queryResult = runSqlQuery(sqlcommand)





from PyQt5 import QtCore, QtGui, QtWidgets
MovieNameA=""
GenreA1=""
GenreA2=""
GenreA3=""
class Ui_Form3(object):
   
    def click_on_MovieA(self):
        global MovieNameA
        MovieNameA=self.Movie_Name_2.text()
        print(MovieNameA)
    
    def click_on_GenreA1(self):
        global GenreA1
        GenreA1=self.Genre.currentText()
        print(GenreA1)
        sqlcommand='execute ins_movie(\''+MovieNameA+'\',\''+GenreA1+'\',\''+GenreA2+'\',\''+GenreA3+'\');'
        ans4=runSqlQuery(sqlcommand)
        print(ans4[0])
    
    def click_on_GenreA2(self):
        global GenreA2
        GenreA2=self.Genre_2.currentText()
        print(GenreA2)
       
    def click_on_GenreA3(self):
        global GenreA3
        GenreA3=self.Genre_3.currentText()
        print(GenreA3)
    
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(515, 517)
       
        self.Movie_Name_2 = QtWidgets.QLineEdit(Form)
        self.Movie_Name_2.setGeometry(QtCore.QRect(80, 170, 371, 22))
        self.Movie_Name_2.setObjectName("Movie_Name_2")
        self.OK_MovieName_2 = QtWidgets.QPushButton(Form)
        self.OK_MovieName_2.setGeometry(QtCore.QRect(220, 200, 93, 28))
        self.OK_MovieName_2.setObjectName("OK_MovieName_2")
        self.OK_MovieName_2.clicked.connect(self.click_on_MovieA)
        
        self.Genre = QtWidgets.QComboBox(Form)
        self.Genre.setGeometry(QtCore.QRect(340, 290, 105, 22))
        self.Genre.setObjectName("Genre")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.OK_Genre_3 = QtWidgets.QPushButton(Form)
        self.OK_Genre_3.setGeometry(QtCore.QRect(350, 320, 81, 28))
        self.OK_Genre_3.setObjectName("OK_Genre_3")
        self.OK_Genre_3.clicked.connect(self.click_on_GenreA1)
        
        self.Genre_2 = QtWidgets.QComboBox(Form)
        self.Genre_2.setGeometry(QtCore.QRect(210, 290, 105, 22))
        self.Genre_2.setObjectName("Genre_2")
        self.Genre_2.addItem("")
        self.Genre_2.addItem("")
        self.Genre_2.addItem("")
        self.Genre_2.addItem("")
        self.Genre_2.addItem("")
        self.Genre_2.addItem("")
        self.Genre_2.addItem("")
        self.Genre_2.addItem("")
        self.Genre_2.addItem("")
        self.Genre_2.addItem("")
        self.Genre_2.addItem("")
        self.Genre_2.addItem("")
        self.Genre_2.addItem("")
        self.Genre_2.addItem("")
        self.Genre_2.addItem("")
        self.Genre_2.addItem("")
        self.OK_Genre = QtWidgets.QPushButton(Form)
        self.OK_Genre.setGeometry(QtCore.QRect(220, 320, 81, 28))
        self.OK_Genre.setObjectName("OK_Genre")
        self.OK_Genre.clicked.connect(self.click_on_GenreA2)
        
        
        self.Genre_3 = QtWidgets.QComboBox(Form)
        self.Genre_3.setGeometry(QtCore.QRect(80, 290, 105, 22))
        self.Genre_3.setObjectName("Genre_3")
        self.Genre_3.addItem("")
        self.Genre_3.addItem("")
        self.Genre_3.addItem("")
        self.Genre_3.addItem("")
        self.Genre_3.addItem("")
        self.Genre_3.addItem("")
        self.Genre_3.addItem("")
        self.Genre_3.addItem("")
        self.Genre_3.addItem("")
        self.Genre_3.addItem("")
        self.Genre_3.addItem("")
        self.Genre_3.addItem("")
        self.Genre_3.addItem("")
        self.Genre_3.addItem("")
        self.Genre_3.addItem("")
        self.Genre_3.addItem("")
        self.OK_Genre_2 = QtWidgets.QPushButton(Form)
        self.OK_Genre_2.setGeometry(QtCore.QRect(90, 320, 81, 28))
        self.OK_Genre_2.setObjectName("OK_Genre_2")
        self.OK_Genre_2.clicked.connect(self.click_on_GenreA3)
                
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(-40, -40, 931, 791))
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.raise_()
        self.Movie_Name_2.raise_()
        self.OK_MovieName_2.raise_()
        self.Genre.raise_()
        self.Genre_2.raise_()
        self.Genre_3.raise_()
        self.OK_Genre.raise_()
        self.OK_Genre_2.raise_()
        self.OK_Genre_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Movie_Name_2.setWhatsThis(_translate("Form", "<html><head/><body><p>Relevant Keyword</p><p><br/></p></body></html>"))
        self.Movie_Name_2.setText(_translate("Form", "Movie Name"))
        self.OK_MovieName_2.setText(_translate("Form", "OK"))
        self.Genre.setWhatsThis(_translate("Form", "<html><head/><body><p>Genre</p></body></html>"))
        self.Genre.setItemText(0, _translate("Form", "Genre3"))
        self.Genre.setItemText(1, _translate("Form", "NULL"))
        self.Genre.setItemText(2, _translate("Form", "Comedy"))
        self.Genre.setItemText(3, _translate("Form", "Horror"))
        self.Genre.setItemText(4, _translate("Form", "Romance"))
        self.Genre.setItemText(5, _translate("Form", "Drama"))
        self.Genre.setItemText(6, _translate("Form", "Action"))
        self.Genre.setItemText(7, _translate("Form", "Thriller"))
        self.Genre.setItemText(8, _translate("Form", "Adventure"))
        self.Genre.setItemText(9, _translate("Form", "Documentary"))
        self.Genre.setItemText(10, _translate("Form", "Crime"))
        self.Genre.setItemText(11, _translate("Form", "Children"))
        self.Genre.setItemText(12, _translate("Form", "Animation"))
        self.Genre.setItemText(13, _translate("Form", "Sci-Fi"))
        self.Genre.setItemText(14, _translate("Form", "Mystery"))
        self.Genre.setItemText(15, _translate("Form", "Musical"))
        self.Genre_2.setWhatsThis(_translate("Form", "<html><head/><body><p>Genre</p></body></html>"))
        self.Genre_2.setItemText(0, _translate("Form", "Genre2"))
        self.Genre_2.setItemText(1, _translate("Form", "NULL"))
        self.Genre_2.setItemText(2, _translate("Form", "Comedy"))
        self.Genre_2.setItemText(3, _translate("Form", "Horror"))
        self.Genre_2.setItemText(4, _translate("Form", "Romance"))
        self.Genre_2.setItemText(5, _translate("Form", "Drama"))
        self.Genre_2.setItemText(6, _translate("Form", "Action"))
        self.Genre_2.setItemText(7, _translate("Form", "Thriller"))
        self.Genre_2.setItemText(8, _translate("Form", "Adventure"))
        self.Genre_2.setItemText(9, _translate("Form", "Documentary"))
        self.Genre_2.setItemText(10, _translate("Form", "Crime"))
        self.Genre_2.setItemText(11, _translate("Form", "Children"))
        self.Genre_2.setItemText(12, _translate("Form", "Animation"))
        self.Genre_2.setItemText(13, _translate("Form", "Sci-Fi"))
        self.Genre_2.setItemText(14, _translate("Form", "Mystery"))
        self.Genre_2.setItemText(15, _translate("Form", "Musical"))
        self.Genre_3.setWhatsThis(_translate("Form", "<html><head/><body><p>Genre</p></body></html>"))
        self.Genre_3.setItemText(0, _translate("Form", "Genre1"))
        self.Genre_3.setItemText(1, _translate("Form", "NULL"))
        self.Genre_3.setItemText(2, _translate("Form", "Comedy"))
        self.Genre_3.setItemText(3, _translate("Form", "Horror"))
        self.Genre_3.setItemText(4, _translate("Form", "Romance"))
        self.Genre_3.setItemText(5, _translate("Form", "Drama"))
        self.Genre_3.setItemText(6, _translate("Form", "Action"))
        self.Genre_3.setItemText(7, _translate("Form", "Thriller"))
        self.Genre_3.setItemText(8, _translate("Form", "Adventure"))
        self.Genre_3.setItemText(9, _translate("Form", "Documentary"))
        self.Genre_3.setItemText(10, _translate("Form", "Crime"))
        self.Genre_3.setItemText(11, _translate("Form", "Children"))
        self.Genre_3.setItemText(12, _translate("Form", "Animation"))
        self.Genre_3.setItemText(13, _translate("Form", "Sci-Fi"))
        self.Genre_3.setItemText(14, _translate("Form", "Mystery"))
        self.Genre_3.setItemText(15, _translate("Form", "Musical"))
        self.OK_Genre.setText(_translate("Form", "OK"))
        self.OK_Genre_2.setText(_translate("Form", "OK"))
        self.OK_Genre_3.setText(_translate("Form", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form3()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

