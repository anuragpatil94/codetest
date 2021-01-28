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


####################################################
#                     CODETEST LIB
####################################################
class _CodeTest:
    def __init__(self, tests: list, options) -> None:
        self.tests = tests
        self.options = options

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
            sTest = _SingleTest(
                Problem, function, index, inputParams, outputParams, self.options
            )
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


####################################################
#                     SINGLETEST
####################################################
class _SingleTest:
    def __init__(
        self,
        cls: object,
        fn: str,
        testIndex: int,
        input: [_IOObject],
        output: [_IOObject],
        options,
    ):
        self.cls = cls
        self.fn = fn
        self.testIndex = testIndex
        self.input = input
        self.output = output
        self.options = options

    def _getInputArray(self):
        pass

    def _getOutputArray(self):
        pass

    def _getMessage(self, expectedOutput=None, computedOutput=None, time=""):
        return {
            "success": self._getSuccessMessage(time)
            if not self.options["messages"].get("onlyFailed", False)
            else None,
            "failed": self._getErrorMessage(expectedOutput, computedOutput, time),
        }

    def _getSuccessMessage(self, time):
        # Minimum Length of Horizontal Line
        mLen = 60
        resLen = 20

        heading = "".join(
            [
                "[TEST {}]".format(str(self.testIndex)).center(mLen, "-"),
                "{}SUCCESS{}".format(bcolors.OKGREEN, bcolors.ENDC).rjust(resLen, "-"),
            ]
        )

        # Revised len for ending horizontal line
        # -9 because ENDC takes 5 char space and Color takes 4 char spaces
        revisedLen = mLen + resLen - 9
        txt = """{}\n{}""".format(
            heading,
            str(("[Time: " + str(round(time * 1000, 3))) + "ms]").rjust(revisedLen),
            "".center(revisedLen, "-"),
        )
        return txt

    def _getErrorMessage(self, expectedOutput, computedOutput, time):
        # Any output here will be in the std type format which can be easily converted to string
        strExpectedOp = str(expectedOutput)
        strComputedOp = str(computedOutput)

        # Minimum Length of Horizontal Line
        mLen = 60
        resLen = 20

        heading = "".join(
            [
                "[TEST {}]".format(str(self.testIndex)).center(mLen, "-"),
                "{}FAILED{}".format(bcolors.FAIL, bcolors.ENDC).rjust(resLen, "-"),
            ]
        )
        # Revised len for ending horizontal line
        # -9 because ENDC takes 5 char space and Color takes 4 char spaces
        revisedLen = mLen + resLen - 9
        txt = """{}\nExpected Output: {}\nComputed Output: {}\n{}\n{}
        """.format(
            heading,
            strExpectedOp,
            strComputedOp,
            str(("[Time: " + str(round(time * 1000, 3))) + "ms]").rjust(revisedLen),
            "".center(revisedLen, "-"),
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
            message = self._getMessage(time=totaltime)["success"]
            if message is not None:
                print(message)
        except Exception as e:
            print(self._getMessage(expectedOp, computedOp, totaltime)["failed"])

    def _execute(self, *args):
        pass


####################################################
#                     COLORS
####################################################
class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"

    def disable(self):
        self.HEADER = ""
        self.OKBLUE = ""
        self.OKGREEN = ""
        self.WARNING = ""
        self.FAIL = ""
        self.ENDC = ""
