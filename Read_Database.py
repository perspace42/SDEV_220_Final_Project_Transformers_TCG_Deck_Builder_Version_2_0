'''
Author: Scott Field
Version: 2.0
Date: 4/25/2023
Program Name: Read_Database
Program Purpose: Read the card data from the TransformersDatabase.db file
and convert it into the classes shown in the Card_Data.py File
'''

from Card_Data import *
import sqlite3

#Functions

#Get Number Of Table Rows
def numRows(conn,tableName):
    sql = "SELECT COUNT(*) FROM " + tableName
    rows = conn.execute(sql)
    results = conn.fetchall()
    return results[0][0]

#Get CardsFunctions

#Get Bot Cards By Type
def addBotCards(conn):
    #Initiailize Empty List
    botCardList = []
    #Initialize Empty Dictionaries To Store Card Values
    cardDict = {}

    #Bot Sides
    botSideDict = {}
    altSideDict = {}

    #Get All Bot Values
    sql = "SELECT * FROM Bot WHERE cardType = 'Bot'"
    conn.execute(sql)
    resultsBot = conn.fetchall()

    #Uncomment this to see the amount of data
    #print("Datasize: ", numRows(conn,"Bot"))

    for row in resultsBot:
        #Get Card Global Values (Do Not Usually Change Between Sides)
        cardDict = {
            "cardType" : row[2],
            "name" : row[0], #Name Can Change Between Sides, But this is rare, if it does a different name will be used in sideDict.
            "subName" : row[1],
            "cost" : row[3],
            "loyalty" : row[4],
            "path" : row[5]
        }

        #Get Bot Side of the card
        sql = "SELECT * FROM BotMode WHERE name='" + cardDict['name'] + "' AND subName='" + cardDict['subName'] + "'"
        conn.execute(sql)
        resultsBotMode = conn.fetchall()

        for botRow in resultsBotMode:
            botSideDict = {
                "sideName" : "Bot",
                "name" : botRow[0],
                "subName" : botRow[1],
                "traits" : botRow[2].split(), #Convert Traits Into A List Containing All Traits
                "attack" : botRow[3],
                "health" : botRow[4],
                "defense": botRow[5],
                "text" : botRow[6]
            }

        #Get Alt Side of the card
        sql = "SELECT * FROM AltMode WHERE name='" + cardDict['name'] + "' AND subName='" + cardDict['subName'] + "'"
        conn.execute(sql)
        resultsAltMode = conn.fetchall()

        for altRow in resultsAltMode:
            altSideDict = {
                "sideName" : "Alt",
                "name" : altRow[0],
                "subName" : altRow[1],
                "traits" : altRow[2].split(), #Convert Traits Into A List Containing All Traits
                "attack" : altRow[3],
                "health" : altRow[4],
                "defense": altRow[5],
                "text" : altRow[6]
            }

        #Add Dictionaries To Card Classes
        botSide = Side(botSideDict)
        altSide = Side(altSideDict)

        card = Card([botSide,altSide],cardDict)

        #Add Upgrades To The Bot Card List
        botCardList.append(card)

        #Uncomment This To See What Has Been Added
        #print("Database Data:")
        #print(row)
        #print("Card Data:")
        #print(card)

    #return list
    return botCardList


