Transformer game.py
class Transformer:
    def __init__(self, name, strength, intelligence, speed):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.speed = speed

    def __repr__(self):
        return f"Transformer(name='{self.name}', strength={self.strength}, intelligence={self.intelligence}, speed={self.speed})"


class Deck:
    def __init__(self):
        self.transformers = []

    def add_transformer(self, transformer):
        self.transformers.append(transformer)

    def remove_transformer(self, transformer):
        if transformer in self.transformers:
            self.transformers.remove(transformer)
        else:
            print(f"Transformer '{transformer.name}' not found in the deck.")

    def get_transformers(self):
        return self.transformers

    def get_transformer(self, name):
        for transformer in self.transformers:
            if transformer.name == name:
                return transformer
        print(f"Transformer '{name}' not found in the deck.")
        return None


# Create Transformer objects
t1 = Transformer("Optimus Prime", 10, 9, 8)
t2 = Transformer("Megatron", 9, 8, 7)
t3 = Transformer("Bumblebee", 7, 6, 9)
t4 = Transformer("Starscream", 8, 7, 8)

# Create a deck
deck = Deck()

# Add Transformers to the deck
deck.add_transformer(t1)
deck.add_transformer(t2)
deck.add_transformer(t3)
deck.add_transformer(t4)

# Get all Transformers in the deck
print("Transformers in the deck:")
for transformer in deck.get_transformers():
    print(transformer)

# Get a specific Transformer by name
t = deck.get_transformer("Bumblebee")
if t:
    print(f"Found Transformer: {t}")

# Remove a Transformer from the deck
deck.remove_transformer(t2)

# Get all Transformers in the deck after removal
print("Transformers in the deck after removal:")
for transformer in deck.get_transformers():
    print(transformer)

    def __repr__(self):
        return f"Transformer(name='{self.name}', strength={self.strength}, intelligence={self.intelligence}, speed={self.speed})"


class Deck:
    def __init__(self):
        self.transformers = []

    def add_transformer(self, transformer):
        self.transformers.append(transformer)

    def remove_transformer(self, transformer):
        if transformer in self.transformers:
            self.transformers.remove(transformer)
        else:
            print(f"Transformer '{transformer.name}' not found in the deck.")

    def get_transformers(self):
        return self.transformers

    def get_transformer(self, name):
        for transformer in self.transformers:
            if transformer.name == name:
                return transformer
        print(f"Transformer '{name}' not found in the deck.")
        return None


# Create Transformer objects
t1 = Transformer("Optimus Prime", 10, 9, 8)
t2 = Transformer("Megatron", 9, 8, 7)
t3 = Transformer("Bumblebee", 7, 6, 9)
t4 = Transformer("Starscream", 8, 7, 8)

# Create a deck
deck = Deck()

# Add Transformers to the deck
deck.add_transformer(t1)
deck.add_transformer(t2)
deck.add_transformer(t3)
deck.add_transformer(t4)

# Get all Transformers in the deck
print("Transformers in the deck:")
for transformer in deck.get_transformers():
    print(transformer)

# Get a specific Transformer by name
t = deck.get_transformer("Bumblebee")
if t:
    print(f"Found Transformer: {t}")

# Remove a Transformer from the deck
deck.remove_transformer(t2)

# Get all Transformers in the deck after removal
print("Transformers in the deck after removal:")
for transformer in deck.get_transformers():
    print(transformer)
