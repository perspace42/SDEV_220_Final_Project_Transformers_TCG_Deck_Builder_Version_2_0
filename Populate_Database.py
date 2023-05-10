'''
Author: Scott Field, Reece Harkness
Version: 2.0
Date: 4/26/2023
Program Name: Populate_Database
Program Purpose: Populate the database that the project will be using
'''


#import library
import sqlite3

#Print Added Data Function (Remember the database must be commited to before pulling its values)
def printData(conn,tableName):
  #Get Table
  sql = "SELECT * FROM " + tableName
  conn.execute(sql)
  #Get all Values Within The Table
  data = conn.fetchall()
  #Iterate Across Database Data To Get Values
  for item in data:
    print(item)


#Creating Database Connection
db = sqlite3.connect('TransformersDatabase.db')

#Create Database
conn = db.cursor()


#Action Cards

sql = "INSERT INTO Action(name,icon,text,cost,path) VALUES"
sql += "("
sql += "'Ancient Wisdom'," #Name
sql += "'Orange'," #Icon
sql += "'Scrap the top 2 cards of your deck. Put an Action and an Upgrade scapped this way into your hand. You may play Unleash Potential.'," #Text
sql += "0," #Cost
sql += "'./img/battle/ancient_wisdom.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Action(name,icon,text,cost,path) VALUES"
sql += "("
sql += "'Backup Plan'," #Name
sql += "'White'," #Icon
sql += "'Scrap your hand. Then draw 3 cards.'," #Text
sql += "0," #Cost
sql += "'./img/battle/backup_plan.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Action(name,icon,text,cost,path) VALUES"
sql += "("
sql += "'Counterespionage'," #Name
sql += "'Black Green'," #Icon
sql += "'Name an Action. Then look at you opponents hand and each face-down enemy Secret Action. Your opponent scraps each card among them with that name.'," #Text
sql += "0," #Cost
sql += "'./img/battle/counterespionage.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Action(name,icon,text,cost,path) VALUES"
sql += "("
sql += "'Equipment Enthusiast'," #Name
sql += "'White'," #Icon
sql += "'Draw a card for each of your Upgrades.'," #Text
sql += "0," #Cost
sql += "'./img/battle/equipment_enthusiast.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Action(name,icon,text,cost,path) VALUES"
sql += "("
sql += "'High Five'," #Name
sql += "'Green'," #Icon
sql += "'Choose 2 of your characters. If they share a trait, repair 1 damage from each of them. (Traits appear with icons under character names.)'," #Text
sql += "0," #Cost
sql += "'./img/battle/high_five.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Action(name,icon,text,cost,path) VALUES"
sql += "("
sql += "'One Shall Stand One Shall Fall'," #Name (Comma in the middle was removed to avoid problems with the database)
sql += "'None'," #Icon
sql += "'Choose one of your characters and an enemy character. Do 3 damage to each of them.'," #Text
sql += "0," #Cost
sql += "'./img/battle/one_shall_stand_one_shall_fall.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Action(name,icon,text,cost,path) VALUES"
sql += "("
sql += "'Rest And Relaxation'," #Name
sql += "'Green'," #Icon
sql += "'Repair 1 damage from one of your characters. (After each battle -> You may swap 1 card from your hand with one of your flipped Green cards)'," #Text
sql += "0," #Cost
sql += "'./img/battle/rest_and_relaxation.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Action(name,icon,text,cost,path) VALUES"
sql += "("
sql += "'Unleash Potential'," #Name
sql += "'Blue'," #Icon
sql += "'If you have played Ancient Wisdom this turn -> Choose a battle card you own from outside the game that has 1 point and put it into your hand.'," #Text
sql += "0," #Cost
sql += "'./img/battle/unleash_potential.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Action(name,icon,text,cost,path) VALUES"
sql += "("
sql += "'War Of Attrition'," #Name
sql += "'Blue Green'," #Icon
sql += "'Your opponent chooses one of their characters and does 1 damage to it. If this is the third War of Attrition you have played this turn -> Repair 3 damage from one of your characters. You may play another War of Attrition.'," #Text
sql += "0," #Cost
sql += "'./img/battle/war_of_attrition.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

#Upgrade Cards

