# Check code with Unittest

**What is Unit Testing?**

_Unit Testing is the first level of software testing where the smallest testable parts of a software are tested. This is used to validate that each unit of the software performs as designed._

**Method:**

White Box Testing method is used for Unit testing.

### Question
1. Write a basic test structure.
2. From the question above, what is a block of running tests?
3. What are the cruxes of each test? What do they do?
4. If we put -v in command line, what does it show?

### Answer

1.
```python
import unittest 
class ExampeleTest(unittest.TestCase): 
	# Returns True or False. 
	def test_bool(self):		 
		self.assertTrue(True)
    
    def test_add(self):
        # 13/8 = 3/4 + 7/8
        self.assertEqual(Numbertest(13,8), Numbertest(3,4)+Fraction(7,8))
        #Numbertest is a class that you want to test.
if __name__ == '__main__': 
	unittest.main() 
```

2.
```python
if __name__ == '__main__': 
	unittest.main()
```

3.  *assertEqual() to check for an expected result
    *assertTrue() or assertFalse() to verify a condition
    *assertRaises() to verify that a specific exception gets raised

4. Passing the -v option to your test script will instruct unittest.main() to enable a higher level of verbosity, and produce the following output:

test_bool (__main__.ExampeleTest) ... ok
test_add (__main__.ExampeleTest) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK