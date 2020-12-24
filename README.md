# codetest

A simple python library which makes it easier to test code after solving a coding problem.

## How to Install

`codetest` can be installed using `pip install codetest`.

- required
  - Python 3.6.0+

> `pip install codetest`

## How to Use

To run a test, you need to pass an array of tests and the class in which the function is written

```python
from codetest import CodeTest

class AnyName:
    def AnyNameFn(self,...AnyNumberOfInputs):
        return result

tests = [
    {},
    ...
]

# Call to the Test Library
CodeTest(tests,AnyName)

```

### How to write a testcase?

```python
#index.py
from codetest import CodeTest
class Problem:
    def sumOfTwoNumbers(self, a=2,b=2):
        return a + b
    def main(self, a=2,b=2):
        return a - b

tests = [
    #Test 0
    {
        "function" : "sumOfTwoNumbers",
        "params" : {
            "input":[
                {"value":5},
                {"value":4},
            ],
            "output":[{"value":8}]
        }
    },
    #Test 1
    {
        "function" : "sumOfTwoNumbers",
        "params" : {
            #input not passed hence the function either takes default values or doesn't expect any inputs
            "output":[{"value":8}]
        }
    },
    #Test 2
    {
        # if function is not passed then `main` is executed
        "params" : {
            #input not passed hence the function either takes default values or doesn't expect any inputs
            "output":[{"value":8}]
        }
    },
]

CodeTest(tests,Problem)
```

- This will result in following output

```text
--------------------------[TEST 0]--------------------------
Expected Output: 8
Computed Output: 9
                                             [Time: 0.001ms]
------------------------------------------------------------
--------------------------[TEST 1]--------------------------
Expected Output: 8
Computed Output: 4
                                             [Time: 0.001ms]
------------------------------------------------------------
--------------------------[TEST 2]--------------------------
Expected Output: 8
Computed Output: 0
                                             [Time: 0.001ms]
------------------------------------------------------------
```

## Tests

### Testcase Structure

`? - Optional`

```python
    tests = [
        {
            function?: "" // default "main"
            params?: {
                input?:[],
                output?:[]
            }
        }
    ]
```

- If `function` is not provided, the default function would be `main`
- The order in which the `input` objects are added would be same as the params passed to the `function`.
- if `input` is not passed, then it is considered same as no inputs passed to the function
- if `output` is not passed, then the test doesn't expect any output to be returned from the function.
- if `params` is not passed, then the function is executed as-is with no input and output

### Input/Output Structure

`? - Optional`

```python
    {
        value: any,
        type?: any,
    }
```

#### Supported Types

1. `int`
2. `float`
3. `list`
4. `tuple`
5. `dict`
6. `set`
7. `bool`
8. `linkedlist`
9. `binarytree`
