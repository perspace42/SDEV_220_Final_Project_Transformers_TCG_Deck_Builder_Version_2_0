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

        #Strategem Values (Values Almost Any Card Will Have)
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
        self.subType = dataDict.get("subType",None)
        self.icon = dataDict.get("icon",None)

    #string method for print function
    def __str__(self):
        return self.dataDict



class Card():
    '''Purpose of this class is to store the sides of a Transformers TCG Card that contain card data and the type of the card'''
    #define class
    def __init__(self,sideList,dataDict):
        #store the data on both sides of the card
        self.dataDict = dataDict
        #store the data unique to each side on the card
        self.sideList = sideList
        #get number of sides on the card
        self.size = len(sideList)
        
        #Store card Global Data (This data does not change when the card is flipped)
        self.cardType = dataDict.get("cardType", None)
        self.name = dataDict.get("name", None),
        self.subName = dataDict.get("subName",None),
        self.cost = dataDict.get("cost",None)
        self.loyalty = dataDict.get("loyalty",None)
        self.path = dataDict.get("path","error.png")
        

    #return a side if the sideName exists, else output an error and return None
    def getSide(self,name):

        for index in range(self.size):
            currentSide = self.sideList[index]

            if (name == currentSide.sideName):
                return currentSide
        
        print("Error side: " + name + " not found!!!")
        return None
    
    #string method for print function
    def __str__(self):
        #get global data from card
        outputString = str(self.dataDict) + "\n"
        #get unique data from sides for any number of sides
        for i in range(self.size):
            outputString += str(self.sideList[i].dataDict) + "\n"

        return outputString

#Function to test Card and Side Class
def test():
    '''Purpose of this class is to ensure that the data passed to a cards sides and global data is displayed correctly'''
    #Example Bot Card Definition

    #Define Bot Side
    botSide = Side({ 
         "sidename" : "Body", 
         "traits" : ["Ranged", "Leader"],
         "attack" : 5,
         "health" : 15,
         "defense": 1,
         "text" : "When you flip to this mode <arrow> This gets +2<attack> until end of turn"
         })
    
    #Define Vehicle Side
    vehicleSide = Side({
         "sidename" : "Alt", 
         "traits" : ["Ranged", "Leader","Tank"],
         "attack" : 4,
         "health" : 15,
         "defense": 3,
         "text" : "When this defends and you flip at least <orange> <arrow> Do 1 damage to the attacker after the battle"
         })
    
    #Add Sides To List Of Sides
    sideList = [botSide,vehicleSide]

    #Define Transformer With Side Data and Global Values
    testTransformer = Card(sideList,{
        "cardType" : "TitanMaster",
        "name" : "Megatron",
        "subName" : "Fallen Hero",
        "cost" : 11,
        "loyalty" : "Decepticon",
        "path" : "./img/bot/megatron_fallen_hero.jpg"
        })
    
    #print example bot card
    print(testTransformer)
    
#call test function
test()