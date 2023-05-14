# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TCG.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost if pyuic5 is
# run again.  Do not run pyuic again, at this stage in the project we need to be editing this file manually

# Original Author: Ashton Wood
# Fixed By: Scott Field

# editors note: the widgets are oranized to have the configuration above the self.centralwidget.setObjectName line.
# The following widgets would be separated in this fashion

# self.BotSearchButton = QtWidgets.QPushButton(self.Bot)
# self.BotSearchButton.setGeometry(QtCore.QRect(100, 220, 75, 23))
# self.BotSearchButton.setObjectName("BotSearchButton")

# self.BotHealthL = QtWidgets.QLabel(self.Bot)
# self.BotHealthL.setGeometry(QtCore.QRect(130, 90, 47, 14))
# self.BotHealthL.setObjectName("BotHealthL")

# self.BotTraitsL = QtWidgets.QLabel(self.Bot)
# self.BotTraitsL.setGeometry(QtCore.QRect(20, 164, 47, 14))
# self.BotTraitsL.setObjectName("BotTraitsL")

# The sections from top to bottom, contain the object widget, location on screen, and name.
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog

#import the custom classes and functions
from Card_Selection import *
from Card_Removal import *
from Card_Total import *
from Deck_File import *

import os


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):

        # Set the object name and resize the main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1134, 924)
        MainWindow.setFocusPolicy(QtCore.Qt.TabFocus)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.VerticalTabs)
        
        # Create the central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create a tab widget to display a list of cards
        self.CardsList = QtWidgets.QTabWidget(self.centralwidget)
        self.CardsList.setGeometry(QtCore.QRect(0, 200, 363, 500)) #313: 363
        self.CardsList.setAutoFillBackground(True)
        self.CardsList.setTabPosition(QtWidgets.QTabWidget.North)
        self.CardsList.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.CardsList.setUsesScrollButtons(True)
        self.CardsList.setMovable(False)
        self.CardsList.setObjectName("CardsList")

        #Define a label for the CardsList
        self.CardsListLabel = QtWidgets.QLabel(self.centralwidget)
        self.CardsListLabel.setGeometry(QtCore.QRect(5,180,231,20))
        self.CardsListLabel.setObjectName("CardsListLabel")

        # Create and configure the totals widget (Stores total number of points spent and cards added)
        self.Totals = Total(self.centralwidget)
        #90 was changed to 20
        self.Totals.setGeometry(QtCore.QRect(507, 30, 291, 170)) #241:291
        self.Totals.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Totals.setObjectName("Totals")

        # Create a widget for the bot and its components
        self.Bot = QtWidgets.QWidget()
        self.Bot.setObjectName("Bot")

        #Create Card Preview Image Display Section
        self.CardPreviewSection = CardPreview(self.centralwidget)
        
        #Card Preview Section Dimensions
        self.CardPreviewSection.setGeometry(QtCore.QRect(887, 20, 855, 950)) #805:855
        self.CardPreviewSection.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.CardPreviewSection.setObjectName("CardPreview")
        
        #Added Custom CardView Class To Replace TreeView 
        self.BotCardTree = CardView(self.Bot,self.CardPreviewSection)
        #By default the quantity of the data model is set to 2
        self.BotCardTree.createDataModel()
        self.BotCardTree.addData(self.BotCardTree.model,botCardList)
        
        #Drawing The CardView (TreeView)
        self.BotCardTree.setGeometry(QtCore.QRect(0, 0, 363, 477)) #313: 363
        self.BotCardTree.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.BotCardTree.setObjectName("BotCardTree")

        self.CardsList.addTab(self.Bot, "")

        #Added Custom CardView Class To Replace TreeView 
        self.Battle = QtWidgets.QWidget()
        self.Battle.setObjectName("Battle")
        
        self.BattleCardTree = CardView(self.Battle,self.CardPreviewSection)
        #By default the quantity of the data model is set to 2
        self.BattleCardTree.createDataModel()
        self.BattleCardTree.addData(self.BattleCardTree.model,battleCardList)

        #add BattleCardTree to window
        self.BattleCardTree.setGeometry(QtCore.QRect(0, 0, 363, 477)) 
        self.BattleCardTree.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.BattleCardTree.setObjectName("BattleCardTree")

        self.CardsList.addTab(self.Battle, "")

        # Create and configure the strategem tab
        #Added Custom CardView Class To Replace TreeView 
        self.Strategem = QtWidgets.QWidget()
        self.Strategem.setObjectName("Strategem")
        
        self.StrategemCardTree = CardView(self.Strategem,self.CardPreviewSection)
        #By default the quantity of the data model is set to 2
        self.StrategemCardTree.createDataModel()
        self.StrategemCardTree.addData(self.StrategemCardTree.model, stratagemCardList)

        #add StrategemCardTree to window
        self.StrategemCardTree.setGeometry(QtCore.QRect(0, 0, 363, 477)) 
        self.StrategemCardTree.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.StrategemCardTree.setObjectName("StrategemCardTree")

        self.CardsList.addTab(self.Strategem, "")

        #configure the section where selected bot and battle cards are placed
        self.SelectedBotCards = CardSelect(self.centralwidget,self.CardPreviewSection)
        self.SelectedBotCards.setGeometry(QtCore.QRect(376, 220, 241, 311))
        self.SelectedBotCards.setObjectName("SelectedBotCards")

        #Set Both CardViews To Add selected Card To SelectedBotCards when double clicked
        self.BotCardTree.setTarget(self.SelectedBotCards)
        self.SelectedBotCards.setTarget(self.SelectedBotCards)

        #Set Both CardViews to Add quantity of cards and cost of cards to the Totals Table
        self.BotCardTree.setTotal(self.Totals)
        self.SelectedBotCards.setTotal(self.Totals)


        self.SelectedBattleCards = CardSelect(self.centralwidget,self.CardPreviewSection)
        #add the quantity column to the selected battle cards CardView (by changing the model to include a third column)
        self.SelectedBattleCards.model = self.SelectedBattleCards.createDataModel(3)
        #set the model that has just been added
        self.SelectedBattleCards.setModel(self.SelectedBattleCards.model)

        self.SelectedBattleCards.setGeometry(QtCore.QRect(638, 220, 230, 441))
        self.SelectedBattleCards.setObjectName("SelectedBattleCards")

        #Set Both CardViews To Add selected Card to SelectedBattleCards when double clicked
        self.BattleCardTree.setTarget(self.SelectedBattleCards)
        self.SelectedBattleCards.setTarget(self.SelectedBattleCards)

        #Set Both CardViews to Add quantity of cards and cost of cards to the Totals Table
        self.BattleCardTree.setTotal(self.Totals)
        self.SelectedBattleCards.setTotal(self.Totals)

        self.SelectedBattleCards.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection) 

        # Create and configure widget showing selected strategem cards
        self.SelectedStrategemCards = CardSelect(self.centralwidget,self.CardPreviewSection)
        self.SelectedStrategemCards.setGeometry(QtCore.QRect(376, 551, 241, 110))
        self.SelectedStrategemCards.setObjectName("SelectedStrategemCards")

        #Set Both CardViews To Add selected Card to SelectedStrategemCards when double clicked
        self.StrategemCardTree.setTarget(self.SelectedStrategemCards)
        self.SelectedStrategemCards.setTarget(self.SelectedStrategemCards)

        #Set Both CardViews to Add quantity of cards and cost of cards to the Totals Table
        self.StrategemCardTree.setTotal(self.Totals)
        self.SelectedStrategemCards.setTotal(self.Totals)

        #configure label for the totals widget
        self.TotalsLabel = QtWidgets.QLabel(self.centralwidget)
        self.TotalsLabel.setGeometry(QtCore.QRect(507,10,231,20))
        self.TotalsLabel.setObjectName("TotalsLabel")

        # Add labels
        self.SelectedBotCardsL = QtWidgets.QLabel(self.centralwidget)
        self.SelectedBotCardsL.setGeometry(QtCore.QRect(380, 200, 231, 20))
        self.SelectedBotCardsL.setObjectName("SelectedBotCardsL")
        self.SelectedBattleCardsL = QtWidgets.QLabel(self.centralwidget)
        self.SelectedBattleCardsL.setGeometry(QtCore.QRect(640, 200, 231, 20))
        self.SelectedBattleCardsL.setObjectName("SelectedBattleCardsL")
        self.CardPreviewL = QtWidgets.QLabel(self.centralwidget)
        self.CardPreviewL.setGeometry(QtCore.QRect(890, 0, 231, 20)) #840: #890
        self.CardPreviewL.setObjectName("CardPreviewL")

        #Add A Label to the Selected Stratagem Cards Section
        #NOTE this needs be renamed as adding a _2 to the end of a variable is a terrible practice
        self.SelectedStrategemCardsLabel = QtWidgets.QLabel(self.centralwidget)
        self.SelectedStrategemCardsLabel.setGeometry(QtCore.QRect(376, 532, 231, 16))
        self.SelectedStrategemCardsLabel.setObjectName("SelectedStrategemCardsL")

        # Create and configure the menu bar and options
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1134, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #Inserting Actions Into File Menu

        #stores current File Name
        self.currentFile = ""

        #Save File
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(lambda func: [print("Saving: " + self.currentFile),self.saveDeck()])

        #Save File As
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_As.triggered.connect(lambda func: [print("Saving As: " + self.currentFile),self.saveDeckAs()])

        #New Window
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.triggered.connect(lambda func: self.newWindow())
        

        #Exit Window
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(lambda func: [print("Closing Window"),MainWindow.close()])

        #Open File
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(lambda func: [print("Opening File"),self.openDeck()])

        #Close File
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClose.triggered.connect(lambda func: [print("Closing File"),self.closeDeck()])

        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        #Add UI labels to UI
        self.retranslateUi(MainWindow)
        self.CardsList.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #Track MainWindow After Adding All of The Widgets To It
        self.MainWindow = MainWindow

    # Sets text and labels for UI
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Transformers TCG Deck Builder"))
        self.CardsList.setToolTip(_translate("MainWindow", "<html><head/><body><p>Battle Cards</p></body></html>"))
        self.CardsList.setTabText(self.CardsList.indexOf(self.Bot), _translate("MainWindow", "Bot"))
        self.CardsList.setTabText(self.CardsList.indexOf(self.Battle), _translate("MainWindow", "Battle"))
        self.CardsList.setTabText(self.CardsList.indexOf(self.Strategem), _translate("MainWindow", "Strategem"))
        self.SelectedBotCardsL.setText(_translate("MainWindow", "Selected Bot Cards"))
        self.SelectedBattleCardsL.setText(_translate("MainWindow", "Selected Battle Cards"))
        self.CardPreviewL.setText(_translate("MainWindow", "Card Preview"))
        self.SelectedStrategemCardsLabel.setText(_translate("MainWindow", "Selected Strategem Cards"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionClose.setText(_translate("MainWindow", "Close"))   
        self.actionOpen.setText(_translate("MainWindow","Open"))
        self.TotalsLabel.setText(_translate("MainWindow","Deck"))
        self.CardsListLabel.setText(_translate("MainWindow","Card List"))

    

    #File Menu Functions

    #Open a new empty window
    def newWindow(self):
        #print what just happened
        print("Opening New Window")
        #define a new user interface instance
        newUi = Ui_MainWindow()
        #define a new main window
        newMainWindow = QtWidgets.QMainWindow()
        #attach the user interface instance to the new main window
        newUi.setupUi(newMainWindow)
        #show the new main window
        newMainWindow.showMaximized()

    #Open a deck (formatted txt) file
    def openDeck(self):
        #set file options
        fileOptions = QFileDialog.Options()
        #set file type
        fileType = "Text Files (*.txt)"
        #get file name
        fileName = QFileDialog.getOpenFileName(MainWindow,"Open Deck","",fileType,options = fileOptions)
        #confirm file name is valid, if it is open it
        print(fileName[0])
        if (os.path.exists(fileName[0])):
            #set the current file equal to the file name
            #NOTE fileName is automatically returned as a tuple, [0] returns the string
            self.currentFile = fileName[0]
            #get the file Data, and convert it to an organized tuple containing several lists
            fileData = readFile(self.currentFile)
            #sort data into lists from the fileData
            
            

            #pull Bot Card path Data list from the provided list
            botData = fileData[0]
            
            #if their is data to pull
            if (fileData[1]!= None):
                #pull Battle Card path Data list from the provided list, and then from the from the tuple within that list
                battleData = fileData[1][0]
                #pull Battle Card quantity Data list from the provided list, and then from the from the tuple within that list
                battleQuantity = fileData[1][1]
            #otherwise inform the porgram that their is no data to pull
            else:
                battleData = None

            #pull Stratagem Card path data from the provided list
            stratagemData = fileData[2]

            #if the lists are not None (automatically happens when no data of that type is found), add the data from them into the treeviews

            #add bot cards if there are any
            if (botData != None):
                botData = cardsFromText(botData,botCardList)
                #iterate across the data, adding the cards to the treeview
                for index in range(len(botData)):
                    self.SelectedBotCards.checkCard(botData[index])

            #add battle cards if there are any
            if (battleData != None):
                battleData = cardsFromText(battleData,battleCardList)
                #iterate across the data, adding the cards to the treeview
                for index in range(len(battleData)):
                    #add the card a number of times equal to its quanity
                    for card in range(int(battleQuantity[index])):
                        self.SelectedBattleCards.checkCard(battleData[index])

            #add stratagem cards if there are any
            if (stratagemData != None):
                stratagemData = cardsFromText(stratagemData,stratagemCardList)
                #iterate across the data, adding the cards to the treeview
                for index in range(len(stratagemData)):
                    self.SelectedStrategemCards.checkCard(stratagemData[index])

    #Close a deck (formatted txt) file
    def closeDeck(self):
        #remove current file
        self.currentFile = ""
        #reset data
        
        #remove rows
        self.SelectedBotCards.model.removeRows(0,self.SelectedBotCards.model.rowCount())
        #remove cards
        self.SelectedBotCards.cardData = []
        #update treeview
        self.SelectedBotCards.reset()

        #remove rows
        self.SelectedBattleCards.model.removeRows(0,self.SelectedBattleCards.model.rowCount())
        #remove cards
        self.SelectedBattleCards.cardData = []
        #update treeview
        self.SelectedBattleCards.reset()

        #remove rows
        self.SelectedStrategemCards.model.removeRows(0,self.SelectedStrategemCards.model.rowCount())
        #remove cards
        self.SelectedStrategemCards.cardData = []
        #update treeview
        self.SelectedStrategemCards.reset()

        #clear the Totals table
        self.Totals.reset()
       
    #save a deck (formatted text) file as the file that the user inputs
    def saveDeckAs(self):
        #set file options
        fileOptions = QFileDialog.Options()
        #set file type
        fileType = "Text Files (*.txt)"
        #get file name
        fileName = QFileDialog.getSaveFileName(None,"Open Deck","",fileType,options = fileOptions)
        
        if (os.path.exists(fileName[0])):
            #store current File
            self.currentFile = fileName[0]
            #If there are any battle cards in the deck get both them and their quantity, otherwise set battleCards to None
            if len(self.SelectedBattleCards.cardData) == 0:
                battleTuple = None
            else:
                #get the cards and quantity of the cards
                battleCards = self.SelectedBattleCards.cardData
                battleQuantity = []
                #iterate across the treeview to find the quantity
                for currentRow in range(len(battleCards)):
                    dataIndex = (self.SelectedBattleCards.model.index(currentRow,2))
                    quantity = int(self.SelectedBattleCards.model.data(dataIndex,Qt.DisplayRole))
                    #add the quantity to the parallel list
                    battleQuantity.append(quantity)
                
                #add both lists to the battleTuple
                battleTuple = (battleCards,battleQuantity)

            #If there are any bot cards in the deck get them
            if len(self.SelectedBotCards.cardData) == 0:
                botCards = None
            else:
                botCards = self.SelectedBotCards.cardData

            #If there are any stratagem cards in the deck get them
            if len(self.SelectedStrategemCards.cardData) == 0:
                strategemCards = None
            else:
                strategemCards = self.SelectedStrategemCards.cardData


            #save the file
            saveFile(self.currentFile,botCards,battleTuple,strategemCards)

    #saves a deck (formatted text file) to the file the user has previously specified
    #if none has been specified the user is asked to submit a file
    def saveDeck(self):
        #if their is no current file
        if (self.currentFile == ""):
            #ask the user to input one before saving
            self.saveDeckAs()
        else:
            #If there are any battle cards in the deck get both them and their quantity, otherwise set battleCards to None
            if len(self.SelectedBattleCards.cardData) == 0:
                battleTuple = None
            else:
                #get the cards and quantity of the cards
                battleCards = self.SelectedBattleCards.cardData
                battleQuantity = []
                #iterate across the treeview to find the quantity
                for currentRow in range(len(battleCards)):
                    dataIndex = (self.SelectedBattleCards.model.index(currentRow,2))
                    quantity = int(self.SelectedBattleCards.model.data(dataIndex,Qt.DisplayRole))
                    #add the quantity to the parallel list
                    battleQuantity.append(quantity)
                
                #add both lists to the battleTuple
                battleTuple = (battleCards,battleQuantity)

            #If there are any bot cards in the deck get them
            if len(self.SelectedBotCards.cardData) == 0:
                botCards = None
            else:
                botCards = self.SelectedBotCards.cardData

            #If there are any stratagem cards in the deck get them
            if len(self.SelectedStrategemCards.cardData) == 0:
                strategemCards = None
            else:
                strategemCards = self.SelectedStrategemCards.cardData


            #save the file
            saveFile(self.currentFile,botCards,battleTuple,strategemCards)

if __name__ == "__main__":
    import sys
    #initialize application
    app = QtWidgets.QApplication(sys.argv)
    #setup main window
    MainWindow = QtWidgets.QMainWindow()
    #setup user interface
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #show main window
    MainWindow.showMaximized()
    #close app on exit
    sys.exit(app.exec_())