sql = "INSERT INTO Upgrade(name,icon,subtype,attack,defense,text,cost,path) VALUES"
sql += "("
sql += "'Blast Shield'," #Name
sql += "'Blue'," #Icon
sql += "'Armor'," #Subtype
sql += "0," #Attack
sql += "2," #Defense
sql += "'After the upgraded character defends -> Scrap this card.'," #Text
sql += "0," #Cost
sql += "'./img/battle/blast_shield.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Upgrade(name,icon,subtype,attack,defense,text,cost,path) VALUES"
sql += "("
sql += "'Crystal Of Power'," #Name
sql += "'Black'," #Icon
sql += "'Weapon Armor'," #Subtype
sql += "3," #Attack
sql += "2," #Defense
sql += "'(This occupies 1 Weapon slot and 1 Armor slot.) When the upgraded character battles -> Scrap this card after the battle.'," #Text
sql += "0," #Cost
sql += "'./img/battle/crystal_of_power.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Upgrade(name,icon,subtype,attack,defense,text,cost,path) VALUES"
sql += "("
sql += "'Energized Field'," #Name
sql += "'Blue Blue'," #Icon
sql += "'Armor'," #Subtype
sql += "0," #Attack
sql += "1," #Defense
sql += "'When the upgraded character defends and you flip at least orange -> Do 1 damage to the attacker. (Your team and deck can have 25 point total.)'," #Text
sql += "1," #Cost
sql += "'./img/battle/energized_field.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Upgrade(name,icon,subtype,attack,defense,text,cost,path) VALUES"
sql += "("
sql += "'Handheld Blaster'," #Name
sql += "'Blue Blue'," #Icon
sql += "'Weapon'," #Subtype
sql += "0," #Attack
sql += "0," #Defense
sql += "'Bold 1 (Flip 1 more battle card when attacking.)'," #Text
sql += "0," #Cost
sql += "'./img/battle/handheld_blaster.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Upgrade(name,icon,subtype,attack,defense,text,cost,path) VALUES"
sql += "("
sql += "'Improvised Shield'," #Name
sql += "'Orange Orange'," #Icon
sql += "'Armor'," #Subtype
sql += "0," #Attack
sql += "0," #Defense
sql += "'Tough 1 (Flip 1 more battle card when defending.)'," #Text
sql += "0," #Cost
sql += "'./img/battle/improvised_shield.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Upgrade(name,icon,subtype,attack,defense,text,cost,path) VALUES"
sql += "("
sql += "'Mounted Missles'," #Name
sql += "'Orange Orange'," #Icon
sql += "'Weapon'," #Subtype
sql += "2," #Attack
sql += "0," #Defense
sql += "'This can be in an Armor or Utility slot. (Your team and deck can have 25 point total.)'," #Text
sql += "1," #Cost
sql += "'./img/battle/mounted_missiles.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Upgrade(name,icon,subtype,attack,defense,text,cost,path) VALUES"
sql += "("
sql += "'Recon System'," #Name
sql += "'Orange Blue'," #Icon
sql += "'Utility'," #Subtype
sql += "0," #Attack
sql += "0," #Defense
sql += "'When the upgraded character is battling -> Flip 1 battle card. Scrap one of the cards you flipped without using its battle icons. (Your team and deck can have 25 point total.)'," #Text
sql += "1," #Cost
sql += "'./img/battle/recon_system.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Upgrade(name,icon,subtype,attack,defense,text,cost,path) VALUES"
sql += "("
sql += "'Terrifying Resilience'," #Name
sql += "'Orange Black'," #Icon
sql += "'Armor'," #Subtype
sql += "0," #Attack
sql += "0," #Defense
sql += "'Cannot be put on Autobots. Tough 2 (Flip 2 more battle cards when defending.)'," #Text
sql += "0," #Cost
sql += "'./img/battle/terrifying_resilience.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Upgrade(name,icon,subtype,attack,defense,text,cost,path) VALUES"
sql += "("
sql += "'Unflinching Courage'," #Name
sql += "'Black Blue'," #Icon
sql += "'Weapon'," #Subtype
sql += "0," #Attack
sql += "0," #Defense
sql += "'Cannot be put on Decepticons. Bold 2 (Flip 2 more battle cards when attacking.)'," #Text
sql += "0," #Cost
sql += "'./img/battle/unflinching_courage.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()


#Secret Actions

sql = "INSERT INTO SecretAction(name,icon,text,cost,path) VALUES"
sql += "("
sql += "'Overheat'," #Name
sql += "'White'," #Icon
sql += "'Reveal -> When an enemy attacks and your opponent flips 7 or more battle cards. When Revealed -> This battle, orange does not add to attack and black does not give Pierce.'," #Text
sql += "0," #Cost
sql += "'./img/battle/overheat.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO SecretAction(name,icon,text,cost,path) VALUES"
sql += "("
sql += "'Sabataged Armaments'," #Name
sql += "'Blue'," #Icon
sql += "'Reveal -> When one of your characters defends. When Revealed -> Scrap all the attackers Weapons.'," #Text
sql += "0," #Cost
sql += "'./img/battle/sabotaged_armaments.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

#Bot Cards (And Bot Card Sides)

