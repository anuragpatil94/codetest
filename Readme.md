# codetest

A simple python library which makes it easier to test code after solving a coding problem.

## Test Structure

    ```python
    Tests = [
        {
            function: "" // default "main"
            params: {
                input:[],
                output:[]
            }
        }
    ]
    ```

- If `function` is not provided, the default function would be `main`
- The order in which the `input` Objects are supposed to be added would be same as the params passed in the `function`.

## How to Install

## How to Use

### Input/Output Structure

    ? - Optional
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
