from timeit import default_timer as timer

if __package__:
    from ._utils import _LinkedList, _BinaryTree, _ListNode, _BinaryTreeNode
else:
    from _utils import _LinkedList, _BinaryTree, _ListNode, _BinaryTreeNode

####################################################
#                     I/O OBJECT
####################################################
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


####################################################
#                     TYPE
####################################################
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
            "linkedlist": _LinkedList,
            "binarytree": _BinaryTree,
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
        elif isinstance(data, _ListNode):
            return "linkedlist"
        elif isinstance(data, _BinaryTreeNode):
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


class _CodeTest:
    def __init__(self, tests: list) -> None:
        self.tests = tests

    def run(self, Problem: object):

        # For each test get input and outputs
        for index, test in enumerate(self.tests):
            # function to test
            function = test["function"] if "function" in test else "main"

            # get input and output params and create list of _IOObject
            inputParams = None
            outputParams = None
            if "params" in test:
                params = test["params"]

                inputParams = (
                    self._containerize(params["input"]) if "input" in params else None
                )
                outputParams = (
                    self._containerize(params["output"]) if "output" in params else None
                )

            # Run a test on the function
            sTest = _SingleTest(Problem, function, index, inputParams, outputParams)
            sTest.run()

    def _containerize(self, ios: list) -> list:
        """Creates a list of IOObject containing Input or Output data"""
        Type = _Type()
        arr = []
        try:
            for io in ios:
                data = io.pop("value")
                convTypeStr = io.pop("type") if "type" in io else None
                default = io.pop("default") if "default" in io else None
                options = io

                if data is None:
                    arr.append(_IOObject(data, None, default, options))
                    continue

                convTypeStr, convTypeCls = Type.getConversionType(data, convTypeStr)
                try:
                    data = convTypeCls(data)
                except TypeError as te:
                    raise TypeError(
                        "data `{}` cannot be converted to type:`{}`".format(
                            str(data), convTypeCls
                        )
                    )
                obj = _IOObject(data, convTypeStr, default, options)
                arr.append(obj)
            return arr
        except Exception as e:
            print(e)

    def visualize(self):
        pass


class _SingleTest:
    def __init__(
        self,
        cls: object,
        fn: str,
        testIndex: int,
        input: [_IOObject],
        output: [_IOObject],
    ):
        self.cls = cls
        self.fn = fn
        self.testIndex = testIndex
        self.input = input
        self.output = output

    def _getInputArray(self):
        pass

    def _getOutputArray(self):
        pass

    def _getErrorMessage(self, expectedOutput, computedOutput, time):
        # Any output here will be in the std type format which can be easily converted to string
        strExpectedOp = str(expectedOutput)
        strComputedOp = str(computedOutput)

        minHorizontalLen = 60

        heading = "[TEST {}]".format(str(self.testIndex)).center(minHorizontalLen, "-")
        txt = """{}\nExpected Output: {}\nComputed Output: {}\n{}\n{}
        """.format(
            heading,
            strExpectedOp,
            strComputedOp,
            str(("[Time: " + str(round(time * 1000, 3))) + "ms]").rjust(
                minHorizontalLen
            ),
            "".center(minHorizontalLen, "-"),
        )
        return txt

    def run(self):
        # get input list
        inputParams = []
        if self.input is not None:
            for input in self.input:
                inputParams.append(input.value)

        # get output
        expectedOpObj = None
        if self.output is not None:
            expectedOpObj = self.output[0]

        # run test
        try:
            DynamicClass = self.cls()
            fnToExecute = getattr(DynamicClass, self.fn)
        except:
            print("Cannot find method ", self.fn)

        start = timer()
        computedOp = fnToExecute(*inputParams)
        end = timer()
        totaltime = end - start

        try:
            # type cast
            if computedOp is not None and expectedOpObj is not None:
                # Find if output needs to be converted
                convTypeStr, convTypeCls = _Type().getConversionType(
                    computedOp, expectedOpObj.type
                )
                computedOp = convTypeCls(computedOp)
        except TypeError as te:
            raise TypeError(
                "data `{}` cannot be converted to type:`{}`".format(
                    str(computedOp), convTypeCls
                )
            )

        expectedOp = None
        if expectedOpObj is not None:
            expectedOp = expectedOpObj.value
        try:
            assert computedOp == expectedOp
        except Exception as e:
            print(self._getErrorMessage(expectedOp, computedOp, totaltime))

    def _execute(self, *args):
        pass