#Autobot Stylor
sql = "INSERT INTO Bot(name,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Autobot Stylor'," #Name
sql += "'TitanMaster Head'," #CardType
sql += "2," #Cost
sql += "'Autobot'," #Loyalty
sql += "'./img/bot/autobot_stylor.jpg'" #Image File Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BotMode(name,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Autobot Stylor'," #Name
sql += "'TitanMaster Ranged'," #Traits
sql += "2," #Attack
sql += "1," #Health
sql += "1," #Defense
sql += "'(This cannot flip.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO HeadMode(name,text) VALUES"
sql += "("
sql += "'Autobot Stylor'," #Name
sql += "'+1 Defense (This begins in head mode on the alt mode of a character that has a body mode. When that character is KO, even if it was your last character, deploy this to the battlefield in bot mode.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Captain Astrotrain
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Captain Astrotrain'," #Name
sql += "'Space Force-Transport'," #SubName
sql += "'Multiform'," #CardType
sql += "12," #Cost
sql += "'Decepticon'," #Loyalty
sql += "'./img/bot/captain_astrotrain.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BotMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Captain Astrotrain'," #Name
sql += "'Space Force-Transport'," #SubName
sql += "'Leader Specialist'," #Traits
sql += "6," #Attack
sql += "14," #Health
sql += "1," #Defense
sql += "'When this has at least 3 Upgrades and battles -> He gets +3 attack and +3 defense until end of battle.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Alt1Mode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Captain Astrotrain'," #Name
sql += "'Space Force-Transport'," #SubName
sql += "'Leader Spaceship Specialist'," #Traits
sql += "5," #Attack
sql += "14," #Health
sql += "2," #Defense
sql += "'When this has at least one Upgrade and defends -> He gets +1 defense until end of turn.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Alt2Mode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Captain Astrotrain'," #Name
sql += "'Space Force-Transport'," #SubName
sql += "'Leader Train Specialist'," #Traits
sql += "6," #Attack
sql += "14," #Health
sql += "2," #Defense
sql += "'When this has at least 2 Upgrades and attacks -> He gets +1 attack until end of turn.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Captain Impactor
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Captain Impactor'," #Name
sql += "'Special Ops-Wrecker'," #SubName
sql += "'Bot'," #CardType
sql += "7," #Cost
sql += "'Autobot'," #Loyalty
sql += "'./img/bot/captain_impactor.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BotMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Captain Impactor'," #Name
sql += "'Special Ops-Wrecker'," #SubName
sql += "'Leader Ranged'," #Traits
sql += "4," #Attack
sql += "12," #Health
sql += "1," #Defense
sql += "'Bold 1 (Flip 1 more battle card when attacking.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO AltMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Captain Impactor'," #Name
sql += "'Special Ops-Wrecker'," #SubName
sql += "'Leader Tank Ranged'," #Traits
sql += "3," #Attack
sql += "12," #Health
sql += "2," #Defense
sql += "'When you flip to this mode -> Each of your characters gets Bold 1 until end of turn. (Flip 1 more battle card when attacking.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Captain Omega Supreme
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Captain Omega Supreme'," #Name
sql += "'Transport-City Defender'," #SubName
sql += "'Combiner'," #CardType
sql += "22," #Cost
sql += "'Autobot'," #Loyalty
sql += "'./img/bot/captain_omega_supreme.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO CombinerMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Captain Omega Supreme'," #Name
sql += "'Transport-City Defender'," #SubName
sql += "'Leader Melee Ranged'," #Traits
sql += "7," #Attack
sql += "33," #Health
sql += "3," #Defense
sql += "'(This begins untapped, has all damage from the combined characters, and keeps 1 Upgrade in each slot.) Pierce 4 (Do at least 4 damage when attacking, but nor more than attack total.) When this attacks -> You may scrap 4 cards from your hand. If you do, scrap all the defenders Upgrades, then do 1 damage to each enemy.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Omega Supreme (Tank)
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Omega Supreme (Tank)'," #Name
sql += "'Transport-City Defender'," #SubName
sql += "'BotPiece'," #CardType
sql += "7," #Cost
sql += "'Autobot'," #Loyalty
sql += "'./img/bot/omega_supreme_tank.jpg'" #Image Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO AltMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Omega Supreme (Tank)'," #Name
sql += "'Transport-City Defender'," #SubName
sql += "'Tank Ranged'," #Traits
sql += "3," #Attack
sql += "9," #Health
sql += "2," #Defense
sql += "'When this attacks -> You may scrap 2 cards from your hand. If you do, do 1 damage to an enemy. When your opponent reshuffles their deck, if you have Omega Supreme (Spaceship) and Omega Supreme (Base) on the battlefield or in you KO area -> Combine them with this into Captain Omega Supreme.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Omega Supreme (Spaceship)
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Omega Supreme (Spaceship)'," #Name
sql += "'Transport-City Defender'," #SubName
sql += "'BotPiece'," #CardType
sql += "7," #Cost
sql += "'Autobot'," #Loyalty
sql += "'./img/bot/omega_supreme_spaceship.jpg'" #Image Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO AltMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Omega Supreme (Spaceship)'," #Name
sql += "'Transport-City Defender'," #SubName
sql += "'Spaceship Ranged'," #Traits
sql += "4," #Attack
sql += "12," #Health
sql += "0," #Defense
sql += "'When this attacks -> You may scrap 2 cards from your hand. If you do, scrap an enemy Upgrade. When your opponent reshuffles their deck, if you have Omega Supreme (Tank) and Omega Supreme (Base) on the battlefield or in you KO area -> Combine them with this into Captain Omega Supreme.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Omega Supreme (Base)
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Omega Supreme (Base)'," #Name
sql += "'Transport-City Defender'," #SubName
sql += "'BotPiece'," #CardType
sql += "8," #Cost
sql += "'Autobot'," #Loyalty
sql += "'./img/bot/omega_supreme_base.jpg'" #Image Path
sql += ")"

