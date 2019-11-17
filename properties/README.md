## Save The Animals!

While doing a physical exam of some animals at Khao Yai,
a Thai veteranian noticed this strange entry in his mobile animal app:

<table border="1">
<tr>
<td>
<p align="center">
<img src="elephant.jpeg">
</p>
<p align="center">
Zimba, age 3
</p>
</tr>
<tr>
<td>
Zimba was found in a sugar cane field near Sai Yok, Kanchanaburi
in 2012, when farmers complained he was eating their crops.
He was brought to Khao Yai to avoid conflict with people,
and has been living there happily ever since.
</td>
</tr>
</table>

"*That's impossible!*" said the vet.  The photo shows an elephant
much older than 3 years, and its inconsistent with the story that
mentions 2012.

Browsing the app used to catalog animals in Thailand's zoos and natural parks, the vet found that many animals have the **wrong age**, and in some cases wrong species.


### The Problem

The apps are all built on the Kasetsart University Zoology API (KUZA)
library, which has an `Animal` class like this:

<table border="1">
<tr>
<th>Animal</th>
</tr>
<tr>
<td>
<pre>
+age: int
+name: string
+species: string
+description: string
</pre>
</td>
</tr>
</table>

Its written in Python as:
```python
class Animal:
    def __init__(self, 
        name: str, age: int, species: str):
        self.name = name
        self.species = species
        self.age = age
        # initial description
        self.description = "a "+str(species)+" named "+name

    def __str__(self):
        # code omitted for brevity
```

You immediately see the problem: `age` is being set as an attribute
that isn't updated reliability.

### First Try at a Solution

Your friend suggests that you replace the attribute `age` with a `birthday` attribute, and write a method named `age()` to return the animal's age.  That way, the age will always be current: 

```python
from datetime import date

class Animal:
    # keep old constructor signature, 
    # for backward compatibility
    def __init__(self, 
            name: str, age: int, species: str):
        self.name = name
        self.species = species
        now = date.today()
        # infer birthday from age
        self.birthday = date(
            now.year-age, now.month, now.day)
    
    def age(self):
        """Get the animal's age in years"""
        today = date.today()
        age = today.year - self.birthday.year
        if (today.month,today.day) <
              (self.birthday.month,self.birthday.day) and age > 0:
            age -= 1
        return age
    
    def set_birthday(self, year:int, month:int, day:int):
        bday = date(year, month, day)
        if bday > date.today():
            raise ValueError(
              "Birthday cannot be in the future")
        self.birthday = bday
```

This works, but it will **break existing applications** that use `Animal`.

Existing apps expect `age` to be an attribute. For example:
```python
print("Animal's name:", animal.name)
print("Age", animal.age)
```

Changing `age` to a method causes code like this to fail.    
We can't rewrite all the existing apps that use `Animal.age`.  

### Solution using a Read-only Property

The above solution breaks existing applications, but you can fix it with just **one line of code**.

Read about properties here:
* https://www.programiz.com/python-programming/property

Then add a single line to the above code to preserve backward compability, so we can access `age` as if it was an attribute of `Animal`.

Verify that the solution works with this example:
```python
zimba = Animal('Zimba', 3, 'Elephant')
zimba.set_birthday(2010, 1, 15)
print("Zimba's age is", zimba.age)
```

Now `age` looks like an attribute, but is coded as a method.

Using a property prevents unwanted changes, too.    
You can't write `zimba.age = 5`.

### Starter Code

[animal.py](animal.py)

### Make `name` be a Read-Write Property

Convert name to a property that can be accessed using:
```python
animal.name
```
and can be set using:
```python
animal.name = 'new name'
```
This *looks* like assignment, but using a property it will be a call to a "setter" method of the "name" property.

Write the `name` property "setter" method to do 3 thing:
1. remove leading/trailing whitespace using string.strip()
2. capitalize the first letter of each word. This is easy: string.title()
3. raise `ValueError` if the new name is an empty string

For example:
```python
>>> animal = Animal('Zimba', 5, 'Elephant')
>>> animal.name
'Zimba'
>>> animal.name = " big ears "
>>> animal.name
'Big Ears'
```
        
### Encapsulation

Encapsulation is one of the *3 Pillars of OOP*.
Encapsulation enables you to hide an object's attributes (called *data hiding*) and expose their values using *accessor methods*.

This enforces the principle of: 
"*code to an interface, not to an implementation*".

The benefits are:
1. you can change the implementation without changing the interface (methods)
2. you can validate values before assigning them to attributes, or make an attribute be "read-only", by providing a "getter" but no "setter"

The problem with the original code is that it exposes its attributes. 

### Encapsulation and Properties

Properties enforce encapsulation and data-hiding, but still let you use the property as if it was an attribute.
