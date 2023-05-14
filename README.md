# Transformers-TCG-Deck-Builder-Version-2_0
This is the second version of the Transformers TCG Deck Builder Project. It contains the added functionality of pulling its data from a SQL Database, contains more cards than the previous deck builder, is able to save and load its data from a file, and was created with PyQt5 instead of Tkinter. The Database can be scaled up to include any number of cards in the Transformers TCG

### How To Install and Run
- You must have PyQt5 as well as Qt5 installed on your system to run this project.
- This project was built using Python 3.11.2, and Qt 5.15.2 it may run on other versions of python and Qt, however to obtain the best results you are encouraged to use Python 3.11.2 and Qt 5.15.2
- Place all the files from this repository in the same directory, then run the UI.py file to begin the program

### Info
Cards Within the deck builder (besides Strategems are color coded to reflect their type)
Bot Cards:
- Red = Autobots 
- Purple = Decepticons
- Dark Gray = Mercenaries
 
Battle Cards (Actions):
- Dark Gray = Secret Actions
- White = Actions

Battle Cards (Upgrades):
- Orange = Weapons
- Green = WeaponArmors
- Blue = Armors
- Gray = Utilities

(Stratagem Cards Are Not Color Coded)
    
### Controls
(This program was made to be navigated using the mouse)
- Left Click a Card in a card list to preview its image
- Double Left Click a Card in a card list to add it to the deck
- Right Click a Card in a card selection section list that has been added to the Deck to remove it from the Deck
- Click the Bot, Battle, and Strategem Tabs to cycle between the card types in the card list

### File Menu Options
- New: open a new window
- Exit: terminate the program
- Save: save the current deck to a .txt file
- Save As: save the current to a .txt file and pick the name of that .txt file
- Close: close the currently open file