def addBotMultiformCards(conn):
    botCardList = []
    #Initialize Empty Dictionaries To Store Card Values
    cardDict = {}

    #Bot Sides
    botSideDict = {}
    alt1SideDict = {}
    alt2SideDict = {}

    #Get All Bot Values
    sql = "SELECT * FROM Bot WHERE cardType = 'Multiform'"
    conn.execute(sql)
    resultsBot = conn.fetchall()

    #Uncomment this to see the amount of data
    #print("Datasize: ", numRows(conn,"Bot"))

    for row in resultsBot:
        #Get Card Global Values (Do Not Usually Change Between Sides)
        cardDict = {
            "cardType" : row[2],
            "name" : row[0], #Name Can Change Between Sides, But this is rare, if it does a different name will be used in sideDict.
            "subName" : row[1],
            "cost" : row[3],
            "loyalty" : row[4],
            "path" : row[5]
        }

        #Get Bot Side of the card
        sql = "SELECT * FROM BotMode WHERE name='" + cardDict['name'] + "' AND subName='" + cardDict['subName'] + "'"
        conn.execute(sql)
        resultsBotMode = conn.fetchall()

        for botRow in resultsBotMode:
            botSideDict = {
                "sideName" : "Bot",
                "name" : botRow[0],
                "subName" : botRow[1],
                "traits" : botRow[2].split(), #Convert Traits Into A List Containing All Traits
                "attack" : botRow[3],
                "health" : botRow[4],
                "defense": botRow[5],
                "text" : botRow[6]
            }

        #Get Alt 1 Side of the card
        sql = "SELECT * FROM Alt1Mode WHERE name='" + cardDict['name'] + "' AND subName='" + cardDict['subName'] + "'"
        conn.execute(sql)
        resultsAlt1Mode = conn.fetchall()

        for alt1Row in resultsAlt1Mode:
            alt1SideDict = {
                "sideName" : "Alt1",
                "name" : alt1Row[0],
                "subName" : alt1Row[1],
                "traits" : alt1Row[2].split(), #Convert Traits Into A List Containing All Traits
                "attack" : alt1Row[3],
                "health" : alt1Row[4],
                "defense": alt1Row[5],
                "text" : alt1Row[6]
            }

        #Get Alt 2 Side of the card
        sql = "SELECT * FROM Alt2Mode WHERE name='" + cardDict['name'] + "' AND subName='" + cardDict['subName'] + "'"
        conn.execute(sql)
        resultsAlt2Mode = conn.fetchall()

        for alt2Row in resultsAlt2Mode:
            alt2SideDict = {
                "sideName" : "Alt2",
                "name" : alt2Row[0],
                "subName" : alt2Row[1],
                "traits" : alt2Row[2].split(), #Convert Traits Into A List Containing All Traits
                "attack" : alt2Row[3],
                "health" : alt2Row[4],
                "defense": alt2Row[5],
                "text" : alt2Row[6]
            }
        

        #Add Dictionaries To Card Classes
        botSide = Side(botSideDict)
        alt1Side = Side(alt1SideDict)
        alt2Side = Side(alt2SideDict)

        card = Card([botSide,alt1Side,alt2Side],cardDict)

        #Add Upgrades To The Battle Card List
        botCardList.append(card)

        #Uncomment This To See What Has Been Added
        #print("Database Data:\n")
        #print(row)
        #print("Card Data:\n")
        #print(card)

    #return list
    return botCardList


def addBotTitanMasterHeadCards(conn):
    botCardList = []
    #Initialize Empty Dictionaries To Store Card Values
    cardDict = {}

    #Titan Master Head Sides
    headSideDict = {}
    botSideDict = {}
   
    #Get All Titan Master Bot Cards that contain a Head Side
    sql = "SELECT * FROM Bot WHERE cardType = 'TitanMaster Head'"
    conn.execute(sql)
    resultsBot = conn.fetchall()

    #Uncomment this to see the amount of data
    #print("Datasize: ", numRows(conn,"Bot"))

    for row in resultsBot:
        #Get Card Global Values (Do Not Usually Change Between Sides)
        cardDict = {
            "cardType" : "TitanMaster Head",
            "name" : row[0], #Name Can Change Between Sides, But this is rare, if it does a different name will be used in sideDict.
            #note the subName (value of none is taking up the [1] spot)
            "cost" : row[3],
            "loyalty" : row[4],
            "path" : row[5]
        }

        #Get Bot Side of the card
        sql = "SELECT * FROM BotMode WHERE name='" + cardDict['name'] + "'" 
        conn.execute(sql)
        resultsBotMode = conn.fetchall()

        for botRow in resultsBotMode:
            botSideDict = {
                "sideName" : "Bot",
                "name" : botRow[0],
                #note the subName (value of none is taking up the [1] spot)
                "traits" : botRow[2].split(), #Convert Traits Into A List Containing All Traits
                "attack" : botRow[3],
                "health" : botRow[4],
                "defense": botRow[5],
                "text" : botRow[6]
            }

        #Get Alt Side of the card
        sql = "SELECT * FROM HeadMode WHERE name='" + cardDict['name'] + "'"
        conn.execute(sql)
        resultsHeadMode = conn.fetchall()

        for headRow in resultsHeadMode:
            headSideDict = {
                "sideName" : "Head",
                "name" : headRow[0],
                "text" : headRow[1]
            }

        #Add Dictionaries To Card Classes
        botSide = Side(botSideDict)
        headSide = Side(headSideDict)

        card = Card([botSide,headSide],cardDict)

        #Add Upgrades To The Bot Card List
        botCardList.append(card)

        #Uncomment This To See What Has Been Added
        #print("Database Data:\n")
        #print(row)
        #print("Card Data:\n")
        #print(card)

    #return list
    return botCardList


