from timeit import default_timer as timer
from utils._type import _Type
from utils._ioobject import _IOObject


class _CodeTest:
    def __init__(self, tests: list) -> None:
        self.tests = tests

    def run(self, Problem: object):

        # For each test get input and outputs
        for index, test in enumerate(self.tests):
            # function to test
            function = test["function"] if "function" in test else "main"

            # get input and output params and create list of _IOObject
            params = test["params"]
            inputParams = self._containerize(params["input"])
            outputParams = self._containerize(params["output"])

            # Run a test on the function
            sTest = _SingleTest(Problem, function, index, inputParams, outputParams)
            sTest.run()

    def _containerize(self, ios: list) -> list:
        """Creates a list of IOObject containing Input or Output data"""
        Type = _Type()
        arr = []
        for io in ios:
            data = io.pop("value")

            convTypeStr = io.pop("type") if "type" in io else None
            convTypeStr, convTypeCls = Type.getConversionType(data, convTypeStr)

            data = convTypeCls(data)
            default = io.pop("default") if "default" in io else None
            options = io
            obj = _IOObject(data, convTypeStr, default, options)
            arr.append(obj)
        return arr

    def visualize(self):
        pass


class _SingleTest:
    def __init__(
        self,
        cls: object,
        fn: object,
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

    def _getErrorMessage(self, expectedOutput, actualOutput, time):
        strExpectedOp = str(expectedOutput)
        strActualOp = str(actualOutput)

        minHorizontalLen = 60

        heading = "[TEST {}]".format(str(self.testIndex)).center(minHorizontalLen, "-")
        txt = """{}\nExpected Output: {}\nActual Output:   {}\n{}\n{}
        """.format(
            heading,
            strExpectedOp,
            strActualOp,
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
        expectedOp = self.output[0]

        # run test
        try:
            DynamicClass = self.cls()
            testFunction = getattr(DynamicClass, self.fn)
        except:
            print("Cannot find method ", self.fn)

        start = timer()
        actualOp = testFunction(*inputParams)
        end = timer()
        totaltime = end - start

        convTypeStr, convTypeCls = _Type().getConversionType(actualOp, expectedOp.type)

        # type cast
        actualOp = convTypeCls(actualOp)

        try:
            assert actualOp == expectedOp.value
        except Exception as e:
            print(self._getErrorMessage(expectedOp.value, actualOp, totaltime))

    def _execute(self, *args):
        pass
