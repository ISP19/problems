# Draw a UML Class Diagram
>The Unified Modeling Language (UML) is a general-purpose, developmental, modeling language in the field of software engineering that is intended to provide a standard way to visualize the design of a system.

from [Wikipedia](https://en.wikipedia.org/wiki/Unified_Modeling_Language)

## Question

Given `Animal` as an object. This object has `name(string)`, `id(int)`, `age(int)`, and `weight(int)` as attributes. There are 3 different kinds of animals. The first one is `Tortoise`, the second is `Cat`, and the last one is `Bird`. All these 3 animals have the same attributes as the `Animal` except for the `Cat` has one more attribute named `leg_length(int)`. However, if two or more `Tortoise` live together, then they form a group called a `Creep`. The `Animal` also have function `eat()`. Only `Cat` can eat the `Bird`.

Draw a UML Class Diagram, show the relationship between objects using UML notation.

## Answer

![Screenshot](https://github.com/ISP19/problems/blob/vichyawat/draw-uml/Class%20Diagram%20with%20UML%20Notation.png)

- Use ⇾ for `Tortoise`, `Cat` and `Bird` to show the **inheritance** that there is the subclass of `Animal`.

- Use ━◇ for `Creep` to show the **aggregation** that `Tortoise` is part of the `Creep`

## References

- [Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language) - Wikipedia
- [UML Class Diagram Relationships Explained with Examples](https://creately.com/blog/diagrams/class-diagram-relationships/) - Creately