conn.execute(sql)
db.commit()
sql = "INSERT INTO AltMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Omega Supreme (Base)'," #Name
sql += "'Transport-City Defender'," #SubName
sql += "'Specialist'," #Traits
sql += "0," #Attack
sql += "12," #Health
sql += "1," #Defense
sql += "'When this defends -> Do 2 damage to the attacker. Your opponent scraps the top 2 cards of their deck. (This can combine with Omega Supreme Tank and Spaceship to form Captain Omega Supreme.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Chasm
sql = "INSERT INTO Bot(name,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Chasm'," #Name
sql += "'TitanMaster Head'," #CardType
sql += "4," #Cost
sql += "'Decepticon'," #Loyalty
sql += "'./img/bot/chasm.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BotMode(name,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Chasm'," #Name
sql += "'TitanMaster Melee'," #Traits
sql += "4," #Attack
sql += "4," #Health
sql += "0," #Defense
sql += "'(This cannot flip.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO HeadMode(name,text) VALUES"
sql += "("
sql += "'Chasm'," #Name
sql += "'+2 Attack (This begins in head mode on the alt mode of a character that has a body mode. When that character is KO, even if it was your last character, deploy this to the battlefield in bot mode.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Deadlock
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Deadlock'," #Name
sql += "'Soldier of Fortune'," #SubName
sql += "'Bot'," #CardType
sql += "9," #Cost
sql += "'Mercenary'," #Loyalty
sql += "'./img/bot/deadlock_soldier_of_fortune.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BotMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Deadlock'," #Name
sql += "'Soldier of Fortune'," #SubName
sql += "'Ranged'," #Traits
sql += "4," #Attack
sql += "12," #Health
sql += "0," #Defense
sql += "'When this does enough attack damage to KO an enemy -> Use this cards Bounty ability. Bounty -> Flip this and draw 2 cards.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO AltMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Deadlock'," #Name
sql += "'Soldier of Fortune'," #SubName
sql += "'Car Ranged'," #Traits
sql += "5," #Attack
sql += "12," #Health
sql += "0," #Defense
sql += "'Stealth against Autobots and Decepticons (Those enemies attack other characters if able.) When you flip to this mode -> Autobots and Decepticons cannot use Stealth this turn.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#General Optimus Prime
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'General Optimus Prime'," #Name
sql += "'Galactic Commander'," #SubName
sql += "'Bot'," #CardType
sql += "15," #Cost
sql += "'Autobot'," #Loyalty
sql += "'./img/bot/general_optimus_prime_galactic_commander.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BotMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'General Optimus Prime'," #Name
sql += "'Galactic Commander'," #SubName
sql += "'Leader Ranged'," #Traits
sql += "8," #Attack
sql += "21," #Health
sql += "2," #Defense
sql += "'This has 3 Utility slots. When this attacks and you flip at least orange blue -> You may play one of your flipped Upgrades onto this after battle.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO AltMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'General Optimus Prime'," #Name
sql += "'Galactic Commander'," #SubName
sql += "'Leader Truck Ranged'," #Traits
sql += "7," #Attack
sql += "21," #Health
sql += "2," #Defense
sql += "'This has 3 Utility slots. When you flip to this mode -> Reveal the top card of your deck. If it is an Action, you may play it.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Lord Megatron
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Lord Megatron'," #Name
sql += "'Conqueror of Cybertron'," #SubName
sql += "'Bot'," #CardType
sql += "12," #Cost
sql += "'Decepticon'," #Loyalty
sql += "'./img/bot/lord_megatron_conqueror_of_cybertron.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BotMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Lord Megatron'," #Name
sql += "'Conqueror of Cybertron'," #SubName
sql += "'Leader Ranged'," #Traits
sql += "4," #Attack
sql += "17," #Health
sql += "2," #Defense
sql += "'When your oppenent reshuffles their deck -> They choose one of their characters and do damage to it equal to this characters attack total.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO AltMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Lord Megatron'," #Name
sql += "'Conqueror of Cybertron'," #SubName
sql += "'Leader Tank Ranged'," #Traits
sql += "6," #Attack
sql += "17," #Health
sql += "3," #Defense
sql += "'When you flip to this mode -> Your opponent scraps a number of cards from the top of their deck equal to this characters defense total.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Megatron
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Megatron'," #Name
sql += "'Fallen Hero'," #SubName
sql += "'TitanMaster Body'," #CardType
sql += "11," #Cost
sql += "'Decepticon'," #Loyalty
sql += "'./img/bot/megatron_fallen_hero.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BodyMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Megatron'," #Name
sql += "'Fallen Hero'," #SubName
sql += "'Leader Ranged'," #Traits
sql += "5," #Attack
sql += "15," #Health
sql += "1," #Defense
sql += "'When you flip to this mode -> This gets +2 attack until end of turn.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO AltMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Megatron'," #Name
sql += "'Fallen Hero'," #SubName
sql += "'Leader Tank Ranged'," #Traits
sql += "4," #Attack
sql += "15," #Health
sql += "3," #Defense
sql += "'When this defends and you flip at least orange -> Do 1 damage to the attacker after the battle. (This begins with a character on him in head mode.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Optimus Prime
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Optimus Prime'," #Name
sql += "'Legendary Warrior'," #SubName
sql += "'TitanMaster Body'," #CardType
sql += "12," #Cost
sql += "'Autobot'," #Loyalty
sql += "'./img/bot/optimus_prime_legendary_warrior.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BodyMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Optimus Prime'," #Name
sql += "'Legendary Warrior'," #SubName
sql += "'Leader Ranged'," #Traits
sql += "6," #Attack
sql += "16," #Health
sql += "1," #Defense
sql += "'When this attacks -> Repair 1 damage from one of your characters. Then, if you have fewer characters on the battlefield than you opponent, repair 1 or more damage from that character.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO AltMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Optimus Prime'," #Name
sql += "'Legendary Warrior'," #SubName
sql += "'Leader Truck Ranged'," #Traits
sql += "5," #Attack
sql += "16," #Health
sql += "2," #Defense
sql += "'When you flip to this mode -> Draw a card. Then, if you have fewer cards in hand than your other opponent, draw another card. (This begins with a character on him in head mode.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Private Firedrive
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Private Firedrive'," #Name
sql += "'Ground Command-Artillery'," #SubName
sql += "'Battle Master'," #CardType
sql += "7," #Cost
sql += "'Autobot'," #Loyalty
sql += "'./img/bot/private_firedrive.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BattleUpgrade(name,subName,upgradeName,traits,subType,attack,defense,text) VALUES"
sql += "("
sql += "'Private Firedrive'," #Name
sql += "'Ground Command-Artillery'," #SubName
sql += "'Duo-Charge Electrostatic Photon Cannon'," #upgradeName
sql += "'BattleMaster'," #Traits
sql += "'Weapon'," #subType
sql += "3," #Attack
sql += "0," #Defense
sql += "'When the upgraded character attacks -> Scrap any number of cards from your hand. For each one scrapped this way, the upgraded character gets +1 attack until end of turn. If this would leave the battlefield -> Put it into your KO area instead.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BotMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Private Firedrive'," #Name
sql += "'Ground Command-Artillery'," #SubName
sql += "'BattleMaster Ranged'," #Traits
sql += "3," #Attack
sql += "10," #Health
sql += "0," #Defense
sql += "'When this attacks -> Draw a card. (A Battle Master begins in bot mode and cannot flip. When it is KO, play its Upgrade side.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Private Lionizer
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Private Lionizer'," #Name
sql += "'Ground Command-Artillery'," #SubName
sql += "'Battle Master'," #CardType
sql += "7," #Cost
sql += "'Autobot'," #Loyalty
sql += "'./img/bot/private_lionizer.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BattleUpgrade(name,subName,upgradeName,traits,subType,attack,defense,text) VALUES"
sql += "("
sql += "'Private Lionizer'," #Name
sql += "'Ground Command-Artillery'," #SubName
sql += "'RS Firesteel Saber'," #upgradeName
sql += "'BattleMaster'," #Traits
sql += "'Weapon'," #subType
sql += "0," #Attack
sql += "0," #Defense
sql += "'Bold 4 (Flip 4 more battle cards when attacking.) When the upgraded character attacks -> Plan 1 (You may put 1 card from your hand on top of your deck.) If this would leave the battlefield -> Put it into your KO area instead.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BotMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Private Firedrive'," #Name
sql += "'Ground Command-Artillery'," #SubName
sql += "'BattleMaster Melee'," #Traits
sql += "0," #Attack
sql += "8," #Health
sql += "2," #Defense
sql += "'Bold 4 (Flip 4 more battle cards when attacking.) (A Battle Master beigns in bot mode and cannot flip. When it is KO, play its Upgrade side.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Private Pterazadon
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Private Pterazadon'," #Name
sql += "'Air Command-Artillery'," #SubName
sql += "'Battle Master'," #CardType
sql += "6," #Cost
sql += "'Autobot'," #Loyalty
sql += "'./img/bot/private_pteraxadon.png'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BattleUpgrade(name,subName,upgradeName,traits,subType,attack,defense,text) VALUES"
sql += "("
sql += "'Private Pterazadon'," #Name
sql += "'Air Command-Artillery'," #SubName
sql += "'Binary Edgewing Scythe'," #upgradeName
sql += "'BattleMaster'," #Traits
sql += "'Weapon'," #subType
sql += "3," #Attack
sql += "0," #Defense
sql += "'(A Battle Master begins in bot mode and cannot flip. When it is KO, play its Upgrade side.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BotMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Private Pterazadon'," #Name
sql += "'Air Command-Artillery'," #SubName
sql += "'BattleMaster Melee'," #Traits
sql += "3," #Attack
sql += "9," #Health
sql += "0," #Defense
sql += "'When the upgraded character attack and you flip at least white white -> The defenders base defense becomes 0 during this battle. If this would leave the battlefield -> Put it into your KO area instead.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Private Tote
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Private Tote'," #Name
sql += "'Special Ops-Infiltration'," #SubName
sql += "'Bot'," #CardType
sql += "4," #Cost
sql += "'Autobot'," #Loyalty
sql += "'./img/bot/private_tote.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BotMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Private Tote'," #Name
sql += "'Special Ops-Infiltration'," #SubName
sql += "'Off-RoadPatrol Melee'," #Traits
sql += "2," #Attack
sql += "5," #Health
sql += "1," #Defense
sql += "'-->,Scrap a black card from your hand -> Untap one of your characters that has 6 stars or fewer. (To -->, tap this character before you attack.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO AltMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Private Tote'," #Name
sql += "'Special Ops-Infiltration'," #SubName
sql += "'Off-RoadPatrol Truck Melee'," #Traits
sql += "2," #Attack
sql += "5," #Health
sql += "1," #Defense
sql += "'This has Stealth while untapped. (Enemies attack other characters if able.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Raider Aimless
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Raider Aimless'," #Name
sql += "'Air Force-Weapons'," #SubName
sql += "'Battle Master'," #CardType
sql += "7," #Cost
sql += "'Decepticon'," #Loyalty
sql += "'./img/bot/raider_aimless.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BattleUpgrade(name,subName,upgradeName,traits,subType,attack,defense,text) VALUES"
sql += "("
sql += "'Raider Aimless'," #Name
sql += "'Air Force-Weapons'," #SubName
sql += "'Manifold Ion Particle Blaster'," #upgradeName
sql += "'BattleMaster Ranged'," #Traits
sql += "'Weapon'," #subType
sql += "3," #Attack
sql += "0," #Defense
sql += "'Tough 3 (Flip 3 more battle cards when defending.) (A Battle Master begins in bot mode and cannot flip. When it is KO, play its Upgrade side.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BotMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Raider Aimless'," #Name
sql += "'Air Force-Weapons'," #SubName
sql += "'BattleMaster Ranged'," #Traits
sql += "3," #Attack
sql += "8," #Health
sql += "0," #Defense
sql += "'When the upgraded character attack and you flip at least blue blue blue -> Do 3 damage to the defender. If this would leave the battlefield -> Put it into your KO area instead.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Raider Apeface
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Raider Apeface'," #Name
sql += "'Espionage-Commando'," #SubName
sql += "'Multiform'," #CardType
sql += "10," #Cost
sql += "'Decepticon'," #Loyalty
sql += "'./img/bot/raider_apeface.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BotMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Raider Apeface'," #Name
sql += "'Espionage-Commando'," #SubName
sql += "'Ranged'," #Traits
sql += "5," #Attack
sql += "14," #Health
sql += "1," #Defense
sql += "'While this has 10 or more damage counter -> He has Tough 3. (Flip 3 more battle cards when defending.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Alt1Mode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Raider Apeface'," #Name
sql += "'Espionage-Commando'," #SubName
sql += "'Plane Ranged'," #Traits
sql += "5," #Attack
sql += "14," #Health
sql += "1," #Defense
sql += "'While this is undamaged -> He has Focus 1. (Before flipping battle cards when battling -> Look at the top card of your deck. You may scrap it.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Alt2Mode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Raider Apeface'," #Name
sql += "'Espionage-Commando'," #SubName
sql += "'Beast Melee'," #Traits
sql += "5," #Attack
sql += "14," #Health
sql += "1," #Defense
sql += "'While this has 1 to 9 damage counters -> He has Bold 2. (Flip 2 more battle cards when attacking.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Raider Blowpipe
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Raider Blowpipe'," #Name
sql += "'Air Force-Weapons'," #SubName
sql += "'Battle Master'," #CardType
sql += "5," #Cost
sql += "'Decepticon'," #Loyalty
sql += "'./img/bot/raider_blowpipe.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BattleUpgrade(name,subName,upgradeName,traits,subType,attack,defense,text) VALUES"
sql += "("
sql += "'Raider Blowpipe'," #Name
sql += "'Air Force-Weapons'," #SubName
sql += "'Dual-Impact Shatterblast Compression Cannon'," #upgradeName
sql += "'BattleMaster'," #Traits
sql += "'Weapon'," #subType
sql += "0," #Attack
sql += "0," #Defense
sql += "'When the upgraded character attacks and you flip battle cards -> It gets +1 attack until end of turn for each different color among battle icons you flipped. If this would leave the battlefield -> Put it into your KO area instead.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BotMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Raider Blowpipe'," #Name
sql += "'Air Force-Weapons'," #SubName
sql += "'BattleMaster Ranged'," #Traits
sql += "'2'," #Attack
sql += "'7'," #Health
sql += "'1'," #Defense
sql += "'Focus 1 (Before flipping battle cards when battling -> Look at the top card of your deck. You may scrap it.) (A Battle Master begins in bot mode and cannot flip. When it is KO, play its Upgrade side.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Raider Storm Cloud
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Raider Storm Cloud'," #Name
sql += "'Infantry-Electronic Warfare'," #SubName
sql += "'Bot'," #CardType
sql += "4," #Cost
sql += "'Decepticon'," #Loyalty
sql += "'./img/bot/raider_storm_cloud.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BotMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Raider Storm Cloud'," #Name
sql += "'Infantry-Electronic Warfare'," #SubName
sql += "'AirStrikePatrol Ranged'," #Traits
sql += "3," #Attack
sql += "6," #Health
sql += "0," #Defense
sql += "'-->, Scrap 3 green cards from your hand -> One of your characters get Bold 3 until end of turn. If the 3 scrapped cards have the same name, instead that character get Bold 6 until end of turn. (To -->, tap this characters before you attack.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO AltMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Raider Storm Cloud'," #Name
sql += "'Infantry-Electronic Warfare'," #SubName
sql += "'AirStrikePatrol Ranged'," #Traits
sql += "3," #Attack
sql += "6," #Health
sql += "0," #Defense
sql += "'This has Stealth while untapped. (Enemies attack other characters if able.)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Specialist Sandstorm
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Specialist Sandstorm'," #Name
sql += "'Special Ops-Advance Guard'," #SubName
sql += "'Multiform'," #CardType
sql += "11," #Cost
sql += "'Autobot'," #Loyalty
sql += "'./img/bot/specialist_sandstorm.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BotMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Specialist Sandstorm'," #Name
sql += "'Special Ops-Advance Guard'," #SubName
sql += "'Specialist'," #Traits
sql += "6," #Attack
sql += "15," #Health
sql += "1," #Defense
sql += "'When you flip to this mode -> Do 1 damage to an enemy Specialist.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Alt1Mode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Specialist Sandstorm'," #Name
sql += "'Special Ops-Advance Guard'," #SubName
sql += "'Car Melee'," #Traits
sql += "6," #Attack
sql += "15," #Health
sql += "1," #Defense
sql += "'While this is attacking a Melee character -> This has +2 attack.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO Alt2Mode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Specialist Sandstorm'," #Name
sql += "'Special Ops-Advance Guard'," #SubName
sql += "'Helicopter Ranged'," #Traits
sql += "6," #Attack
sql += "15," #Health
sql += "1," #Defense
sql += "'While this is defending against a Ranged character -> This has +2 defense.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Starscream Decepticon King
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Starscream'," #Name
sql += "'Decepticon King'," #SubName
sql += "'Bot'," #CardType
sql += "13," #Cost
sql += "'Decepticon'," #Loyalty
sql += "'./img/bot/starscream_decepticon_king.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BotMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Starscream'," #Name
sql += "'Decepticon King'," #SubName
sql += "'Leader Ranged'," #Traits
sql += "6," #Attack
sql += "15," #Health
sql += "1," #Defense
sql += "'When you flip Decepticon Crown while this is battling -> This gets +3 attack and +3 defense until end of turn.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO AltMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Starscream'," #Name
sql += "'Decepticon King'," #SubName
sql += "'Leader Plane Ranged'," #Traits
sql += "5," #Attack
sql += "15," #Health
sql += "2," #Defense
sql += "'When you flip this mode -> Return a card that lets you Plan from your scap pile to hand.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Starscream Decepticon Lieutenant
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Starscream'," #Name
sql += "'Decepticon Lieutenant'," #SubName
sql += "'Bot'," #CardType
sql += "5," #Cost
sql += "'Decepticon'," #Loyalty
sql += "'./img/bot/starscream_decepticon_lieutenant.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO BotMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Starscream'," #Name
sql += "'Decepticon Lieutenant'," #SubName
sql += "'Melee'," #Traits
sql += "4," #Attack
sql += "7," #Health
sql += "0," #Defense
sql += "'Tough 1 (Flip 1 more battle card when defending)'" #Text
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO AltMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Starscream'," #Name
sql += "'Decepticon Lieutenant'," #SubName
sql += "'Plane Melee'," #Traits
sql += "3," #Attack
sql += "7," #Health
sql += "1," #Defense
sql += "''" #Text (The plane side of Starscream has no ability)
sql += ")"

