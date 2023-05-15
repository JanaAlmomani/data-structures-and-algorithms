from queue import *
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
    A class representing an animal shelter that holds both dogs and cats.
    The shelter operates using a first-in, first-out approach.
    """
    def __init__(self):
        """
        Initializes an empty AnimalShelter.
        """
        self.animal_queue = Queue()

    # def __str__(self):
    #         """
    #         Returns a string representation of the animal shelter.
    #         """
    #         if self.animal_queue.front is None:
    #             return "Empty Queue"
    #         current = self.animal_queue.front
    #         output = f"{current.value.species} ({current.value.name})"
    #         current = current.next
    #         while current is not None:
    #             output += f" --> {current.value.species} ({current.value.name})"
    #             current = current.next
    #         return output + " --> None"

    def __str__(self):
        """
        Returns a string representation of the animal shelter.
        """
        if self.animal_queue.front is None:
            return "Empty Queue"
        current = self.animal_queue.front
        output = f"{current.value.species.capitalize()} ({current.value.name.capitalize()})"
        current = current.next
        while current is not None:
            output += f" --> {current.value.species.capitalize()} ({current.value.name.capitalize()})"
            current = current.next
        return output + " --> None"


    def __repr__(self):
        """
        Returns a string representation of the animal shelter.
        """
        return repr(self.animal_queue)

    def enqueue(self, animal):
        """
        Adds an animal to the end of the queue.
        """
        self.animal_queue.enqueue(animal)

    def dequeue(self, pref):
        """
        Removes and returns the next available animal of the requested species from the queue.
        """
        current = self.animal_queue.front
        previous = None
        while current:
            if current.value.species == pref:
                if previous:
                    previous.next = current.next
                else:
                    self.animal_queue.front = current.next
                if current == self.animal_queue.rear:
                    self.animal_queue.rear = previous
                return current.value
            previous = current
            current = current.next
        return None


cat = Animal("cat", "Whiskers")
dog = Animal("dog", "Fido")
animal_shelter = AnimalShelter()
animal_shelter.enqueue(cat)
animal_shelter.enqueue(dog)
print(animal_shelter.dequeue("dog"))
# expected = dog