# codetest

A simple python library which makes it easier to test code after solving a coding problem.

## How to Install

> `pip install codetest`

## How to Use

### How to write a testcase?

```python
#index.py
from codetest import CodeTest
class Problem:
    def sumOfTwoNumbers(self, a,b):
        return a + b

tests = [{
    "function" : "sumOfTwoNumbers",
    "params" : {
        "input":[
            {"value":5},
            {"value":4},
        ],
        "output":[{"value":8}]
    }
}]

CodeTest(tests,Problem)
```

- This will result in following output

```
--------------------------[TEST 0]--------------------------
Expected Output: 8
Actual Output:   9
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
            params: {
                input:[],
                output:[]
            }
        }
    ]
```

- If `function` is not provided, the default function would be `main`
- The order in which the `input` Objects are supposed to be added would be same as the params passed in the `function`.

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
