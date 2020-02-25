class Animal:
    def __init__(self, name):
        self.species = None
        self.name = name
    
    def make_noise():
        print("\n")


class Tiger(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.species = "tiger"
    
    def make_noice():
        print("roar")


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.species = "dog"
    
    def make_noice():
        print("bark")


class Cow(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.species = "cow"
    
    def make_noise():
        print("moo")


#from Animal_Class import Animal
class Zoo:
    def __init__(self):
        self.animals = []
    
    def add(self, Animal):
        self.animals.append(Animal.name)
        # except:
        #     TypeError("Only animals can be added")

    def show_animals(self):
        for animal in self.animals:
           print (animal.name, "the ", animal.species, "\n", animal.make_noise())

mike = Tiger("Mike")
molly = Dog("Molly")
bessie = Cow("Bessie")

zoo = Zoo()
zoo.add(mike)
zoo.add(molly)
zoo.add(bessie)

zoo.show_animals()