def addBotTitanMasterBodyCards(conn):
    botCardList = []
    #Initialize Empty Dictionaries To Store Card Values
    cardDict = {}

    #Bot Sides
    bodySideDict = {}
    altSideDict = {}

    #Get All Bot Values
    sql = "SELECT * FROM Bot WHERE cardType = 'TitanMaster Body'"
    conn.execute(sql)
    resultsBot = conn.fetchall()

    #Uncomment this to see the amount of data
    #print("Datasize: ", numRows(conn,"Bot"))

    for row in resultsBot:
        #Get Card Global Values (Do Not Usually Change Between Sides)
        cardDict = {
            "cardType" : row[2],
            "name" : row[0], #Name Can Change Between Sides, But this is rare, if it does a different name will be used in sideDict.
            "subName" : row[1],
            "cost" : row[3],
            "loyalty" : row[4],
            "path" : row[5]
        }

        #Get Bot Side of the card
        sql = "SELECT * FROM BodyMode WHERE name='" + cardDict['name'] + "' AND subName='" + cardDict['subName'] + "'"
        conn.execute(sql)
        resultsBodyMode = conn.fetchall()

        for bodyRow in resultsBodyMode:
            bodySideDict = {
                "sideName" : "Body",
                "name" : bodyRow[0],
                "subName" : bodyRow[1],
                "traits" : bodyRow[2].split(), #Convert Traits Into A List Containing All Traits
                "attack" : bodyRow[3],
                "health" : bodyRow[4],
                "defense": bodyRow[5],
                "text" : bodyRow[6]
            }

        #Get Alt Side of the card
        sql = "SELECT * FROM AltMode WHERE name='" + cardDict['name'] + "' AND subName='" + cardDict['subName'] + "'"
        conn.execute(sql)
        resultsAltMode = conn.fetchall()

        for altRow in resultsAltMode:
            altSideDict = {
                "sideName" : "Alt",
                "name" : altRow[0],
                "subName" : altRow[1],
                "traits" : altRow[2].split(), #Convert Traits Into A List Containing All Traits
                "attack" : altRow[3],
                "health" : altRow[4],
                "defense": altRow[5],
                "text" : altRow[6]
            }

        #Add Dictionaries To Card Classes
        bodySide = Side(bodySideDict)
        altSide = Side(altSideDict)

        card = Card([bodySide,altSide],cardDict)

        #Add Upgrades To The Bot Card List
        botCardList.append(card)

        #Uncomment This To See What Has Been Added
        #print("Database Data:\n")
        #print(row)
        #print("Card Data:\n")
        #print(card)

    #return list
    return botCardList


def addBotCombinerCards(conn):
    botCardList = []
    #Initialize Empty Dictionaries To Store Card Values
    cardDict = {}

    #Bot Sides
    combinerSideDict = {}
    

    #Get All Bot Values
    sql = "SELECT * FROM Bot WHERE cardType = 'Combiner'"
    conn.execute(sql)
    resultsBot = conn.fetchall()

    #Uncomment this to see the amount of data
    #print("Datasize: ", numRows(conn,"Bot"))

    for row in resultsBot:
        #Get Card Global Values (Do Not Usually Change Between Sides)
        cardDict = {
            "cardType" : row[2],
            "name" : row[0], #Name Can Change Between Sides, But this is rare, if it does a different name will be used in sideDict.
            "subName" : row[1],
            "cost" : row[3],
            "loyalty" : row[4],
            "path" : row[5]
        }

        #Get Bot Side of the card
        sql = "SELECT * FROM CombinerMode WHERE name='" + cardDict['name'] + "' AND subName='" + cardDict['subName'] + "'"
        conn.execute(sql)
        resultsBotMode = conn.fetchall()

        for botRow in resultsBotMode:
            combinerSideDict = {
                "sideName" : "Combiner",
                "name" : botRow[0],
                "subName" : botRow[1],
                "traits" : botRow[2].split(), #Convert Traits Into A List Containing All Traits
                "attack" : botRow[3],
                "health" : botRow[4],
                "defense": botRow[5],
                "text" : botRow[6]
            }
        
        #Add Dictionaries To Card Classes
        combinerSide = Side(combinerSideDict)
        card = Card([combinerSide],cardDict)

        #Add Upgrades To The Bot Card List
        botCardList.append(card)

        #Uncomment This To See What Has Been Added
        #print("Database Data:\n")
        #print(row)
        #print("Card Data:\n")
        #print(card)

    #return list
    return botCardList


