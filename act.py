class Noun:
    def __init__(self, name, color, petals):
        self.name = name
        self.color = color
        self.petals = petals

    def display(self):
        print(f"Name: {self.name}")
        print(f"Color: {self.color}")
        print(f"Petals: {self.petals}")

class SpecificFlower(Noun):
    def __init__(self, name, color, petals, fragrance, thorns):
        Noun.__init__(self, name, color, petals)  # Call the parent class constructor directly
        self.fragrance = fragrance
        self.thorns = thorns

    def display(self):
        Noun.display(self)  # Call the parent class display method directly
        print(f"Fragrance: {self.fragrance}")
        print(f"Thorns: {self.thorns}")

flower3 = SpecificFlower("Tulip", "Yellow", 6, "Mild", "Yes")
flower4 = SpecificFlower("Cactus", "Green", 0, "None", "Yes")

print("Flower 3:")
flower3.display()
print("\nFlower 4:")
flower4.display()
