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
            selectedIndex = self.currentIndex()
            #initialize current row and item text
            text = ""
            #get the current row
            self.currentRow = selectedIndex.row()
            #use the index to get the name, cost from the selected item (that has been printed to the treeview)
            item = self.model.itemFromIndex(selectedIndex)
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
            #Remove the row From The Treeview, if the type isn't battle (and therefore there is not quantity tab)
            selectedIndex = self.currentIndex()
            self.currentRow = selectedIndex.row()

            print ("Removing: ",self.cardData[self.currentRow].dataDict['name'], " from the deck")

            if (self.type != "Battle"):
                self.model.removeRow(self.currentRow,self.currentIndex().parent())
                #Remove the Card From The Parallel List
                self.cardData.pop(self.currentRow)

            #If the card type is battle check quantity before removing
            else:
                #using the cards current row and the quantity column (2) pull the quantity from the treeview
                dataIndex = (self.model.index(self.currentRow,2))
                quantity = int(self.model.data(dataIndex,Qt.DisplayRole))
                if (quantity > 1):
                        #increment quantity
                        quantity -= 1
                        #add new quantity to treeview
                        self.target.model.setData(dataIndex, quantity)
                #if the quantity is 1 then simply remove the card
                else:
                    #Remove the Row from the Treeview
                    selectedIndex = self.currentIndex()
                    self.currentRow = selectedIndex.row()

                    self.model.removeRow(self.currentRow,self.currentIndex().parent())

                    #Remove the Card From The Parallel List
                    self.cardData.pop(self.currentRow)

            
                     

                
            


    

        
        