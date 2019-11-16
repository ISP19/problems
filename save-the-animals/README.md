## Save The Animals!

While doing a physical exam of some animals at Khao Yai,
a Thai veteranian noticed this strange entry:

<table border="1">
<tr>
<td>
<img src="elephant.jpeg">
</td>
<p align="center">
Zimba, age 3
</p>
</tr>
<tr>
<td>
Zimba was found in a sugar cane field near Sai Yok, Kanchanaburi
in 2012, after farmers complained he was eating their crops.
He was brought to Khao Yai to avoid conflicts with people,
and has been living there happily ever since.
</td>
</tr>
</table>

"*That's impossible!*" thought the vet.  The photo shows an elephant
much older than 3 years, and its inconsistent with the story that
mentions 2012.

It turns out that many animals have the wrong age, 
according to the web-based software that visitors and veteranians are using.


### The Problem

The apps are all built on the Kasetsart University Zoology API (KUZA)
library, which has an `Animal` class like this:

<table border="1">
<tr>
<th>Animal</th>
</tr>
<tr>
<td>
<code>
+age: int
+name: string
+species: Species {{enum}}
+description: string
</code>
</td>
</tr>
</table>

Its written in Python as:
```python
class Animal(Model):

    def __init__(self, name: str, species: Species, age: int):
        self.name = name
        self.species = species
        self.age = age
        # initial description, can reassign this
        self.description = "a "+str(species.value)+" named "+name

    def __str__(self):
        return f"{self.name}, a {self.age}-year old {str(self.species.value)}"
```

You immediately see the problem: the `age` is being set as an attribute
that isn't updated reliability.

### Weak Encapsulation

Encapsulation is one of the *3 Pillars of OOP*.
One benefit of encapsulation is that you can hide an objects attributes,
called *data hiding*.

This enforces the principle of: 
"*code to an interface, not to an implementation*".

Letting other objects directly access an object's attributes means:

- you can't change the implementation without "breaking" other code
- you cannot control change to the attributes

### First Try at a Solution

Your SKE friend suggests that you change `age` to a method `age()`,
and add an attribute to store the animal's date of birth.


Letting other code directly access your
This
Looking at the app used by zoologists to catalog new animals,
the code looks something like this:
```
# simplied
name = input("Name of animal? ")
species_name = input("Species? ")
species = Species.find_by_name(species_name)
age = int(input("Estimated age (years)? "))
# add animal to catalog
animal = Animal(name, species, age)
```
        



Some animals around KU are at least 20 years old,
App developers around Thailand have used the
The Kasetsart U. Zoology API (
The Kasetsart Zoo has some software and an API to let app developers
create apps to display info about animals around KU.
Unfortunately, KU Zoo API (KUZA) has a class
