# Automate Testing

This is a small Testing Library I created with my own requirements to make
it easier to test my code after solving a problem.

## Version

### V1 (current)

    DONE Takes any number of variables as the input
    TODO Add Support for LinkedList
    TODO Add Support for Tree
    TODO Add Support for Binary Tree
    TODO Custom return feature when used or default return for tests

### V2

    TODO Show Execution Analytics
    TODO Show Error List
    TODO Show Stacktrace Option

### V3

    TODO Visualization

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

### Input/Output Structure

    ```python
    {
        value: any,
        type?: any,
        default?:any,
        visualize?: boolean
    }
    ```

#### Supported Types

1. `int`
2. `float`
3. ?`complex`
4. `list`
5. `tuple`
6. `dict`
7. `set`
8. `bool`
9. `linkedlist`
10. `tree`
11. `binarytree`

### Class Structure