'''
Authors: Scott Field, Reece Harkness
Version: 2.0
Date: 4/19/2023
Program Name: Create_Database
Program Purpose: Create the database that the project will be using
'''
#import library
import sqlite3

#Creating Database Connection
db = sqlite3.connect('TransformersDatabase.db')

#Create Database
conn = db.cursor()



#Create Tranformer (Bot Cards) Tables

#Create Bot Table (Ordinary Transformer Bot Card)
sql = ""
sql += "Create TABLE IF NOT EXISTS Bot("
#Name and subName are compound Primary Keys
sql += "[name] TEXT," #Got Rid of Primary Key Here SQlite3 automatically defines primary key so it was unnecessary for me to do it here, as composite primary keys did not work as expected
sql += "[subName] TEXT," 
sql += "[cardType] TEXT,"
#A Transformer Bot Card Can Be Uniquely Identified By Its Name + Subname
sql += "[cost] INTEGER,"
sql += "[loyalty] TEXT,"
sql += "[path] TEXT"
sql += ")"
print(sql)
conn.execute(sql)

#Create BotMode Table (Stores data on Bot Side of Card)
sql = ""
sql += "Create TABLE IF NOT EXISTS BotMode("
sql += "[name] TEXT,"
sql += "[subName] TEXT,"
sql += "[traits] TEXT,"
sql += "[attack] INTEGER,"
sql += "[health] TEXT,"
sql += "[defense] INTEGER,"
sql += "[text] TEXT,"
#Foreign Key Must Be At The End Of The SQL Query
sql += "FOREIGN KEY([subName]) REFERENCES Bot([subName]),"
sql += "FOREIGN KEY([name]) REFERENCES Bot([name])"
sql += ")"
print(sql)
conn.execute(sql)

#Create AltMode Table (Stores data on Alt (Vehicle) Side of Card)
sql = ""
sql += "Create TABLE IF NOT EXISTS AltMode("
#Attach Altmode To Bot By The Foreign Key
sql += "[name] TEXT,"
sql += "[subName] TEXT,"
sql += "[traits] TEXT,"
sql += "[attack] INTEGER,"
sql += "[health] INTEGER,"
sql += "[defense] INTEGER,"
sql += "[text] TEXT,"
#Foreign Key Must Be At The End Of The SQL Query
sql += "FOREIGN KEY([subName]) REFERENCES Bot([subName]),"
sql += "FOREIGN KEY([name]) REFERENCES Bot([name])"
sql += ")"
print(sql)
conn.execute(sql)

#Create HeadMode Table (Stores data on Head Side of TitanMaster Card)
sql = ""
sql += "Create TABLE IF NOT EXISTS HeadMode("
sql += "[name] TEXT,"
sql += "[subName] TEXT,"
sql += "[text] TEXT," #Remember The Important Text in a HeadMode is where the name is on any other card
#Foreign Key Must Be At The End Of The SQL Query
sql += "FOREIGN KEY([subName]) REFERENCES Bot([subName]),"
sql += "FOREIGN KEY([name]) REFERENCES Bot([name])"
sql += ")"
print(sql)
conn.execute(sql)

#Create BodyMode Table (Stores data on Body Side of TitanMaster Card)
sql = ""
sql += "Create TABLE IF NOT EXISTS BodyMode("
sql += "[name] TEXT,"
sql += "[subName] TEXT,"
sql += "[traits] TEXT,"
sql += "[attack] INTEGER,"
sql += "[health] INTEGER,"
sql += "[defense] INTEGER,"
sql += "[text] TEXT,"
sql += "FOREIGN KEY([subName]) REFERENCES Bot([subName]),"
sql += "FOREIGN KEY([name]) REFERENCES Bot([name])"
sql += ")"
print(sql)
conn.execute(sql)

#Create Alt1Mode For Multiform Transformers (Bots)
sql = ""
sql += "Create TABLE IF NOT EXISTS Alt1Mode("
sql += "[name] TEXT,"
sql += "[subName] TEXT,"
sql += "[traits] TEXT,"
sql += "[attack] INTEGER,"
sql += "[health] INTEGER,"
sql += "[defense] INTEGER,"
sql += "[text] TEXT,"
#Foreign Key Must Be At The End Of The SQL Query
sql += "FOREIGN KEY([subName]) REFERENCES Bot([subName]),"
sql += "FOREIGN KEY([name]) REFERENCES Bot([name])"
sql += ")"
print(sql)
conn.execute(sql)

