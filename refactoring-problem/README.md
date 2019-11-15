# Refactoring Problem

## Question

Given code as below. Find the code that can be more clean or refactor and change it to make it look better.

```python
class ticketprice:

    def __init__(adult:int,child:int):
        self.Adult = adult
        self.child = child

    def calculate(self):
        ADULT_PRICE = self.Adult * 200
        child_price = self.child * 100
        return ADULT_PRICE + child_price

    def __str__(self):
     return f"The total price is {self.calculate()}"
```

## Answer

Your answer should be look like this.

```python
class TicketPrice:

    ADULT_TICKET_PRICE = 200
    CHILD_TICKET_PRICE = 100

    def __init__(adult:int,child:int):
        self.adult = adult
        self.child = child

    def calculate(self):
        adult_price = self.adult * ADULT_TICKET_PRICE
        child_price = self.child * CHILD_TICKET_PRICE
        return adult_price + child_price

    def __str__(self):
     return f"The total price is {self.calculate()}"
```

## Reference

[Patterns from Refactoring book.](http://refactoring.com)
