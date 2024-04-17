class Animals:
    def __init__(self, eats, sounds, activities):
        self.eats = eats
        self.sounds = sounds
        self.activities = activities

    def grass_eating(self):
        print("Herbivorous")
    def animal_eating(self):
        print("Carnivorous")
    def plant_animal_eating(self):
        print("Omnivorous")

class Cow(Animals):
    def __init__(self):
        super().__init__("grass", "moo", "grazing")
    def moo(self):
        print("Moos")

class Dog(Animals):
    def __init__(self):
        super().__init__("plants and animals", "barks", "fetching")
    def barks(self):
        print("Barks")

class Tiger(Animals):
    def __init__(self):
        super().__init__("animals", "roars", "hunting")
    def roars(self):
        print("Roars")

cow1 = Cow()
dog1 = Dog()
tiger1 = Tiger()
cow1.grass_eating()
dog1.plant_animal_eating()
tiger1.animal_eating()