#Create Alt2Mode For Multiform Tranformers (Bots)
sql = ""
sql += "Create TABLE IF NOT EXISTS Alt2Mode("
sql += "[name] TEXT,"
sql += "[subName] TEXT,"
sql += "[traits] TEXT,"
sql += "[attack] INTEGER,"
sql += "[health] INTEGER,"
sql += "[defense] INTEGER,"
sql += "[text] TEXT,"
#Foreign Key Must Be At The End Of The SQL Query
sql += "FOREIGN KEY([subName]) REFERENCES Bot([subName]),"
sql += "FOREIGN KEY([name]) REFERENCES Bot([name])"
sql += ")"
print(sql)
conn.execute(sql)

#Create BattleUpgrade Table For Upgrade Side of Battle Master Transformers (Bots)
sql = ""
sql += "Create TABLE IF NOT EXISTS BattleUpgrade("
sql += "[name] TEXT,"
sql += "[subName] TEXT,"
sql += "[upgradeName] TEXT," #This is the name of the upgrade side of the Battle Master
sql += "[traits] TEXT,"
sql += "[subtype] TEXT,"
sql += "[attack] INTEGER,"
sql += "[defense] INTEGER,"
sql += "[text] TEXT,"
#Foreign Key Must Be At The End Of The SQL Query
sql += "FOREIGN KEY([subName]) REFERENCES Bot([subName]),"
sql += "FOREIGN KEY([name]) REFERENCES Bot([name])"
sql += ")"
print(sql)
conn.execute(sql)

#Create CombinerMode For Combiner Transformers (Bots)
sql = ""
sql += "Create TABLE IF NOT EXISTS CombinerMode("
sql += "[name] TEXT,"
sql += "[subName] TEXT,"
sql += "[traits] TEXT,"
sql += "[attack] INTEGER,"
sql += "[health] INTEGER,"
sql += "[defense] INTEGER,"
sql += "[text] TEXT,"
#Foreign Key Must Be At The End Of The SQL Query
sql += "FOREIGN KEY([subName]) REFERENCES Bot([subName]),"
sql += "FOREIGN KEY([name]) REFERENCES Bot([name])"
sql += ")"
print(sql)
conn.execute(sql)

#Create Battle Cards Tables

#Action Cards Tables

#Action Cards Table
sql = ""
sql += "Create TABLE IF NOT EXISTS Action("
sql += "[name] TEXT PRIMARY KEY,"
sql += "[icon] TEXT,"
sql += "[text] TEXT,"
sql += "[cost] INTEGER,"
sql += "[path] TEXT"
sql += ")"
print(sql)
conn.execute(sql)

#Secret Action Cards Table
sql = ""
sql += "Create TABLE IF NOT EXISTS SecretAction("
sql += "[name] TEXT PRIMARY KEY ,"
sql += "[icon] TEXT,"
sql += "[text] TEXT,"
sql += "[cost] INTEGER,"
sql += "[path] TEXT"
sql += ")"
print(sql)
conn.execute(sql)

#Upgrade Cards Table
sql = ""
sql += "Create TABLE IF NOT EXISTS Upgrade("
sql += "[name] TEXT PRIMARY KEY,"
sql += "[icon] TEXT,"
sql += "[subtype] TEXT,"
sql += "[attack] INTEGER,"
sql += "[defense] INTEGER,"
sql += "[text] TEXT,"
sql += "[cost] INTEGER,"
sql += "[path] TEXT"
sql += ")"
print(sql)
conn.execute(sql)


#Create Strategem Cards Table
sql = ""
sql += "Create TABLE IF NOT EXISTS Stratagem("
sql += "[name] TEXT PRIMARY KEY,"
sql += "[cost] INTEGER,"
sql += "[text] TEXT,"
sql += "[path] TEXT"
sql += ")"
print(sql)
conn.execute(sql)

#Commit Data To Database
db.commit()




