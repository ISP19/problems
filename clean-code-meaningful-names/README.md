## Clean Code : Meaningful names

### Question

Given the simple rules that creating your variable's name meaningful below :

- ####  A. Use Intention-Revealing Names
- ####  B. Avoid Disinformtion
- ####  C. Make Meaningful Distinction
- ####  D. Use Pronouncable names
- ####  E. Use Searchable names
- ####  F. Don't Be Cute
- ####  G. Avoid Mental Mapping
- ####  H. Pick One Word per Concept

Match the rule that best describe the way of creating the meaningful variable.

1. _____  Choosing a name that specifies what is being measured and the unit of that measurement for example  elapsedTimeInDays , daysSinceCreation 
2. _____  Creating the variable name ***moneyAmount*** which is indistinguishable from ***money*** or 
***customerInfo*** which is indistinguishable from ***customer***.
3. _____ Using variable ***generationTimestamp*** instead of ***genymdhms*** (generation date, year, month, day, hour, minute,and second)
4. _____ Shouldn't call the things that walk through a list Enumerators instead of Iterators.
5. _____ Using function name ***HolyHandGrenade*** is not show what it supposed to do in your program? It's cute, but in this case ***ListItemRemover*** might be a better name. 
6. _____  Do not refer to a grouping of accounts as an accountList unless it’s actually a List.
7. _____ Using variable ***WORK_DAYS_PER_WEEK*** instead of ***5*** 
8. _____ It is confusing to have fetch, retrieve, and get as equivalent methods of different classes.

### Answer

1. __ **A** __ **Use Intention-Revealing Names** : Choosing names that reveal intent can make it much easier to understand and change
code.
2. __ **C** __ **Make Meaningful Distinction** : Distinguish names in such a way that the reader knows what the differences offer
3. __ **D** __ **Use Pronouncable names** : If you can’t pronounce it, you can’t discuss it without sounding like an idiot.
4. __ **G** __ **Avoid Mental Mapping** : Because the term iterator is in common use in software circles and was completely appropriate to the domain and also because the term enumeration typically has a very different meaning.Between the two, most developers have to translate enumerator to iterator mentally as the conversations about such things go on.
5. __ **F** __ **Don't Be Cute** : If names are too clever, they will bememorable only to people who share the
author’s sense of humor, and only as long as these people remember the joke.
6. __ **B** __ **Avoid Disinformtion** : The word list means something specific to programmers. If the container holding the accounts is not actually a List, it may lead to false conclusions.1 So accountGroup or
bunchOfAccounts or just plain accounts would be better.
7. __ **E** __ **Use Pronouncable names** : Considering how much easier it will be to find WORK_DAYS_PER_WEEK than to find all the places where 5 was used and filter the list down to just the instances with the intended meaning.
8. __ **H** __ **Pick One Word per Concept** : Pick one word for one abstract concept and stick with it.



**References**
- [**Clean Code by Robert C. Martin**](http://se.cpe.ku.ac.th/doc/books/programming/Clean%20Code.pdf)
- [How To Create Meaningful Names In Code](https://medium.com/better-programming/how-to-create-meaningful-names-in-code-20d7476537d4)
