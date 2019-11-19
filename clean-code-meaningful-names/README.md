## Clean Code: Meaningful Names

### Question

Given these rules for creating good variables names:

A. Use Intention-Revealing Names    
B. Avoid Disinformtion        
C. Make Meaningful Distinction    
D. Use Pronounceable names    
E. Use Searchable names    
F. Don't Be Cute    
G. Avoid Mental Mapping    
H. Pick One Word per Concept 
I. Avoid Magic Numbers   

Match the rule with the example which best describes it:

1. _____ Choosing a name that specifies what is being measured and the unit of that measurement for example ***elapsedTimeInDays***, ***daysSinceCreation***.
2. _____ Don't use a variable name ***moneyAmount*** which is indistinguishable from ***money***, or 
***customerInfo*** which is indistinguishable from ***customer***.
3. _____ Use ***generationTimestamp*** instead of ***genymdhms*** (generation date, year, month, day, hour, minute, and second)
4. _____ Don't name a type that walks through a list ***Enumerator***, instead name it ***Iterator***.
5. _____ Does a function name like ***HolyHandGrenade*** suggest what it is supposed to do in your program? It's cute, but not descriptive. 
6. _____ Do not refer to a grouping of accounts as an accountList unless it’s actually a List.
7. _____ Instead of using the number 5 in your code for workdays per week, define a named constant (once) ***WORK_DAYS_PER_WEEK*** and use that everyplace that refers to days worked per week (even if its used only once). 
8. _____ It is confusing to have method names `fetch`, `retrieve`, and `get` for equivalent methods in different classes.
9. __  __ (Example of "Use Pronouncable Names" to be added).

### Answer

1. __ **A** __ **Use Intention-Revealing Names**: Choosing names that reveal intent can make it much easier to understand and change code.
2. __ **C** __ **Make Meaningful Distinction**: Distinguish names in such a way that the reader knows what the differences are.
3. __ **D** __ **Use Pronounceable names**: If you can’t pronounce it, you can’t discuss it without sounding like an idiot.
4. __ **G** __ **Avoid Mental Mapping**: The term *iterator* is a standard name in software development for this kind of behavior, whereas the term *enumeration* typically has a very different meaning. Most developers would have to mentally translate "enumerator" to "iterator" as the conversations about such things go on.
5. __ **F** __ **Don't Be Cute**: If names are too clever, they will be memorable only to people who share the author’s sense of humor, and only as long as these people remember the joke.
6. __ **B** __ **Avoid Disinformtion**: The term *list* means something specific to programmers. If the container holding the accounts is not a List, it may lead to false assumptions. So ***accountGroup*** or
***bunchOfAccounts*** or just plain ***accounts*** would be better.
7. __ **I** __ **Avoid Magic Numbers**: Using a number for a specific quantity makes code harder to understand and harder to change.  Imagine changing to a 4-day work week. This rule also applies to using named string constants instead of string literals.
8. __ **H** __ **Pick One Word per Concept**: Pick one word for one abstract concept and stick with it.
9. __  __ To be added.



### References

- [Clean Code](http://se.cpe.ku.ac.th/doc/books/programming/Clean%20Code.pdf) by Robert C. Martin
- [How To Create Meaningful Names In Code](https://medium.com/better-programming/how-to-create-meaningful-names-in-code-20d7476537d4)

And:

* *Pay Attention to Requirements*.  This assignment said that references should be specific, not an **entire book**.
