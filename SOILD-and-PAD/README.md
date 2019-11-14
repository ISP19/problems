# Question
Do any of the PAD tip is resemble SOLID principle and why?


# Answer
|SOLID Principle| PAD|
|:-------------------------------------------------|--------|
|S (Single responsibility principle) |PAD30 (Write Cohesive Code)|
|O (Open/closed principle) | - |
|L (Liskov substitution principle) |PAD32 (Substitute by Contract)
|I (Interface segregation principle)| - |
|D (Dependency inversion principle)| - |

# S, PAD30
"Write cohesive code." - ***PAD30***

"A class should only have a single responsibility, that is, only changes to one part of the software's specification should be able to affect the specification of the class." - 
***Single responsibility principle***

**PAD30**
Write cohesive/high **cohesion** code

**Cohesion** is a measure of how functionally related the members of a
component. High cohesion indicates that the members work toward one feature or set of features.

# L, PAD32

"Substitute by Contract." - ***PAD32***

"Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program."- ***Liskov substitution principle***

**PAD32**

Derived class must be able to replace base class.
