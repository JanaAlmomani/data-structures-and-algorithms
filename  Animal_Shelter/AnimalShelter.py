class Animal:
    """
    A class representing an animal.
    """
    def __init__(self, species, name):
        """
        Initializes an empty Animal.
        """
        self.species = species
        self.name = name

class AnimalShelter:
    """
    A class representing an animal shelter that holds only dogs and cats.
    The shelter operates using a first-in, first-out approach.
    """
    def __init__(self):
        """
        Initializes an empty AnimalShelter.
        """
        self.dog_queue = []
        self.cat_queue = []

    def __str__(self):
        """
        Returns a string representation of the animal shelter.
        """
        dog_str = ", ".join([dog.name for dog in self.dog_queue])
        cat_str = ", ".join([cat.name for cat in self.cat_queue])
        return f"AnimalShelter(dogs: [{dog_str}], cats: [{cat_str}])"
    
    def __reper__(self):
        """
        Returns a string representation of the animal shelter.
        """
        dog_str = ", ".join([dog.name for dog in self.dog_queue])
        cat_str = ", ".join([cat.name for cat in self.cat_queue])
        return f"AnimalShelter(dogs: [{dog_str}], cats: [{cat_str}])"

    def enqueue(self, animal):
        """
        Adds an animal to the appropriate queue based on its species.
        """
        # getattr() function is used to dynamically access the appropriate queue based on the animal's species.
        getattr(self, f'{animal.species}_queue').append(animal)

    def dequeue(self, pref):
        """
        Removes and returns the next available dog or cat from the appropriate queue based on preference.
        """
        queue = self.dog_queue if pref == 'dog' else self.cat_queue
        if queue:
            return queue.pop(0)
        return None
