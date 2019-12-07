# Refactoring Problem

## Question

Given code as below. Find the code that can be more clean or refactor and change it to make it look better.

```python
class ticketprice:

    def __init__(self, adult:int,child:int):
        self.Adult = adult
        self.child = child

    def calculate(self):
    """"Calculate the ticket price. If group of adult and child are more than ten, cut the price in half"""
    if self.Adult + self.child < 10:
        ADULT_PRICE = self.Adult * 200
        child_price = self.child * 100
    else:
        ADULT_PRICE = self.Adult * 100
        child_price = self.child * 50
    return ADULT_PRICE + child_price

    def __str__(self):
     return f"The total price is {self.calculate()}"
```

## Answer

Your answer should be look like this.

```python
ADULT_TICKET_PRICE = 200
CHILD_TICKET_PRICE = 100
DISCOUNT = 2


class TicketPrice:

    def __init__(self, adult: int, child: int):
        self.adult = adult
        self.child = child

    def calculate(self):
    """"Calculate the ticket price. If group of adult and child are more than ten, cut the price in half"""
    if self.adult + self.child < 10:
        adult_price = self.adult * ADULT_TICKET_PRICE
        child_price = self.child * CHILD_TICKET_PRICE
    else:
        adult_price = self.adult * (ADULT_TICKET_PRICE / DISCOUNT)
        child_price = self.child * (CHILD_TICKET_PRICE / DISCOUNT)
    return adult_price + child_price

    def __str__(self):
        return f"The total price is {self.calculate()}"

```

Actully, you can add variable of ticket price and discount into the class instead of using global variable too.

## Why change number into global variable or nomal variable ?

From "Software Development, Design and Coding With Patterns, Debugging, Unit Testing, and Refactoring" by John F.Dooley. He said that the magic number which are the number use in function should be the constant to make it very easy to change since your need to change only one place in your code.

## Reference

[Chapter 14 from "Software Development, Design and Coding With Patterns, Debugging, Unit Testing, and Refactoring".](https://se.cpe.ku.ac.th/doc/books/refactoring/Refactoring%20-%20Dooley.pdf)