conn.execute(sql)
db.commit()

#Tidal Wave
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Tidal Wave'," #Name
sql += "'Dark Fleet'," #SubName
sql += "'Combiner'," #CardType
sql += "24," #Cost
sql += "'Decepticon'," #Loyalty
sql += "'./img/bot/tidal_wave_dark_fleet.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO CombinerMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Tidal Wave'," #Name
sql += "'Dark Fleet'," #SubName
sql += "'Ranged'," #Traits
sql += "7," #Attack
sql += "21," #Health
sql += "2," #Defense
sql += "'(This begins untapped, has all damage from the combined characters, and keeps 1 Upgrade in each slot.) When this is combined -> Tap an enemy.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Tidal Wave (Dark Fleet Battleship)
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Tidal Wave'," #Name
sql += "'Dark Fleet (Battleship)'," #SubName
sql += "'BotPiece'," #CardType
sql += "8," #Cost
sql += "'Decepticon'," #Loyalty
sql += "'./img/bot/tidal_wave_dark_fleet_battleship.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO AltMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Tidal Wave'," #Name
sql += "'Dark Fleet (Battleship)'," #SubName
sql += "'Boat Ranged'," #Traits
sql += "4," #Attack
sql += "10," #Health
sql += "1," #Defense
sql += "'Stealth (Enemies attack other characters if able.) When your second character is KO this game and you had Tidal Wave, Dark Fleet (Aircraft Carrier) and Tidal Wave, Dark Fleet (Transport) on your starting team -> Combine them with this into Tidal Wave, Dark Fleet.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Tidal Wave (Dark Fleet Aircraft Carrier)
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Tidal Wave'," #Name
sql += "'Dark Fleet (Aircraft Carrier)'," #SubName
sql += "'BotPiece'," #CardType
sql += "8," #Cost
sql += "'Decepticon'," #Loyalty
sql += "'./img/bot/tidal_wave_dark_fleet_aircraft_carrier.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO AltMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Tidal Wave'," #Name
sql += "'Dark Fleet (Aircraft Carrier)'," #SubName
sql += "'Boat Specialist'," #Traits
sql += "1," #Attack
sql += "6," #Health
sql += "2," #Defense
sql += "'This starts the game with a Plane or Helicopter under it that has 4 stars or fewer. When this attacks, combines, or is KO -> Deploy the character from under this to the battlefield in alt mode. If this is attacking, you get extra attack this turn, but only with the deployed character.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Tidal Wave (Dark Fleet Transport)
sql = "INSERT INTO Bot(name,subName,cardType,cost,loyalty,path) VALUES"
sql += "("
sql += "'Tidal Wave'," #Name
sql += "'Dark Fleet (Transport)'," #SubName
sql += "'BotPiece'," #CardType
sql += "8," #Cost
sql += "'Decepticon'," #Loyalty
sql += "'./img/bot/tidal_wave_dark_fleet_transport.jpg'" #Path
sql += ")"

