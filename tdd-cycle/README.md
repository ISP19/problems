# Test-Driven Development
  
Test-driven development (TDD) is a software development practice that relies on the repetition of a very short development cycle: requirements are turned into very specific test cases, then the software is written just enough that the tests pass.  

### The Three Laws of TDD
1. You are not allowed to write any production code unless it is to make a failing unit test pass.
2. You are not allowed to write any more of a unit test than is sufficient to fail; and compilation failures are failures.
3. You are not allowed to write any more production code than is sufficient to pass the one failing unit test.


## Question
Order the processes of TDD cycle.  
  
__ Run all tests and see them all succeed.  
__ Run all tests and see some of them fail.  
__ Write the code.  
__ Add a test.  

----

Run Python unittest in `test_remove_vowel.py`. You will see that some cases are failed.  
Edit `remove_vowel` function in `remove_vowel.py` until all test cases in `test_remove_vowel.py` are passed.  

## Answer
Order the processes of TDD cycle.  
_ 4 _  
_ 2 _  
_ 3 _  
_ 1 _  

----
Edited `remove_vowel` function  
[remove_vowel.py](answer/remove_vowel.py)  

## References
[Wikipedia](https://en.wikipedia.org/wiki/Test-driven_development)  
Test-Driven Development By Example - Kent Beck