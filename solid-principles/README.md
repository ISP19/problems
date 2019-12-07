## SOLID Principles

### Question

Match these SOLID Principles to the situations below

>Single responsibility  
>Open–closed  
>Liskov substitution  
>Interface segregation  
>Dependency inversion  

1. ______ Pat wrote 2 classes, Animal and a child class, Dog. Any function that uses Animal can accept a Dog instead without any problem.

2. ______ Pam wrote a class in a way that its behavior can be customized or extended without modifying the original code

3. ______ Park programmed a game with a function called update() that calls update player position and also renders player.  This violated which solid principle?

4. ______ Pablo created a module that allows coder to send objects to another computer but must follow certain class structure. Which solid principles did Pablo breaks?

5. ______ In Pam's action game, initially she wrote one interface for all the events the occur in the game:

|GameEvent   |
|:-----------|
| run()      |
| pause()    |
| throws()   |
| hits()     |
| exlodes()  |
| isHit()    |

but most of the objects that use or implement this interface only need one or two methods.  The others are either ignored (in dependent objects) or implemented as `pass` (classes implementing the interface).

So in the next revision Pam divides them into interfaces containing only the methods each object needs:

|GameEvent   |
|:-----------|
| run()      |
| pause()    |

|WarriorEvent|
|:-----------|
| throws()   |
| isHit()    |

|WeaponEvent |
|:-----------|
| hits()     |
| exlodes()   |


<br/>
<details>
<summary><b>Answers</b></summary>

1. Liskov substitution  
2. Open–closed  
3. Single responsibility
4. Dependency inversion  
5. Interface segregation  

</details>

**References**

- [Single responsibility](https://www.youtube.com/watch?v=L2m-S0Pj_Xk)
- [Open–closed](https://www.youtube.com/watch?v=Ryhy7333mqQ)
- [Liskov substitution](https://www.youtube.com/watch?v=Mmy1EUKC_iE)
- [Interface segregation](https://www.youtube.com/watch?v=Ye1h3zKl1lg)
- [Dependency inversion](https://www.youtube.com/watch?v=qL2-5g_lJTs)
