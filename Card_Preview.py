'''
Author: Scott
Version: 2.1
Name: Card_Preview
Date: 05/09/2023
Purpose: Create a CardPreview class to add an image after a card is selected from the Card_Selection
'''

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem

class CardPreview(QGraphicsView):
    #Widget must be a QtWidgets.Qwidget
    def __init__(self,widget):
        super().__init__(widget)

        self.scene = QGraphicsScene()

    def addImage(self,imagePath):
        #clear any previous image
        self.scene.clear()
        #load the image
        pixmap = QPixmap(imagePath)
        #place the loaded image into an item the QGraphicsView can read
        pixmapItem = QGraphicsPixmapItem(pixmap)  
        #add the item to the QGraphicsScene
        self.scene.addItem(pixmapItem)
        #add the scene to the QGraphicsView
        self.setScene(self.scene)
        #show the QGraphicsView
        self.show()
        

