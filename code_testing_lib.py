"""
TODO: Tree Type Class
"""
from timeit import default_timer as timer
from utils.tree import *
from utils.linked_list import *


class _IOObject:
    def __init__(self, value, type=None, default=None, options={}):
        self.value = value
        self.type = type
        self.default = default
        self.options = options

    def __repr__(self):
        return str(
            {
                "value": self.value,
                "type": self.type,
                "default": self.default,
                "options": self.options,
            }
        )


class _Type:
    def __init__(self):
        pass

    def getDefaultTypeAsClass(self, typeAsString):
        defaultTypes = {
            "int": int,
            "float": float,
            "list": list,
            "tuple": tuple,
            "dict": dict,
            "set": set,
            "bool": bool,
            "str": str,
        }
        return defaultTypes.get(typeAsString, None)

    def getCustomTypeAsClass(self, typeAsString):
        customTypes = {
            "linkedlist": LinkedList,
            "binarytree": BinaryTree,
        }
        return customTypes.get(typeAsString, None)

    def getTypeAsString(self, typeAsClass) -> str:
        if isinstance(typeAsClass, int):
            return "int"
        elif isinstance(typeAsClass, str):
            return "str"
        elif isinstance(typeAsClass, float):
            return "float"
        elif isinstance(typeAsClass, list):
            return "list"
        elif isinstance(typeAsClass, tuple):
            return "tuple"
        elif isinstance(typeAsClass, dict):
            return "dict"
        elif isinstance(typeAsClass, set):
            return "set"
        elif isinstance(typeAsClass, bool):
            return "bool"
        elif isinstance(typeAsClass, ListNode):
            return "linkedlist"
        elif isinstance(typeAsClass, BinaryTreeNode):
            return "binarytree"

    def getConversionType(self, data, conversionTypeString=None):
        actualDataTypeString = self.getTypeAsString(data)

        if self.getCustomTypeAsClass(actualDataTypeString) or not conversionTypeString:
            return (
                actualDataTypeString,
                self.getCustomTypeAsClass(actualDataTypeString)
                or self.getDefaultTypeAsClass(actualDataTypeString),
            )

        if conversionTypeString:
            return (
                conversionTypeString,
                self.getCustomTypeAsClass(conversionTypeString)
                or self.getDefaultTypeAsClass(conversionTypeString),
            )


class CodingTest:
    def __init__(self, tests: list) -> None:
        self.tests = tests

    def run(self, Problem):

        # For each test get input and outputs
        for test in self.tests:
            # function to test
            function = test["function"] if "function" in test else "main"

            # get input and output params
            params = test["params"]
            inputParams = self._containerize(params["input"])
            outputParams = self._containerize(params["output"])

            # Run Test on the function
            sTest = SingleTest(inputParams, outputParams)
            sTest.run(Problem, function)

    def _containerize(self, ios: list) -> list:
        """Creates a list of IOObject Object containing ios data"""
        Type = _Type()
        arr = []
        for io in ios:
            data = io.pop("value")

            conversionTypeString = io.pop("type") if "type" in io else None
            conversionTypeString, conversionTypeClass = Type.getConversionType(
                data, conversionTypeString
            )

            data = conversionTypeClass(data)
            default = io.pop("default") if "default" in io else None
            options = io
            obj = _IOObject(data, conversionTypeString, default, options)
            arr.append(obj)
        return arr

    def toString(self):
        pass

    def visualize(self):
        pass


class SingleTest:
    def __init__(self, input: [_IOObject], output: [_IOObject]):
        self.input = input
        self.output = output

    def _getInputArray(self):
        pass

    def _getOutputArray(self):
        pass

    def run(self, cls, fn):
        print("running test {}".format(fn))

        # get input list
        inputParams = []
        for input in self.input:
            inputParams.append(input.value)

        # get output
        outputIOObject = self.output[0]

        # run test
        try:
            DynamicClass = cls()
            testFunction = getattr(DynamicClass, fn)
        except:
            print("Cannot find method ", fn)

        start = timer()
        output = testFunction(*inputParams)
        end = timer()
        totaltime = end - start
        print(
            "Time taken to run this test: {}{}".format(round(totaltime * 1000, 3), "ms")
        )

        Type = _Type()

        conversionTypeString, conversionTypeClass = Type.getConversionType(
            output, outputIOObject.type
        )
        output = conversionTypeClass(output)
        assert output == outputIOObject.value

        def _execute(*args):
            pass