def addBotPieceCards(conn):
    botCardList = []
    #Initialize Empty Dictionaries To Store Card Values
    cardDict = {}

    #Bot Sides
    botSideDict = {}
    altSideDict = {}

    #Get All Bot Values
    sql = "SELECT * FROM Bot WHERE cardType = 'BotPiece'"
    conn.execute(sql)
    resultsBot = conn.fetchall()

    #Uncomment this to see the amount of data
    #print("Datasize: ", numRows(conn,"Bot"))

    for row in resultsBot:
        #Get Card Global Values (Do Not Usually Change Between Sides)
        cardDict = {
            "cardType" : row[2],
            "name" : row[0], #Name Can Change Between Sides, But this is rare, if it does a different name will be used in sideDict.
            "subName" : row[1],
            "cost" : row[3],
            "loyalty" : row[4],
            "path" : row[5]
        }

        #Get Bot Side of the card
        sql = "SELECT * FROM BotMode WHERE name='" + cardDict['name'] + "' AND subName='" + cardDict['subName'] + "'"
        conn.execute(sql)
        resultsBotMode = conn.fetchall()

        for botRow in resultsBotMode:
            botSideDict = {
                "sideName" : "Bot",
                "name" : botRow[0],
                "subName" : botRow[1],
                "traits" : botRow[2].split(), #Convert Traits Into A List Containing All Traits
                "attack" : botRow[3],
                "health" : botRow[4],
                "defense": botRow[5],
                "text" : botRow[6]
            }

        #Get Alt Side of the card
        sql = "SELECT * FROM AltMode WHERE name='" + cardDict['name'] + "' AND subName='" + cardDict['subName'] + "'"
        conn.execute(sql)
        resultsAltMode = conn.fetchall()

        for altRow in resultsAltMode:
            altSideDict = {
                "sideName" : "Alt",
                "name" : altRow[0],
                "subName" : altRow[1],
                "traits" : altRow[2].split(), #Convert Traits Into A List Containing All Traits
                "attack" : altRow[3],
                "health" : altRow[4],
                "defense": altRow[5],
                "text" : altRow[6]
            }

        #Add Dictionaries To Card Classes
        botSide = Side(botSideDict)
        altSide = Side(altSideDict)

        #There are a few double sided combiner pieces in the game
        if (len(botSide.dataDict) != 0):
            #If both sides have value
            if (len(altSide.dataDict != 0)):
                #add them both to the card
                card = Card([botSide,altSide],cardDict)
            #if only the bot side has value add only it to the card
            else:
                card = Card([botSide],cardDict)

        #if only the altSide has value, add only that side
        else:
            card = Card([altSide],cardDict)

        

        #Add Upgrades To The Bot Card List
        botCardList.append(card)

        #Uncomment This To See What Has Been Added
        #print("Database Data:")
        #print(row)
        #print("Card Data:")
        #print(card)

    #return list
    return botCardList


