'''
Author: Scott
Version: 3.0
Name: Card_Selection
Date: 05/10/2023
Purpose: Create a CardView class to add a Treeview for viewing cards to be added to the UI.py file
'''
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QStandardItemModel, QBrush, QColor
from PyQt5.QtWidgets import  QTreeView, QAbstractItemView

from Read_Database import *
from Card_Preview import *

#NOTE These three functions (while functional) need to be optimized as alot of their code can be eliminated due to the Card_Selection.py files updated structure

#Function To Add bot cards to treeview data model
def treeBotCards(model,list):
    for i in range(len(list)-1,-1,-1):
        #Get First Card
        currentCard = list[i]

        #Get Name and Cost
        fullName = currentCard.dataDict['name'] + " " + currentCard.dataDict.get('subName',"")
        cost = currentCard.dataDict['cost']

            
        #Insert at Index 0
        model.insertRow(0)
        #Insert Full Name Of The Bot
        model.setData(model.index(0, 0), fullName)
        #Insert Cost Of The Bot
        model.setData(model.index(0, 1), cost)
            
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

        #Add Color To Name Column
        model.setData(model.index(0, 0), QBrush(QColor(r,g,b)), Qt.BackgroundRole)
        #Add Color To Cost Column
        model.setData(model.index(0, 1), QBrush(QColor(r,g,b)), Qt.BackgroundRole)

    #return data model
    return model
        
#Function To Add battle cards to treeview data model
def treeBattleCards(model,list):
    for i in range(len(list)-1,-1,-1):
        #Get First Card
        currentCard = list[i]

        #Get Name and Cost
        fullName = currentCard.dataDict['name']
        cost = currentCard.dataDict['cost']

            
        #Insert at Index 0
        model.insertRow(0)
        #Insert Full Name Of The Battle Card
        model.setData(model.index(0, 0), fullName)
        #Insert Cost Of The Battle Card
        model.setData(model.index(0, 1), cost)
            
        #Change Battle Card Background Color Based On Loyalty
        #initialize color values for background color
        r = 0
        g = 0
        b = 0

        #if the card is an Action, set the background color values to white
        if (currentCard.dataDict['cardType'] == "Action"):
            r = 255
            g = 255
            b = 255
        #if the card is an Secret Action, set the background color values to dark grey
        elif(currentCard.dataDict['cardType'] == "Secret Action"):
            r = 51
            g = 51
            b = 51
        #if the card is an Upgrade Determine its subType by looking at its side, then set its colors accordingly
        else:
            #If the card is an Weapon set the background color values to an orange
            if (currentCard.sideList[0].dataDict['subType'] == "Weapon"):
                r = 230
                g = 149
                b = 0
            #If the card is an Armor set the background color to a light cyan
            elif(currentCard.sideList[0].dataDict['subType'] == "Armor"):
                r = 0
                g = 255
                b = 255
            #If the card is an Utility set the background color values to light grey
            elif(currentCard.sideList[0].dataDict['subType'] == "Utility"):
                r = 128
                g = 128
                b = 128
            #If the card is an Weapon Armor set the background color values to light green
            else:
                r = 115
                g = 202
                b = 128
        
        
            
        #Add Color To Both Columns

        #Add Color To Name Column
        model.setData(model.index(0, 0), QBrush(QColor(r,g,b)), Qt.BackgroundRole)
        #Add Color To Cost Column
        model.setData(model.index(0, 1), QBrush(QColor(r,g,b)), Qt.BackgroundRole)

    #return data model
    return model

#Function To Add stratagem cards to treeview data model (stratagem cards are not color coded)
def treeStratagemCards(model,list):
    for i in range(len(list)-1,-1,-1):
        #Get First Card
        currentCard = list[i]

        #Get Name and Cost
        fullName = currentCard.dataDict['name']
        cost = currentCard.dataDict['cost']

            
        #Insert at Index 0
        model.insertRow(0)
        #Insert Full Name Of The Battle Card
        model.setData(model.index(0, 0), fullName)
        #Insert Cost Of The Battle Card
        model.setData(model.index(0, 1), cost)

    #return data model
    return model


