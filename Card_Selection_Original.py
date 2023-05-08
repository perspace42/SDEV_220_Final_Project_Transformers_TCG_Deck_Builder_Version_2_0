'''
Author: Scott
Version: 1.0
Name: Card_Selection
Date: 05/02/2023
Purpose: Create the card selection section
'''
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QBrush, QColor
from PyQt5.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QTreeView, QVBoxLayout, QWidget)

from Read_Database import *

class App(QWidget):
    #define column locations
    NAME,COST = range(2)
    
    #set size
    def __init__(self):
        super().__init__()
        self.title = 'Window Title'
        self.left = 20
        self.top = 10
        self.width = 500
        self.height = 500
        self.initUI()

    #Set Treeview attributes    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #Define Treeview
        self.dataView = QTreeView()

        #Remove space from treeview
        self.dataView.setRootIsDecorated(False)

        #Set Treeview Background Color
        self.setStyleSheet("background-color: grey")
        
        #Create Items That Will Be Added To Treeview
        self.model = self.createDataModel(self)
        self.dataView.setModel(self.model)

        #Create Layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.dataView)
        self.setLayout(mainLayout)
        
        #Draw Placed Widgets
        self.show()

    def createDataModel(self,parent):
        #Set Column Headers
        model = QStandardItemModel(0, 2,parent)
        model.setHeaderData(self.NAME, Qt.Horizontal, "Name")
        model.setHeaderData(self.COST, Qt.Horizontal, "Cost")
        return model
    
    def addData(self,model,list):
        #Add Data From List To Columns
        for i in range(len(list)):
            #Get Name and Cost
            currentCard = list[i]
            fullName = currentCard.dataDict['name'] + " " + currentCard.dataDict.get('subName',"")
            cost = currentCard.dataDict['cost']

            
            #Insert at Index 0
            model.insertRow(0)
            #Insert Full Name Of The Bot
            model.setData(model.index(0, self.NAME), fullName)
            #Insert Cost Of The Bot
            model.setData(model.index(0, self.COST), cost)
            
            #Change Bot Background Color Based On Loyalty
            #initialize color values for background color
            r = 0
            g = 0
            b = 0

            #if the bot is an Autobot, set the background color values to red
            if (currentCard.dataDict['loyalty'] == "Autobot"):
                r = 178
                g = 0
                b = 0
            #if the bot is a Decepticon, set the background color values to purple
            elif(currentCard.dataDict['loyalty'] == "Decepticon"):
                r = 67
                g = 0
                b = 67
            #Otherwise the bot is a Mercenary, set the background color values to dark grey    
            else:
                r = 51
                g = 51
                b = 51
            
            #Add Color To Both Columns
            model.setData(model.index(0, self.NAME), QBrush(QColor(r,g,b)), Qt.BackgroundRole)
            model.setData(model.index(0, self.COST), QBrush(QColor(r,g,b)), Qt.BackgroundRole)
        
        #Set Column Width (Must Be Set After Adding Data)
        self.dataView.setColumnWidth(self.NAME,300)
        self.dataView.setColumnWidth(self.COST,5)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.addData(ex.model,botCardList)
    sys.exit(app.exec_())