def addBotBattleMasterCards(conn):
    botCardList = []
    #Initialize Empty Dictionaries To Store Card Values
    cardDict = {}

    #Bot Sides
    botSideDict = {}
    upgradeSideDict = {}

    #Get All Bot Values
    sql = "SELECT * FROM Bot WHERE cardType = 'Battle Master'"
    conn.execute(sql)
    resultsBot = conn.fetchall()

    #Uncomment this to see the amount of data
    #print("Datasize: ", numRows(conn,"Bot"))

    for row in resultsBot:
        #Get Card Global Values (Do Not Usually Change Between Sides)
        cardDict = {
            "cardType" : row[2],
            "name" : row[0], #Name Can Change Between Sides, But this is rare, if it does a different name will be used in sideDict.
            "subName" : row[1],
            "cost" : row[3],
            "loyalty" : row[4],
            "path" : row[5]
        }

        #Get Bot Side of the card
        sql = "SELECT * FROM BotMode WHERE name='" + cardDict['name'] + "' AND subName='" + cardDict['subName'] + "'"
        conn.execute(sql)
        resultsBotMode = conn.fetchall()

        for botRow in resultsBotMode:
            botSideDict = {
                "sideName" : "Bot",
                "name" : botRow[0],
                "subName" : botRow[1],
                "traits" : botRow[2].split(), #Convert Traits Into A List Containing All Traits
                "attack" : botRow[3],
                "health" : botRow[4],
                "defense": botRow[5],
                "text" : botRow[6]
            }

        #Get Alt Side of the card
        sql = "SELECT * FROM BattleUpgrade WHERE name='" + cardDict['name'] + "' AND subName='" + cardDict['subName'] + "'"
        conn.execute(sql)
        resultsUpgradeMode = conn.fetchall()

        for upgradeRow in resultsUpgradeMode:
            upgradeSideDict = {
                "sideName" : "Upgrade",
                "name" : upgradeRow[0],
                "subName" : upgradeRow[1],
                "upgradeName" : upgradeRow[2],
                "traits" : upgradeRow[3].split(), #Convert Traits Into A List Containing All Traits
                "subtype": upgradeRow[4],
                "attack" : upgradeRow[5],
                "defense": upgradeRow[6],
                "text" : upgradeRow[7]
            }

        #Add Dictionaries To Card Classes
        botSide = Side(botSideDict)
        upgradeSide = Side(upgradeSideDict)

        card = Card([botSide,upgradeSide],cardDict)

        #Add Upgrades To The Bot Card List
        botCardList.append(card)

        #Uncomment This To See What Has Been Added
        #print("Database Data:")
        #print(row)
        #print("Card Data:")
        #print(card)

    #return list
    return botCardList


#Get Battle Cards
def addUpgradeCards(conn):
    battleCardList = []
    #Initialize Empty Dictionaries To Store Card Values
    cardDict = {}
    sideDict = {}
    
    #Get All Upgrade Values
    sql = "SELECT * FROM Upgrade"
    conn.execute(sql)
    results = conn.fetchall()

    #Uncomment this to see the amount of data
    #print("Datasize: ", numRows(conn,"Upgrade"))

    for row in results:
        #Get Card Global Values (Do Not Usually Change Between Sides)
        cardDict = {
            "cardType" : "Upgrade",
            "name" : row[0], #Name Can Change Between Sides, But this is rare, if it does a different name will be used in sideDict.
            "cost" : row[6],
            "path" : row[7]
        }
        #Get Card Dependent Values (Can Change Between Sides)
        sideDict = {
            "sideName" : "Front", #note upgrade sidename is not written anywhere on card, it is just convienent to give it a name
            "name" : row[0],
            "icon" : row[1],
            "subType" : row[2],
            "attack" : row[3],
            "defense" : row[4],
            "text" : row[5]
        }

        #Add Dictionaries To Card Classes
        side = Side(sideDict)
        card = Card([side],cardDict)

        #Add Upgrades To The Battle Card List
        battleCardList.append(card)

        #Uncomment This To See What Has Been Added
        #print("Database Data:\n")
        #print(row)
        #print("Card Data:\n")
        #print(card)

    #return list
    return battleCardList
   
#Get Action Cards
def addActionCards(conn):
    battleCardList = []
    #Initialize Empty Dictionaries To Store Card Values
    cardDict = {}
    sideDict = {}
    
    #Get All Action Values
    sql = "SELECT * FROM Action"
    conn.execute(sql)
    results = conn.fetchall()

    #Uncomment This to see the amount of data
    #print("Datasize: ", numRows(conn,"Action"))
    for row in results:
        #Get Card Global Values (Do Not Usually Change Between Sides)
        cardDict = {
            "cardType" : "Action",
            "name" : row[0], #Name Can Change Between Sides, But this is rare, if it does a different name will be used in sideDict.
            "cost" : row[3],
            "path" : row[4]
        }
        #Get Card Dependent Values (Can Change Between Sides)
        sideDict = {
            "sideName" : "Front", #note action sidename is not written anywhere on card, it is just convienent to give it a name
            "name" : row[0],
            "icon" : row[1],
            "text" : row[2]
        }

        #Add Dictionaries To Card Classes
        side = Side(sideDict)
        card = Card([side],cardDict)

        #Add Upgrades To The Battle Card List
        battleCardList.append(card)

        #Uncomment This To See What Has Been Added
        #print("Database Data:")
        #print(row)
        #print("Card Data:")
        #print(card)

    #return list
    return battleCardList

