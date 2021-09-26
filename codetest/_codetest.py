from timeit import default_timer as timer

# import traceback

if __package__:
    from ._utils import _LinkedList, _BinaryTree, _ListNode, _BinaryTreeNode
else:
    from _utils import _LinkedList, _BinaryTree, _ListNode, _BinaryTreeNode

####################################################
#                     TEST MODEL
####################################################
class Test:
    def __init__(self, cls, test):
        self.cls = cls

        self.validate(test)

        self.function = self._getFunctions(test)
        self.params = self._getTestParams(test)
        self.description = description

    def _getFunctionList(self):
        function_list = set([m for m in dir(self.cls) if m.startswith("__") is False])

    def _getFunctions(self, test):
        functions = []
        functionList = self._getFunctionList()
        if "function" in test:
            function = test["function"]
            if function not in functionList:
                raise Exception(f"function '{function}' not found.")
            if isinstance(function, str):
                raise TypeError(f"function should be of type string")
            functions.append("function")
        else:
            if "main" in functionList:
                functions.append("main")
            functions += list(
                filter(
                    lambda x: x.startswith("solution"),
                    functionList,
                )
            )
        pass

    def validate(self, test):
        try:
            # Functions
            functionList = self._getFunctionList()
            if "function" in test:
                function = test["function"]
                if function not in functionList:
                    raise Exception(f"function '{function}' not found.")
                if isinstance(function, str):
                    raise TypeError(f"function should be of type string")
            else:
                if "main" not in functionList:
                    if not len(
                        list(
                            filter(
                                lambda x: x.startswith("solution"),
                                functionList,
                            )
                        )
                    ):
                        raise Exception(
                            f"""either create a function with name 
                        'main' or function starting with 'solution'. or add 
                        'function' property to the test"""
                        )

            # Params
            if "params" in test:
                params = test["params"]
                inputParams = None
                outputParams = None

                def _(data):
                    for io in data:
                        if type(io) == "dict":
                            if "value" not in io:
                                raise AttributeError("attribute value not found")
                        else:
                            # TODO: Named Attributes
                            pass

                if "input" in params:
                    ips = _(params["input"])
                if "output" in params:
                    ops = _(params["output"])
            pass
        except Exception as error:
            raise Exception(error)

            pass

    def _getTestParams(self, test):
        # get input and output params and create list of _IOObject
        inputParams = None
        outputParams = None
        if "params" in test:
            params = test["params"]

            inputParams = (
                self.createParamObject(params["input"]) if "input" in params else None
            )
            outputParams = (
                self.createParamObject(params["output"]) if "output" in params else None
            )
        return inputParams, outputParams

    def createParamObject(self, params):
        """Creates a list of IOObject containing Input or Output data"""
        Type = _Type()
        arr = []
        try:
            for io in params:
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

    def getDefaultTypeAsClass(self, typeAsString: str):
        defaultTypes = {
            "int": int,
            "float": float,
            "list": list,
            "tuple": tuple,
            "dict": dict,
            "set": set,
            "bool": bool,
            "boolean": bool,
            "str": str,
            "string": str,
        }
        return defaultTypes.get(typeAsString.lower(), None)

    def getCustomTypeAsClass(self, typeAsString: str):
        customTypes = {
            "linkedlist": _LinkedList,
            "binarytree": _BinaryTree,
        }
        return customTypes.get(typeAsString.lower(), None)

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
class _Options:
    def __init__(self, options):
        self.ONLY_FAILED = (
            options["messages"]["onlyFailed"]
            if "messages" in options and "onlyFailed" in options["messages"]
            else False
        )
        self.SHOW_DESCRIPTION = (
            options["showDescription"] if "showDescription" in options else False
        )
        self.SHOW_DETAILS = (
            options["showDetails"] if "showDetails" in options else False
        )


