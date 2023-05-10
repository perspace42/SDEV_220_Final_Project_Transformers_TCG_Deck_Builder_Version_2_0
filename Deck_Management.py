from PyQt5.QtWidgets import QTreeView, QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QModelIndex

class CardView(QTreeView):
    def __init__(self,parentWidget,imageWidget):
        super().__init__(parentWidget)

        #Create Treeview Items
        self.setRootIsDecorated(False)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.model = self.createDataModel(self)
        self.setModel(self.model)

        self.cardData = []
        self.imageWidget = imageWidget
        self.currentRow = 999

        self.clicked.connect(self.on_clicked)
        self.doubleClicked.connect(self.on_double_clicked)

    def save(self):
        filename = self.parent().filename
        if filename:
            # Save the card selection data to the file
            print(f"Saving card selection data to {Card_Selection.py}")
        else:
            self.saveAs()

    def saveAs(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(self.parent(),
                                                  "Save As",
                                                  "",
                                                  "All Files (*);;Text Files (*.txt)",
                                                  options=options)
        if filename:
            print(f"Saving card selection data to {Card_Selection.py}")
            self.parent().filename = filename

    def open(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self.parent(),
                                                  "Open",
                                                  "",
                                                  "All Files (*);;Text Files (*.txt)",
                                                  options=options)
        if filename:
            print(f"Reading deck data from {Card_Selection.py}")

    def new(self):
        # Open a new window of the Transformer TCG Deck Builder Program
        print("Opening a new window of the Transformer TCG Deck Builder Program")

    def close(self):
        result = QMessageBox.question(self.parent(),
                                       "Close",
                                       "Are you sure you want to close?",
                                       QMessageBox.Yes | QMessageBox.No,
                                       QMessageBox.No)
        if result == QMessageBox.Yes:
            # Open a new instance of the Transformers TCG Deck Builder Program
            # in the same window.
            print("Opening a new instance of the Transformer TCG Deck Builder Program in the same window.")
        else:
            pass
    def createDataModel(self,parent):
        #Create Header Labels for Treeview
        headers = ["Name","Type","Sub-Type","Rarity","Set","Set Number","Quantity"]
        #create data container for treeview
        model = QStandardItemModel(0, len(headers), parent)
        #set header labels for treeview
        model.setHorizontalHeaderLabels(headers)

        return model

    def on_clicked(self,index):
        #get selected row index
        self.currentRow = index.row()
        #get data stored in selected row
        selectedData = self.cardData[self.currentRow]
        #get image for the selected data
        image = QImage(selectedData["image"])
        #resize image to fit image widget
        pixmap = QPixmap.fromImage(image).scaled(self.imageWidget.width(),
                                                  self.imageWidget.height(),
                                                  Qt.KeepAspectRatio)
        #display image in image widget
        self.imageWidget.setPixmap(pixmap)

    def on_double_clicked(self,index):
        #get selected row index
        self.currentRow = index.row()
        #get data stored in selected row
        selectedData = self.cardData[self.currentRow]
        #get quantity of selected data
        quantity = selectedData["quantity"]
        #increment quantity of selected data
        selectedData["quantity"] = quantity + 1
        #update quantity of selected data in treeview
        self.model.setData(self.model.index(self.currentRow,6),str(selectedData["quantity"]))
        #update quantity of selected data in cardData
        self.cardData[self.currentRow] = selectedData

    
        #Add Card Data to Data Storage Container
        self.cardData.append(cardData)