import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QAction, QTreeView, QFileSystemModel
from PyQt5.QtCore import Qt
from file_management_module import read_deck_from_file, write_deck_to_file

class TransformerDeckBuilder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transformer TCG Deck Builder")
        self.setGeometry(100, 100, 800, 600)
        
        # Create a menu bar and add menu items
        menubar = self.menuBar()
        filemenu = menubar.addMenu('File')
        
        # Create actions for each menu item
        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save)
        filemenu.addAction(save_action)
        
        save_as_action = QAction('Save As', self)
        save_as_action.triggered.connect(self.save_as)
        filemenu.addAction(save_as_action)
        
        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open)
        filemenu.addAction(open_action)
        
        new_action = QAction('New', self)
        new_action.triggered.connect(self.new)
        filemenu.addAction(new_action)
        
        close_action = QAction('Close', self)
        close_action.triggered.connect(self.close)
        filemenu.addAction(close_action)
        
        # Create a QTreeView widget to display card selection data
        self.tree_view = QTreeView()
        self.tree_view.setDragDropMode(QTreeView.InternalMove)
        self.tree_view.setDropIndicatorShown(True)
        self.tree_view.setHeaderHidden(True)
        self.tree_view.setSelectionMode(QTreeView.ExtendedSelection)
        self.setCentralWidget(self.tree_view)
        
        # Create a variable to store the deck data
        self.deck_data = None
        
        self.show()
    
    def save(self):
        if self.deck_data is None:
            self.save_as()
        else:
            filename = self.deck_data['filename']
            with open(filename, 'w') as f:
                pyqt5.dump(self.deck_data['cards'], f)
            QMessageBox.information(self, 'Saved', 'File saved successfully')
    
    def save_as(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Save Deck As', '', 'Deck files (*.deck)')
        if filename:
            with open(filename, 'w') as f:
                pyqt5.dump(self.deck_data['cards'], f)
            self.deck_data = {'filename': filename, 'cards': self.deck_data['cards']}
            QMessageBox.information(self, 'Saved', 'File saved successfully')
    
    def open(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open Deck', '', 'Deck files (*.deck)')
        if filename:
            try:
                with open(filename, 'r') as f:
                    cards = pyqt5.load(f)
                self.deck_data = {'filename': filename, 'cards': cards}
                QMessageBox.information(self, 'Open', 'File opened successfully')
            except:
                QMessageBox.warning(self, 'Error', 'Could not open file')
    
    def new(self):
        TransformerDeckBuilder()
    
    def close(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    td = TransformerDeckBuilder()
    sys.exit(app.exec_())