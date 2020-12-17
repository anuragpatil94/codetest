# codetest

This is a small Testing Library I created with my own requirements to make
it easier to test my code after solving a problem.

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
