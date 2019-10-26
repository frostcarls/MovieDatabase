# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from subprocess import Popen, PIPE
import csv

connectionString = 'SYSTEM/root123'


def runSqlQuery(sqlCommand):
    sqlCommand = "set heading off;\nset serveroutput on;\n" + sqlCommand
    session = Popen(['sqlplus', '-S', connectionString], stdin = PIPE, stdout = PIPE, stderr = PIPE)
    session.stdin.write(sqlCommand.encode('utf-8'))
    result, error = session.communicate()
    return result.decode('utf-8').splitlines()

sqlcommand='@basic_search.sql'
runSqlQuery(sqlcommand)

sqlcommand2='@relevant_search.sql'
runSqlQuery(sqlcommand2)

from PyQt5 import QtCore, QtGui, QtWidgets 
from second1  import Ui_Form2
from third1  import Ui_Form3

MovieName=""
Genreans=""
Ratingans=0
Orderbyans=""
KeywordName=""
Relevanceans=""


class Ui_Form(object):
    def next_window1(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Form2()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def next_window2(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Form3()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def click_on_Movie(self):
        MovieName=self.Movie_Name.text()
        sqlcommand='execute basic_search(\''+MovieName+'\');'
        ans1=runSqlQuery(sqlcommand)
        print(ans1[0])
        print(MovieName)
   
    def click_on_Keyword(self):
        global KeywordName
        KeywordName = self.Keyword.text()
        print(KeywordName)
        
   
    def click_on_Genre(self):
        Genreans=self.Genre.currentText()
        print(Genreans)
    
    def click_on_Rating(self):
        Ratingans=self.IMDB_Rating.currentText()
        print(int(Ratingans[1]))
        
    def click_on_Relevance(self):
        Relevanceans=self.Relevance.currentText()
        print(Relevanceans)
        sqlcommand='execute rs(\''+KeywordName+'\','+Relevanceans+');'
        ans2=runSqlQuery(sqlcommand)
        print(ans2[0])
       
   
    def click_on_Order(self):
        Orderbyans=self.Order_By.currentText()
        print(Orderbyans)
        
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(553, 464)
        self.Genre = QtWidgets.QComboBox(Form)
        self.Genre.setGeometry(QtCore.QRect(50, 160, 105, 22))
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
        self.OK_Genre = QtWidgets.QPushButton(Form)
        self.OK_Genre.setGeometry(QtCore.QRect(60, 190, 81, 28))
        self.OK_Genre.setObjectName("OK_Genre")
        self.OK_Genre.clicked.connect(self.click_on_Genre)

        
        self.IMDB_Rating = QtWidgets.QComboBox(Form)
        self.IMDB_Rating.setGeometry(QtCore.QRect(240, 160, 101, 22))
        self.IMDB_Rating.setObjectName("IMDB_Rating")
        self.IMDB_Rating.addItem("")
        self.IMDB_Rating.addItem("")
        self.IMDB_Rating.addItem("")
        self.IMDB_Rating.addItem("")
        self.IMDB_Rating.addItem("")
        self.IMDB_Rating.addItem("")
        self.IMDB_Rating.addItem("")
        self.OK_IMDB = QtWidgets.QPushButton(Form)
        self.OK_IMDB.setGeometry(QtCore.QRect(250, 190, 81, 28))
        self.OK_IMDB.setObjectName("OK_IMDB")
        self.OK_IMDB.clicked.connect(self.click_on_Rating)

        
        self.Relevance = QtWidgets.QComboBox(Form)
        self.Relevance.setGeometry(QtCore.QRect(200, 360, 161, 22))
        self.Relevance.setObjectName("Relevance")
        self.Relevance.addItem("")
        self.Relevance.addItem("")
        self.Relevance.addItem("")
        self.Relevance.addItem("")
        self.Relevance.addItem("")
        self.OK_Relevance = QtWidgets.QPushButton(Form)
        self.OK_Relevance.setGeometry(QtCore.QRect(240, 390, 93, 28))
        self.OK_Relevance.setObjectName("OK_Relevance")
        self.OK_Relevance.clicked.connect(self.click_on_Relevance)
        
        self.Keyword = QtWidgets.QLineEdit(Form)
        self.Keyword.setGeometry(QtCore.QRect(50, 270, 461, 22))
        self.Keyword.setObjectName("Keyword")
        self.OK_Text = QtWidgets.QPushButton(Form)
        self.OK_Text.setGeometry(QtCore.QRect(230, 300, 111, 28))
        self.OK_Text.setObjectName("OK_Text")
        self.OK_Text.clicked.connect(self.click_on_Keyword)
   
        
        self.OK_Movie = QtWidgets.QPushButton(Form)
        self.OK_Movie.setGeometry(QtCore.QRect(230, 100, 111, 28))
        self.OK_Movie.setObjectName("OK_Movie")
        self.OK_Movie.clicked.connect(self.click_on_Movie)

        self.Movie_Name = QtWidgets.QLineEdit(Form)
        self.Movie_Name.setGeometry(QtCore.QRect(52, 70, 461, 22))
        self.Movie_Name.setObjectName("Movie_Name")
        
        self.Order_By = QtWidgets.QComboBox(Form)
        self.Order_By.setGeometry(QtCore.QRect(390, 160, 121, 22))
        self.Order_By.setObjectName("Order_By")
        self.Order_By.addItem("")
        self.Order_By.addItem("")
        self.Order_By.addItem("")
        self.Order_By.addItem("")
        self.Order_By.addItem("")
        self.Order_By.addItem("")
        self.OK_Order = QtWidgets.QPushButton(Form)
        self.OK_Order.setGeometry(QtCore.QRect(410, 190, 81, 28))
        self.OK_Order.setObjectName("OK_Order")
        self.OK_Order.clicked.connect(self.click_on_Order)
        
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(-10, -10, 571, 481))
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setObjectName("graphicsView")
        self.To_review = QtWidgets.QPushButton(Form)
        self.To_review.setGeometry(QtCore.QRect(440, 420, 93, 28))
        self.To_review.setObjectName("To_review")
        self.To_review.clicked.connect(self.next_window1)
        self.To_admin = QtWidgets.QPushButton(Form)
        self.To_admin.setGeometry(QtCore.QRect(10, 420, 93, 28))
        self.To_admin.setObjectName("To_admin")
        self.To_admin.clicked.connect(self.next_window2)
        
        self.graphicsView.raise_()
        self.Genre.raise_()
        self.OK_Genre.raise_()
        self.OK_IMDB.raise_()
        self.OK_Relevance.raise_()
        self.IMDB_Rating.raise_()
        self.Relevance.raise_()
        self.Keyword.raise_()
        self.OK_Text.raise_()
        self.OK_Movie.raise_()
        self.Movie_Name.raise_()
        self.Order_By.raise_()
        self.OK_Order.raise_()
        self.To_review.raise_()
        self.To_admin.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Genre.setWhatsThis(_translate("Form", "<html><head/><body><p>Genre</p></body></html>"))
        self.Genre.setItemText(0, _translate("Form", "Genre"))
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
        self.OK_Genre.setText(_translate("Form", "OK"))
        self.OK_IMDB.setText(_translate("Form", "OK"))
        self.OK_Relevance.setText(_translate("Form", "OK"))
        self.IMDB_Rating.setWhatsThis(_translate("Form", "<html><head/><body><p>IMDB Rating</p></body></html>"))
        self.IMDB_Rating.setItemText(0, _translate("Form", "Rating"))
        self.IMDB_Rating.setItemText(1, _translate("Form", "NULL"))
        self.IMDB_Rating.setItemText(2, _translate("Form", ">0"))
        self.IMDB_Rating.setItemText(3, _translate("Form", ">1"))
        self.IMDB_Rating.setItemText(4, _translate("Form", ">2"))
        self.IMDB_Rating.setItemText(5, _translate("Form", ">3"))
        self.IMDB_Rating.setItemText(6, _translate("Form", ">4"))
        self.Relevance.setWhatsThis(_translate("Form", "<html><head/><body><p>Relevance</p></body></html>"))
        self.Relevance.setItemText(0, _translate("Form", "Relevance greater than"))
        self.Relevance.setItemText(1, _translate("Form", "0"))
        self.Relevance.setItemText(2, _translate("Form", "0.25"))
        self.Relevance.setItemText(3, _translate("Form", "0.5"))
        self.Relevance.setItemText(4, _translate("Form", "0.75"))
        self.Keyword.setWhatsThis(_translate("Form", "<html><head/><body><p>Relevant Keyword</p><p><br/></p></body></html>"))
        self.Keyword.setText(_translate("Form", "Relavence"))
        self.OK_Text.setText(_translate("Form", "OK"))
        self.OK_Movie.setText(_translate("Form", "OK"))
        self.Movie_Name.setWhatsThis(_translate("Form", "<html><head/><body><p>Relevant Keyword</p><p><br/></p></body></html>"))
        self.Movie_Name.setText(_translate("Form", "Search"))
        self.Order_By.setWhatsThis(_translate("Form", "<html><head/><body><p>Genre</p></body></html>"))
        self.Order_By.setItemText(0, _translate("Form", "Order By"))
        self.Order_By.setItemText(1, _translate("Form", "NULL"))
        self.Order_By.setItemText(2, _translate("Form", "Name (asc)"))
        self.Order_By.setItemText(3, _translate("Form", "Name (dsc)"))
        self.Order_By.setItemText(4, _translate("Form", "Rating (asc)"))
        self.Order_By.setItemText(5, _translate("Form", "Rating (dsc)"))
        self.OK_Order.setText(_translate("Form", "OK"))
        self.To_review.setText(_translate("Form", "Review"))
        self.To_admin.setText(_translate("Form", "Admin"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