class CardView(QTreeView):
    #Parent Widget must be a QtWidgets.Qwidget
    #Image Widget must be a QGraphicsScene Widget
    #Target Widget is the location of where to add cards after are added after being double clicked (default is None)
    def __init__(self,parentWidget,imageWidget):
        super().__init__(parentWidget)
        #Create Treeview Items
        #remove left tab space from treeview
        self.setRootIsDecorated(False)
        #prevent user from editing treeview items (can still select them)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #create data storage container for treeview
        self.model = self.createDataModel(self)
        #add data storage container to treeview
        self.setModel(self.model)

        #Create Preview and Search Items
        #initialize card data list to empty this list will store the cards currently shown within the treeview
        self.cardData = []
        #initialize card preview widget this will display the image of the last card selected within the treeview
        self.imageWidget = imageWidget
        #initialize current row index (This will store the row that was last selected)
        self.currentRow = 999 #if 999 shows up as current row then their is a logic error somewhere
        #initialize selection CardView widget (This will store where a selected card is to be placed
        self.target = None
        #initialize table Total widget (This will store the quantity and point total of the deck)
        self.table = None

        #initialize variable to store type of cards in treeview (Bot,Battle,Strategem)
        self.type = None


    #create the columns for the treeview
    def createDataModel(self,numColumns = 2):
        #Set Column Headers
        #QStandardItemModel will not accept a variable as a parameter only a constant
        model = QStandardItemModel(0, 2)
        model.setHeaderData(0, Qt.Horizontal, "Name")
        model.setHeaderData(1, Qt.Horizontal, "Cost")

        #If there is need for a third column, add it
        if (numColumns == 3):
            model = QStandardItemModel(0, 3)
            model.setHeaderData(0, Qt.Horizontal, "Name")
            model.setHeaderData(1, Qt.Horizontal, "Cost")
            model.setHeaderData(2,Qt.Horizontal, "Quantity")
        
        #return data model
        return model
    
    #add the data from a list of cards to the treeview (called at start of program)
    def addData(self,model,cardList):
        #Add Data From List To Columns (if the given list contains any values)
        if (len(cardList) > 0):
            #Add Cards To Card List (This will be used when searching for the card data a row references)
            self.cardData = cardList
            #Get First Card
            currentCard = cardList[0]

            #Get Card Type

            #If Card Type reveals data to contain bot cards, set the data model accordingly
            if (currentCard.dataDict['cardType'] in ("Battle Master", "BotPiece", "Combiner", "TitanMaster Head", "TitanMaster Body", "Multiform", "Bot")):
                self.type = "Bot"
                model = treeBotCards(model,cardList)

                #Set Column Width (Must Be Set After Adding Data)
                #Set Name Column Width
                self.setColumnWidth(0,300)
                #Set Cost Column Width
                self.setColumnWidth(1,5)

            #If Card Type reveals data to contain battle cards, set the data model accordingly
            elif(currentCard.dataDict['cardType'] in ("Upgrade", "Action", "Secret Action")):
                self.type = "Battle"
                model = treeBattleCards(model,cardList)

                #Set Column Width (Must Be Set After Adding Data)
                #Set Name Column Width
                self.setColumnWidth(0,250)
                #Set Cost Column Width
                self.setColumnWidth(1,5)

            #Otherwise Card Type must be a Stratagem, set the data model accordingly
            else:
                self.type = "Stratagem"
                model = treeStratagemCards(model,cardList)

                #Set Column Width (Must Be Set After Adding Data)

                #Set Name Column Width
                self.setColumnWidth(0,200)
                #Set Cost Column Width
                self.setColumnWidth(1,5)

    #add the data from a single card to a treeview (called on_double_clicked)
    def addCard(self,addedCard):
        #Get Name and Cost
        fullName = addedCard.dataDict['name'] + " " + addedCard.dataDict.get('subName',"")
        cost = addedCard.dataDict['cost']

        #Adjust CardList
        self.cardData.insert(0,addedCard)

        #Insert at Index 0
        self.model.insertRow(0)
        #Insert Full Name Of The Bot
        self.model.setData(self.model.index(0, 0), fullName)
        #Insert Cost Of The Bot
        self.model.setData(self.model.index(0, 1), cost)

        #If the card type is a bot or stratagem add it with the following colors
        if (self.type == "Bot" or self.type == "Stratagem"):
            #Only set colors if the type of card being added is not a Stratagem
            if (self.type != "Stratagem"):
                #if the bot is an Autobot, set the background color values to red
                if (addedCard.dataDict['loyalty'] == "Autobot"):
                    r = 178
                    g = 0
                    b = 0
                #if the bot is a Decepticon, set the background color values to purple
                elif(addedCard.dataDict['loyalty'] == "Decepticon"):
                    r = 67
                    g = 0
                    b = 67
                #Otherwise the bot is a Mercenary, set the background color values to dark grey    
                else:
                    r = 51
                    g = 51
                    b = 51
                    
                #Add Color To Both Columns

                #Add Color To Name Column
                self.model.setData(self.model.index(0, 0), QBrush(QColor(r,g,b)), Qt.BackgroundRole)
                #Add Color To Cost Column
                self.model.setData(self.model.index(0, 1), QBrush(QColor(r,g,b)), Qt.BackgroundRole)

       #If the card type is a battle card add it with the following colors
        else:
            #Set quantity of added card to 1
            self.model.setData(self.model.index(0,2),1)  
            #Change Battle Card Background Color Based On type
            
            #if the card is an Action, set the background color values to white
            if (addedCard.dataDict['cardType'] == "Action"):
                r = 255
                g = 255
                b = 255
            #if the card is an Secret Action, set the background color values to dark grey
            elif(addedCard.dataDict['cardType'] == "Secret Action"):
                r = 51
                g = 51
                b = 51
            #if the card is an Upgrade Determine its subType by looking at its side, then set its colors accordingly
            else:
                #If the card is an Weapon set the background color values to an orange
                if (addedCard.sideList[0].dataDict['subType'] == "Weapon"):
                    r = 230
                    g = 149
                    b = 0
                #If the card is an Armor set the background color to a light cyan
                elif(addedCard.sideList[0].dataDict['subType'] == "Armor"):
                    r = 0
                    g = 255
                    b = 255
                #If the card is an Utility set the background color values to light grey
                elif(addedCard.sideList[0].dataDict['subType'] == "Utility"):
                    r = 128
                    g = 128
                    b = 128
                #If the card is an Weapon Armor set the background color values to light green
                else:
                    r = 115
                    g = 202
                    b = 128
            
            #Add Color To All Three Columns

            #Add Color To Name Column
            self.model.setData(self.model.index(0, 0), QBrush(QColor(r,g,b)), Qt.BackgroundRole)
            #Add Color To Cost Column
            self.model.setData(self.model.index(0, 1), QBrush(QColor(r,g,b)), Qt.BackgroundRole)
            #Add Color To Quantity Column
            self.model.setData(self.model.index(0, 2), QBrush(QColor(r,g,b)), Qt.BackgroundRole)

    #method for setting which treeview cards should be added to
    def setTarget(self,CardSelectionTree):
        self.target = CardSelectionTree
        #set types to be equal
        CardSelectionTree.type = self.type

    #method for storing the totals table
    def setTotal(self,TotalTable):
        self.table = TotalTable

    #Add The Cards Data To The Totals Table         
    def adjustTotal(self,cardLocation,adding = True):
        #Find the Cost Of The Bot Card To Add To The Totals Table
            dataIndex = (self.target.model.index(cardLocation,1))
            cost = int(self.target.model.data(dataIndex,Qt.DisplayRole))
                
            if (self.type == "Bot"):
                cardPoint = "Bot Point"
                cardType = "Bot Card"
            elif(self.type == "Stratagem"):
                cardPoint = "Stratagem Point"
                cardType = "Stratagem Card"
            #type is Battle
            else:
                cardPoint = "Battle Point"
                cardType = "Battle Card"

            #adding checks if cards are being removed or added to the quantity total
            if (adding):
                self.table.addValue(cost,cardPoint)
                self.table.addValue(1,cardType)
            else:
                self.table.addValue(-1*cost,cardPoint)
                self.table.addValue(-1,cardType)

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
            

    def mouseDoubleClickEvent(self,event):
        #override the default event behavior
        super().mouseDoubleClickEvent(event)
        #If the left mouse button is pressed and it has selected an row add the card to the selection area
        if (event.button() == Qt.LeftButton and self.selectedIndexes()):
            print("double click result:")
            #using current row, get selected card data
            selectedCard = self.cardData[self.currentRow]

            #Check if the card is already in the selection CardView
            if (selectedCard in (self.target.cardData)):
                print("Card is a duplicate")
                #If the card to be added to the deck is a Battle Card (Action, Secret Action, Upgrade)
                if (self.target.type == "Battle"):
                    #find the location of the card (the location in the parallel list will be identical to the row in the treeview)
                    cardLocation = self.target.cardData.index(selectedCard)
                    #using the cards location and the quantity column (2) pull the quantity from the treeview
                    dataIndex = (self.target.model.index(cardLocation,2))
                    quantity = int(self.target.model.data(dataIndex,Qt.DisplayRole))
                    #by rule only 3 of the same battle card are allowed in the same deck, this enforces that constraint
                    if (quantity < 3):
                        #increment quantity
                        quantity += 1
                        #add new quantity to treeview
                        self.target.model.setData(dataIndex, quantity)
                        print("The Quantity of: " + selectedCard.dataDict['name'] + " is now ", quantity)

                        #Add The Cards Data To The Totals Table
                        self.adjustTotal(self.target.cardData.index(selectedCard))
                    else:
                        print("Three copies of ",selectedCard.dataDict['name'], " have already been added to the deck")

                #if the card is not a battle card, than duplicate cards cannot be added
                else:
                    print("Duplicate Bot or Stratagem Cards Cannot Be Added")

            #If the card has not been added yet, add it to its proper selection section
            else:
                print("Adding: " + selectedCard.dataDict['name'] + " To the deck")
                #Add the card to the treeview
                self.target.addCard(selectedCard)

                #Add The Cards Data To The Totals Table
                self.adjustTotal(self.target.cardData.index(selectedCard))

           

        
        
    


            
          

            
        






            
            




