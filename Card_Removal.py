'''
Author: Scott
Version: 1.0
Name: Card_Removal
Date: 05/10/2023
Purpose: Create a CardSelect class that inherits the CardView class to add the ability to 
remove a card from a treeview
'''
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QBrush, QColor
from PyQt5.QtWidgets import  QTreeView, QAbstractItemView

from Card_Selection import *
class CardSelect(CardView):
    #Parent Widget must be a QtWidgets.Qwidget
    #Image Widget must be a QGraphicsScene Widget
    #Target Widget is the location of where to add cards after are added after being double clicked (default is None)
    def __init__(self,parentWidget,imageWidget):
        super().__init__(parentWidget,imageWidget)

    #Override Mouse Press Method
    #Output the signals
    def mousePressEvent(self,event):
        #override the default event behavior
        super().mousePressEvent(event)
        #If the left mouse button is pressed and it has selected an row add the card image to the card preview section
        if (event.button() == Qt.LeftButton and self.selectedIndexes()):
            #Get all of the indexes of all of the columns within the row
            selectedIndex = self.selectedIndexes()
            #initialize current row and item text
            text = ""

            #For the number of Qmodels get the items
            for i in range(len(selectedIndex)):
                #track where the index is currently
                currentIndex = selectedIndex[i]
                #get the current row
                self.currentRow = currentIndex.row()
                #use the index to get the name, cost from the selected item (that has been printed to the treeview)
                item = self.model.itemFromIndex(currentIndex)
                #add selection to test
                text += item.text() + " "
            
            path = self.cardData[self.currentRow].dataDict["path"]
            #print results of selection (useful when debugging)
            print("\nNEW SELECTION\n")
            print("Selection Text:",text)
            print("Selection Row:", self.currentRow)
            print("Selection Image String:", path)

            #add image to image preview
            self.imageWidget.addImage(path)
        
        #If the right mouse button is pressed and it has selected an row remove that row from the CardSelect
        if (event.button() == Qt.RightButton and self.selectedIndexes()):
            print("Removing A Card")

    

        
        