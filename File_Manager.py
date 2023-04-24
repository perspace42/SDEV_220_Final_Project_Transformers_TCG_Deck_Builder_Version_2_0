#Create function for reading and loading
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
    A function to add a list of transformer card tuple pairs containing 'name' and 'sub name'
    to a txt file.

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
