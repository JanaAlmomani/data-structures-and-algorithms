from AnimalShelter import *

def test_animal_shelter():
    animal_shelter = AnimalShelter()


    cat1 = Animal("cat", "Whiskers")
    dog1 = Animal("dog", "Fido")
    animal_shelter.enqueue(cat1)
    animal_shelter.enqueue(dog1)


    actual = animal_shelter.dequeue("dog")
    expected = dog1
    assert actual == expected, f"Expected {expected}, but got {actual}"

    cat2 = Animal("cat", "Socks")
    dog2 = Animal("dog", "Rover")
    animal_shelter.enqueue(cat2)
    animal_shelter.enqueue(dog2)


    actual1 = animal_shelter.dequeue("cat")
    actual2 = animal_shelter.dequeue("dog")
    expected1 = cat1
    expected2 = dog2
    assert actual1 == expected1, f"Expected {expected1}, but got {actual1}"
    assert actual2 == expected2, f"Expected {expected2}, but got {actual2}"

def test_animal_shelter_str():
    cat = Animal("cat", "Whiskers")
    dog = Animal("dog", "Fido")
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(cat)
    animal_shelter.enqueue(dog)
    actual = str(animal_shelter)
    expected = "Cat (Whiskers) --> Dog (Fido) --> None"
    assert actual == expected

