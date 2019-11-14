# Type Hinting –– an introduction

Content:

- [Motivations for using type hints](#motivations-for-using-type-hints)
- [Ways to type hint](#ways-to-type-hint)
  - [Function Annotations (PEP 3107)](#function-annotations-pep-3107)
  - [The typing module (PEP 484)](#the-typing-module-pep-484)
  - [Variable Annotations (PEP 526)](#variable-annotations-pep-526)
  - [Summary](#summary)
- [Question / Problem / Task](#question--problem--task)

## Motivations for using type hints

- Improved **readability** for humans and machine
  * Allow/Improve code completion for IDEs
- Acts as live **documentation**
  * Solves the problem of docstrings not being maintained
  * Docstrings don't allow complex types
- Reduce errors
  * Helps a lot in large projects

While Python is known for its _dynamic_ or "duck" typing (and some people will
argue against any form of enforced type checking), many (including the retired
BDFL) agree that _static type checking_ is still welcomed (in the form of 
"gradual type hinting"). 

## Ways to type hint

### Function Annotations (PEP 3107)

Function annotations were introduced in [**PEP 3107**](https://www.python.org/dev/peps/pep-3107/)
and is available from Python 3.0.
The PEP allows for this syntax

```python
def foo(a: expression, b: expression = default_value):
    ...
def bar(*args: expression, **kwargs: expression):
    ...
def bazz() -> expression:
    ...
```

This results in a `dict` mapping from parameter names to the Python _expression_; 
the return value is denoted by the key `'return'`. The expression is evaluated
during function definition.

This `dict` can be accessed via a _dunder_ attribute `.__annotations__` which 
doesn't have any effect on the program on its own.

[**PEP 3107**](https://www.python.org/dev/peps/pep-3107/) 
allows for any valid python expression to be there including any `str`, 
`int`, or whatever, but in current practice, we put classes in there.

```python
def catch_all(*args, **kwargs) -> None:
    return

def double_string(string: str, sep: str = '') -> str:
    return f'{string}{sep}{string}'

def my_abs(x: int) -> int:
    if x < 0:
        x = -x
    return x
```

```
>>> catch_all.__annotations__
{'return': None}
>>> double_string.__annotations__
{'string': <class 'str'>, 'return': <class 'str'>}
>>> my_abs.__annotations__
{'x': <class 'int'>, 'return': <class 'int'>}
```

With these, IDEs and static type checkers like `mypy` can help you check for 
any type issues, before actual runtime.

### The typing module (PEP 484)

[**PEP 484**](https://www.python.org/dev/peps/pep-0484/) introduces the 
[`typing`](https://docs.python.org/3/library/typing.html) module,
which allows for more complex types.

Let's se it in action.

```python
from typing import Any, Union

Number = Union[int, float, complex]

def catch_all(*args: Any, **kwargs: Any) -> None: ...

def double_string(string: str, sep: str = '') -> str: ...

def my_abs(x: Number) -> Number: ...
```

With `Union`, you can now call `my_abs()` with any numbers and the IDE or `mypy`
won't yell at you.

Some more examples:

```python
from typing import Optional

def swap_keys_and_values(dict_: dict) -> Optional[dict]: ...
```

You and the IDE both know that `swap_keys_and_values()` can return both a `dict`
or a `None` (probably if the keys and values can't be swapped).

```python
from typing import Dict, Any

def parse_request_data(data: Dict[str, Any]) -> None: ...
```

This function only accepts data in the form of a `dict` with a `str` as the key.

```python
class Question:
    ...
    def get_voted_choices(self) -> models.QuerySet:
        """
        Returns an iterable that iterates over all choices of this
        question that has been voted.
        """
```

Any kind of `class` can be used.

Some other useful ones I've used:
- All the standard type extensions: `List`, `Tuple`, `Set`, etc.
- `Iterable` when I only require a function / method's input to be an iterable
  (that is, I can use a for loop with it at least once)
- `Callable` when you're making higher level functions or using a function somewhere
- ...

See the [`typing`](https://docs.python.org/3/library/typing.html) module for more details.

### Variable Annotations (PEP 526)

[**PEP 526**](https://www.python.org/dev/peps/pep-0526/) introduces a new syntax
for defining variables available from Python 3.6 onwards.

```bnf
annotated_assignment_stmt ::=  augtarget ":" expression ["=" expression]
```

Don't worry if you don't understand what this means. This is in an Extended 
[Backus-Naur Form](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form), a 
modified version of BNF used by [Python](https://docs.python.org/3.7/reference/introduction.html#notation).

What that means is basically that you can now do this

```python
x: int = 5
```

or just this

```python
x: int
```


It might not look very useful cause many of the time that's pretty obvious and
static type checkers and IDE can figure these things out pretty easily. But in
some cases: 

```python
choice_text: str = Cls.call(some_object).complicated.chained.access().andfunc().calls['choice_text']
```

The IDE already lost track of what the types are after the first few calls. (And
probably also whoever is reading your code.) By adding type hints to the variable
IDE regains knowledge of what type the variable is, so it can now do code
completion for you again, and whoever your code can now be a little bit happier.

### Summary

In summary, you can annotate both the parameters and the return value of 
functions, classes, and variables, with the help of the `typing` module for more
complex types.

All of these are Python 3 specific. Some options I haven't shown you that is 
possible for Python 2 (or C in case of the standard library) is using type 
comments and stub files.

I'll just put a link down here to my (unfinished) slides (missing some examples)
for the `typing` module) in case you want to know about them (skip to the end of
the slides).
https://docs.google.com/presentation/d/1zoazXU6r4XZhYgjxGkpdDLirccB9TZg9mN40bW-0D6M/edit

For other sources I suggest reading `typing` module in the docs and the PEPs it 
links to.

## Question / Problem / Task

> **Note:** to run `mypy` simply
> ```bash
> $ pip install mypy
> ```
> then
> ```bash
> $ mypy path/to/yourfile.py
> ```

### 1. Fill in the blanks with type annotations that would make objects on the right pass `mypy` type check
That is, `mypy` should not yell at you for
```
x: <your answer> = <an object on the right>
```
no points for being too broad (if it's too broad, it doesn't help you with anything)

**Example:**

______int\______   0. `(3,)` or `(4,)`  ❌ # fails type check, no points  
_____object\____   0. `(3,)` or `(4,)`  ❌ # passes type check, but too broad, no points  
_____tuple\_____   0. `(3,)` or `(4,)`  ⭕ # passes type check, but could be better, partial credits  
___Tuple\[int]\___ 0. `(3,)` or `(4,)`  ⭕ # passes type check, full points  

________________   1. `'\u005e\u005e'` or `'just a string'`  
________________   2. `[<__main__.A object at 0x000001A6C4F18610>, <__main__.A object at 0x000001A6C4F18C40>]`  
________________   3. `[1, 2, 3, 4, 5]` or `[2.75, 5.5, 8.25]` but not `[1, 2.]`  
________________   4. `{'one': 1, 'two': 2, 'three': 3}` but not `{'one': '1', 'two': '2'}`  
________________   5. `<QuerySet []>` or `range()`  
________________   6. `[(0, 5), (5, 0), (5, 5)]`    
________________   7. `lambda x: None`  
________________   8. `lambda: 'some string'`

### 2. For each type annotation, give an example of objects that would pass `mypy` type check

**Example:**

&nbsp; 0. `Dict[str, Dict[str, Any]]`
```pythonstub
{'data': {'question_id': 34, 'choice_id': 132, 'error_msg': None}}
```
\
&nbsp; 1. `Iterable[Union[int, float]]`  
```

```
&nbsp; 2. `Sequence[Dict[str, float]]`
```

```
&nbsp; 3.  `Any`
```

```
&nbsp; 4.  `None`
```

```
&nbsp; 5.  `Dict[str, Optional[str]]`
```

```
&nbsp; 6.  `Literal['r', 'rt', 'w', 'wt']`
```

```
&nbsp; 7.  `N = TypeVar('Number', int, float); Tuple[N, N]`
```

```
&nbsp; 8.  `Mapping[float, int]`
```

```

### 3. Add appropriate type hints to these code snippets
There should be type hints for all function/method's parameters and return value.
Try to be forgiving for parameter types and specific for return type.

**Example:**
```python
from typing import *
def my_map(a: Callable, b: Iterable) -> Iterator:
    return map(a, b)
```

### 4. Fill in the blanks in the code so that the `mypy` type checks passes

**Example:**

```python
from typing import Iterable, List, Tuple, TypeVar, cast
T = TypeVar('T')

def pair_up(iterable: Iterable[T]) -> List[Tuple[T, T]]:
    lst = []
    pair = []
    for elem in iterable:
        pair.append(elem)
        if len(pair) == 2:
            temp = tuple(pair)  
            temp = cast(Tuple[T, T], temp) 
            lst.append(temp)
            pair.clear()
    return lst
```

## References

- https://docs.python.org/3/library/typing.html
- https://www.python.org/dev/peps/pep-0484/
- https://www.python.org/dev/peps/pep-0526/
- https://www.python.org/dev/peps/pep-3107/
- [Type Hints - Guido van Rossum - PyCon 2015](https://www.youtube.com/watch?v=2wDvzy6Hgxg)  
  If I didn't convince you to use type hints, maybe he will. Highly recommended video.