# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TCG.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost if pyuic5 is
# run again.  Do not run pyuic again, at this stage in the project we need to be editing this file manually

# Authors: Ashton Wood, Scott Field

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
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QWidget
#import the custom treeview
from Card_Selection import *


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
        self.CardsList.setGeometry(QtCore.QRect(0, -4, 313, 750))
        self.CardsList.setAutoFillBackground(True)
        self.CardsList.setTabPosition(QtWidgets.QTabWidget.South)
        self.CardsList.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.CardsList.setUsesScrollButtons(True)
        self.CardsList.setMovable(False)
        self.CardsList.setObjectName("CardsList")

        # Create a widget for the bot and its components
        self.Bot = QtWidgets.QWidget()
        self.Bot.setObjectName("Bot")

        #Create Card Preview Image Display Section
        self.CardPreviewSection = CardPreview(self.centralwidget)
        
        #The Dimensions Of This Section Have Been Fixed It Just Needs To Be Moved Farther Right
        self.CardPreviewSection.setGeometry(QtCore.QRect(837, 20, 805, 950))
        self.CardPreviewSection.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.CardPreviewSection.setObjectName("CardPreview")
        
        #Added Custom CardView Class To Replace TreeView 
        self.BotCardTree = CardView(self.Bot,self.CardPreviewSection)
        #By default the quantity of the data model is set to 2
        self.BotCardTree.createDataModel()
        self.BotCardTree.addData(self.BotCardTree.model,botCardList)
        

        #Drawing The CardView (TreeView)
        self.BotCardTree.setGeometry(QtCore.QRect(0, 250, 313, 477))
        self.BotCardTree.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.BotCardTree.setObjectName("BotCardTree")

        # Set object names and geometry for the checkboxes, line edits, and labels
        # and create checkboxes
        self.DecepticonCheckbox = QtWidgets.QCheckBox(self.Bot)
        self.DecepticonCheckbox.setGeometry(QtCore.QRect(230, 90, 81, 31))
        self.DecepticonCheckbox.setObjectName("DecepticonCheckbox")
        self.MercenaryCheckbox = QtWidgets.QCheckBox(self.Bot)
        self.MercenaryCheckbox.setGeometry(QtCore.QRect(230, 60, 81, 31))
        self.MercenaryCheckbox.setObjectName("MercenaryCheckbox")
        self.AutobotCheckbox = QtWidgets.QCheckBox(self.Bot)
        self.AutobotCheckbox.setGeometry(QtCore.QRect(230, 30, 81, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AutobotCheckbox.sizePolicy().hasHeightForWidth())
        self.AutobotCheckbox.setSizePolicy(sizePolicy)
        self.AutobotCheckbox.setObjectName("AutobotCheckbox")

        # Bot search labels and parameters
        self.BotTextSearch = QtWidgets.QLineEdit(self.Bot)
        self.BotTextSearch.setGeometry(QtCore.QRect(80, 60, 141, 20))
        self.BotTextSearch.setObjectName("BotTextSearch")
        self.BotNameSearch = QtWidgets.QLineEdit(self.Bot)
        self.BotNameSearch.setGeometry(QtCore.QRect(80, 0, 141, 20))
        self.BotNameSearch.setObjectName("BotNameSearch")
        self.BotNameL = QtWidgets.QLabel(self.Bot)
        self.BotNameL.setGeometry(QtCore.QRect(20, 0, 31, 21))
        self.BotNameL.setObjectName("BotNameL")
        self.BotSideNameL = QtWidgets.QLabel(self.Bot)
        self.BotSideNameL.setGeometry(QtCore.QRect(20, 135, 51, 16))
        self.BotSideNameL.setObjectName("BotSideNameL")
        self.BotAttackL = QtWidgets.QLabel(self.Bot)
        self.BotAttackL.setGeometry(QtCore.QRect(20, 90, 47, 14))
        self.BotAttackL.setObjectName("BotAttackL")
        self.BotDefenseL = QtWidgets.QLabel(self.Bot)
        self.BotDefenseL.setGeometry(QtCore.QRect(20, 110, 47, 14))
        self.BotDefenseL.setObjectName("BotDefenseL")
        self.BotCardTextL = QtWidgets.QLabel(self.Bot)
        self.BotCardTextL.setGeometry(QtCore.QRect(20, 60, 51, 16))
        self.BotCardTextL.setObjectName("BotCardTextL")
        self.BotAttackSearch = QtWidgets.QLineEdit(self.Bot)
        self.BotAttackSearch.setGeometry(QtCore.QRect(80, 90, 31, 20))
        self.BotAttackSearch.setObjectName("BotAttackSearch")
        self.BotDefenseSearch = QtWidgets.QLineEdit(self.Bot)
        self.BotDefenseSearch.setGeometry(QtCore.QRect(80, 110, 31, 20))
        self.BotDefenseSearch.setObjectName("BotDefenseSearch")
        self.BotHealthSearch = QtWidgets.QLineEdit(self.Bot)
        self.BotHealthSearch.setGeometry(QtCore.QRect(170, 90, 31, 20))
        self.BotHealthSearch.setObjectName("BotHealthSearch")
        self.BotSidenameSearch = QtWidgets.QLineEdit(self.Bot)
        self.BotSidenameSearch.setGeometry(QtCore.QRect(80, 135, 141, 20))
        self.BotSidenameSearch.setObjectName("BotSidenameSearch")
        self.BotSearchButton = QtWidgets.QPushButton(self.Bot)
        self.BotSearchButton.setGeometry(QtCore.QRect(100, 220, 75, 23))
        self.BotSearchButton.setObjectName("BotSearchButton")
        self.BotHealthL = QtWidgets.QLabel(self.Bot)
        self.BotHealthL.setGeometry(QtCore.QRect(130, 90, 47, 14))
        self.BotHealthL.setObjectName("BotHealthL")
        self.BotTraitsL = QtWidgets.QLabel(self.Bot)
        self.BotTraitsL.setGeometry(QtCore.QRect(20, 164, 47, 14))
        self.BotTraitsL.setObjectName("BotTraitsL")
        self.BotModeSearch = QtWidgets.QComboBox(self.Bot)
        self.BotModeSearch.setGeometry(QtCore.QRect(80, 190, 141, 20))
        self.BotModeSearch.setObjectName("BotModeSearch")
        self.BotModeSearch.addItem("")
        self.BotModeSearch.addItem("")
        self.BotModeSearch.addItem("")
        self.BotModeSearch.addItem("")
        self.BotModeSearch.addItem("")
        self.BotModeL = QtWidgets.QLabel(self.Bot)
        self.BotModeL.setGeometry(QtCore.QRect(20, 190, 47, 13))
        self.BotModeL.setObjectName("BotModeL")
        self.BotSubNameSearch = QtWidgets.QLineEdit(self.Bot)
        self.BotSubNameSearch.setGeometry(QtCore.QRect(80, 30, 141, 20))
        self.BotSubNameSearch.setObjectName("BotSubNameSearch")
        self.BotSubNameL = QtWidgets.QLabel(self.Bot)
        self.BotSubNameL.setGeometry(QtCore.QRect(20, 30, 51, 21))
        self.BotSubNameL.setObjectName("BotSubNameL")
        self.BotCostL = QtWidgets.QLabel(self.Bot)
        self.BotCostL.setGeometry(QtCore.QRect(130, 110, 47, 13))
        self.BotCostL.setObjectName("BotCostL")
        self.BotCostSearch = QtWidgets.QLineEdit(self.Bot)
        self.BotCostSearch.setGeometry(QtCore.QRect(170, 110, 31, 20))
        self.BotCostSearch.setObjectName("BotCostSearch")

        # Bot traits setup and paramters
        self.BotTraitsSearch = QtWidgets.QListWidget(self.Bot)
        self.BotTraitsSearch.setGeometry(QtCore.QRect(80, 160, 141, 21))
        self.BotTraitsSearch.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.BotTraitsSearch.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.BotTraitsSearch.setObjectName("BotTraitsSearch")
        item = QtWidgets.QListWidgetItem()
        self.BotTraitsSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.BotTraitsSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.BotTraitsSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.BotTraitsSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.BotTraitsSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.BotTraitsSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.BotTraitsSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.BotTraitsSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.BotTraitsSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.BotTraitsSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.BotTraitsSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.BotTraitsSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.BotTraitsSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.BotTraitsSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.BotTraitsSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.BotTraitsSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.BotTraitsSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.BotTraitsSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.BotTraitsSearch.addItem(item)
        self.CardsList.addTab(self.Bot, "")

        #Added Custom CardView Class To Replace TreeView 
        self.Battle = QtWidgets.QWidget()
        self.Battle.setObjectName("Battle")
        
        self.BattleCardTree = CardView(self.Battle,self.CardPreviewSection)
        #By default the quantity of the data model is set to 2
        self.BattleCardTree.createDataModel()
        self.BattleCardTree.addData(self.BattleCardTree.model,battleCardList)

        #add BattleCardTree to window
        self.BattleCardTree.setGeometry(QtCore.QRect(0, 250, 313, 477))
        self.BattleCardTree.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.BattleCardTree.setObjectName("BattleCardTree")

        # Battle search creation and parameters, with labels
        self.BattleNameSearch = QtWidgets.QLineEdit(self.Battle)
        self.BattleNameSearch.setGeometry(QtCore.QRect(80, 20, 141, 20))
        self.BattleNameSearch.setObjectName("BattleNameSearch")
        self.BattleTextSearch = QtWidgets.QLineEdit(self.Battle)
        self.BattleTextSearch.setGeometry(QtCore.QRect(80, 60, 141, 20))
        self.BattleTextSearch.setObjectName("BattleTextSearch")
        self.BattleNameL = QtWidgets.QLabel(self.Battle)
        self.BattleNameL.setGeometry(QtCore.QRect(20, 20, 31, 21))
        self.BattleNameL.setObjectName("BattleNameL")
        self.BattleCardTextL = QtWidgets.QLabel(self.Battle)
        self.BattleCardTextL.setGeometry(QtCore.QRect(20, 60, 51, 16))
        self.BattleCardTextL.setObjectName("BattleCardTextL")
        self.BattleCardTypeL = QtWidgets.QLabel(self.Battle)
        self.BattleCardTypeL.setGeometry(QtCore.QRect(20, 100, 61, 16))
        self.BattleCardTypeL.setObjectName("BattleCardTypeL")
        self.BattleTypeSearch = QtWidgets.QComboBox(self.Battle)
        self.BattleTypeSearch.setGeometry(QtCore.QRect(80, 100, 141, 22))
        self.BattleTypeSearch.setEditable(False)
        self.BattleTypeSearch.setObjectName("BattleTypeSearch")
        self.BattleTypeSearch.addItem("")
        self.BattleTypeSearch.addItem("")
        self.BattleTypeSearch.addItem("")
        self.BattleTypeSearch.addItem("")
        self.BattleTypeSearch.addItem("")
        self.BattleTypeSearch.addItem("")
        self.BattleTypeSearch.addItem("")
        self.BattleSearchButton = QtWidgets.QPushButton(self.Battle)
        self.BattleSearchButton.setGeometry(QtCore.QRect(100, 220, 75, 23))
        self.BattleSearchButton.setObjectName("BattleSearchButton")
        self.BattleIconL = QtWidgets.QLabel(self.Battle)
        self.BattleIconL.setGeometry(QtCore.QRect(20, 150, 47, 13))
        self.BattleIconL.setObjectName("BattleIconL")
        self.listWidget = QtWidgets.QListWidget(self.Battle)
        self.listWidget.setGeometry(QtCore.QRect(80, 150, 141, 21))
        self.listWidget.setAutoScroll(False)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
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
        self.StrategemCardTree.setGeometry(QtCore.QRect(0, 250, 313, 477))
        self.StrategemCardTree.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.StrategemCardTree.setObjectName("StrategemCardTree")

        # Strategem search creation and parameters, with labels
        self.StrategemNameSearch = QtWidgets.QLineEdit(self.Strategem)
        self.StrategemNameSearch.setGeometry(QtCore.QRect(80, 80, 141, 20))
        self.StrategemNameSearch.setObjectName("StrategemNameSearch")
        self.StrategemTextSearch = QtWidgets.QLineEdit(self.Strategem)
        self.StrategemTextSearch.setGeometry(QtCore.QRect(80, 150, 141, 20))
        self.StrategemTextSearch.setObjectName("StrategemTextSearch")
        self.StrategemNameL = QtWidgets.QLabel(self.Strategem)
        self.StrategemNameL.setGeometry(QtCore.QRect(20, 80, 31, 21))
        self.StrategemNameL.setObjectName("StrategemNameL")
        self.CardTextL = QtWidgets.QLabel(self.Strategem)
        self.CardTextL.setGeometry(QtCore.QRect(20, 150, 51, 16))
        self.CardTextL.setObjectName("CardTextL")
        self.StrategemSearchButton = QtWidgets.QPushButton(self.Strategem)
        self.StrategemSearchButton.setGeometry(QtCore.QRect(100, 220, 75, 23))
        self.StrategemSearchButton.setObjectName("StrategemSearchButton")
        self.CardsList.addTab(self.Strategem, "")

        #configure the section where selected bot and battle cards are placed
        self.SelectedBotCards = CardView(self.centralwidget,self.CardPreviewSection)
        self.SelectedBotCards.setGeometry(QtCore.QRect(326, 220, 241, 311))
        self.SelectedBotCards.setObjectName("SelectedBotCards")

        #Set Both CardViews To Add selected Card To SelectedBotCards when double clicked
        self.BotCardTree.setTarget(self.SelectedBotCards)
        self.SelectedBotCards.setTarget(self.SelectedBotCards)

        self.SelectedBattleCards = CardView(self.centralwidget,self.CardPreviewSection)
        #add the quantity column to the selected battle cards CardView (by changing the model to include a third column)
        self.SelectedBattleCards.model = self.SelectedBattleCards.createDataModel(3)
        #set the model that has just been added
        self.SelectedBattleCards.setModel(self.SelectedBattleCards.model)

        self.SelectedBattleCards.setGeometry(QtCore.QRect(588, 220, 230, 441))
        self.SelectedBattleCards.setObjectName("SelectedBattleCards")

        #Set Both CardViews To Add selected Card to SelectedBattleCards when double clicked
        self.BattleCardTree.setTarget(self.SelectedBattleCards)
        self.SelectedBattleCards.setTarget(self.SelectedBattleCards)

        self.SelectedBattleCards.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection) #what is the purpose of this line Ashton?

        # Create and configure widget showing selected strategem cards
        self.SelectedStrategemCards = CardView(self.centralwidget,self.CardPreviewSection)
        self.SelectedStrategemCards.setGeometry(QtCore.QRect(326, 551, 241, 110))
        self.SelectedStrategemCards.setObjectName("SelectedStrategemCards")

        #Set Both CardViews To Add selected Card to SelectedStrategemCards when double clicked
        self.StrategemCardTree.setTarget(self.SelectedStrategemCards)
        self.SelectedStrategemCards.setTarget(self.SelectedStrategemCards)

        # Create and configure the totals widget
        self.Totals = QtWidgets.QTreeView(self.centralwidget)
        self.Totals.setGeometry(QtCore.QRect(457, 660, 241, 91))
        self.Totals.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Totals.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.Totals.setObjectName("Totals")

        # Add labels
        self.SelectedBotCardsL = QtWidgets.QLabel(self.centralwidget)
        self.SelectedBotCardsL.setGeometry(QtCore.QRect(330, 200, 231, 20))
        self.SelectedBotCardsL.setObjectName("SelectedBotCardsL")
        self.SelectedBattleCardsL = QtWidgets.QLabel(self.centralwidget)
        self.SelectedBattleCardsL.setGeometry(QtCore.QRect(590, 200, 231, 20))
        self.SelectedBattleCardsL.setObjectName("SelectedBattleCardsL")
        self.CardPreviewL = QtWidgets.QLabel(self.centralwidget)
        self.CardPreviewL.setGeometry(QtCore.QRect(840, 0, 231, 20))
        self.CardPreviewL.setObjectName("CardPreviewL")

        #Add A Label to the Selected Stratagem Cards Section
        #NOTE this needs be renamed as adding a _2 to the end of a variable is a terrible practice
        self.SelectedStrategemCards_2 = QtWidgets.QLabel(self.centralwidget)
        self.SelectedStrategemCards_2.setGeometry(QtCore.QRect(326, 532, 231, 16))
        self.SelectedStrategemCards_2.setObjectName("SelectedStrategemCardsL")

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
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        #Add UI labels to UI
        self.retranslateUi(MainWindow)
        self.CardsList.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # Sets text and labels for UI
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CardsList.setToolTip(_translate("MainWindow", "<html><head/><body><p>Battle Cards</p></body></html>"))
        self.DecepticonCheckbox.setText(_translate("MainWindow", "Decepticons"))
        self.MercenaryCheckbox.setText(_translate("MainWindow", "Mercenaries"))
        self.AutobotCheckbox.setText(_translate("MainWindow", "AutoBots"))
        self.BotNameL.setText(_translate("MainWindow", "Name:"))
        self.BotSideNameL.setText(_translate("MainWindow", "SideName:"))
        self.BotAttackL.setText(_translate("MainWindow", "Attack:"))
        self.BotDefenseL.setText(_translate("MainWindow", "Defense:"))
        self.BotCardTextL.setText(_translate("MainWindow", "CardText:"))
        self.BotSearchButton.setText(_translate("MainWindow", "Search"))
        self.BotHealthL.setText(_translate("MainWindow", "Health:"))
        self.BotTraitsL.setText(_translate("MainWindow", "Traits:"))
        self.BotModeSearch.setItemText(0, _translate("MainWindow", "All Modes"))
        self.BotModeSearch.setItemText(1, _translate("MainWindow", "Bot Mode"))
        self.BotModeSearch.setItemText(2, _translate("MainWindow", "Alt Mode"))
        self.BotModeSearch.setItemText(3, _translate("MainWindow", "Alt 2"))
        self.BotModeSearch.setItemText(4, _translate("MainWindow", "Alt 3"))
        self.BotModeL.setText(_translate("MainWindow", "Mode:"))
        self.BotSubNameL.setText(_translate("MainWindow", "SubName:"))
        self.BotCostL.setText(_translate("MainWindow", "Cost:"))
        __sortingEnabled = self.BotTraitsSearch.isSortingEnabled()
        self.BotTraitsSearch.setSortingEnabled(False)
        item = self.BotTraitsSearch.item(0)
        item.setText(_translate("MainWindow", "Leader"))
        item = self.BotTraitsSearch.item(1)
        item.setText(_translate("MainWindow", "Titan"))
        item = self.BotTraitsSearch.item(2)
        item.setText(_translate("MainWindow", "TitanMaster"))
        item = self.BotTraitsSearch.item(3)
        item.setText(_translate("MainWindow", "BattleMaster"))
        item = self.BotTraitsSearch.item(4)
        item.setText(_translate("MainWindow", "Insecticon"))
        item = self.BotTraitsSearch.item(5)
        item.setText(_translate("MainWindow", "DinoBot"))
        item = self.BotTraitsSearch.item(6)
        item.setText(_translate("MainWindow", "AirStrikePatrol"))
        item = self.BotTraitsSearch.item(7)
        item.setText(_translate("MainWindow", "Melee"))
        item = self.BotTraitsSearch.item(8)
        item.setText(_translate("MainWindow", "Specialist"))
        item = self.BotTraitsSearch.item(9)
        item.setText(_translate("MainWindow", "Ranged"))
        item = self.BotTraitsSearch.item(10)
        item.setText(_translate("MainWindow", "Boat"))
        item = self.BotTraitsSearch.item(11)
        item.setText(_translate("MainWindow", "Motorcycle"))
        item = self.BotTraitsSearch.item(12)
        item.setText(_translate("MainWindow", "Car"))
        item = self.BotTraitsSearch.item(13)
        item.setText(_translate("MainWindow", "Truck"))
        item = self.BotTraitsSearch.item(14)
        item.setText(_translate("MainWindow", "Tank"))
        item = self.BotTraitsSearch.item(15)
        item.setText(_translate("MainWindow", "Train"))
        item = self.BotTraitsSearch.item(16)
        item.setText(_translate("MainWindow", "Helicopter"))
        item = self.BotTraitsSearch.item(17)
        item.setText(_translate("MainWindow", "Plane"))
        item = self.BotTraitsSearch.item(18)
        item.setText(_translate("MainWindow", "Spaceship"))
        self.BotTraitsSearch.setSortingEnabled(__sortingEnabled)
        self.CardsList.setTabText(self.CardsList.indexOf(self.Bot), _translate("MainWindow", "Bot"))
        self.BattleNameL.setText(_translate("MainWindow", "Name:"))
        self.BattleCardTextL.setText(_translate("MainWindow", "Card Text:"))
        self.BattleCardTypeL.setText(_translate("MainWindow", "Card Type:"))
        self.BattleTypeSearch.setItemText(0, _translate("MainWindow", "All Types"))
        self.BattleTypeSearch.setItemText(1, _translate("MainWindow", "Action"))
        self.BattleTypeSearch.setItemText(2, _translate("MainWindow", "Secret Action"))
        self.BattleTypeSearch.setItemText(3, _translate("MainWindow", "Weapon Armor"))
        self.BattleTypeSearch.setItemText(4, _translate("MainWindow", "Upgrade - Weapon"))
        self.BattleTypeSearch.setItemText(5, _translate("MainWindow", "Upgrade - Armor"))
        self.BattleTypeSearch.setItemText(6, _translate("MainWindow", "Upgrade - Utility"))
        self.BattleSearchButton.setText(_translate("MainWindow", "Search"))
        self.BattleIconL.setText(_translate("MainWindow", "Icon:"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "no icon"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "blue"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "orange"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "white"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "green"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "black"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.CardsList.setTabText(self.CardsList.indexOf(self.Battle), _translate("MainWindow", "Battle"))
        self.StrategemNameL.setText(_translate("MainWindow", "Name:"))
        self.CardTextL.setText(_translate("MainWindow", "Card Text:"))
        self.StrategemSearchButton.setText(_translate("MainWindow", "Search"))
        self.CardsList.setTabText(self.CardsList.indexOf(self.Strategem), _translate("MainWindow", "Strategem"))
        self.SelectedBotCardsL.setText(_translate("MainWindow", "Selected Bot Cards"))
        self.SelectedBattleCardsL.setText(_translate("MainWindow", "Selected Battle Cards"))
        self.CardPreviewL.setText(_translate("MainWindow", "Card Preview"))
        self.SelectedStrategemCards_2.setText(_translate("MainWindow", "Selected Strategem Cards"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionClose.setText(_translate("MainWindow", "Close"))       

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