class _CodeTest(_Options):
    def __init__(self, tests: list, options: dict) -> None:
        self.tests = tests
        self.options = options
        super().__init__(options)
        self.messages = []

    def run(self, Problem: object):
        """runs tests on class

        Args:
            Problem (object): The class in which the function is written.
        """

        # For each test get input and outputs
        for index, test in enumerate(self.tests):
            test = Test(Problem, test)
            # Get function or list of functions for testing
            # functions = self._getMethodList(Problem, test)
            inputParams, outputParams = self._getTestParams(test)
            description = test.get("description")

            # TODO: pass test object.. also add outputs to test object
            # for function in functions:
            #     # Run a test on the function
            #     sTest = _SingleTest(
            #         Problem,
            #         function,
            #         description,
            #         index,
            #         inputParams,
            #         outputParams,
            #         self.options,
            #     )
            #     # returns a PASS/FAIL Message
            #     messageObj = sTest.run()
            #     if messageObj is not None:
            #         self.messages.append(messageObj)
        print(self.messages)
        self._printStrip()
        # self._printMessages()

    def _getMethodList(self, Problem, test):
        """[summary]

        Args:
            Problem (object): class instance
            test (dict): contains single test object

        Raises:
            Exception: if method not defined in the class

        Returns:
            list: list fo method names in the class
        """
        functions = []
        method_list = set([m for m in dir(Problem) if m.startswith("__") is False])
        if "function" in test:
            if test["function"] not in method_list:
                raise Exception("method not found")
            functions.append(test["function"])
        else:
            if "main" in method_list:
                functions.append("main")
            else:
                functions = list(
                    filter(
                        lambda x: x.startswith("solution"),
                        method_list,
                    )
                )
        return functions

    def _getTestParams(self, test):
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
        return inputParams, outputParams

    def _printStrip(self):
        print("".join([obj["message"] for obj in self.messages]))

    def _printMessages(self):
        for messageObj in self.messages:
            # if showDetails is True
            if self.SHOW_DETAILS is True:
                if self.ONLY_FAILED is True and not messageObj["success"]:
                    print(messageObj["message"])
                if self.ONLY_FAILED is False:
                    print(messageObj["message"])

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
class _SingleTest(_Options):
    def __init__(
        self,
        cls: object,
        fn: str,
        description: str,
        testIndex: int,
        input: [_IOObject],
        output: [_IOObject],
        options: dict,
    ):
        self.cls = cls
        self.fn = fn
        self.description = description
        self.testIndex = testIndex
        self.input = input
        self.output = output
        super().__init__(options)

    def _getInputArray(self):
        pass

    def _getOutputArray(self):
        pass

    def _getMessage(self, expectedOutput=None, computedOutput=None, time=""):

        return {
            "success": self._getSuccessMessage(time),
            "failed": self._getFailedMessage(expectedOutput, computedOutput, time),
        }

    def _getSuccessMessage(self, time):
        if self.SHOW_DETAILS is False:
            return {
                "success": True,
                "message": "{}S{}".format(_BColors.OKGREEN, _BColors.ENDC),
            }
        # Minimum Length of Horizontal Line
        mLen = 60
        resLen = 20

        heading = "".join(
            [
                "[TEST {}]".format(str(self.testIndex)).center(mLen, "-"),
                "{}SUCCESS{}".format(_BColors.OKGREEN, _BColors.ENDC).rjust(
                    resLen, "-"
                ),
            ]
        )

        # Revised len for ending horizontal line
        # -9 because ENDC takes 5 char space and Color takes 4 char spaces
        revisedLen = mLen + resLen - 9
        txt = """{}{}\n{}\n{}""".format(
            heading,
            "\nTest Description: {}".format(self.description)
            if self.SHOW_DESCRIPTION == True
            else "",
            str(("[Time: " + str(round(time * 1000, 3))) + "ms]").rjust(revisedLen),
            "".center(revisedLen, "-"),
        )
        return {
            "success": True,
            "message": txt,
        }

    def _getFailedMessage(self, expectedOutput, computedOutput, time):
        if self.SHOW_DETAILS == False:
            return {
                "success": False,
                "message": "{}F{}".format(_BColors.FAIL, _BColors.ENDC),
            }

        # Any output here will be in the std type format which can be easily converted to string
        strExpectedOp = str(expectedOutput)
        strComputedOp = str(computedOutput)

        # Minimum Length of Horizontal Line
        mLen = 60
        resLen = 20

        heading = "".join(
            [
                "[TEST {}]".format(str(self.testIndex)).center(mLen, "-"),
                "{}FAILED{}".format(_BColors.FAIL, _BColors.ENDC).rjust(resLen, "-"),
            ]
        )
        # Revised len for ending horizontal line
        # -9 because ENDC takes 5 char space and Color takes 4 char spaces
        revisedLen = mLen + resLen - 9
        txt = """{}{}\nExpected Output: {}\nComputed Output: {}\n{}\n{}
        """.format(
            heading,
            "\nTest Description: {}".format(self.description)
            if self.SHOW_DESCRIPTION == True
            else "",
            strExpectedOp,
            strComputedOp,
            str(("[Time: " + str(round(time * 1000, 3))) + "ms]").rjust(revisedLen),
            "".center(revisedLen, "-"),
        )
        return {
            "success": False,
            "message": txt,
        }

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
        try:
            computedOp = fnToExecute(*inputParams)
        except Exception as e:
            print(str(e))
            # just_the_string = traceback.format_exc()
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
            return self._getMessage(time=totaltime)["success"]
        except Exception as e:
            return self._getMessage(expectedOp, computedOp, totaltime)["failed"]

    def _execute(self, *args):
        pass


####################################################
#                     MESSAGES
####################################################
class _TestOutputs:
    def __init__(self):
        self.outputs = []
        pass

    def _addNewTestOutput(self, test: dict):

        pass

    def _printTestOutput(self):
        pass

    def _printTestOutputString(self):
        pass


class _TestOutput:
    def __init__(self, cls, functions):
        pass

    def setOutput(self, output):
        pass


####################################################
#                     COLORS
####################################################
class _BColors:
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
