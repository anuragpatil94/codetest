# Automate Testing

This is a small Testing Library I created with my own requirements to make
it easier to test my code after solving a problem.

## Version

### V1 (current)

    DONE Takes any number of variables as the input
    DONE Add Support for LinkedList
    DONE Add Support for Binary Tree
    DONE Time to run function
    TODO Custom return feature when used or default return for tests

### V2

    TODO: More Flexible Type names like str can be string or str. Case Independent
    TODO Test Description 
    TODO Show Execution Analytics
    TODO Show Error List
    TODO Show Stacktrace Option

### V3

    TODO Add Support for Tree
    TODO: Add Test Cases for tree as dict
    TODO: Add Test Cases for tree as MultiDimentionalList
    TODO: Linked List, Doubly Linked List, Circular Linked List using a settings param in Linkedlist class
    TODO: Add Test for output as LinkedList
    TODO Add Test Cases for string as Boolean
    TODO Add support for JSON as param
    TODO Support More than one output
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
3. `list`
4. `tuple`
5. `dict`
6. `set`
7. `bool`
8. `linkedlist`
9. `tree`
10. `binarytree`

### Class Structure