conn.execute(sql)
db.commit()

sql = "INSERT INTO AltMode(name,subName,traits,attack,health,defense,text) VALUES"
sql += "("
sql += "'Tidal Wave'," #Name
sql += "'Dark Fleet (Transport)'," #SubName
sql += "'Boat Specialist'," #Traits
sql += "0," #Attack
sql += "5," #Health
sql += "3," #Defense
sql += "'This starts the game wiht a Car, Truck, or Tank under it that has 4 stars or fewer. When this attacks, combines, or is KO -> Deploy the character from under this to the battlefield in alt mode. If this is attacking, you get extra attack this turn, but only with the deployed character.'" #Text
sql += ")"

conn.execute(sql)
db.commit()

#Heroic Spotlight
sql = "INSERT INTO Stratagem(name,cost,text,path) VALUES"
sql += "("
sql += "'Heroic Spotlight'," #Name
sql += "1," #Cost
sql += "'If your starting team is only Autobots -> Your deck can have up to 2 extra stars of blue cards. (Play up to one stratagem with the characters of the named faction. Stratagems begin on the battlefield.)'," #Text
sql += "'./img/stratagem/heroic_spotlight.jpg'"
sql += ")"

conn.execute(sql)
db.commit()

#Villainous Spotlight
sql = "INSERT INTO Stratagem(name,cost,text,path) VALUES"
sql += "("
sql += "'Villainous Spotlight'," #Name
sql += "1," #Cost
sql += "'If your starting team is only Decepticons -> Your deck can have up to 2 extra stars of orange cards. (Play up to one stratagem with the characters of the named faction. Stratagems begin on the battlefield.)'," #Text
sql += "'./img/stratagem/villainous_spotlight.jpg'"
sql += ")"

conn.execute(sql)
db.commit()


#Database must be commited to before pulling its values

#Print Bot Card Data
printData(conn,"Bot")
printData(conn,"BotMode")
printData(conn,"AltMode")
printData(conn,"Alt1Mode")
printData(conn,"Alt2Mode")
printData(conn,"HeadMode")
printData(conn,"BodyMode")
printData(conn,"CombinerMode")
printData(conn,"BattleUpgrade")

#Print Battle Card Data
printData(conn,"Action")
printData(conn,"SecretAction")
printData(conn,"Upgrade")

#Print Strategem Card Data
printData(conn,"Stratagem")


#Close Database
conn.close()
db.close()
