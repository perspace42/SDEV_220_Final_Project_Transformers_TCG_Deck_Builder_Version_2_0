# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TCG.ui'
#
# Created by: PyQt5 UI code generator 5.15.4

# Importing modules from PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Set the object name and resize the main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1134, 924)
        # Create a central widget and set its object name
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Create a QTabWidget and set its properties
        self.CardsList = QtWidgets.QTabWidget(self.centralwidget)
        self.CardsList.setGeometry(QtCore.QRect(0, -4, 313, 717))
        self.CardsList.setTabPosition(QtWidgets.QTabWidget.North)
        self.CardsList.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.CardsList.setMovable(False)
        self.CardsList.setObjectName("CardsList")
        # Create a QWidget and set its object name
        self.Bot = QtWidgets.QWidget()
        self.Bot.setObjectName("Bot")
        # Create a QTreeWidget and set its properties
        self.BotCardList = QtWidgets.QTreeWidget(self.Bot)
        self.BotCardList.setGeometry(QtCore.QRect(0, 220, 307, 471))
        self.BotCardList.setObjectName("BotCardList")
        self.BotCardList.headerItem().setText(0, "1")
        # Create a QCheckBox and set its properties
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
        # Create QLineEdit widgets and set their properties
        self.BotTextSearch = QtWidgets.QLineEdit(self.Bot)
        self.BotTextSearch.setGeometry(QtCore.QRect(80, 30, 141, 20))
        self.BotTextSearch.setObjectName("BotTextSearch")
        self.BotNameSearch = QtWidgets.QLineEdit(self.Bot)
        self.BotNameSearch.setGeometry(QtCore.QRect(80, 0, 141, 20))
        self.BotNameSearch.setObjectName("BotNameSearch")
        self.label_4 = QtWidgets.QLabel(self.Bot)
        self.label_4.setGeometry(QtCore.QRect(20, 0, 31, 21))
        #  Create Labels
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Bot)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.Bot)
        self.label_6.setGeometry(QtCore.QRect(20, 60, 47, 14))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.Bot)
        self.label_8.setGeometry(QtCore.QRect(20, 80, 47, 14))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.Bot)
        self.label_10.setGeometry(QtCore.QRect(20, 110, 51, 16))
        self.label_10.setObjectName("label_10")
        # Create QLineEdit widgets and set their properties
        self.BotAttackSearch = QtWidgets.QLineEdit(self.Bot)
        self.BotAttackSearch.setGeometry(QtCore.QRect(80, 60, 31, 20))
        self.BotAttackSearch.setObjectName("BotAttackSearch")
        self.BotDefenseSearch = QtWidgets.QLineEdit(self.Bot)
        self.BotDefenseSearch.setGeometry(QtCore.QRect(80, 80, 31, 20))
        self.BotDefenseSearch.setObjectName("BotDefenseSearch")
        self.BotHealthSearch = QtWidgets.QLineEdit(self.Bot)
        self.BotHealthSearch.setGeometry(QtCore.QRect(170, 60, 31, 20))
        self.BotHealthSearch.setObjectName("BotHealthSearch")
        # Create QComboBox widget for traits search and set its properties
        self.BotTraitsSearch = QtWidgets.QComboBox(self.Bot)
        self.BotTraitsSearch.setGeometry(QtCore.QRect(170, 80, 31, 20))
        self.BotTraitsSearch.setEditable(False)
        self.BotTraitsSearch.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.BotTraitsSearch.setObjectName("BotTraitsSearch")
        self.BotSidenameSearch = QtWidgets.QLineEdit(self.Bot)
        self.BotSidenameSearch.setGeometry(QtCore.QRect(80, 110, 141, 20))
        self.BotSidenameSearch.setObjectName("BotSidenameSearch")
        # Create QPushButton widget for search button and set its properties
        self.BotSearchButton = QtWidgets.QPushButton(self.Bot)
        self.BotSearchButton.setGeometry(QtCore.QRect(100, 170, 75, 23))
        self.BotSearchButton.setObjectName("BotSearchButton")
        self.label_7 = QtWidgets.QLabel(self.Bot)
        self.label_7.setGeometry(QtCore.QRect(130, 60, 47, 14))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.Bot)
        self.label_9.setGeometry(QtCore.QRect(130, 80, 47, 14))
        self.label_9.setObjectName("label_9")
        # Create QComboBox widget for mode search and set its properties
        self.BotModeSearch = QtWidgets.QComboBox(self.Bot)
        self.BotModeSearch.setGeometry(QtCore.QRect(80, 140, 141, 20))
        self.BotModeSearch.setObjectName("BotModeSearch")
        self.BotModeSearch.addItem("")
        self.BotModeSearch.addItem("")
        self.BotModeSearch.addItem("")
        # Create QLabel widgets for the battle search section
        self.label_15 = QtWidgets.QLabel(self.Bot)
        self.label_15.setGeometry(QtCore.QRect(20, 140, 47, 13))
        self.label_15.setObjectName("label_15")
        # Add a new tab for the battle section to the QTabWidget
        self.CardsList.addTab(self.Bot, "")
        # Create a QWidget object for the battle section
        self.Battle = QtWidgets.QWidget()
        self.Battle.setObjectName("Battle")
        # Create a QListWidget object to display the battle card list
        self.BattleCardList = QtWidgets.QListWidget(self.Battle)
        self.BattleCardList.setGeometry(QtCore.QRect(0, 220, 306, 471))
        self.BattleCardList.setObjectName("BattleCardList")
        # Create a QScrollBar object to scroll through the battle card list
        self.verticalScrollBar_3 = QtWidgets.QScrollBar(self.Battle)
        self.verticalScrollBar_3.setGeometry(QtCore.QRect(306, -1, 20, 471))
        self.verticalScrollBar_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_3.setObjectName("verticalScrollBar_3")
        # Create QLineEdit widgets for the battle search fields
        self.BattleNameSearch = QtWidgets.QLineEdit(self.Battle)
        self.BattleNameSearch.setGeometry(QtCore.QRect(80, 0, 141, 20))
        self.BattleNameSearch.setObjectName("BattleNameSearch")
        self.BattleTextSearch = QtWidgets.QLineEdit(self.Battle)
        self.BattleTextSearch.setGeometry(QtCore.QRect(80, 30, 141, 20))
        self.BattleTextSearch.setObjectName("BattleTextSearch")
        # Create QLabel widgets for the battle search field labels
        self.label_12 = QtWidgets.QLabel(self.Battle)
        self.label_12.setGeometry(QtCore.QRect(20, 0, 31, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.Battle)
        self.label_13.setGeometry(QtCore.QRect(20, 30, 51, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.Battle)
        self.label_14.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.label_14.setObjectName("label_14")
        self.BattleTypeSearch = QtWidgets.QComboBox(self.Battle)
        self.BattleTypeSearch.setGeometry(QtCore.QRect(80, 60, 141, 22))
        self.BattleTypeSearch.setObjectName("BattleTypeSearch")
        # Add empty items to combobox
        self.BattleTypeSearch.addItem("")
        self.BattleTypeSearch.addItem("")
        self.BattleTypeSearch.addItem("")
        self.BattleTypeSearch.addItem("")
        self.BattleTypeSearch.addItem("")
        self.BattleTypeSearch.addItem("")
        # Add and Configure Battle Search Button
        self.BattleSearchButton = QtWidgets.QPushButton(self.Battle)
        self.BattleSearchButton.setGeometry(QtCore.QRect(100, 170, 75, 23))
        self.BattleSearchButton.setObjectName("BattleSearchButton")

        # Add and Configure a Tabbed User Interface
        self.CardsList.addTab(self.Battle, "")
        self.Strategem = QtWidgets.QWidget()
        self.Strategem.setObjectName("Strategem")

        # Add and Configure a Vertical Scrollbar
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.Strategem)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(306, -1, 20, 471))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")

        # Add and Configure a List Widget for the Strategem Tab
        self.StrategemCardList = QtWidgets.QListWidget(self.Strategem)
        self.StrategemCardList.setGeometry(QtCore.QRect(0, 220, 306, 471))
        self.StrategemCardList.setObjectName("StrategemCardList")

        # Add and Configure a Line Edit Widget for Searching by Name in the Strategem Tab 
        self.StrategemNameSearch = QtWidgets.QLineEdit(self.Strategem)
        self.StrategemNameSearch.setGeometry(QtCore.QRect(80, 0, 141, 20))
        self.StrategemNameSearch.setObjectName("StrategemNameSearch")

        # Add and Configure a Line Edit Widget for Searching by Card Text in the Strategem Tab 
        self.StrategemTextSearch = QtWidgets.QLineEdit(self.Strategem)
        self.StrategemTextSearch.setGeometry(QtCore.QRect(80, 30, 141, 20))
        self.StrategemTextSearch.setObjectName("StrategemTextSearch")

        # Add and Configure Labels for the Strategem Tab
        self.label_16 = QtWidgets.QLabel(self.Strategem)
        self.label_16.setGeometry(QtCore.QRect(20, 0, 31, 21))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.Strategem)
        self.label_17.setGeometry(QtCore.QRect(20, 30, 51, 16))
        self.label_17.setObjectName("label_17")

        # Add and Configure a QLineEdit widget for Searching by SideName in the Strategem Tab
        self.StrategemSideNameSearch = QtWidgets.QLineEdit(self.Strategem)
        self.StrategemSideNameSearch.setGeometry(QtCore.QRect(80, 110, 141, 20))
        self.StrategemSideNameSearch.setObjectName("StrategemSideNameSearch")

        # Add and Configure Label for Strategem Tab
        self.label_18 = QtWidgets.QLabel(self.Strategem)
        self.label_18.setGeometry(QtCore.QRect(20, 110, 51, 16))
        self.label_18.setObjectName("label_18")

        # Add and Configure a QPushButton widget for executing the Search in the Strategem Tab
        self.StrategemSearchButton = QtWidgets.QPushButton(self.Strategem)
        self.StrategemSearchButton.setGeometry(QtCore.QRect(100, 170, 75, 23))
        self.StrategemSearchButton.setObjectName("StrategemSearchButton")

        # Raise all needed widgets to the top of the stack
        self.StrategemCardList.raise_()
        self.verticalScrollBar_2.raise_()
        self.StrategemNameSearch.raise_()
        self.StrategemTextSearch.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.StrategemSideNameSearch.raise_()
        self.label_18.raise_()
        self.StrategemSearchButton.raise_()

        
        # Add the Strategem widget to the CardsList tab stack
        self.CardsList.addTab(self.Strategem, "")

        # Add and Configure a QGraphicsView widget for displaying the selected card
        self.CardPreview = QtWidgets.QGraphicsView(self.centralwidget)
        self.CardPreview.setGeometry(QtCore.QRect(837, 220, 296, 471))
        self.CardPreview.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.CardPreview.setObjectName("CardPreview")

        # Add and Configure QTreeWidget
        self.SelectedBotCards = QtWidgets.QTreeWidget(self.centralwidget)
        self.SelectedBotCards.setGeometry(QtCore.QRect(326, 220, 241, 311))
        self.SelectedBotCards.setObjectName("SelectedBotCards")
        self.SelectedBotCards.headerItem().setText(0, "1")

        # Add and Configure QTableWidget
        self.SelectedBattleCards = QtWidgets.QTableWidget(self.centralwidget)
        self.SelectedBattleCards.setGeometry(QtCore.QRect(588, 220, 230, 441))
        self.SelectedBattleCards.setObjectName("SelectedBattleCards")
        self.SelectedBattleCards.setColumnCount(2)
        self.SelectedBattleCards.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.SelectedBattleCards.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SelectedBattleCards.setHorizontalHeaderItem(1, item)
        self.SelectedBattleCards.horizontalHeader().setDefaultSectionSize(20)
        self.SelectedBattleCards.horizontalHeader().setMinimumSectionSize(10)
        self.SelectedBattleCards.horizontalHeader().setStretchLastSection(True)

        
        # Add and configure QListWidget
        self.Totals = QtWidgets.QListWidget(self.centralwidget)
        self.Totals.setGeometry(QtCore.QRect(457, 660, 241, 89))
        self.Totals.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Totals.setObjectName("Totals")
        item = QtWidgets.QListWidgetItem()
        self.Totals.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Totals.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Totals.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Totals.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Totals.addItem(item)

        # Add and Configure Labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 200, 231, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 200, 231, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(840, 200, 231, 20))
        self.label_3.setObjectName("label_3")

        # Add and Configure a List Widget to hold selected Strategem Cards
        self.SelectedStrategemCards = QtWidgets.QListWidget(self.centralwidget)
        self.SelectedStrategemCards.setGeometry(QtCore.QRect(326, 551, 241, 110))
        self.SelectedStrategemCards.setObjectName("SelectedStrategemCards")

        # Add and Configurea label for the Selected Strategem Cards list widget
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(326, 532, 231, 16))
        self.label_11.setObjectName("label_11")

        # Add and Configure the Menu Bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1134, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)

        # Add and Configure the status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Add and Configure actions for File Menu
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

        # Add the actions to the File menu
        self.menubar.addAction(self.menuFile.menuAction())

        # Initialize and connect UI components
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
        self.label_4.setText(_translate("MainWindow", "Name:"))
        self.label_5.setText(_translate("MainWindow", "Card Text:"))
        self.label_6.setText(_translate("MainWindow", "Attack:"))
        self.label_8.setText(_translate("MainWindow", "Defense:"))
        self.label_10.setText(_translate("MainWindow", "SideName:"))
        self.BotSearchButton.setText(_translate("MainWindow", "Search"))
        self.label_7.setText(_translate("MainWindow", "Health:"))
        self.label_9.setText(_translate("MainWindow", "Traits:"))
        self.BotModeSearch.setItemText(0, _translate("MainWindow", "All Modes"))
        self.BotModeSearch.setItemText(1, _translate("MainWindow", "Bot Mode"))
        self.BotModeSearch.setItemText(2, _translate("MainWindow", "Alt Mode"))
        self.label_15.setText(_translate("MainWindow", "Mode:"))
        self.CardsList.setTabText(self.CardsList.indexOf(self.Bot), _translate("MainWindow", "Bot"))
        self.label_12.setText(_translate("MainWindow", "Name:"))
        self.label_13.setText(_translate("MainWindow", "Card Text:"))
        self.label_14.setText(_translate("MainWindow", "Card Type:"))
        self.BattleTypeSearch.setItemText(0, _translate("MainWindow", "All Types"))
        self.BattleTypeSearch.setItemText(1, _translate("MainWindow", "Action"))
        self.BattleTypeSearch.setItemText(2, _translate("MainWindow", "Secret Action"))
        self.BattleTypeSearch.setItemText(3, _translate("MainWindow", "Upgrade - Weapon"))
        self.BattleTypeSearch.setItemText(4, _translate("MainWindow", "Upgrade - Armor"))
        self.BattleTypeSearch.setItemText(5, _translate("MainWindow", "Upgrade - Utility"))
        self.BattleSearchButton.setText(_translate("MainWindow", "Search"))
        self.CardsList.setTabText(self.CardsList.indexOf(self.Battle), _translate("MainWindow", "Battle"))
        self.label_16.setText(_translate("MainWindow", "Name:"))
        self.label_17.setText(_translate("MainWindow", "Card Text:"))
        self.label_18.setText(_translate("MainWindow", "SideName:"))
        self.StrategemSearchButton.setText(_translate("MainWindow", "Search"))
        self.CardsList.setTabText(self.CardsList.indexOf(self.Strategem), _translate("MainWindow", "Strategem"))
        self.SelectedBattleCards.setSortingEnabled(False)
        item = self.SelectedBattleCards.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#"))
        item = self.SelectedBattleCards.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Card Name"))
        __sortingEnabled = self.Totals.isSortingEnabled()
        self.Totals.setSortingEnabled(False)
        item = self.Totals.item(0)
        item.setText(_translate("MainWindow", "Bot Cards:"))
        item = self.Totals.item(1)
        item.setText(_translate("MainWindow", "Strategem Cards:"))
        item = self.Totals.item(2)
        item.setText(_translate("MainWindow", "Battle Cards:"))
        item = self.Totals.item(3)
        item.setText(_translate("MainWindow", "Card Total:"))
        item = self.Totals.item(4)
        item.setText(_translate("MainWindow", "Point Total:"))
        self.Totals.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Selected Bot Cards"))
        self.label_2.setText(_translate("MainWindow", "Selected Battle Cards"))
        self.label_3.setText(_translate("MainWindow", "Card Preview"))
        self.label_11.setText(_translate("MainWindow", "Selected Strategem Cards"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionClose.setText(_translate("MainWindow", "Close"))

        # Initializes the application
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

