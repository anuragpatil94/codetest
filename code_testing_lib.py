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

    def getTypeAsString(self, data) -> str:
        if isinstance(data, int):
            return "int"
        elif isinstance(data, str):
            return "str"
        elif isinstance(data, float):
            return "float"
        elif isinstance(data, list):
            return "list"
        elif isinstance(data, tuple):
            return "tuple"
        elif isinstance(data, dict):
            return "dict"
        elif isinstance(data, set):
            return "set"
        elif isinstance(data, bool):
            return "bool"
        elif isinstance(data, ListNode):
            return "linkedlist"
        elif isinstance(data, BinaryTreeNode):
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
        for index, test in enumerate(self.tests):
            # function to test
            function = test["function"] if "function" in test else "main"

            # get input and output params
            params = test["params"]
            inputParams = self._containerize(params["input"])
            outputParams = self._containerize(params["output"])

            # Run Test on the function
            sTest = SingleTest(Problem, function, index, inputParams, outputParams)
            sTest.run()

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

    def visualize(self):
        pass


class SingleTest:
    def __init__(self, cls, fn, testIndex, input: [_IOObject], output: [_IOObject]):
        self.cls = cls
        self.fn = fn
        self.testIndex = testIndex
        self.input = input
        self.output = output

    def _getInputArray(self):
        pass

    def _getOutputArray(self):
        pass

    def _getErrorMessage(self, expectedOutput, actualOutput, time):
        strExpectedOut = str(expectedOutput)
        strActualOut = str(actualOutput)

        minHorizontalLen = 60

        heading = "[TEST {}]".format(str(self.testIndex)).center(minHorizontalLen, "-")
        txt = """{}\nExpected Output: {}\nActual Output:   {}\n{}\n{}
        """.format(
            heading,
            strExpectedOut,
            strActualOut,
            str(("[Time: " + str(round(time * 1000, 3))) + "ms]").rjust(
                minHorizontalLen
            ),
            "".center(minHorizontalLen, "-"),
        )
        return txt

    def run(self):
        # get input list
        inputParams = []
        for input in self.input:
            inputParams.append(input.value)

        # get output
        outputIOObject = self.output[0]

        # run test
        try:
            DynamicClass = self.cls()
            testFunction = getattr(DynamicClass, self.fn)
        except:
            print("Cannot find method ", self.fn)

        start = timer()
        output = testFunction(*inputParams)
        end = timer()
        totaltime = end - start

        Type = _Type()

        conversionTypeString, conversionTypeClass = Type.getConversionType(
            output, outputIOObject.type
        )
        output = conversionTypeClass(output)
        try:
            assert output == outputIOObject.value
        except Exception as e:
            print(self._getErrorMessage(outputIOObject.value, output, totaltime))

    def _execute(self, *args):
        pass