#Get Secret Action Cards
def addSecretActionCards(conn):
    battleCardList = []
    #Initialize Empty Dictionaries To Store Card Values
    cardDict = {}
    sideDict = {}
    
    #Get All Action Values
    sql = "SELECT * FROM SecretAction"
    conn.execute(sql)
    results = conn.fetchall()

    #Uncomment This to see the amount of data
    #print("Datasize: ", numRows(conn,"SecretAction"))
    for row in results:
        #Get Card Global Values (Do Not Usually Change Between Sides)
        cardDict = {
            "cardType" : "Secret Action",
            "name" : row[0], #Name Can Change Between Sides, But this is rare, if it does a different name will be used in sideDict.
            "cost" : row[3],
            "path" : row[4]
        }
        #Get Card Dependent Values (Can Change Between Sides)
        sideDict = {
            "sideName" : "Front", #note action sidename is not written anywhere on card, it is just convienent to give it a name
            "name" : row[0],
            "icon" : row[1],
            "text" : row[2]
        }

        #Add Dictionaries To Card Classes
        side = Side(sideDict)
        card = Card([side],cardDict)

        #Add Upgrades To The Battle Card List
        battleCardList.append(card)

        #Uncomment This To See What Has Been Added
        #print("Database Data:")
        #print(row)
        #print("Card Data:")
        #print(card)

    #return list
    return battleCardList

#Add Stratagem Cards
def addStratagemCards(conn):
    stratagemCardList = []
    #Initialize Empty Dictionaries To Store Card Values
    cardDict = {}
    sideDict = {}
    
    #Get All Upgrade Values
    sql = "SELECT * FROM Stratagem"
    conn.execute(sql)
    results = conn.fetchall()

    #Uncomment This to see the amount of data
    #print("Datasize: ", numRows(conn,"Stratagem"))
    for row in results:
        #Get Card Global Values (Do Not Usually Change Between Sides)
        cardDict = {
            "cardType" : "Stratagem",
            "name" : row[0], #Name Can Change Between Sides, But this is rare, if it does a different name will be used in sideDict.
            "cost" : row[1],
            "path" : row[3]
        }
        #Get Card Dependent Values (Can Change Between Sides)
        sideDict = {
            "sideName" : "Front", #note sidename is not written anywhere on card, it is just convienent to give it a name
            "name" : row[0],
            "text" : row[2]
        }

        #Add Dictionaries To Card Classes
        side = Side(sideDict)
        card = Card([side],cardDict)

        #Add Upgrades To The Battle Card List
        stratagemCardList.append(card)

        #Uncomment This To See What Has Been Added
        #print("Database Data:")
        #print(row)
        #print("Card Data:")
        #print(card)

    #return list
    return stratagemCardList



#Create Database Connection
db = sqlite3.connect('TransformersDatabase.db')
#Create Database Cursor
conn = db.cursor()

botCardList = []
battleCardList = []
stratagemCardList = []

#Add Bot Cards
botCardList += addBotCards(conn)
botCardList += addBotMultiformCards(conn)
botCardList += addBotTitanMasterHeadCards(conn)
botCardList += addBotTitanMasterBodyCards(conn)

botCardList += addBotCombinerCards(conn)
botCardList += addBotPieceCards(conn)

botCardList += addBotBattleMasterCards(conn)



#Add Battle Cards
battleCardList += addUpgradeCards(conn)
battleCardList += addActionCards(conn)
battleCardList += addSecretActionCards(conn)

#Add Stratagem Cards
stratagemCardList += addStratagemCards(conn)

#Print Data Added To Lists

#Print All Added Bot Cards
print("All Bot Cards\n")
for i in range(len(botCardList)):
    print(botCardList[i])
    #print(botCardList[i].dataDict["traits"])
print("\n")

#Print All Added Battle Cards
print("All Battle Cards\n")
for i in range(len(battleCardList)):
    print(battleCardList[i])
print("\n")

#Print All Stratagem Cards
print("All Stratagem Cards\n")
for i in range(len(stratagemCardList)):
    print(stratagemCardList[i])
print("\n")


#Close database and cursor
conn.close()
db.close()




