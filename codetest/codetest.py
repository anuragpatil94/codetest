if __package__:
    from ._codetest import _CodeTest
else:
    from _codetest import _CodeTest

"""[summary]
A simple library to run multiple tests on the written coding problem
"""

# PUBLIC INTERFACE


def CodeTest(tests: list, cls: object):
    """Pass a list of tests and code class as param to run the tests

    Args:
        tests (list): a list of tests that are to be performed on your function
        cls (object): The class which contains the code function

        eg.
        * ? - Optional
        tests = [
            {
                function?: "<name_of_fn>"// default: `main`
                params: {
                    input:[
                        {
                            value: any, // supports following types
                            type?: str, // if provided the value is converted to specified type
                        }
                    ],
                    output:[            // Expected Output
                        {
                            value: any,
                            type?: str,
                        }
                    ]
                }
            }
        ]

    ### Types Supported
    1. `int`
    2. `float`
    3. `list`
    4. `tuple`
    5. `dict`
    6. `set`
    7. `bool`
    8. `linkedlist`
    9. `binarytree`
    """
    codetest = _CodeTest(tests)
    codetest.run(cls)
