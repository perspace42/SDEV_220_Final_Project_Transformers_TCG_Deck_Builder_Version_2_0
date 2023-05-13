#Authors: Reece Harkness, 
#Deck_Managment.py
#Last updated: 5/12/23

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QFileDialog, QTreeView

class DeckBuilder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.filename = None
        self.deck_data = None
        
        # create the menu bar
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        new_action = QAction("New", self)
        new_action.triggered.connect(self.new)
        filemenu.addAction(new_action)
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open)
        filemenu.addAction(open_action)
        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save)
        filemenu.addAction(save_action)
        save_as_action = QAction("Save As", self)
        save_as_action.triggered.connect(self.save_as)
        filemenu.addAction(save_as_action)
        close_action = QAction("Close", self)
        close_action.triggered.connect(self.close)
        filemenu.addAction(close_action)
        
        # create a label to display deck data
        self.deck_label = QLabel(self)
        self.deck_label.setGeometry(10, 30, 400, 200)
        self.deck_label.setText("Deck data will appear here")
        
        # create a tree view
        self.tree_view = QTreeView(self)
        self.tree_view.setGeometry(10, 240, 400, 200)
        self.tree_view.setHeaderHidden(True)
        self.tree_view.setRootIsDecorated(False)
        
        # set the main window properties
        self.setGeometry(100, 100, 420, 450)
        self.setWindowTitle("Transformer TCG Deck Builder")
        
    def new(self):
        # implementation of new function
        pass
        
    def open(self):
        # implementation of open function
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filetypes = "Text files (*.txt);;All files (*)"
        filename, _ = QFileDialog.getOpenFileName(self, "Open Deck", "", filetypes, options=options)
        if filename:
            self.filename = filename
            with open(filename, "r") as f:
                self.deck_data = f.read()
                self.deck_label.setText(self.deck_data)
                
    def save(self):
        # implementation of save function
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.deck_data)
        else:
            self.save_as()
            
    def save_as(self):
        # implementation of save as function
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filetypes = "Text files (*.txt);;All files (*)"
        filename, _ = QFileDialog.getSaveFileName(self, "Save Deck As", "", filetypes, options=options)
        if filename:
            self.filename = filename
            with open(filename, "w") as f:
                f.write(self.deck_data)
                
    def close(self):
        # implementation of close function
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    deck_builder = DeckBuilder()
    
    # get user input for file path
    file_path, _ = QFileDialog.getOpenFileName(deck_builder, "Select Deck File", "", "Text files (*.txt);;All files (*)")
    if file_path:
        with open(file_path, "r") as f:
            deck_data = f.read()
            deck_builder.deck_data = deck_data
            deck_builder.deck_label.setText(deck_data)