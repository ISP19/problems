from datetime import date
from typing import Tuple

class Animal:
    """
    These doctests will pass after you make age be a property
    and name be a read/write property with name normalization.


    >>> zimba = Animal("Zimba", 3, "Elephant")
    >>> zimba.age
    3
    >>> zimba.set_birthday(2000, 12, 30)
    >>> zimba.age
    18
    >>> zimba.name
    'Zimba'
    >>> zimba.name = "big ears"
    >>> zimba.name
    'Big Ears'
    """

    def __init__(self, 
            name: str, age: int, species: str): 
        self.name = name
        self.species = species
        now = date.today()
        # estimate the birthdate from age
        # This is a hack for backward compatility with old code which
        # used age as an attribute.
        # New code should call set_birthday to set the animal's birthdate.
        self.set_birthday(now.year-age, now.month, now.day)
        # initial description, can reassign this
        self.description = "A "+str(species)+" named "+name

    def age(self):
        """Get the animal's age."""
        today = date.today()
        age = today.year - self.birthday.year
        if (today.month,today.day) < (self.birthday.month,self.birthday.day) and age > 0:
            age -= 1
        return age

    def set_birthday(self, year: int, month: int, day: int):
        bday = date(year, month, day)
        if bday > date.today():
            raise ValueError("Birthday cannot be in the future")
        self.birthday = bday

    def __str__(self):
        #TODO change self.age() to property reference after you make age a property
        return f"{self.name}, a {self.age()}-year old {str(self.species)}"

        
