'''
Author: Scott Field
Version: 1.0
Date: 4/10/2023
Program Name: Card_Data
Program Purpose: Create Classes and Functions For Displaying Card Data
This program is called by the TranformersTCG_Deck_Builder.py file
'''

class Side():
    '''Purpose of this class is to store the data on a side of a Transformers TCG Card'''
    def __init__(self,dataDict):
        self.dataDict = dataDict
        self.sideName = dataDict.get("sideName",None)

        #Strategem Values (Values Any Card Will Have)
        self.name = dataDict.get("name",None)
        self.text = dataDict.get('text',None)
        self.cost = dataDict.get('cost',0)
        self.imagePath = dataDict.get('path','error.png')
        
        #Bot Card Values
        self.subName = dataDict.get("subName",None)
        self.traits = dataDict.get('traits',None)

        self.attack = dataDict.get('attack',None)
        self.health = dataDict.get('health',None)
        self.defense = dataDict.get('defense',None)
        
        self.loyalty = dataDict.get('text',None)
        
        #Battle Card Values
        self.subType = dataDict.get("subtype",None)
        self.icon = dataDict.get("icon",None)



class Card():
    '''Purpose of this class is to store the sides of a Transformers TCG Card that contain card data and the type of the card'''

    #define class
    def __init__(self,sideList,cardType):
        #get number of sides on the card
        self.size = len(sideList)
        #get the type of card
        self.cardType = cardType
        #store the data on each side on the card
        self.sideList = sideList

    #return a side if the sideName exists, else output an error and return None
    def getSide(self,name):

        for index in range(self.size):
            currentSide = self.sideList[index]

            if (name == currentSide.sideName):
                return currentSide
        
        return None


def main():
    botSide = Side({})
    vehicleSide = Side({})
    sideList = [botSide,vehicleSide]

    testTransformer = Card(sideList,"Bot")
        