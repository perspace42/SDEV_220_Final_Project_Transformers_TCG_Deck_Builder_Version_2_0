#Create function for reading and loading ard data to and from the program using a txt file.

1. strat
2. bot card
3. battle card

Card_Data.py
BOT_START ='bot'
BATTLE_START = 'battle'
STRAT_START = 'strat'

FILE_NAME = 'file.txt'
def read_cards():
    bot_cards = []
    strat_cards = []
    bat_cards = []
    with open(FILE_NAME) as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            list_line = line.split()
            word = list_line[0]
            if list_line ==BOT_START:
                bot_cards.append(line)
            elif word == BATTLE_START:
                bat_cards.append(line)
             elif word == STRAT_START:
                strat_cards.append(line)
             else:
                print('Unknown cards')
              return bot_cards,strat_cards,bat_cards/
  #

BOT_START = 'bot'
BATTLE_START ='battle'
STRAT_START = 'strat'

FILE_NAME ='cardfile.txt'
def read-cards =[]
    bot_cards = []
    strat_cards = []
    bat_cards = []
    with open(FILE_NAME) as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            list_line = line.split()
            word = list_line[0]
         if list_line == BOT_START:
            bot_cards.append(line)
         elif word == BATTLE_START:
            bat_cards.append(line)
          elif word == STRAT_START:
            strat_cards.append(line)
          else:
            prrint('Unknown cards')
     return bot_cards,strat_cards,bat_cards

def main():
    bot_cards,strat_cards,bat_cards =read_cards()
    print('bot_cards=',bot_cards)
    print('strat_cards=',bot-cards)
    print('bat_cards=',bot_cards)

def add_names_to_txt(names, file_name):
    """
    Args:
        names (list): List of transformer card names.
        file_name (str): Name of the txt file to which names will be added.
    Returns:
        None
    """
    with open(file_name, 'w') as file:
        for name in names:
            file.write(name + '\n')


def get_names_from_txt(file_name):
    """
    A function to get a list of transformer card 'names' from a txt file.
    Args:
        file_name (str): Name of the txt file from which names will be retrieved.
    Returns:
        list: List of transformer card names.
    """
    names = []
    with open(file_name, 'r') as file:
        for line in file:
            names.append(line.strip())
    return names


def add_name_subname_pairs_to_txt(name_subname_pairs, file_name):
    
    """
    Args:
        name_subname_pairs (list): List of tuple pairs containing transformer card name and subname.
        file_name (str): Name of the txt file to which name-subname pairs will be added.
    Returns:
        None
    """
    with open(file_name, 'w') as file:
        for name, subname in name_subname_pairs:
            file.write(name + ',' + subname + '\n')


def get_name_subname_pairs_from_txt(file_name):
    """
    A function to get a list of transformer card tuple pairs containing 'name' and 'sub name'
    from a txt file.
    Args:
        file_name (str): Name of the txt file from which name-subname pairs will be retrieved.
    Returns:
        list: List of tuple pairs containing transformer card name and subname.
    """
    name_subname_pairs = []
    with open(file_name, 'r') as file:
        for line in file:
            name, subname = line.strip().split(',')
            name_subname_pairs.append((name, subname))
    return name_subname_pairs
    """
  
            'name': card_name,
            'image': image_file,
            'description': '\

"""

bot_stratagem_cards = []
battle_cards = []

with open('cards.txt', 'r') as f:
    lines = f.readlines()

    # Initialize variables for storing card data
    card_name = None
    card_type = None
    image_file = None
    card_description = []
    card_mechanics = []
    card_notes = []

    # Loop through each line in the file
    for line in lines:
        # Check for a new card section
        if line.startswith('Card Name:'):
            # If this is a new card section, add the previous card to the appropriate list
            if card_type == 'Battle':
                battle_cards.append({
                    'name': card_name,
                    'type': card_type,
                    'image': image_file,
                    'description': '\n'.join(card_description),
                    'mechanics': '\n'.join(card_mechanics),
                    'notes': '\n'.join(card_notes)
                })
            elif card_type == 'Stratagem':
                bot_stratagem_cards.append({
                    'name': card_name,
                    'image': image_file,
                    'description': '\n'.join(card_description),
                    'mechanics': '\n'.join(card_mechanics),
                    'notes': '\n'.join(card_notes)
                })

            # Initialize variables for the new card section
            card_name = line.split(':')[1].strip()
            card_type = line.split(':')[2].strip()
            image_file = None
            card_description = []
            card_mechanics = []
            card_notes = []
        elif line.startswith('Image File:'):
            image_file = line.split(':')[1].strip()
        elif line.startswith('[Card Description]'):
            card_description = []
        elif line.startswith('[Card Mechanics]'):
            card_mechanics = []
        elif line.startswith('[Card Notes]'):
            card_notes = []
        else:
            if card_type:
                if line.strip() != '':
                    if line.startswith('-'):
                        card_mechanics.append(line.strip())
                    else:
                        card_description.append(line.strip())
                else:
                    card_notes.append(line.strip())

    # Add the last card to the appropriate list
    if card_type == 'Battle':
        battle_cards.append({})
        'name': card_name;
        'type': card_type: 
     '
bot_cards = []
bot_stratagem_cards = []
battle_cards = []

with open('cards.txt', 'r') as f:
    lines = f.readlines()

    # Initialize variables for storing card data
    card_name = None
    card_type = None
    sub_name = None
    image_file = None
    card_description = []
    card_stats = []
    card_abilities = []
    card_notes = []

    for line in lines:
        # Check for a new card section
        if line.startswith('Card Name:'):
            # If this is a new card section, add the previous card to the appropriate list
            if card_type == 'Bot':
                if sub_name == 'Stratagem':
                    bot_stratagem_cards.append({
                        'name': card_name,
                        'image': image_file,
                        'description': '\n'.join(card_description),
                        'stats': '\n'.join(card_stats),
                        'abilities': '\n'.join(card_abilities),
                        'notes': '\n'.join(card_notes)
                    })
                else:
                    bot_cards.append({
                        'name': card_name,
                        'sub_name': sub_name,
                        'image': image_file,
                        'description': '\n'.join(card_description),
                        'stats': '\n'.join(card_stats),
                        'abilities': '\n'.join(card_abilities),
                        'notes': '\n'.join(card_notes)
                    })
            elif card_type == 'Battle':
                battle_cards.append({
                    'name': card_name,
                    'type': card_type,
                    'image': image_file,
                    'description': '\n'.join(card_description),
                    'mechanics': '\n'.join(card_mechanics),
                    'notes': '\n'.join(card_notes)
                })

            # Initialize variables for the new card section
            card_name = line.split(':')[1].strip()
            card_type = line.split(':')[2].strip()
            sub_name = line.split(':')[3].strip()
            image_file = None
            card_description = []
            card_stats = []
            card_abilities = []
            card_notes = []
        elif line.startswith('Image File:'):
            image_file "="


